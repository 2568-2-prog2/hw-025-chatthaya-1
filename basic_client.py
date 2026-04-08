import requests

def call_dice_api():
    url = "http://127.0.0.1:8081/roll_dice"
    payload = {
        "probabilities": [0.1, 0.1, 0.1, 0.1, 0.1, 0.5],
        "number_of_random": 5
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            print("--- Roll Results ---")
            print(f"Results: {data['results']}")
            print(f"Message: {data['message']}")
        else:
            print(f"Server Error: {response.status_code}")
            print(response.text)
    except Exception as e:
        print("Error connecting to server:", e)

if __name__ == "__main__":
    call_dice_api()