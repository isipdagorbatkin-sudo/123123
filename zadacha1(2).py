import json

country = {
    "название": "Япония",
    "столица": "Токио",
    "население": 125800000
}

with open("country.json", "w", encoding="utf-8") as file:
    json.dump(country, file, ensure_ascii=False, indent=4)
