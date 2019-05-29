import arcade
import arcade

WIDTH = 640
HEIGHT = 480

circle_1_x = WIDTH/2
circle_1_y = HEIGHT/2
circle_1_delta_x = 10
circle_1_delta_y = 10

circle_2_x = 100
circle_2_y = 100
circle_2_delta_x = -10
circle_2_delta_y = -10

def on_update(delta_time):
    global circle_1_delta_y, circle_1_delta_x, circle_1_y, circle_1_x, circle_2_delta_x, circle_2_delta_y, circle_2_x, circle_2_y, distance
    circle_1_x += circle_1_delta_x
    circle_1_y += circle_1_delta_y

    circle_2_x += circle_2_delta_x
    circle_2_y += circle_2_delta_y

    if circle_1_x >= WIDTH - 50 or circle_1_x <= 50:
        circle_1_delta_x *= -1
    if circle_1_y >= HEIGHT - 50 or circle_1_y <= 50:
        circle_1_delta_y *= -1

    if circle_2_x >= WIDTH - 50 or circle_2_x <= 50:
        circle_2_delta_x *= -1
    if circle_2_y >= HEIGHT - 50 or circle_2_y <= 50:
        circle_2_delta_y *= -1

    distance = ((circle_1_x - circle_2_x)**2 + (circle_1_y - circle_2_y)**2)**0.5
    if distance <= 100:
        circle_1_delta_x *= -1
        circle_1_delta_y *= -1
        circle_2_delta_x *= -1
        circle_2_delta_y *= -1

def on_draw():
    arcade.start_render()
    # Draw in here...

    arcade.draw_circle_filled(circle_1_x, circle_1_y, 50, arcade.color.BLUE)
    arcade.draw_circle_filled(circle_2_x, circle_2_y, 50, arcade.color.BLACK)




def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1 / 240)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw


    arcade.run()


if __name__ == '__main__':
    setup()
