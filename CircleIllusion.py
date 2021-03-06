import pygame
from Track import Track, Point
import numpy as np

class CircleIllusion:
    """
    Draw a circle created out of balls moving on seperate tracks using pygame
    """

    def __init__(self, width: int, height: int, radius: int = 280, speed: float = 0.005):
        self.size = Point(width, height)
        self.radius = radius
        self.speed = speed
        self.running = True
        pygame.display.init()
        pygame.display.set_caption("Circle Illusion")
        pygame.key.set_repeat(60)
        self.screen = pygame.display.set_mode(self.size)
        self.number_of_tracks = 15
        self.create_tracks(self.number_of_tracks)
        self.show_lines = True

    def create_tracks(self, num: int) -> None:
        self.tracks = []
        i = 0 
        while i < np.pi:
            self.tracks.append(Track(self.screen, Point(self.size.x // 2, self.size.y // 2), self.radius, i))
            i += np.pi / num

    def run(self) -> None:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.kbin(event.unicode)
            self.screen.fill((0, 0, 0))
            if self.show_lines:
                for track in self.tracks:
                    track.draw_line()
            for track in self.tracks:
                track.draw_point()
                track.update(self.speed)
            pygame.display.update()

    def kbin(self, key: str) -> None:
        if key == 'q':
            self.running = False
        elif key == '-':
            self.number_of_tracks -= 1
            if self.number_of_tracks < 1:
                self.number_of_tracks = 1
            self.create_tracks(self.number_of_tracks)
        elif key == '+':
            self.number_of_tracks += 1
            self.create_tracks(self.number_of_tracks)
        elif key == 'l':
            self.show_lines = not self.show_lines
        elif key == '[':
            self.speed -= 0.001
            if self.speed <= 0:
                self.speed = 0
        elif key == ']':
            self.speed += 0.001
        elif key == 's':
            for track in self.tracks:
                track.special_elipse = not track.special_elipse

    @staticmethod
    def print_controls() -> None:
        print("=" * 75)
        print("- - Decrease number of tracks")
        print("+ - Increase number of tracks")
        print("[ - Decrease speed")
        print("] = Increase speed")
        print("l - Toggle lines")
        print("s - Toggle special elipse")
        print("q - Quit")
        print("=" * 75)
