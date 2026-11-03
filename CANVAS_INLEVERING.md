# Canvas-inlevering — Sprint 3 AI-agent

**Projectteam 721 · Hogeschool Utrecht**  
**Makers:** Jesmar Oosterom en de overige leden van Projectteam 721.

## Titel

Organisatiespecifieke AI Backlog Refinement Agent — Sprint 3

## Beschrijving voor Canvas

Voor Sprint 3 heeft Projectteam 721 een organisatiespecifieke AI-agent gebouwd in **Microsoft 365 Copilot**. De agent helpt het Scrumteam om businessdoelen en de Product Goal om te zetten naar **kandidaat-userstory's, acceptatiecriteria (Given/When/Then) en uitvoerbare taken**.

Voor de agent zijn **zes vaardigheden** ingericht: projectcontext, Scrum/refinement, technische randvoorwaarden, Sprint 3-kwaliteitscontrole, een gedateerde backlogmomentopname en een aanvullende vaardigheid waarin ontvangen refinementfeedback is verwerkt. Daarnaast zijn drie voorgestelde prompts ingesteld om snel userstory's te genereren, bestaand werk te analyseren en refinements voor te bereiden.

Tijdens het refinement van **3 november 2026** zijn aandachtspunten teruggegeven over het concreet maken van businesswaarde, het koppelen van stories aan een MVP, het scherp formuleren van acceptatiecriteria, het voorkomen van dubbel werk en het veilig gebruiken van testdata. Deze aandachtspunten zijn vervolgens vertaald naar aanvullende instructies in de zesde vaardigheid.

De echte Copilot-agent is getest met een MVP-gerichte opdracht. De aangeleverde output bevatte **twee kandidaat-userstory's, vijf acceptatiecriteria per story, taken per discipline, controle op mogelijke backlogoverlap en een kritische MVP-beoordeling**. De inhoudelijke beoordeling is in geanonimiseerde vorm vastgelegd. De scores van de agent zijn daarbij nadrukkelijk **geen onafhankelijk bewijs van werkelijke MVP-acceptatie**.

De GitHub-repository beschrijft de aanpak, promptopbouw en feedbackverwerking en bevat daarnaast een **reproduceerbare offline demonstratie met fictieve gegevens**. De bijbehorende geautomatiseerde tests zijn geslaagd. Vertrouwelijke projectdocumentatie en interne backloggegevens zijn niet opgenomen in de openbare demonstratie.

### Link naar de repository

https://github.com/Zer0Stride/Project-721-AI-Agent

### Belangrijkste onderdelen voor de beoordeling

- [README: projectoverzicht](README.md)
- [Ontwikkelproces](docs/01-ontwikkelproces.md)
- [Promptontwerp en zes vaardigheden](docs/02-promptontwerp.md)
- [Refinementfeedback](docs/07-refinement-terugkoppeling.md)
- [Feedback verwerkt in zesde skill](docs/08-refinement-skill.md)
- [Geanonimiseerd resultaat van echte Copilot-test](docs/09-copilot-testresultaat.md)
- [Uitvoerbare demonstratie](demo/generate.py)
- [Automatische tests](tests/test_generate.py)
