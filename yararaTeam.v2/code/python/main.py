import socket
import time
# Configura el servidor TCP
host = '127.0.0.1'  # La dirección IP de localhost
port = 12345  # El puerto que desees usar

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Esperando una conexión en {host}:{port}")

# Acepta una conexión
client_socket, _ = server_socket.accept()

while True:
    # Procesa las imágenes y obtén la información que deseas enviar
    info = "Información que deseas enviar"
    time.sleep(0.5)
    client_socket.send(info.encode())
