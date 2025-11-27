from typing import Final
from random import randint
import pygame as pg

pg.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 720, 720
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
FPS = 120
BLOCK_SIZE = 40
BLOCK_SPACING = 5
SNAKE_SPEED_MS = 150

BACKGROUND_COLOR = (33, 37, 41)
SNAKE_PRIMARY_COLOR = (56, 102, 65)
SNAKE_SECONDARY_COLOR = (106, 153, 78)
SCORE_TEXT_COLOR = (242, 232, 207)
FOOD_COLOR = (173, 40, 49)


class Direction:
    UP: Final = (0, -1)
    DOWN: Final = (0, 1)
    RIGHT: Final = (1, 0)
    LEFT: Final = (-1, 0)


snake = []
food = []
direction_vector = (0, 0)
snake_length = 2
last_move_time = 0

score_font = pg.font.Font("minecrafter.ttf", 36)


def get_map_center() -> list[int]:
    return [WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2]


def spawn_food():
    while True:
        x = randint(0, (WINDOW_WIDTH - 1) // BLOCK_SIZE) * BLOCK_SIZE
        y = randint(0, (WINDOW_HEIGHT - 1) // BLOCK_SIZE) * BLOCK_SIZE
        pos = [x, y]
        if pos not in snake:
            food.append(pos)
            break


def reset_game():
    global snake, snake_length, direction_vector, food, last_move_time
    snake = [get_map_center()]
    snake_length = 2
    direction_vector = (0, 0)
    food.clear()
    spawn_food()
    last_move_time = pg.time.get_ticks()


window = pg.display.set_mode(WINDOW_SIZE)
clock = pg.time.Clock()

pg.display.set_caption("Змейка от AkatoTheDragon")
pg.display.set_icon(pg.image.load("icon.png"))

reset_game()

running = True
while running:
    current_time = pg.time.get_ticks()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                if direction_vector != Direction.DOWN:
                    direction_vector = Direction.UP
            elif event.key == pg.K_DOWN:
                if direction_vector != Direction.UP:
                    direction_vector = Direction.DOWN
            elif event.key == pg.K_RIGHT:
                if direction_vector != Direction.LEFT:
                    direction_vector = Direction.RIGHT
            elif event.key == pg.K_LEFT:
                if direction_vector != Direction.RIGHT:
                    direction_vector = Direction.LEFT

    if direction_vector != (0, 0) and current_time - last_move_time >= SNAKE_SPEED_MS:
        last_move_time = current_time

        head_x, head_y = snake[-1]
        d_x, d_y = direction_vector
        new_head = [
            (head_x + d_x * BLOCK_SIZE) % WINDOW_WIDTH,
            (head_y + d_y * BLOCK_SIZE) % WINDOW_HEIGHT
        ]

        if new_head in snake:
            reset_game()
            continue

        snake.append(new_head)

        if new_head in food:
            food.remove(new_head)
            snake_length += 1
            spawn_food()
        
        elif len(snake) > snake_length:
            snake.pop(0)

    window.fill(BACKGROUND_COLOR)

    segment_rect = pg.Rect(0, 0, BLOCK_SIZE - 2 * BLOCK_SPACING, BLOCK_SIZE - 2 * BLOCK_SPACING)
    for i, pos in enumerate(snake):
        x, y = pos

        if i % 2 == 0:
            segment_color = SNAKE_PRIMARY_COLOR
        else:
            segment_color = SNAKE_SECONDARY_COLOR

        segment_rect.topleft = (x + BLOCK_SPACING, y + BLOCK_SPACING)
        
        pg.draw.rect(window, segment_color, segment_rect)

    for x, y in food:
        segment_rect.topleft = (x + BLOCK_SPACING, y + BLOCK_SPACING)
        pg.draw.rect(window, FOOD_COLOR, segment_rect)

    score_text = score_font.render(f"Счёт: {snake_length - 2}", False, SCORE_TEXT_COLOR)
    window.blit(score_text, (15, 15))

    pg.display.flip()
    clock.tick(FPS)

pg.quit()