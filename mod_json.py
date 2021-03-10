import json
import re

with open('session_mod.json', mode='r', encoding='utf-8') as f:
    session = json.load(f)

new_dict = {
    "day1": {
        "1": {
            "startTime": "13:30",
            "endTime": "14:30",
            "sessions": []
        },
        "2": {
            "startTime": "14:40",
            "endTime": "15:40",
            "sessions": []
        },
        "3": {
            "startTime": "15:50",
            "endTime": "16:50",
            "sessions": []
        },
        "4": {
            "startTime": "17:00",
            "endTime": "18:00",
            "sessions": []
        }
    },
    "day2": {
        "1": {
            "startTime": "13:30",
            "endTime": "14:30",
            "sessions": []
        },
        "2": {
            "startTime": "14:40",
            "endTime": "15:40",
            "sessions": []
        },
        "3": {
            "startTime": "15:50",
            "endTime": "16:50",
            "sessions": []
        },
        "4": {
            "startTime": "17:00",
            "endTime": "18:00",
            "sessions": []
        }
    },
    "day3": {
        "1": {
            "startTime": "11:00",
            "endTime": "12:00",
            "sessions": []
        },
        "2": {
            "startTime": "13:30",
            "endTime": "14:30",
            "sessions": []
        },
        "3": {
            "startTime": "14:40",
            "endTime": "15:40",
            "sessions": []
        },
        "4": {
            "startTime": "15:50",
            "endTime": "16:50",
            "sessions": []
        },
        "5": {
            "startTime": "17:00",
            "endTime": "18:00",
            "sessions": []
        }
    }
}

for k, v in session.items():
    s = re.search(r"(day[0-9])_([0-9])", k)
    day = s.group(1)
    num = s.group(2)
    new_dict[day][num]["sessions"] = v
with open('final.json', mode='w', encoding='utf-8') as f:
    json.dump(new_dict, f, ensure_ascii=False)
# print(json.dumps(new_dict, indent=2, ensure_ascii=False))
