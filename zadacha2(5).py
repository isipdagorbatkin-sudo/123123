import csv
import json

# Данные
data = [
    {'name': 'Bobik', 'class': 'dog', 'age': 5},
    {'name': 'valera', 'class': 'slon', 'age': 6},
    {'name': 'Dimon', 'class': 'papugay', 'age': 2}
]

# Создаем animals.csv
with open('animals.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

# Читаем CSV и сохраняем в JSON
with open('animals.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    animals = list(reader)

with open('zoo.json', 'w', encoding='utf-8') as file:
    json.dump(animals, file, ensure_ascii=False, indent=4)

print('animals.csv и zoo.json созданы')
