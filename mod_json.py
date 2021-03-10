import json
import re

with open('risou.json', mode='r', encoding='utf-8') as f:
    session = json.load(f)

new_dict = {
    "day1": {
        "1": [],
        "2": [],
        "3": [],
        "4": []
    },
    "day2": {
        "1": [],
        "2": [],
        "3": [],
        "4": []
    },
    "day3": {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": []
    }
}

for k, v in session.items():
    s = re.search(r"(day[0-9])_([0-9])", k)
    day = s.group(1)
    num = s.group(2)
    new_dict[day][num] = v
with open('final.json', mode='w', encoding='utf-8') as f:
    json.dump(new_dict, f, ensure_ascii=False)
# print(json.dumps(new_dict, indent=2, ensure_ascii=False))