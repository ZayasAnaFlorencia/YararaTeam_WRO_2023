import socket
import threading
import time

# Función que manejará cada conexión de cliente
def handle_client(client_socket, client_address):
    print(f"Conexión aceptada desde {client_address}")
    
    while True:
        try:
            # Envía información al cliente de manera continua
            info = "Información de Python"
            client_socket.send(info.encode())
            time.sleep(1)  # Espera 1 segundo antes de enviar nuevamente

            # Intenta recibir datos del cliente
            data = client_socket.recv(1024)

            if not data:
                print(f"La conexión con {client_address} se ha cerrado por el cliente")
                client_socket.close()
                break  # Sale del bucle y termina el hilo

            # Procesa los datos recibidos
            print(f"Datos recibidos de {client_address}: {data.decode()}")

        except ConnectionResetError:
            print(f"La conexión con {client_address} se ha cerrado por el cliente")
            client_socket.close()
            break  # Sale del bucle y termina el hilo

# Configura el servidor TCP
host = '127.0.0.1'  # La dirección IP de localhost
port = 1235  # El puerto que desees usar

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)  # Número máximo de conexiones pendientes

print(f"Esperando conexiones en {host}:{port}")

while True:
    # Acepta una conexión
    client_socket, client_address = server_socket.accept()
    
    # Inicia un hilo para manejar la conexión del cliente
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
