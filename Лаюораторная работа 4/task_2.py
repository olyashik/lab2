import json
# TODO решите задачу
filename = 'input.json'
def task() -> float:
    file = open(filename, mode='r', encoding='utf-8')
    rows = json.load(file)
    result = 0
    for piece in rows:
        result += piece['score']*piece['weight']
    return round(result, 3)


print(task())
