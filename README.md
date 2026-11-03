# Project 721 — AI Backlog Refinement Agent

**Projectteam 721 · Hogeschool Utrecht**

**Gemaakt door:** Jesmar Oosterom en de overige leden van Projectteam 721 (HU).

[![Demo en tests](https://github.com/Zer0Stride/Project-721-AI-Agent/actions/workflows/demo-tests.yml/badge.svg)](https://github.com/Zer0Stride/Project-721-AI-Agent/actions/workflows/demo-tests.yml)

## Over de agent

Projectteam 721 heeft een **organisatiespecifieke AI-agent in Microsoft 365 Copilot** ingericht om Scrum-refinement te ondersteunen. Hij werkt met afgeschermde context over **businessdoelen, Product Goal, technische randvoorwaarden en bestaande backlogitems** en helpt daarmee om:

- kleine **kandidaat-userstory's** te formuleren vanuit gebruikersbehoeften;
- de **businesswaarde en MVP-bijdrage** per story te onderbouwen;
- **Given/When/Then-acceptatiecriteria** op te stellen;
- uitvoerbare **Scrumtaken** voor te stellen;
- mogelijke overlap met bestaand werk te signaleren;
- vragen voor een **refinement** voor te bereiden.

De agent is gemaakt met eigen instructies, **vijf oorspronkelijke gespecialiseerde vaardigheden (met een zesde vaardigheid voor refinementfeedback die apart kan worden toegevoegd)** en **drie voorgestelde prompts**. De projectgebonden kennis en interne documenten zijn bewust **niet in deze repository gepubliceerd**.

## Van projectdoel naar refinement

\`\`\`text
Businessdoel + Product Goal + (optioneel) Sprint Goal
                         |
                Copilot-agent + skills
                         |
            Kandidaat-userstory's
              + acceptatiecriteria
              + taken + MVP-waarde
                         |
               Kritische refinement
                         |
            Scrumteam neemt besluit
\`\`\`

## Werkende demonstratie

Naast de Copilot-agent bevat deze repository een **reproduceerbare Python-demo met volledig fictieve gegevens**. Je kunt lokaal zien hoe het gewenste storyformat en de controle op dubbele backlogtitels werken. Dit script is een **offline demonstratie**, niet de onderliggende generatieve Copilot-agent.

\`\`\`bash
python demo/generate.py --input demo/voorbeeldcontext.json
python -m unittest discover -s tests -v
\`\`\`

Dezelfde demo en tests draaien automatisch via [GitHub Actions](.github/workflows/demo-tests.yml).

## De aanpak

| Stap | Inrichting |
|---|---|
| 1. Relevante input bepalen | Gebruikers, businessdoel, Product Goal, Sprint Goal en randvoorwaarden |
| 2. Instructies opbouwen | Waarde en MVP voorop, maximaal drie stories, expliciete aannames |
| 3. Vaardigheden toevoegen | Projectcontext, Scrum, technische context, Sprint 3 en backlogmomentopname |
| 4. Output structureren | Userstory, 3–5 acceptatiecriteria, taken, risico's en testbewijs |
| 5. Beoordelen binnen Scrum | Overlap en haalbaarheid bespreken, feedback vastleggen, zo nodig aanscherpen |

De **doorslaggevende vraag** bij refinement is: *Leveren deze userstory's daadwerkelijk waarde voor de opdrachtgever en dragen ze bij aan een MVP?* De AI doet voorstellen; **het team en de opdrachtgever bepalen** wat bruikbaar is.

## Documentatie

- [Ontwikkelproces](docs/01-ontwikkelproces.md)
- [Promptontwerp en vaardigheden](docs/02-promptontwerp.md)
- [Voorbeeld met fictieve userstory's](docs/03-voorbeelduitvoer.md)
- [Kwaliteitscontrole en Scrum-refinement](docs/04-scrum-refinement.md)
- [Aansluiting op Sprint 3-opdracht](docs/05-sprint3.md)
- [Demo in Sprint Review](docs/06-presentatie.md)
- [Vastgelegde refinementfeedback](docs/07-refinement-terugkoppeling.md)
- [Hoe feedback is verwerkt in de zesde Copilot-skill](docs/08-refinement-skill.md)
- [Userstory-template](templates/userstory.md)
- [Refinementformulier](templates/refinement.md)
- [Publicatiechecklist](PUBLICATIECHECK.md)

## Transparantie

De Copilot-agent is ingericht; de openbare demo toont **uitvoerbare controles met synthetische voorbeelden**. Deze repository doet geen ongeverifieerde uitspraken over opdrachtgevergoedkeuring of reeds gehouden refinements. Echte inhoudelijke feedback en screenshots kunnen zo nodig afzonderlijk, binnen de toegestane onderwijsomgeving, worden ingeleverd.

**Project:** 721 · **Instelling:** Hogeschool Utrecht · **Makers:** Jesmar Oosterom en de overige teamleden.
