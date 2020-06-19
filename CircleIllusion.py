import pygame
from Track import Track, Point
import numpy as np

class CircleIllusion:
    """
    Draw a circle created out of balls moving on seperate tracks using pygame
    """

    def __init__(self, width, height, radius = 280, speed = 0.005):
        self.size = Point(width, height)
        self.radius = radius
        self.speed = speed
        self.running = True
        pygame.display.init()
        pygame.display.set_caption("Circle Illusion")
        self.screen = pygame.display.set_mode(self.size)
        self.tracks = []
        self.create_tracks(1500)

    def create_tracks(self, num: int) -> None:
        self.tracks.append(Track(self.screen, Point(self.size.x // 2, self.size.y // 2), self.radius, 0, 0))

    def run(self) -> None:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((0, 0, 0))
            for track in self.tracks:
                track.draw()
                track.update(self.speed)
            pygame.display.update()