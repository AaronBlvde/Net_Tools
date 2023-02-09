import socket

def get_ip():
    hostname = input('Please enter hostname: ')
    try:
        return f'Hostname: {hostname}\nIP Address: {socket.gethostbyname(hostname)}'
    except socket.gaierror as error:
        return f'Invalid Hostname - error'

print(get_ip())
