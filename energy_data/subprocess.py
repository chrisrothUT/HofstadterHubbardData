import subprocess

# List of your scripts in the exact order you want them to run

for N in (192,432):
    for i in np.arange(2):
        if i == 0:
            nelec = 7*N//8
        else:
            nelec = 23*N//24

    subprocess.run(["python3", "combine.py", "hello", "world"], check=True)


