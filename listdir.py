import os

dirs = []
files = []

for item in os.listdir(os.getcwd()):
    if os.path.isdir(item):
        dirs.append(item)
    elif os.path.isfile(item):
        files.append(item)

print("\n-= ПАПКИ: =-")
for item in dirs:
    print(item)

print("\n-= ФАЙЛЫ: =-")
for item in files:
    print(item)

input("\n-= Для выхода нажмите Enter =-")
