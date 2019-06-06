import arcade
import time

# start
start = False
dead_screen = False
restart = False
# time counter
then = time.time()


# window setup
WIDTH = 640
HEIGHT = 480

# score counter
score = 0

# texture loading
background = arcade.load_texture("Textures_game/background.jpg")
background_start = arcade.load_texture("Textures_game/giphy.gif")
virus = arcade.load_texture("Textures_game/computer+virus.png")
laptop = arcade.load_texture("Textures_game/laptop-png-29.png")
# start player position in middle of window
player_x = WIDTH / 2
player_y = HEIGHT / 2

# Variables to record if certain keys are being pressed.
up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False

# moving block
center_x = 100  # Initial x position
center_y = 50  # Initial y position
delta_x = 3  # change in x
delta_y = 1  # change in y

RECT_WIDTH = 50
RECT_HEIGHT = 50

#  block to avoid
my_button = [100, 200, 150, 50]

# dead counter
dead = False



def title_screen(state):
    if state is False:
        arcade.set_viewport(-640, 0, -480, 0)

    if state:
        arcade.set_viewport(0, 640, 0, 480)


def on_collision():
    global player_x, player_y, dead, center_y, center_x, score
    if 75 <= player_x <= 275 and 175 <= player_y <= 275:
        dead = True

    if center_x - 45 <= player_x <= center_x + 45 and center_y - 45 <= player_y <= center_y + 45:
        dead = True

    if not dead:
        if center_x - 100 <= player_x <= center_x + 100 and center_y - 100 <= player_y <= center_y + 100:
            score += 1
        if center_x - 80 <= player_x <= center_x + 80 and center_y - 80 <= player_y <= center_y + 80:
            score += 2



def on_update(delta_time):
    global up_pressed, player_y, down_pressed, right_pressed, left_pressed, player_x
    if up_pressed:
        player_y += 5
    if down_pressed:
        player_y -= 5
    if right_pressed:
        player_x += 5
    if left_pressed:
        player_x -= 5
    on_collision()

    title_screen(start)

    if start:
        global center_x, center_y
        global delta_x, delta_y

        center_x += delta_x
        center_y += delta_y

        # Figure out if we hit the edge and need to reverse.
        if center_x < RECT_WIDTH // 2 or center_x > WIDTH - RECT_WIDTH // 2:
            delta_x *= -1.1
            if delta_x < 0:
                print(delta_x * -1, "is the current speed")
            else:
                print(delta_x, "is the current speed")

        if center_y < RECT_HEIGHT // 2 or center_y > HEIGHT - RECT_HEIGHT // 2:
            delta_y *= -1.1

        if player_x - 25 <= 0:
            player_x = 25
            print("YEET")

        if player_x + 25 >= WIDTH:
            player_x = WIDTH - 25

        if player_y - 25 <= 0:
            player_y = 25

        if player_y + 25 >= HEIGHT:
            player_y = HEIGHT - 25


def on_draw():
    global player_x, player_y, dead, now, printed, start, state, center_y, center_x, delta_x, delta_y, score

    arcade.start_render()
    # Draw in here...
    arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, 852, 480, background)
#    arcade.draw_circle_filled(player_x, player_y, 25, arcade.color.RED)

    arcade.draw_texture_rectangle(player_x, player_y, 0.15*laptop.width, 0.15*laptop.height, laptop, 0)

    # Draw in here...
    arcade.draw_xywh_rectangle_filled(my_button[0],
                                      my_button[1],
                                      my_button[2],
                                      my_button[3],
                                      arcade.color.BLACK)
#    arcade.draw_rectangle_filled(center_x, center_y, RECT_WIDTH, RECT_HEIGHT, arcade.color.BLUE)

    arcade.draw_texture_rectangle(center_x, center_y, 0.4*virus.width, 0.4*virus.height, virus, 0)

    arcade.draw_text("VIRUS", 110, 210, (210, 255, 248), 30, font_name='CONSOLAS')

    arcade.draw_text("Score: " + str(score), 100, 50, arcade.color.BLACK, font_name='CONSOLAS')

    arcade.draw_texture_rectangle(-320, -240, 640, 480, background_start)

    arcade.draw_text("Welcome to the Game \npress 'e' to start", -560, -100, (210, 255, 248), 30, font_name='CONSOLAS')
    arcade.draw_text("Avoid the Virus, \nthe aura of antivirus, \ngives you score", -560, -200, (210, 255, 248), 15, font_name='CONSOLAS')
    arcade.draw_text("Antivirus doesn't \nprotect you completly \nso play smart \njust like being smart online", -560, -300, (210, 255, 248), 15, font_name='CONSOLAS')
    arcade.draw_text("Use W A S D to control", -560, -460, (210, 255, 248), 10, font_name='CONSOLAS')

    if dead:
        arcade.set_background_color(arcade.color.RED)
        arcade.draw_text("INFECTED, your score is " + str(score), 25, HEIGHT - 100, (210, 255, 248), 30, font_name='CONSOLAS')
        now = time.time()

        if restart is True:
            player_x = WIDTH/2
            player_y = HEIGHT/2
            center_x = 100  # Initial x position
            center_y = 50  # Initial y position
            delta_x = 3  # change in x
            delta_y = 1  # change in y
            score = 0
            dead = False

def on_key_press(key, modifiers):
    global up_pressed, start, restart
    if key == arcade.key.W:
        up_pressed = True
    global down_pressed
    if key == arcade.key.S:
        down_pressed = True
    global right_pressed
    if key == arcade.key.D:
        right_pressed = True
    global left_pressed
    if key == arcade.key.A:
        left_pressed = True

    if key == arcade.key.UP:
        up_pressed = True
    if key == arcade.key.DOWN:
        down_pressed = True
    if key == arcade.key.RIGHT:
        right_pressed = True
    if key == arcade.key.LEFT:
        left_pressed = True


    if key == arcade.key.E:
        start = True
    if key == arcade.key.R:
        restart = True



def on_key_release(key, modifiers):
    global up_pressed, restart
    if key == arcade.key.W:
        up_pressed = False
    global down_pressed
    if key == arcade.key.S:
        down_pressed = False
    global right_pressed
    if key == arcade.key.D:
        right_pressed = False
    global left_pressed
    if key == arcade.key.A:
        left_pressed = False

    if key == arcade.key.UP:
        up_pressed = False
    if key == arcade.key.DOWN:
        down_pressed = False
    if key == arcade.key.RIGHT:
        right_pressed = False
    if key == arcade.key.LEFT:
        left_pressed = False
    if key == arcade.key.R:
        restart = False



def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")

    arcade.set_background_color(arcade.color.TROPICAL_RAIN_FOREST)
    arcade.schedule(on_update, 1 / 240)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_collision = on_collision
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()
