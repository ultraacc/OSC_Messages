from pythonosc import udp_client


def main():
    client = udp_client.SimpleUDPClient("127.0.0.1", 9000)
    b = True
    while True:
        message = input("Message: ")
        if len(message) > 144:
            print(
                "Your message reached the limit of 144 characters, your message might be cut off"
            )
        client.send_message(
            "/chatbox/input", [message.encode("ascii", errors="replace").decode(), b]
        )


if __name__ == "__main__":
    main()
