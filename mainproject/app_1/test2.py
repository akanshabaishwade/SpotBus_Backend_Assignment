time = 300

data = [
    {"actions": ["16240460244e2bfcad"], "start_time": 0},
    {"actions": ["1623967784bedf7e11"], "start_time": 150},
    {"actions": ["16240415523fcd04b1"], "start_time": 500},
    {"actions": ["16239672904b3607eb"], "start_time": 600},
    {"actions": ["162404650463d27dc4"], "start_time": 700},
    {"actions": ["16573026045da7c3bd"], "start_time": 1000},
]

students = [
    {"id": "16573026045da7c3bd", "name": "Sagar"},
    {"id": "1623967784bedf7e11", "name": "Bean"}
]

for i in data:
    actions = i[actions]
    for j in students:
        id = j[id]
        for action in actions:
            if action == id:
                store = [{"id": id, "name": "name", "stop_no": "start_time"}]
            else:
                pass



