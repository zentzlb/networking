from network import Network
from client import Player
import pygame

n = Network()

while True:
    outgoing_data = input('enter message')
    n.send_text(outgoing_data)
    incoming_data = n.receive()
    print(incoming_data)
