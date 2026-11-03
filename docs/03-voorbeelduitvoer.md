# Werkend voorbeeld: fictieve userstory's

Deze case gaat over een **volledig fictieve demonstratieomgeving**. De voorbeeldgegevens zijn te vinden in [voorbeeldcontext.json](../demo/voorbeeldcontext.json).

## Context

- **Businessdoel:** minder handmatige stappen en duidelijkere voortgang.
- **Product Goal:** eenvoudige omgeving om testtaken met synthetische gegevens te starten en volgen.
- **Sprintdoel:** een doorlopende demonstratie van starten tot resultaat.
- **Backlog:** een paar fictieve voorbeeldtitels.

## Uitvoerbare demonstratie

```bash
python demo/generate.py --input demo/voorbeeldcontext.json
```

De demo produceert kleine stories met:

- een duidelijke gebruiker en de reden voor de behoefte;
- expliciete businesswaarde en MVP-bijdrage;
- drie **Given/When/Then**-criteria;
- uitvoerbare taken;
- signalering van vergelijkbare backlogtitels.

**Voorbeeldstory:**

> **Als** onderzoeker **wil ik** de voortgang van mijn voorbeeldtesttaak zien, **zodat** ik weet wanneer het resultaat beschikbaar is.

**Acceptatiecriterium:**  
**Given** een voorbeeldtesttaak is gestart, **When** de gebruiker het statusoverzicht opent, **Then** wordt de actuele voorbeeldstatus zichtbaar.

**Taken:** ontwerp een statusweergave, geef teststatussen terug en leg een reproduceerbare statuscontrole vast.

## Geautomatiseerde controle

```bash
python -m unittest discover -s tests -v
```

De tests controleren het storyformat, de aanwezigheid van acceptatiecriteria, duplicate-detectie en de eis dat de demo alleen fictieve gegevens verwerkt.

> **Let op:** het Python-script is een herhaalbare demonstratie van outputstructuur en validatie. **De generatieve agent draait apart in Microsoft 365 Copilot.**
