import os
import sys
import json

path = '.'

RED = '\033[0;31m'
NC = '\033[0m'

if len(sys.argv) == 1:
    print(r"usage: python checknames.py {work-dir}")
    if input("Would you link to run the script in the current working directory?(Y/N)").upper() != "Y":
        exit(0)
else:
    path = sys.argv[1]

print(f"path = {path}")

files = os.listdir(path)

settings = {
    "name_format": "{classname}-{id}-{name}{extname}",
    "classname": "软件191",
    "names": {"李华": "190265461", "王小美": "190265462"}
}

if os.path.exists('settings.json'):
    try:
        with open("settings.json", 'rb') as f:
            settings = json.load(f)
    except Exception as e:
        print(f"{RED}settings.json format error. Delete ")
else:
    print(f"{RED}File created: settings.json{NC}")
    print(
        "Please put the classnames, student_names and student_id in [settings.json], then try again.")
    with open('settings.json', 'wb') as f:
        f.write(json.dumps(settings, ensure_ascii=False).encode('utf-8'))
    exit()

gotten = {}

for name in settings['names']:
    for file in files:
        if name in file:
            gotten[name] = file
            break
    else:
        gotten[name] = "nope"


renamed = {}

for name in sorted(gotten, key=lambda _: gotten[_]):
    if gotten[name] == 'nope':
        print(f"{RED}{name}\t==>\t{gotten[name]} {NC}")
    else:

        extname = os.path.splitext(gotten[name])[-1]
        formatted = settings['name_format'].format(
            classname=settings['classname'], id=settings['names'][name], name=name, extname=extname)
        if gotten[name] != formatted:
            renamed[gotten[name]] = formatted
            print(
                f"{NC}{name}\t==>\t{RED}{gotten[name]:30}{NC}\t==>\t{formatted}")
        else:
            print(f"{NC}{name}\t==>\t{gotten[name]:30}")


if input(f"{RED}Rename files?(Y/N){NC}\n").upper() == 'Y':
    for name in renamed:
        print(f"{RED}{name:30}{NC}\t==>\t{renamed[name]}")
        src_file = os.path.join(path, name)
        dst_file = os.path.join(path, renamed[name])
        os.rename(src_file, dst_file)
