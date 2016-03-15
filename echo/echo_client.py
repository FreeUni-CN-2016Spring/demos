"""
Simple Echo Client for demo
"""
import sys
from socket import socket, AF_INET, SOCK_STREAM
import echo_utils

HOST = sys.argv[-1] if len(sys.argv) > 1 else '127.0.0.1'
PORT = echo_utils.PORT


def send_msg(msg):
    """ Send given message to echo server """
    with socket(AF_INET, SOCK_STREAM) as sock:  # calls sock.close() for you
        sock.connect((HOST, PORT))
        print('\nConnected to {}:{}'.format(HOST, PORT))
        echo_utils.send_msg(sock, msg)  # Blocks until sent
        print('Sent message: {}'.format(msg))
        msg = echo_utils.recv_msg(sock)  # Block until msg
        print('Received echo: ' + msg)
    print('Closed connection to server\n')


if __name__ == '__main__':
    while True:
        print("Type message, enter to send, 'q' to quit")
        text = input()  # pylint: disable=C0103
        if text is 'q':
            break

        try:
            send_msg(text)
        except ConnectionError:
            print('Socket error')
            break
