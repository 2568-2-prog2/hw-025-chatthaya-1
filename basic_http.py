import socket
import json
from dice import Dice

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8081))
server_socket.listen(1)

dice = Dice()

print("Server is listening on port 8081...")

while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1024).decode('utf-8')
    
    if not request:
        client_socket.close()
        continue

    lines = request.split("\r\n")
    first_line = lines[0]
    
    if first_line.startswith("POST /roll_dice"):
        body = request.split("\r\n\r\n")[1]
        try:
            data = json.loads(body)
            probs = data.get("probabilities")
            num = data.get("number_of_random", 1)

            results = dice.roll(probs, num)

            response_data = {
                "status": "success",
                "results": results,
                "message": "Dice rolled successfully!"
            }
            status_code = "200 OK"
        except Exception as e:
            response_data = {"status": "error", "message": str(e)}
            status_code = "400 Bad Request"

        response_json = json.dumps(response_data)
        response = f"HTTP/1.1 {status_code}\r\nContent-Type: application/json\r\n\r\n{response_json}"
    
    elif first_line.startswith("GET /myjson"):
        response_data = {"status": "success", "message": "Hello, KU!"}
        response_json = json.dumps(response_data)
        response = f"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{response_json}"
        
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n"

    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()