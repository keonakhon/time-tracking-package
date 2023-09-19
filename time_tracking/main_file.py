import time
import socket
import argparse


localhost_network = "127.0.0.1"
socket_port = 52000


# Sender Data to socket
def send_data():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to Receiver
        s.connect((localhost_network, socket_port))

        current_time = time.strftime("%Y-%m-%d %H:%M:%S")

        s.send(current_time.encode())

        # Close the connection
        s.close()
    except Exception:
        pass


# Receive Data from socket
def receive_data():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set the SO_REUSEADDR option
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind and listen
        s.bind((localhost_network, socket_port))
        s.listen()

        # Accept connections
        while True:
            (clientConnected, _) = s.accept()
            try:
                data_from_client = clientConnected.recv(1024)
                data_to_print = data_from_client.decode()
                print(data_to_print)
            finally:
                # Close the connection
                clientConnected.close()
    except socket.error:
        pass
    except KeyboardInterrupt:
        pass
    except Exception:
        pass
    finally:
        s.close()


def main_func():
    try:
        parser = argparse.ArgumentParser(allow_abbrev=False)

        # Define start argument
        parser.add_argument(
            '--start',
            action='store_true',
            help="Use this argument on systemd"
        )

        args = parser.parse_args()

        # Condition when user pass argument start
        if args.start:
            while True:
                send_data()
                time.sleep(5)
        else:
            receive_data()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main_func()
