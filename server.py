import socket
import pickle
from pickle import UnpicklingError
from _thread import *
import sys
from client import *
from counter import *
from com import *
import pygame


class Server:

    server = socket.gethostbyname(socket.gethostname())
    port = 5555
    run = True
    player_count = 0

    players = []

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def __init__(self):

        pygame.init()

        try:
            self.s.bind((self.server, self.port))
            # print('bound')
        except socket.error as e:
            print(e)

        self.s.listen(2)
        print('waiting for connection, server started')

    def main(self):
        while self.run:
            conn, addr = self.s.accept()
            print(f"connected to: {addr}")
            start_new_thread(self.threaded_client, (conn, ))
            # if input('press q to quit') == 'q':
            #     self.close()

    def close(self):
        # self.s.shutdown(socket.SHUT_RDWR)
        self.s.close()
        del self

    def threaded_client(self, conn: socket.socket):
        # conn.send(str)
        # conn.send(str.encode("Connected"))
        send_text(conn, "Connected")
        # reply = 'no reply'
        player = Player(3, 3, 10, 10, (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255)))
        self.players.append(player)
        # player = self.players[self.player_count]
        self.player_count += 1
        print(f"number of players: {self.player_count}")

        while True:

            try:
                data = receive(conn)
                # print(data[pygame.K_UP])
                player.scoot(data)
                # send_obj(conn, data)
                if not data:
                    print("Disconnected")
                    break
                else:
                    b = pickle.dumps(self.players)
                    conn.send(b)

                # conn.sendall(str.encode(f"received {reply}"))

            except socket.error as e:
                conn.close()
                print(e)
                break

        print('Lost Connection')
        del player
        self.player_count -= 1
        print(f"number of players: {self.player_count}")
        conn.close()


if __name__ == '__main__':
    my_server = Server()
    my_server.main()
