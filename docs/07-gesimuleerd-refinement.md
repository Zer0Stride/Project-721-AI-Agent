# Gesimuleerd refinement — uitgewerkt demonstratievoorbeeld

> **Status: OEFENVOORBEELD / SIMULATIE.** Dit document beschrijft geen daadwerkelijk gehouden gesprek met een opdrachtgever. De feedback, rollen, scores en besluiten hieronder zijn fictief en dienen uitsluitend om de werking van de AI-agent en de kwaliteitscontrole te demonstreren.
>
> **Projectteam:** Projectteam 721, Hogeschool Utrecht · Jesmar Oosterom en overige teamleden.  
> **Casus:** een fictief portaal voor testtaken met synthetische gegevens.  
> **Bron:** openbare, fictieve demo in `demo/voorbeeldcontext.json` en `demo/generate.py`.

## Doel van deze oefening

Laten zien hoe een AI-agent een kandidaat-userstory omzet in een toetsbaar voorstel en hoe een *gesimuleerde refinementronde* dit voorstel verbetert op basis van businesswaarde, MVP-bijdrage, haalbaarheid en acceptatiecriteria.

**Businessdoel (fictief):** verminder handmatige stappen en maak de voortgang van testtaken inzichtelijk.  
**Product Goal (fictief):** een eenvoudige omgeving om testtaken met synthetische gegevens te starten en te volgen.  
**Sprintdoel (fictief):** toon een gebruikersflow van start tot resultaat.

## 1. Eerste concept (v1)

**Kandidaat-userstory:**

> Als onderzoeker wil ik mijn testtaken beheren, zodat ik eenvoudiger kan werken.

**Voorgestelde taken:**
- Een scherm voor testtaken maken.
- Gegevens koppelen.
- De gebruikersflow testen.

**Kritische beoordeling:** deze story is te breed en onduidelijk. "Beheren" is niet observeerbaar genoeg om goed te testen. De gebruiker en waarde zijn benoemd, maar niet concreet gekoppeld aan een kleine MVP-demonstratie.

## 2. Fictieve feedbackronde

Deze feedback is **geconstrueerd voor het voorbeeld** en is dus **niet afkomstig van een werkelijke opdrachtgever of teamvergadering**.

| Onderwerp | Gesimuleerde feedback | Verbeteractie |
|---|---|---|
| Businesswaarde | "Wat levert dit de gebruiker concreet op?" | Focus op minder onduidelijkheid over voortgang. |
| MVP-bijdrage | "Maak de story klein genoeg voor een demo." | Alleen status bekijken; starten van taken is een andere story. |
| Acceptatiecriteria | "Wat is precies zichtbaar na een actie?" | Drie Given/When/Then-criteria met verwachte uitkomst. |
| Backlogoverlap | "Controleer of er al een vergelijkbare taak bestaat." | Vergelijk titels en verfijn een bestaand item in plaats van dubbel aanmaken. |
| Privacy | "Gebruik voor deze demonstratie geen echte gegevens." | Uitsluitend synthetische testdata. |

### Beoordelingsmatrix — fictieve oefenscores

Score: **0 = onvoldoende, 1 = deels, 2 = voldoende**.

| Criterium | Concept v1 | Verbeterd v2 |
|---|---:|---:|
| Gebruikers-/businesswaarde | 1 | 2 |
| Bijdrage aan Product Goal en MVP | 1 | 2 |
| Toetsbare acceptatiecriteria | 0 | 2 |
| Kleine en haalbare scope | 0 | 2 |
| Voorkomen van backlogoverlap | 1 | 2 |
| Rekening houden met randvoorwaarden | 1 | 2 |
| **Totaal** | **4/12** | **12/12** |

Deze cijfers zijn **illustratieve oefenscores**, geen echte beoordeling.

## 3. Aangescherpte agentinstructie (demonstratie)

**Voorbeeldverbetering van de prompt:**

> Genereer maximaal drie kleine kandidaat-userstory's voor het fictieve Product Goal. Beschrijf per story één observeerbare gebruikershandeling, concreet gebruikersvoordeel en bijdrage aan de MVP. Voeg drie Given/When/Then-acceptatiecriteria, uitvoerbare taken, afhankelijkheden en testbewijs toe. Controleer eerst of de story al lijkt op een bestaande backlogtitel. Gebruik uitsluitend synthetische testdata en vermeld dat elke story een kandidaat is die nog door het team beoordeeld moet worden.

Deze tekst is een **voorbeeld van promptaanscherping**. Het is geen bewering dat de configuratie van de werkelijke Copilot-agent na een echte refinement is gewijzigd.

## 4. Verbeterd voorstel (v2)

**Titel:** De voortgang van een testtaak bekijken.

**Userstory:**

> Als onderzoeker wil ik de status van mijn voorbeeldtesttaak zien, zodat ik weet wanneer de taak klaar is.

**Businesswaarde:** de gebruiker hoeft niet telkens handmatig naar de status te vragen.  
**MVP-bijdrage:** maakt de fictieve gebruikersflow van starten tot resultaat zichtbaar.

### Acceptatiecriteria

1. **Given** een synthetische voorbeeldtaak is gestart, **When** de gebruiker het statusoverzicht opent, **Then** ziet de gebruiker de actuele voorbeeldstatus.
2. **Given** een synthetische voorbeeldtaak is afgerond, **When** de gebruiker de details opent, **Then** wordt de afronding duidelijk getoond.
3. **Given** een opgegeven voorbeeldtaak niet bestaat, **When** de gebruiker het overzicht probeert te openen, **Then** verschijnt een begrijpelijke foutmelding zonder technische details.

### Uitvoerbare taken

- [ ] Een eenvoudige statusweergave ontwerpen.
- [ ] Vaste fictieve statussen leveren: *gepland*, *actief*, *afgerond*, *mislukt*.
- [ ] Testgevallen maken voor de vier statussen en een ontbrekende taak.
- [ ] De criteria demonstreren met uitsluitend synthetische gegevens.

**Afhankelijkheid:** een testtaak moet eerst een herkenbare identificatie hebben.  
**Testbewijs:** een demonstratie waarin alle statussen en de foutmelding zichtbaar zijn.  
**Backlogoverlap:** in de opgegeven voorbeeldbacklog is geen gelijknamige statusstory gevonden; titelvergelijking alleen bewijst geen inhoudelijke uniciteit.

## 5. Uitkomst van de simulatie

| Vraag | Uitkomst van de oefening |
|---|---|
| Is de oorspronkelijke story al klein en testbaar? | **Nee** — de scope was te breed. |
| Is de verbeterde story geschikt als kandidaat voor een MVP? | **Ja, in dit fictieve scenario** — duidelijke waarde en testbare scope. |
| Mag de agent deze story zelfstandig definitief goedkeuren? | **Nee** — het Scrumteam neemt dat besluit. |
| Is hier een echte opdrachtgever-refinement aangetoond? | **Nee** — dit is uitsluitend een simulatie. |

### Wat laat dit voorbeeld aantoonbaar zien?

Het laat zien **hoe je AI-output kritisch beoordeelt, versmalt en omzet naar acceptatiecriteria en taken**. De automatische testbare offline demonstratie staat in `demo/generate.py`; dit document is een handmatig uitgewerkt **voorbeeld van een refinementronde**.

Voor bewijs van een daadwerkelijk gehouden sessie moet het team de echte datum, aanwezigen, feedback en besluiten apart vastleggen, zonder vertrouwelijke gegevens openbaar te maken.
