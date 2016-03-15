"""
Simple Echo Server for demo
"""
import echo_utils

HOST = echo_utils.HOST
PORT = echo_utils.PORT


def handle_client(sock, addr):
    """ Receive data from the client via sock and echo it back """

    try:
        msg = echo_utils.recv_msg(sock)     # Blocks until received
        # complete message
        print('{}: {}'.format(addr, msg))
        echo_utils.send_msg(sock, msg)      # Blocks until sent
    except (ConnectionError, BrokenPipeError):
        print('Socket error')
    finally:
        print('Closed connection to {}'.format(addr))
        sock.close()


def serve():
    """ Set up server and start serving"""
    listen_sock = echo_utils.create_listen_socket(HOST, PORT)
    addr = listen_sock.getsockname()
    print('Listening on {}'.format(addr))

    while True:
        client_sock, addr = listen_sock.accept()
        print('Connection from {}'.format(addr))
        handle_client(client_sock, addr)


if __name__ == '__main__':
    serve()
