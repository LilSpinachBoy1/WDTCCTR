import pygame
import conversions
pygame.init()


class Enemy:
    def __init__(self, start_y: int, move_range_pcnt: int) -> None:
        self.move_cap = 10 + move_range_pcnt
        self.coords = [10, start_y]  # Written in percentages
        self.direction = 1
        self.rect = pygame.Rect(*conversions.pe2pi(self.coords), conversions.pe2piSINGLE(5, True), conversions.pe2piSINGLE(5, True))

    def process_move(self, speed: int) -> None:
        # Move the enemy based on the current direction
        self.coords[0] += speed * self.direction

        # If we reach the boundaries, reverse direction
        if self.coords[0] >= self.move_cap:
            self.direction = -1  # Move left
        elif self.coords[0] <= 10:
            self.direction = 1  # Move right

    def check_collide(self, player) -> bool:
        return self.rect.colliderect(player)

    def update(self, SURF: pygame.Surface, COLOUR: tuple) -> None:
        self.rect = pygame.Rect(*conversions.pe2pi(self.coords), conversions.pe2piSINGLE(5, True), conversions.pe2piSINGLE(5, True))
        pygame.draw.rect(SURF, COLOUR, self.rect)
        