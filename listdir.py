import os

path = os.getcwd()
dirs = []
files = []

for item in os.listdir(path):
    if os.path.isdir(item):
	    dirs.append(item)
    elif os.path.isfile(item):
	    files.append(item)

print("-= ПАПКИ: =-")
for i in dirs:
    print(i)

print("-= ФАЙЛЫ: =-")
for i in files:
    print(i)

input("\n-= Для выхода нажмите Enter =-")
