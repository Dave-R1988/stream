from http.client import HTTPConnection, HTTPResponse
import time


def producer():
    while True:
        try:
            print("Attempting to connect to resource-service...")
            conn: HTTPConnection = HTTPConnection("resource-service", 8000)
            conn.request("GET", "/cpu_percent")
            response: HTTPResponse = conn.getresponse()
            print(response.status, response.reason)
            data: bytes = response.read()
            print(data.decode())
            conn.close()
        except ConnectionRefusedError:
            print("Connection refused, retrying in 5 seconds...")
            time.sleep(5)
            continue
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            time.sleep(5)
            continue
        time.sleep(5)


if __name__ == "__main__":
    producer()
