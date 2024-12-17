import json
import csv

file_path = 'openings.json'
with open(file_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)
items = json_data['items']

with open("test.csv", "w", encoding="utf-8", newline="") as csvfile:
    f = csv.writer(csvfile)
    f.writerow(["company", "title", "quota", "wage", "working_condition", "tags", "selected"])

    for item in items:
        tags = ', '.join(tag["tagName"] for tag in item["tags"])
        f.writerow([
            item["company"]["companyNameTh"],
            item["title"],
            item["quota"],
            item["compensationAmount"],
            item["workingCondition"],
            tags,
            item["inStudentDraftCount"]
        ])
