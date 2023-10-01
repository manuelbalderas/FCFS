import pygame


class Horse:
    def __init__(self, position_x, position_y, distance, time):
        self.position_x = position_x
        self.position_y = position_y
        self.velocity = (distance / time)
        self.has_arrived = False

    def move(self):
        if not self.has_arrived:
            self.position_x += self.velocity

    def stop(self):
        self.has_arrived = True

    def display_horse_gif(self, screen, frame_index, gif_frames, rotation_angle, scale_factor):
        original_surface = gif_frames[frame_index]

        rotated_surface = pygame.transform.rotate(original_surface, rotation_angle)

        new_width = int(rotated_surface.get_width() * scale_factor)
        new_height = int(rotated_surface.get_height() * scale_factor)

        rotated_surface = pygame.transform.flip(rotated_surface, False, True)
        scaled_surface = pygame.transform.scale(rotated_surface, (new_width, new_height))

        screen.blit(scaled_surface, (self.position_x, self.position_y))
