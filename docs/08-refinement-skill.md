# Refinementfeedback toegepast in nieuwe Copilot-vaardigheid

**Projectteam 721 — Hogeschool Utrecht**  
**Refinementdatum:** 3 november 2026  
**Aanwezigen:** volgens de teamopgave het volledige projectteam.

## Van ontvangen feedback naar een nieuwe skill

Naar aanleiding van de inhoudelijk bevestigde feedback is een **zesde vaardigheid** ontworpen voor de Microsoft 365 Copilot-agent: **`refinement-feedback-721`**.

Deze vaardigheid vult de vijf oorspronkelijke specialisaties aan. Hij verandert de kwaliteitscontrole die de agent uitvoert bij het genereren, verbeteren of vergelijken van kandidaat-userstory's.

| Teruggekoppeld aandachtspunt | Verwerkt in de zesde skill |
|---|---|
| Maak businesswaarde concreet | Iedere story krijgt een specifieke gebruiker, behoefte en waarde. |
| Houd rekening met het MVP | Iedere story moet één zichtbare, kleine MVP-bijdrage beschrijven. |
| Formuleer toetsbare criteria | Minimaal drie Given/When/Then-acceptatiecriteria, waar zinvol met foutpad. |
| Vermijd dubbel werk | Eerst zoeken naar mogelijke overlap met beschikbare backlogtitels. |
| Gebruik veilige testdata | Alleen synthetische of uitdrukkelijk goedgekeurde gegevens in demonstraties. |

## Hoe de agent de feedback gebruikt

1. Bepaal relevante context: businessdoel, Product Goal en eventueel Sprint Goal.
2. Controleer mogelijke overlap met een beschikbare backlogmomentopname.
3. Genereer maximaal drie **kandidaatstories** met acceptatiecriteria en taken.
4. Beoordeel waarde, MVP-bijdrage, testbaarheid, omvang, overlap en randvoorwaarden (0–2 per criterium, of 'onbekend').
5. Stel bij onvoldoende waarde of MVP-bijdrage een scherpere story voor.
6. Presenteer een wijziging als `v1 → feedback → aangescherpte instructie → v2`.

## Voorbeeld van de verbetering

**Voor:** 'Als gebruiker wil ik testtaken beheren, zodat ik makkelijker kan werken.'

**Na:** 'Als onderzoeker wil ik de status van een synthetische voorbeeldtaak zien, zodat ik weet wanneer het resultaat beschikbaar is.'

Het uitgewerkte voorbeeld bevat daarna observeerbare criteria voor een lopende, afgeronde en niet-bestaande voorbeeldtaak. De voorbeeldstory is fictief; de algemene feedbackpunten zijn door een teamlid als daadwerkelijk ontvangen bevestigd.

## Beschikbaarheid

De zesde skill wordt als afzonderlijk ZIP-bestand (`SKILL.md` plus ondersteunende tekstbestanden) geüpload via **Microsoft 365 Copilot → Agent bewerken → Vaardigheden → Toevoegen**. De projectinterne vaardigheidsbestanden blijven buiten deze voor openbare inzage bedoelde repository.

**Status:** skillpakket ontworpen en als ZIP opgebouwd. De daadwerkelijke upload, activering en uitkomsten in Microsoft 365 Copilot zijn alleen controleerbaar in de agentomgeving zelf; deze repo claimt die stap niet al te hebben uitgevoerd.

Zie [vastgelegde refinementfeedback](07-refinement-terugkoppeling.md) voor de bron van deze aanscherping.
