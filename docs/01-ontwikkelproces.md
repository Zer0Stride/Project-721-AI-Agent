# Ontwikkelproces van de AI-agent

## Waarom deze agent?

De Sprint 3-opdracht vraagt om een organisatiespecifieke agent die op basis van businessdoelen en Product Goal **bruikbare kandidaat-userstory's met acceptatiecriteria en taken** oplevert. Het doel is niet om automatisch zoveel mogelijk issues te maken, maar om de kwaliteit van refinement te verbeteren.

## 1. Inputselectie

De agent is ontworpen rond deze contextsoorten:

| Input | Waarom relevant? |
|---|---|
| Organisatie-/gebruikersprofiel | Welke gebruiker heeft werkelijk een behoefte? |
| Businessdoel | Wat is de concrete waarde van de story? |
| Product Goal | Hoe past de story binnen het product? |
| Sprint Goal, indien bekend | Wat is voor deze sprint relevant en haalbaar? |
| Technische context | Welke randvoorwaarden en afhankelijkheden bestaan er? |
| Bestaande backlogitems | Hoe voorkomen we dubbele taken? |
| Feedback uit refinement | Welke aanname of instructie moet beter? |

De achterliggende projectbestanden blijven in de afgeschermde werkomgeving. In deze repository staan **alleen fictieve voorbeelden**.

## 2. Agentconfiguratie

In Microsoft 365 Copilot Agent Builder is een agent met een eigen identiteit, instructies, drie voorgestelde prompts en vijf gespecialiseerde basisskills opgezet. Naar aanleiding van ontvangen refinementfeedback is een zesde aanvullende vaardigheid voorbereid.

De skills verdelen het werk in projectcontext, Scrum-refinement, technische aandachtspunten, Sprint 3-kwaliteitscontrole en een gedateerde backlogmomentopname.

## 3. Genereren

De agentinstructies sturen op maximaal drie kandidaatstories met een herkenbare gebruikersrol, toetsbare acceptatiecriteria en kleine uitvoerbare taken. Ook moet de agent onderscheid maken tussen bekende informatie en aannames.

## 4. Beoordelen en verbeteren

Voor een bruikbare story zijn **businesswaarde, MVP-bijdrage, testbaarheid, haalbaarheid en geen onnodige overlap** belangrijker dan een mooi geformuleerde tekst. In een refinement toetst het team de AI-output met een vaste scorekaart. Feedback kan leiden tot verduidelijkte context, een aangepast prompt en een tweede generatie.

## 5. Zichtbaar maken

De openbare voorbeeldcase en GitHub Actions-tests tonen een herhaalbaar outputformat. Voor de feitelijke inzet van de Copilot-agent gebruikt het team de afgeschermde Copilot-omgeving en het eigen Scrumproces.
