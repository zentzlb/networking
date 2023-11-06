import pygame
from network import Network
import random as rnd


class Player(pygame.Rect):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h)
        self.color = color
        self.vel = 3

    def __reduce__(self):
        return type(self), (self.x, self.y, self.width, self.height, self.color)

    def __str__(self):
        return f'Player ({self.__dict__})'

    def __repr__(self):
        return self.__str__()

    def draw(self, surf: pygame.Surface) -> None:
        """
        display player on window
        :param surf: game window
        :return:
        """
        pygame.draw.rect(surf, self.color, self)

    def scoot(self, keys) -> None:
        """
        update player position
        :return:
        """
        # keys = pygame.key.get_pressed()
        if keys:
            if keys[pygame.K_UP]:
                self.y -= self.vel
            if keys[pygame.K_DOWN]:
                self.y += self.vel
            if keys[pygame.K_LEFT]:
                self.x -= self.vel
            if keys[pygame.K_RIGHT]:
                self.x += self.vel


class Engine:
    def __init__(self, w: int, h: int, background: tuple[int, int, int]):
        self.players = []
        self.WIN = pygame.display.set_mode((w, h))
        self.background = background

    def update(self) -> None:
        """
        updates and draws
        :return:
        """
        [player.scoot() for player in self.players]
        self.draw()
        k = pygame.key.get_pressed()

    def add_player(self) -> None:
        """
        add player to game
        :return:
        """
        self.players.append(Player(3, 3, 10, 10, (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255))))

    def draw(self) -> None:
        """
        displays players on window surface
        :return:
        """
        self.WIN.fill(self.background)
        [player.draw(self.WIN) for player in self.players]
        pygame.display.update()


def main() -> None:
    """
    game loop
    :return:
    """

    W = 800
    H = 500
    FPS = 60
    WHITE = (255, 255, 255)
    pygame.init()
    engine = Engine(W, H, WHITE)

    run = True
    n = Network()

    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get(eventtype=pygame.QUIT):
            run = False
            pygame.quit()
            return

        k = pygame.key.get_pressed()
        n.send_obj(k)
        engine.players = n.receive()
        engine.draw()


if __name__ == '__main__':
    main()
