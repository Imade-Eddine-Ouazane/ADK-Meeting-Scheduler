# Intelligent Meeting Scheduler (ADK multi‑agents)

Assistant multi‑agents pour planifier des réunions de bout en bout avec Google ADK.
Il collecte les besoins, propose des créneaux, vérifie la météo, suggère des salles,
recommande l’équipement et le traiteur, génère l’agenda, crée l’invitation (ICS),
estime le budget, produit les follow‑ups et un compte‑rendu.

## Aperçu
- Orchestration principale: `SequentialAgent` (pipeline)
- Agents supplémentaires: agents autonomes (hors pipeline) pour validation intake et budget
- Modèles: mélange de Gemini (`gemini-2.5-flash-lite`) et LiteLLM/Ollama (`qwen2.5:7b-instruct`)
- Outils: slots calendrier (offline), météo (Open‑Meteo), salles (catalogue interne),
  équipement (heuristique), traiteur (catalogue), ICS, budget et policy budget, validation email

## Architecture
- Pipeline (séquentiel):
  1. intake →
  2. participants →
  3. slots →
  4. meteo →
  5. rooms →
  6. equipment →
  7. catering →
  8. agenda →
  9. invites →
  10. budget →
  11. followups →
  12. minutes

- Agents autonomes (hors pipeline):
  - `intake_validator_agent`: vérifie la complétude de l’intake (emails, fenêtre ISO, durée, etc.)
  - `budget_policy_agent`: contrôle limites par personne et plafond total, propose des optimisations
  - `budget_scenarios_agent`: calcule 3 scénarios (léger/standard/premium) via `estimate_budget`

## Détails des agents
- intake_agent (Gemini): collecte objectif, participants, ville, fenêtre (ISO), durée, contraintes
- participants_agent (Ollama): structure noms/emails/rôles et valide les emails
- slot_agent (Gemini): propose 2–3 créneaux via `find_common_slots`
- meteo_agent (Ollama): appelle `get_weather_tool(city, date)` (Open‑Meteo) et résume
- room_agent (Gemini): suggère des salles via `find_rooms` (catalogue interne)
- equipment_agent (Ollama): recommande l’équipement AV selon taille/remote
- catering_agent (Ollama): propose des traiteurs par ville/régime/budget pp
- agenda_agent (Gemini): rédige un agenda concis, timeboxé
- invites_agent (Ollama): génère un fichier ICS via `create_ics_event`
- budget_agent (Ollama): estime le budget total et le détail
- followups_agent (Gemini): actions, responsables, dates
- minutes_agent (Ollama): compte‑rendu depuis transcript ou modèle vierge

## Outils & données
- `tools/calendar_tool.py` → `find_common_slots(window_start, window_end, duration_minutes, ...)`
- `tools/meteo_tool.py` → `get_weather_tool(city, date)` (Open‑Meteo; timezone Africa/Casablanca)
- `tools/room_tool.py` + `memory/room_catalog.py` → recherche de salles
- `tools/equipment_tool.py` → recommandations AV (heuristique offline)
- `tools/catering_tool.py` + `memory/catering_catalog.py` → options traiteur
- `tools/invite_tool.py` → génération ICS (texte)
- `tools/budget_tool.py` → `estimate_budget(...)`
- `tools/budget_policy_tool.py` → `check_budget_policy(...)`
- `tools/validator_tool.py` → `validate_contact(email, phone)`

## Scénarios d’usage (exemples)
- Réunion d’équipe (hybride) à Paris, semaine prochaine, 60 min
  - Intake → Participants → Slots → Météo (2026‑01‑11) → Salle (10 pers, vidéo) → Équipement → Agenda → Invitation (ICS) → Budget → Follow‑ups → Minutes
- Atelier client (présentiel) à Lyon, 20 pers, traiteur végétarien ≤ 18€
  - Salle (capacité ≥ 20) → Catering (diet=vegetarian, max=18) → Équipement (PA, micro) → Agenda → ICS → Budget → Policy budget
- Validation intake & conformité budget (hors pipeline)
  - `intake_validator_agent` pour compléter les infos manquantes
  - `budget_policy_agent` pour vérifier plafonds pp et total
  - `budget_scenarios_agent` pour comparer léger/standard/premium

## Installation & lancement
Prérequis:
- Python 3.10+
- Google ADK installé (bibliothèque et CLI)
- (Optionnel) Ollama en local pour les modèles `qwen2.5:7b-instruct`

Configuration `.env` (dans `agent/`):
```ini
GOOGLE_GENAI_USE_VERTEXAI=0
# Définir UNE seule clé selon usage
GOOGLE_API_KEY=...  # ou GEMINI_API_KEY=...
```

Ollama (si utilisé):
```bash
ollama pull qwen2.5:7b-instruct
# Vérifier que le service Ollama tourne (par défaut http://localhost:11434)
```

Lancement (depuis le dossier projet racine contenant l’app ADK):
```bash
adk web
# Ouvrir: http://127.0.0.1:8000/apps/agent
```

## Exemples de prompts
- « Organise une réunion à Paris entre 2026‑01‑10 et 2026‑01‑12 (60 min). Donne aussi la météo pour 2026‑01‑11. »
- « 12 participants dont 3 à distance; propose une salle avec visio et l’équipement recommandé. »
- « Traiteur végétarien à Lyon ≤ 18€ par personne pour 20 personnes. »
- « Calcule le budget total (catering=15€, room=250€, equipment=120€). Vérifie la policy 20€/pp et 800€ total. »
- (Hors pipeline) « Vérifie la complétude de l’intake et propose les questions manquantes. »

## Dépannage
- 429/Quota ou 503/Overload (Gemini)
  - Basculez davantage d’agents vers LiteLLM/Ollama (modèles locaux), ou réduisez les appels
  - Évitez d’avoir GOOGLE_API_KEY et GEMINI_API_KEY définies en même temps
- Ollama
  - Assurez‑vous que le modèle est installé et que le service tourne
- Réseau/API
  - `get_weather_tool` dépend d’Open‑Meteo; vérifiez la connectivité Internet
- Conflits de port
  - Modifiez le port Uvicorn si besoin ou stoppez le processus déjà en cours

## Personnalisation & extension
- Ajouter `timezone_agent` (conversion et normalisation des horaires)
- `conflict_resolver_agent` (détection et résolution auto des conflits)
- Intégration Calendrier Google/Microsoft pour disponibilité et création d’événements réels
- `doc_agent` (contexte depuis documents précédents), `translation_agent` (FR/EN)

## Structure du dossier `agent/`
```
agent/
  ├─ agent.py                # Orchestration SequentialAgent
  ├─ .env                    # Variables d’environnement (clés API, etc.)
  ├─ agents/
  │   ├─ intake_agent.py
  │   ├─ participants_agent.py
  │   ├─ slot_agent.py
  │   ├─ meteo_agent.py
  │   ├─ room_agent.py
  │   ├─ equipment_agent.py
  │   ├─ catering_agent.py
  │   ├─ agenda_agent.py
  │   ├─ invites_agent.py
  │   ├─ budget_agent.py
  │   ├─ followups_agent.py
  │   ├─ minutes_agent.py
  │   ├─ intake_validator_agent.py        # (hors pipeline)
  │   ├─ budget_policy_agent.py           # (hors pipeline)
  │   └─ budget_scenarios_agent.py        # (hors pipeline)
  ├─ tools/
  │   ├─ calendar_tool.py
  │   ├─ meteo_tool.py
  │   ├─ room_tool.py
  │   ├─ equipment_tool.py
  │   ├─ catering_tool.py
  │   ├─ invite_tool.py
  │   ├─ budget_tool.py
  │   ├─ budget_policy_tool.py
  │   └─ validator_tool.py
  ├─ memory/
  │   ├─ room_catalog.py
  │   └─ catering_catalog.py
  └─ callbacks/
      └─ log_callbacks.py
```
