import random
import pygame
import imageio
from Process import Process


def render_label(value, scale_factor):
    text = FONT.render(f"{int(value / scale_factor)}", True, COLORS["BLACK"])
    return text


pygame.init()

WIDTH, HEIGHT = 1080, 800
FRAME_DELAY = 33
TIME_SCALE_FACTOR = 30
COLORS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
}
FONT = pygame.font.Font(None, 36)
TEXT_X = 50
TEXT_Y = 0
GIF_SCALE_FACTOR = 0.5
GIF_ROTATION_ANGLE = 90
gif_frames = [pygame.surfarray.make_surface(frame) for frame in imageio.get_reader("./horse_animation.gif")]

for frame in gif_frames:
    frame.set_colorkey(COLORS["WHITE"], pygame.RLEACCEL)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Horse Racing")

process_data = [(_, random.randint(0, 9) * TIME_SCALE_FACTOR, random.randint(1, 9) * TIME_SCALE_FACTOR) for _ in
                range(5)]
process_data.sort(key=lambda pair: pair[1])
processes = []

clock = pygame.time.Clock()

completion_time = 0

for data in process_data:
    pid, arrival_time, burst_time = data
    completion_time += burst_time
    processes.append(Process(pid, arrival_time, burst_time, completion_time, WIDTH))
processes.sort(key=lambda process: process.pid)

burst_time = 0
turnaround_time = 0
waiting_time = 0

print("PID\tAT\tBT\tCT\tTAT\tWT")
for process in processes:
    burst_time += process.burst_time / TIME_SCALE_FACTOR
    turnaround_time += process.turnaround_time / TIME_SCALE_FACTOR
    waiting_time += process.waiting_time / TIME_SCALE_FACTOR
    print(process.__str__(TIME_SCALE_FACTOR))

print("\t" * 2 + str(burst_time / len(processes)) + "\t" + str(completion_time / TIME_SCALE_FACTOR) + "\t" + str(
    turnaround_time / len(processes)) + "\t" + str(waiting_time / len(processes)))

frame_index = 0
current_time = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(COLORS["WHITE"])

    pygame.draw.line(screen, COLORS["BLACK"], (10, 0), (10, HEIGHT), 2)
    pygame.draw.line(screen, COLORS["BLACK"], (215, 0), (215, HEIGHT), 2)
    pygame.draw.line(screen, COLORS["BLACK"], (WIDTH - 12, 0), (WIDTH - 12, HEIGHT), 2)

    label = render_label(current_time, TIME_SCALE_FACTOR)
    screen.blit(label, (TEXT_X, TEXT_Y))

    if current_time <= completion_time:

        for process in processes:
            horse = process.horse
            if current_time < process.arrival_time:
                continue
            elif current_time == completion_time:
                horse.stop()
            elif current_time in range(process.arrival_time, (process.arrival_time + process.waiting_time)):
                horse.display_horse_gif(screen, 4, gif_frames, GIF_ROTATION_ANGLE, GIF_SCALE_FACTOR)
            elif current_time in range((process.arrival_time + process.waiting_time), process.completion_time):
                horse.display_horse_gif(screen, frame_index, gif_frames, GIF_ROTATION_ANGLE, GIF_SCALE_FACTOR)
                horse.move()

        frame_index = (frame_index + 1) % len(gif_frames)

        pygame.display.flip()

        current_time += 1
        clock.tick(TIME_SCALE_FACTOR)
        pygame.time.delay(10)

pygame.quit()
