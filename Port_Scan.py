import socket

IP_src = input('IP SOURCE: ')
print('Please wait...')
for port in range(1, 65535):
    client = socket.socket()
    client.settimeout(0.05)

    if client.connect_ex((IP_src, port)) == 0:
        print('Founded ports: ', port)
print('Done.')