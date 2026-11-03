# Testresultaat — Copilot-agent en MVP-gerichte userstory's

**Projectteam 721 · Hogeschool Utrecht**  
**Datum van de aangeleverde testuitvoer:** 3 november 2026  
**Type test:** inhoudelijke controle van een door het projectteam aangeleverd antwoord van de Microsoft 365 Copilot-agent  
**Privacy:** dit document bevat uitsluitend een beperkte, geanonimiseerde samenvatting; de originele output en afgeschermde projectgegevens zijn niet gepubliceerd.

## Testdoel

Controleren of de ingerichte Copilot-agent op basis van businessdoelen, Product Goal, een voorlopige MVP-hypothese en de beschikbare context:

1. relevante bestaande backlogitems kan aanwijzen;
2. kleine, waardevolle kandidaat-userstory's opstelt;
3. toetsbare acceptatiecriteria en uitvoerbare taken levert;
4. dubbel werk voorkomt door bestaande taken als mogelijke verfijningspunten te herkennen;
5. businesswaarde en MVP-bijdrage kritisch beoordeelt.

## Geobserveerde uitvoer

| Controlepunt | Resultaat in aangeleverde Copilot-uitvoer | Beoordeling |
|---|---|---|
| Bestaande backlog | Vijf relevante items met status en peildatum herkend | Geslaagd; gecontroleerd tegen beschikbare momentopname |
| Storyvoorstellen | Twee kandidaatstories, ieder gericht op één hoofdbehoefte | Geslaagd |
| Acceptatiecriteria | Vijf Given/When/Then-criteria per story | Geslaagd |
| Taken | Meerdere taken, verdeeld over relevante teamdisciplines | Geslaagd |
| Waarde en MVP | Beide stories onderbouwd met verwachte waarde en bijdrage | Geslaagd als *onderbouwing*; nog geen bewijs van gerealiseerde waarde |
| Dubbel werk | De agent adviseert bestaande backlogitems te verfijnen, niet te dupliceren | Geslaagd |
| Risico's en aannames | Gegevensveiligheid, toegangsrechten, testgegevens en open vragen vermeld | Geslaagd; de technische resultaten zijn niet uitgevoerd of bewezen door deze AI-output |

## Door de agent berekende scores

De agent gaf de twee kandidaatstories respectievelijk **10/12** en **11/12** op een eigen zesdelige scorekaart.

**Belangrijk:** dit zijn **zelfbeoordelingen van het taalmodel**. Een hoge score toont dat het model de aangeleerde beoordelingscriteria toepast; de scores zijn geen onafhankelijke validatie, gebruikersacceptatie of bewijs dat een technische implementatie werkt.

## Kritische controle door het projectteam

**Sterk aan de output**
- De agent formuleert een zichtbare gebruikersbehoefte met een reden (*Als / wil ik / zodat*).
- De acceptatiecriteria zijn grotendeels observeerbaar en bevatten ook negatieve scenario's.
- Er is expliciete koppeling met de voorlopige MVP-hypothese.
- De agent herkent een waarschijnlijk duplicaat en adviseert refinement van een bestaand item.
- Open vragen en aannames worden niet stilzwijgend als definitieve eisen behandeld.

**Nog scherp te houden**
- **Haalbaarheid:** de agent mag geen maximale score geven zonder informatie over beschikbare infrastructuur, capaciteit en planning.
- **Veiligheid:** beschreven controles en geplande testen zijn nog geen uitgevoerd testbewijs.
- **Status:** een gedateerde momentopname is geen actuele bevestiging van het Scrumboard.
- **Opmaak:** de geplakte uitvoer bevat enkele onvolledig weergegeven bronverwijzingen en samengevallen tabellen. Voor inlevering kan de tekst opnieuw worden geëxporteerd of netjes worden opgemaakt.

## Oordeel ten opzichte van de Sprint 3-vraag

> Leveren de gegenereerde userstory's echt waarde en dragen ze bij aan het MVP?

**Voorlopig: ja, inhoudelijk is dat aannemelijk.** Beide kandidaatstories beschrijven een concreet gebruikers- of kwaliteitsdoel en passen binnen de gekozen *MVP-hypothese*. De agent toont bovendien dat hij mogelijke backlogoverlap meeweegt.

Het daadwerkelijke oordeel over de afgesproken MVP, prioriteit en gerealiseerde waarde blijft bij het projectteam en bevoegde betrokkenen. Deze test is **geen bewijs van implementatie, productiegeschiktheid of formele goedkeuring**.

## Wat dit aantoont

Dit testresultaat laat zien dat de **werkelijke Copilot-agent** een inhoudelijk gestructureerd antwoord kon produceren met bestaande werkzaamheden, twee kandidaatstories, acceptatiecriteria, taken, een scorekaart en vervolgvragen. Dit is **een andere test** dan de automatische Python-demonstratie in dezelfde repository.

**Herkomst:** originele, door een teamlid aangeleverde tekstuitvoer uit Copilot; op deze openbare pagina zijn geen volledige prompts, interne bronnen, privélocaties of vertrouwelijke documentdetails overgenomen.

**Makers:** Jesmar Oosterom en de overige leden van Projectteam 721, Hogeschool Utrecht.
