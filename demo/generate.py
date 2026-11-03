#!/usr/bin/env python3
"""Offline demo met fictieve gegevens. Dit script is niet de generatieve Copilot-agent."""
from __future__ import annotations

import argparse
from difflib import SequenceMatcher
import json
from pathlib import Path
import re

DEFAULT_INPUT = Path(__file__).with_name("voorbeeldcontext.json")

STORY_TEMPLATES = [
    {
        "title": "Een testtaak starten met synthetische gegevens",
        "role": "onderzoeker",
        "need": "een voorbeeldtesttaak kunnen starten",
        "value": "ik minder handmatige stappen hoef te doorlopen",
        "business_value": "Een eenvoudige startflow verlaagt de instapdrempel.",
        "mvp_value": "Demonstreert de eerste gebruikershandeling.",
        "criteria": [
            ("het startscherm zichtbaar is", "ik een nieuwe taak kies", "een invoerformulier verschijnt"),
            ("een geldige synthetische dataset geselecteerd is", "ik de taak start", "een herkenbare taakstatus ontstaat"),
            ("de invoer onvolledig is", "ik op Start klik", "een duidelijke validatiemelding verschijnt"),
        ],
        "tasks": ["Maak een klein startformulier.", "Voeg validatie voor de voorbeeldinvoer toe.", "Test de startflow met synthetische gegevens."],
    },
    {
        "title": "De voortgang van een testtaak bekijken",
        "role": "onderzoeker",
        "need": "de status van mijn voorbeeldtesttaak zien",
        "value": "ik weet wanneer de taak klaar is",
        "business_value": "Voortgangsinzicht vermindert onnodig navragen.",
        "mvp_value": "Maakt de gebruikersflow van starten tot resultaat zichtbaar.",
        "criteria": [
            ("een voorbeeldtaak gestart is", "ik het statusoverzicht open", "ik de actuele voorbeeldstatus zie"),
            ("de voorbeeldtaak afgerond is", "ik de details open", "de afronding zichtbaar is"),
            ("de taak niet gevonden wordt", "ik het overzicht open", "een begrijpelijke foutmelding verschijnt"),
        ],
        "tasks": ["Ontwerp een eenvoudige statusweergave.", "Lever een vaste verzameling voorbeeldstatussen.", "Test de weergave voor starten, afronden en fouten."],
    },
    {
        "title": "Een synthetische dataset selecteren",
        "role": "onderzoeker",
        "need": "een goedgekeurde synthetische voorbeelddataset kiezen",
        "value": "ik geen echte persoonsgegevens nodig heb voor de demonstratie",
        "business_value": "Een veilige demo met testmateriaal vermindert risico's.",
        "mvp_value": "Ondersteunt een reproduceerbare voorbeeldflow.",
        "criteria": [
            ("het selectieformulier beschikbaar is", "ik de datasetlijst open", "uitsluitend vooraf ingestelde synthetische voorbeelden verschijnen"),
            ("een synthetische dataset gekozen is", "ik de selectie bevestig", "de gekozen dataset zichtbaar is"),
            ("een niet-toegestane waarde wordt opgegeven", "ik de keuze verstuur", "de invoer geweigerd wordt"),
        ],
        "tasks": ["Lever een kleine fictieve datasetlijst.", "Beperk keuzes tot voorbeelddatasets.", "Test dat onbekende datasetnamen worden geweigerd."],
    },
]


def normalize(value: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", str(value).lower()))


def match_existing(title: str, backlog: list[dict]) -> dict | None:
    best = None
    for item in backlog:
        candidate = str(item.get("titel", ""))
        if not candidate:
            continue
        ratio = SequenceMatcher(None, normalize(title), normalize(candidate)).ratio()
        if best is None or ratio > best["similarity"]:
            best = {"title": candidate, "status": item.get("status", "Onbekend"), "similarity": round(ratio, 3)}
    return best if best and best["similarity"] >= 0.72 else None


def generate(context: dict) -> dict:
    if context.get("fictief") is not True:
        raise ValueError("Deze openbare demo accepteert uitsluitend expliciet fictieve gegevens.")
    required = ("businessdoel", "product_goal", "sprintdoel", "bestaande_backlog")
    if any(not context.get(key) for key in required):
        raise ValueError("Verplichte fictieve context ontbreekt.")
    backlog = context["bestaande_backlog"]
    if not isinstance(backlog, list):
        raise ValueError("bestaande_backlog moet een lijst zijn.")
    generated, overlaps = [], []
    for template in STORY_TEMPLATES:
        existing = match_existing(template["title"], backlog)
        if existing:
            overlaps.append({"candidate": template["title"], "existing": existing})
            continue
        generated.append({
            "title": template["title"],
            "userstory": f"Als {template['role']} wil ik {template['need']}, zodat {template['value']}.",
            "business_value": template["business_value"],
            "mvp_value": template["mvp_value"],
            "acceptance_criteria": [
                f"Given {given}, When {when}, Then {then}."
                for given, when, then in template["criteria"]
            ],
            "tasks": template["tasks"],
            "status": "Kandidaat voor refinement — niet goedgekeurd",
        })
    return {
        "example_only": True,
        "business_goal": context["businessdoel"],
        "product_goal": context["product_goal"],
        "sprint_goal": context["sprintdoel"],
        "stories": generated[:3],
        "possible_duplicates": overlaps,
    }


def to_markdown(result: dict) -> str:
    parts = [
        "# FICTIEVE DEMO — kandidaat-userstory's",
        "",
        "**Dit is offline voorbeelduitvoer, geen transcript van Copilot.**",
        "",
        f"**Businessdoel:** {result['business_goal']}",
        f"**Product Goal:** {result['product_goal']}",
        f"**Sprintdoel:** {result['sprint_goal']}",
    ]
    for index, story in enumerate(result["stories"], 1):
        parts += [
            "", f"## {index}. {story['title']}", "",
            story["userstory"], "",
            f"**Businesswaarde:** {story['business_value']}",
            f"**MVP-bijdrage:** {story['mvp_value']}",
            "**Acceptatiecriteria:**",
            *[f"- {criterion}" for criterion in story["acceptance_criteria"]],
            "**Taken:**",
            *[f"- [ ] {task}" for task in story["tasks"]],
            f"**Status:** {story['status']}",
        ]
    parts += ["", "## Mogelijke bestaande items"]
    if result["possible_duplicates"]:
        for duplicate in result["possible_duplicates"]:
            e = duplicate["existing"]
            parts.append(f"- {duplicate['candidate']}: lijkt op '{e['title']}' (status: {e['status']}); niet opnieuw voorstellen zonder refinement.")
    else:
        parts.append("- Geen sterke titeloverlap gevonden in de fictieve voorbeeldbacklog.")
    parts += ["", "**Vervolg:** bespreek waarde, MVP, haalbaarheid en acceptatiecriteria in refinement."]
    return "\n".join(parts) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Veilige, fictieve refinement-demo")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    args = parser.parse_args()
    context = json.loads(args.input.read_text(encoding="utf-8"))
    result = generate(context)
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.format == "json" else to_markdown(result))


if __name__ == "__main__":
    main()
