import socket
import threading

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8081))
client.send(nickname.encode('utf-8'))

# List to store received messages
received_messages = []

def receive():
    global received_messages
    while True: 
        try: 
            message = client.recv(1024).decode('utf-8')
            received_messages.append(message)
            display_recent_conversation()
        except:
            print("An error occurred")
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode('utf-8'))

def display_recent_conversation():
    # Clear the console before displaying the recent conversation
    print("\033[H\033[J")  # ANSI escape codes to clear the screen
    # Display the most recent conversation
    recent_conversation = '\n'.join(received_messages[-10:])  # Display last 10 messages
    print(recent_conversation)

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
