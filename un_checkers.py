import subprocess
import time
import psutil


def check_glibc_version():
    result = subprocess.run(['dpkg', '-l', 'libc6'], capture_output=True, text=True)
    output = result.stdout
    if "2.35-0ubuntu3.1" in output:
        print("Версия glibc уязвима")
    elif "2.35-0ubuntu3.7" in output:
        print("Версия glibc не уязвима")
    else:
        print("Не удалось определить версию glibc")


def check_file_for_string(file_path, target_string):
    with open(file_path, 'r') as file:
        for line in file:
            if target_string in line:
                return True
    return False


def check_major_version():
    file_path = "/var/www/html/modules/thumb/thumb.php"
    target_string_1 = "$stream_options = '-rtsp_transport ' . $_GET['transport'] . ' ' . $stream_options;"
    target_string_2 = "$stream_options = '-rtsp_transport ' . escapeshellarg($transport) . ' ' . $stream_options;"
    if check_file_for_string(file_path, target_string_1):
        print("Версия Majordomo уязвима")
    elif check_file_for_string(file_path, target_string_2):
        print("Версия Majordomo не уязвима")
    else:
        print("Не удалось проверить уязвимость")


def check_meterpreter():
    SHELL_PORTS = [4444, 5555]
    connections = psutil.net_connections()
    meter_status = any(connection.raddr and connection.raddr.port in SHELL_PORTS for connection in connections)
    meter_status = bool(meter_status)
    if meter_status == True:
        print('Сессия метерпретер существует')
    else:
        print('Cессия метерпретер не существует')

def main():
    while True:
        check_glibc_version()
        check_major_version()
        check_meterpreter()
        print()
        time.sleep(10)

if __name__ == '__main__':
    main()

