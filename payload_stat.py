import time
import psutil

SHELL_PORTS = [4444, 5555]

def check_meterpreter():
    connections = psutil.net_connections()
    return any(connection.raddr and connection.raddr.port in SHELL_PORTS for connection in conn>

def main():
    while True:
        meter_status = check_meterpreter()
        if meter_status == True:
            print('Сессия метерпретер существует')
        else:
            print('Cессия метерпретер не существует')
        time.sleep(5)

if __name__ == '__main__':
    main()
