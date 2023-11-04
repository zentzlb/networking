import socket
import pickle
from pickle import UnpicklingError


class Network:
    def __init__(self):
        # print('asddasdassda')
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostbyname(socket.gethostname())
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()
        print(self.pos)
        # self.send_obj('asdadsasdads')

    def get_pos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            print(self.addr)
            return self.receive()
        except socket.error as e:
            print(e)

    def send_obj(self, obj: object) -> None:
        """
        send pickled object
        :param obj: object of any type
        :return:
        """
        try:
            b = pickle.dumps(obj)
            self.client.send(b)
            # return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

    def send_text(self, text: str) -> None:
        """
        send string
        :param text: string message
        :return:
        """
        print(text)
        try:
            self.client.sendall(text.encode())
        except socket.error as e:
            print(e)

    def receive(self) -> object:
        """
        receive and unpickle object of any type
        :return: object
        """
        data = self.client.recv(2048)
        try:
            # print(data)
            return pickle.loads(data)
        except UnpicklingError:
            return data.decode("utf-8")


if __name__ == '__main__':
    n = Network()

    # n.send_obj('b')
    # n.client.send(str.encode("your mother"))
    # n.send_obj('waka waka')


