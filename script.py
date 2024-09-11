import subprocess
i = 1
while i <= 3:
    subprocess.call("ansible-playbook playbook%d.yml -b"%i,shell=True)
    i = i + 1

