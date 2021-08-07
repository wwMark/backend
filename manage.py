#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
from pathlib import Path
from PIL import Image
'''
BASE_DIR = Path(__file__).resolve().parent
qr_path = os.path.join(BASE_DIR, 'qrcode_generator'),
sys.path.append(qr_path)
print(sys.path)
'''
import qrcode_generator
from qrcode_generator import qrcode_generator

BASE_DIR = Path(__file__).resolve().parent
qr_img_path = os.path.join(BASE_DIR, "qrcode_generator")
qr_img_path = os.path.join(qr_img_path, "qrcode_with_border.png")

'''
def setup_program():
    hostname = socket.gethostname()
    ## getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    ## printing the hostname and ip_address
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")
    # ctypes.windll.user32.MessageBoxW(0, ip_address, "Enter the following ip", 1)
    root = Tk()
    w = Label(root, text='     请在浏览器里输入： http://' + ip_address + ':8000/jimajiang/     ', font="Times 32")
    w.pack()
    root.mainloop()
'''
import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def address_maker(ip_address):
    # hostname = socket.gethostname()
    # ip_address = socket.gethostbyname(hostname)
    address = "http://" + ip_address + ":8000/" + "jimajiang/"
    return address

def show_qrcode():
    print("1")
    address = address_maker(get_ip())
    print(address)
    qrcode_generator.QR_With_Central_Img(link=address)
    image = Image.open(qr_img_path)
    image.show()

def main():
    print("main")
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'majong.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # show_qrcode_thread = Thread(target=show_qrcode)
    # show_qrcode_thread.start()
    show_qrcode()
    # execute_from_command_line(sys.argv)
    collect_static_argv = ['manage.py', 'collectstatic']
    execute_from_command_line(collect_static_argv)
    custom_argv = ['manage.py', 'runserver', '--noreload', '0.0.0.0:8000']
    execute_from_command_line(custom_argv)


if __name__ == '__main__':
    main()
