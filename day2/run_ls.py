from subprocess import Popen, PIPE
command = Popen(["ls", "-l", "/usr/local"], stdout=PIPE)

for line in command.stdout:
    fields = line.split()
    if len(fields) > 3:
        print(line.split()[4])

