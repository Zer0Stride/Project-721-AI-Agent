# Refinement — ontvangen feedback en verwerking

**Project:** Projectteam 721 · Hogeschool Utrecht  
**Opsteller:** Projectteam 721 — Jesmar Oosterom en overige teamleden  
**Type registratie:** terugblik op ontvangen refinementfeedback, achteraf vastgelegd  
**Datum sessie:** 03-11-2026  
**Aanwezigen:** nog in te vullen

## Aanleiding en doel

Het projectteam gebruikt een AI-agent voor het formuleren van kandidaat-userstory's, acceptatiecriteria en taken. De kwaliteit van die voorstellen wordt binnen het Scrumproces beoordeeld op gebruikerswaarde, bijdrage aan het MVP, haalbaarheid en toetsbaarheid.

Een teamlid heeft bevestigd dat de onderstaande aandachtspunten **inhoudelijk overeenkomen met feedback die het team daadwerkelijk heeft ontvangen**. Het zijn daarom **parafrases van ontvangen feedback**, geen woordelijke citaten of verzonnen scores.

## Teruggekoppelde aandachtspunten

| Onderwerp | Ontvangen feedback, samengevat | Wat dit betekent voor een AI-userstory |
|---|---|---|
| Businesswaarde | Maak duidelijk welk concreet probleem of welke behoefte wordt opgelost. | Vermeld de gebruikersrol, het probleem en het verwachte voordeel. |
| MVP-bijdrage | Houd voorstellen klein en relevant voor de demonstrabele eerste versie. | Splits brede stories op in één observeerbare gebruikershandeling. |
| Acceptatiecriteria | Maak helder welk gedrag of resultaat na een actie zichtbaar moet zijn. | Gebruik toetsbare Given/When/Then-criteria. |
| Bestaand werk | Controleer of vergelijkbaar werk al op de backlog staat. | Verfijn waar nodig een bestaand item in plaats van dubbel werk te creëren. |
| Privacy/testdata | Houd demonstraties gescheiden van echte of vertrouwelijke gegevens. | Werk met synthetische of uitdrukkelijk goedgekeurde testdata. |

## Vertaling naar de agentinstructies

Deze feedback levert de volgende concrete kwaliteitsvoorwaarden op:

1. Laat de agent per story expliciet de **businesswaarde** en **MVP-bijdrage** motiveren.
2. Vraag maximaal drie **kleine kandidaatstories**, niet één groot en vaag werkpakket.
3. Vereis minimaal drie **Given/When/Then-acceptatiecriteria** en uitvoerbare taken.
4. Laat de agent mogelijke **overlap met bestaande backlogtitels** benoemen, met bron en peildatum.
5. Laat hem **aannames, afhankelijkheden en ontbrekende informatie** zichtbaar houden.
6. Laat het **Scrumteam** bepalen welke kandidaatstories echt worden overgenomen.

### Aangescherpte voorbeeldvraag

> Analyseer het businessdoel, de Product Goal en de beschikbare projectcontext. Stel maximaal drie kleine kandidaat-userstory's voor. Benoem per story de concrete gebruikerswaarde, bijdrage aan het MVP, drie toetsbare Given/When/Then-acceptatiecriteria, uitvoerbare taken en afhankelijkheden. Controleer mogelijke overlap met de beschikbare backlog. Maak aannames expliciet en laat definitieve prioritering aan het Scrumteam.

## Voorbeeld van hoe een te brede story wordt aangescherpt

Dit is een **toelichtend voorbeeld met fictieve gegevens** dat laat zien hoe de ontvangen feedback toegepast kan worden. Het wordt niet gepresenteerd als een letterlijk transcript van de sessie.

**Te breed:** 'Als gebruiker wil ik mijn testtaken beheren, zodat ik gemakkelijker kan werken.'

**Concreter:** 'Als onderzoeker wil ik de status van mijn synthetische voorbeeldtesttaak zien, zodat ik weet wanneer de taak klaar is.'

**Voorbeelden van acceptatiecriteria:**

- **Given** een voorbeeldtaak is gestart, **When** ik het statusoverzicht open, **Then** zie ik de huidige taakstatus.
- **Given** een voorbeeldtaak is afgerond, **When** ik de taakdetails open, **Then** staat de afronding zichtbaar aangegeven.
- **Given** een taakcode niet bestaat, **When** ik die open, **Then** verschijnt een begrijpelijke melding.

**Voorbeelden van taken:** statusweergave ontwerpen, fictieve statusgegevens aanbieden, testgevallen voor starten/afronden/fouten uitvoeren.

## Wat is vastgesteld en wat moet nog worden aangevuld?

- **Door teamlid bevestigd:** de vijf aandachtspunten hierboven stemmen overeen met daadwerkelijk ontvangen feedback.
- **Niet gedocumenteerd in deze repository:** datum en volledige aanwezigenlijst van die sessie, originele notulen en woordelijke uitspraken.
- **Niet automatisch bewezen door dit verslag:** dat de Copilot-agent tijdens die specifieke sessie is gedemonstreerd, dat precies deze voorbeeldstory toen is gegenereerd of dat een wijziging door de opdrachtgever is goedgekeurd.

Om de Sprint 3-eis **'bespreek de agent tijdens refinement'** aantoonbaar te maken, kan het team de echte datum, de aanwezigen, de besproken agentoutput en de genomen besluiten toevoegen zodra die gegevens zijn gecontroleerd.

## Conclusie

De ontvangen feedback is concreet vertaald naar criteria waarmee Projectteam 721 kandidaat-userstory's uit de AI-agent beoordeelt en gericht kan verbeteren. **Businesswaarde en MVP-bijdrage** blijven doorslaggevend; de agent ondersteunt het refinement, maar neemt geen Scrum-besluiten over.

**Publicatie:** dit verslag bevat alleen algemene, niet-vertrouwelijke formuleringen. Voeg geen interne documenten, persoonsgebonden notulen of vertrouwelijke screenshots toe aan de openbare repository.
