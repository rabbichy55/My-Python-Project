import pygame

pygame.init()

# window
window = pygame.display.set_mode((1200, 400))

# load images
track = pygame.image.load("Self-driving_Car/track4.png")
car = pygame.image.load("Self-driving_Car/tesla.png")

# resize car
car = pygame.transform.scale(car, (30, 60))

# car position
car_x = 150
car_y = 300

camera_x_offset = 0
direction = "up"

drive = True

while drive:

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False

    # draw track FIRST (important)
    window.blit(track, (0, 0))

    # camera position
    camera_x = int(car_x + camera_x_offset)
    camera_y = int(car_y)

    # detect pixels
    up_px = window.get_at((camera_x, camera_y - 30))[0]
    down_px = window.get_at((camera_x, camera_y + 30))[0]
    right_px = window.get_at((camera_x + 25, camera_y))[0]

    print(up_px, right_px, down_px)

    # turn logic
    if direction == "up" and up_px != 255 and right_px == 255:
        direction = "right"
        camera_x_offset = 30
        car = pygame.transform.rotate(car, -90)

    if direction == "right" and right_px != 255 and down_px == 255:
        direction = "down"
        camera_x_offset = 0
        car = pygame.transform.rotate(car, -90)

    # movement
    if direction == "up" and up_px == 255:
        car_y -= 0.1

    elif direction == "right" and right_px == 255:
        car_x += 0.1

    elif direction == "down" and down_px == 255:
        car_y += 0.1

    # draw car
    window.blit(car, (car_x, car_y))

    # camera visualization
    pygame.draw.circle(window, (255, 0, 0), (camera_x + 15, camera_y + 30), 5)

    pygame.display.update()

pygame.quit()