#!/usr/bin/python

import subprocess
import shlex
import sys
import datetime

cmd = "kubectl --namespace notebook get pods"

output = subprocess.run(shlex.split(cmd), capture_output=True, text=True).stdout.strip("\n")

lines = output.split("\n")

hub = None

for line in lines:
    if line.find("hub-") != -1:
        hub = line.split()[0]
        break

if hub is None:
    print("Cannot find the hub!")
    sys.exit(-1)

cmd = f"kubectl --namespace notebook logs {hub}"

output = subprocess.run(shlex.split(cmd), capture_output=True, text=True).stdout.strip("\n")

lines = output.split("\n")

users = open("users.txt").readlines()

last_time = None

with open("users_new.txt", "w") as FILE:
    for user in users:
        user = user.strip()
        FILE.write(user + "\n")
        words = user.split()
        date, time = words[1:3]
        d = datetime.datetime.fromisoformat(f"{date} {time}")

        if last_time is None:
            last_time = d
        elif d > last_time:
            last_time = d

    for line in lines:
        if line.find("User logged in") != -1:
            words = line.split()
            date, time = words[1:3]
            d = datetime.datetime.fromisoformat(f"{date} {time}")

            if d > last_time:
                FILE.write(line + "\n")
                print(line)

cmd = "mv users_new.txt users.txt"

subprocess.run(shlex.split(cmd), capture_output=False)

