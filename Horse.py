import pygame


class Horse:
    def __init__(self, position, distance, time):
        self.position = list(position)
        self.velocity = (distance / time)
        self.frame_index = 4
        self.is_moving = False
        self.has_arrived = False

    def start_moving(self):
        self.is_moving = True

    def move(self):
        if self.is_moving and not self.has_arrived:
            self.position[0] += self.velocity

    def stop(self):
        self.is_moving = False
        self.has_arrived = True

    def display_horse_gif(self, screen, gif_frames, rotation_angle, scale_factor):
        original_surface = gif_frames[self.frame_index]

        rotated_surface = pygame.transform.rotate(original_surface, rotation_angle)

        new_width = int(rotated_surface.get_width() * scale_factor)
        new_height = int(rotated_surface.get_height() * scale_factor)

        rotated_surface = pygame.transform.flip(rotated_surface, False, True)
        scaled_surface = pygame.transform.scale(rotated_surface, (new_width, new_height))

        screen.blit(scaled_surface, (self.position))

        if self.is_moving:
            self.frame_index = (self.frame_index + 1) % len(gif_frames)
