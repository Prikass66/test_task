import os
import time

def check_file_for_string(file_path, target_string):
    with open(file_path, 'r') as file:
        for line in file:
            if target_string in line:
                return True
    return False

def main():
    file_path = "/var/www/html/modules/thumb/thumb.php"
    target_string_1 = "$stream_options = '-rtsp_transport ' . $_GET['transport'] . ' ' . $strea>
    target_string_2 = "$stream_options = '-rtsp_transport ' . escapeshellarg($transport) . ' ' >

    while True:
        if check_file_for_string(file_path, target_string_1):
            print("Версия Majordomo уязвима")
        elif check_file_for_string(file_path, target_string_2):
            print("Версия Majordomo не уязвима")
        else:
            print("Не удалось проверить уязвимость")

        time.sleep(10)

if __name__ == "__main__":
    main()
