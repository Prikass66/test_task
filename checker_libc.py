import subprocess
import time

def check_glibc_version():
    while True:
        result = subprocess.run(['dpkg', '-l', 'libc6'], capture_output=True, text=True)
        output = result.stdout

        if "2.35-0ubuntu3.1" in output:
            print("Версия glibc уязвима")
        elif "2.35-0ubuntu3.7" in output:
            print("Версия glibc не уязвима")
        else:
            print("Не удалось определить версию glibc")

        time.sleep(10)

if __name__ == "__main__":
    check_glibc_version()