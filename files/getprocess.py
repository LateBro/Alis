import psutil
list_id_process = psutil.pids()
string = ''
for s in list_id_process:
    _ = psutil.Process(s)
    string += f'Process:  {_.name()}\nid: {s}\n'
print(string)
input()