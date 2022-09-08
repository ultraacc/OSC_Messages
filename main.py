from pythonosc import udp_client

def main():
    client = udp_client.SimpleUDPClient("127.0.0.1", 9000)
    b = True
    while True:
        message = input("Message: ")
        client.send_message("/chatbox/input", [message.encode('ascii', errors="replace").decode(), b])
    


if __name__ == "__main__":
    main()