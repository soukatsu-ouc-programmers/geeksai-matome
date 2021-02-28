import json

def modify(room, session):
    with open(f'{room}/{session}.json', mode='r', encoding='utf-8') as f:
        data = json.load(f)
    # 付けたし
    new_dict = {'title': '', 'speaker': '', 'tweet': data}
    with open(f'{room}/{session}.json', mode='w', encoding='utf-8') as f:
        json.dump(new_dict, f, ensure_ascii=False)

for room in ['rooma', 'roomb', 'roomc']:
    for i in range(12):
        modify(room, f'session_{i+1}')