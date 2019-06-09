import arcade
import random


# SCREEN DIMENSIONS
WIDTH = 1080
HEIGHT = 700

#   DISPLAYS
start_screen = True
load_screen = False
play_screen = False
end_screen = False

#   PLAYER CONTROLS
up_pressed = False
down_pressed = False
right_pressed = False
left_pressed = False

#   DEAD VARIABLE
dead = False
spawn_protection = True
respawn = False

#   PLAYER START POSITION
player_x = WIDTH/2
player_y = HEIGHT/2


player_speed = 1
virus_speed_x = 4
virus_speed_y = 4
trace_virus_speed = 1

#   AURA RADIUS
aura_radius = 50

#   SCORE TRACKER
score = 0

#   LOAD SCREEN TIMER FOR TIP CYCLING
loading_timer = 0

#   TRACING VIRUS SPAWN COORDINATES
tracing_virus_x = 100
tracing_virus_y = 100

#   TITLE DIMENSIONS
title_x = 100
title_y = 600
title_delta_y = 0.2

#  VIRUS VARIABLES
viruses = []

#   GAME TIMER
game_timer = 0

#   LIST OF TIPS THAT CYCLE DURING THE LOAD SCREEN
title_tips = ["Malware is software that harms your computer",
              "Keep your computer up to date with frequent updates",
              "Report cyberbullying to adults you trust",
              "A Trojan is a virus that disguises itself as helpful",
              "If computer starts lagging with lots of Chrome tabs open, \nit may be time to upgrade the RAM",
              "Avoid downloading software that seems to be \n'too good to be true'",
              "Don't give out your personal information online"]

tip_1 = random.randint(0, len(title_tips)-1)


tip_2 = random.randint(0, len(title_tips)-1)


#   TEXTURE LOADING
start_background = arcade.load_texture("CPT game 2 dir/45e136031edebdabec2032a296bf3184.png")
button_1 = arcade.load_texture("CPT game 2 dir/button1.png")
button_video = arcade.load_texture("CPT game 2 dir/button.png")
load_background = arcade.load_texture("CPT game 2 dir/49373.jpg")
game_background = arcade.load_texture("CPT game 2 dir/1fe9fd735b4c3b198d10236a5fa592f8.png")
virus_image = arcade.load_texture("CPT game 2 dir/computer+virus.png")
trace_virus_image = arcade.load_texture("CPT game 2 dir/67-675122_virus-clipart-black-and-white-virus-icon-png.png")
easy_button = arcade.load_texture("CPT game 2 dir/Easy button.png")
medium_button = arcade.load_texture("CPT game 2 dir/Medium button.png")
hard_button = arcade.load_texture("CPT game 2 dir/Hard button.png")

def game_start_screen():
    global title_x, title_y, title_delta_y
    arcade.draw_texture_rectangle(475, HEIGHT/2,0.7*start_background.width,0.7*start_background.height, start_background, 0)
    title_y += title_delta_y
    if title_y >= 610:
        title_delta_y *= -1
    if title_y <= 590:
        title_delta_y *= -1

    arcade.draw_text("Aura Antivirus",title_x, title_y, (210, 255, 248), 50, font_name='CONSOLAS')
    arcade.draw_text("Avoid the Virus, \nthe aura of antivirus, \ngives you score \nAntivirus doesn't \nprotect you completly \nso play smart \njust like being \nsmart online", 100, 500, (210, 255, 248), 25, font_name='CONSOLAS')
    arcade.draw_text("Use W A S D to control", 100, 150, (210, 255, 248), 15, font_name='CONSOLAS')
    arcade.draw_texture_rectangle(800, 400, 0.8*button_1.width, 0.8*button_1.height, button_1, 0)
  #  arcade.draw_texture_rectangle(705, 300, 0.8*button_video.width, 0.8*button_video.height, button_video, 0)
    arcade.draw_texture_rectangle(750, 300, easy_button.width, easy_button.height, easy_button)
    arcade.draw_texture_rectangle(750, 200, medium_button.width, medium_button.height, medium_button)
    arcade.draw_texture_rectangle(750, 100, hard_button.width, hard_button.height, hard_button)
  #  arcade.draw_circle_filled(705, 300, 5, arcade.color.BLUE)


def game_load_screen():
    global load_screen, play_screen, tip_1
    arcade.set_background_color(arcade.color.BLUE)
    arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, 0.7*load_background.width, 0.7*load_background.height, load_background,0)
   # arcade.draw_text("load screen, Press e to continue", WIDTH/2, HEIGHT/2, arcade.color.PINK_LAVENDER, 30 )
    arcade.draw_text("LOADING", 450, 550, arcade.color.PINK_LAVENDER, 30)
    if loading_timer <= 4:
        arcade.draw_text(title_tips[tip_1], 100, HEIGHT / 2,
                         arcade.color.PINK_LAVENDER, 30)
    if loading_timer > 4:
        arcade.draw_text(title_tips[tip_2], 100, HEIGHT / 2,
                         arcade.color.PINK_LAVENDER, 30)


def game_play_screen():
    arcade.set_background_color(arcade.color.GREEN)
    arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, 0.7*game_background.width, 0.7*game_background.height, game_background, 90)
    player()
    virus()
    tracing_virus()
    on_collision()
    arcade.draw_text("Score:    " + str(score), 100, 100, arcade.color.WHITE, 20, font_name='CONSOLAS')
    arcade.draw_text("Time :    " + str(round((30-game_timer),2)), 800, 600, arcade.color.WHITE, 20, font_name='CONSOLAS')
    if spawn_protection:
        arcade.draw_text("Spawn Protection is on \npress 't' to disable", WIDTH/2, HEIGHT/2, arcade.color.GREEN, 20,font_name= 'CONSOLAS')


class Person:
    def __init__(self,x,y,radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

person = Person(WIDTH/2, HEIGHT/2, 25, arcade.color.BLACK)


class Virus:
    def __init__(self,x,y,width, height, texture, speed_x, speed_y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.texture = texture
        self.speed_x = speed_x
        self.speed_y = speed_y


for i in range(2):
    viruses.append(Virus(random.randint(25,1080), random.randint(25,700), virus_image.width, virus_image.height,  virus_image, virus_speed_x, virus_speed_y))


def virus():
    global viruses, aura_radius
    for i in range(len(viruses)):
        viruses[i].x += viruses[i].speed_x
        viruses[i].y += viruses[i].speed_y
        aura_radius += 0.2
        if aura_radius >= 125:
            aura_radius = 50
        arcade.draw_circle_filled(viruses[i].x, viruses[i].y, aura_radius,(92, 244, 66, 95))
        arcade.draw_texture_rectangle(viruses[i].x, viruses[i].y, 0.5*viruses[i].width, 0.5*viruses[i].height, viruses[i].texture)


def player():
    arcade.draw_circle_filled(person.x, person.y, person.radius, person.color)


def game_end_screen():
    arcade.set_background_color(arcade.color.RED)


def tracing_virus():
    global person, tracing_virus_x, tracing_virus_y, trace_virus_speed

    if tracing_virus_x < person.x:
        tracing_virus_x += trace_virus_speed
    if tracing_virus_x > person.x:
        tracing_virus_x -= trace_virus_speed
    if tracing_virus_y < person.y:
        tracing_virus_y += trace_virus_speed
    if tracing_virus_y > person.y:
        tracing_virus_y -= trace_virus_speed

    #arcade.draw_circle_filled(tracing_virus_x, tracing_virus_y, 25, arcade.color.WHITE)
    arcade.draw_texture_rectangle(tracing_virus_x, tracing_virus_y, 0.15*trace_virus_image.width, 0.15*trace_virus_image.height, trace_virus_image)


def on_collision():
    global person, dead, spawn_protection, score, tracing_virus_x, tracing_virus_y
    if spawn_protection == False:
        for i in range(len(viruses)):
            distance = ((person.x - viruses[i].x) ** 2 + (person.y - viruses[i].y) ** 2) ** 0.5
            if distance <= 60:
                dead = True

    for i in range(len(viruses)):
        if viruses[i].x <= 25 or viruses[i].x >= 1105:
            viruses[i].speed_x *= -1
        if viruses[i].y <= 25 or viruses[i].y >= 725:
            viruses[i].speed_y *= -1

    distance_trace_virus = ((person.x - tracing_virus_x)**2 + (person.y - tracing_virus_y)**2) ** 0.5
    if spawn_protection == False:
        if distance_trace_virus < 50:
            dead = True

    #   WALL COLLISION FOR PERSON
    if person.x < 25:
        person.x = 25
    if person.x > 1055:
        person.x = 1055
    if person.y < 25:
        person.y = 25
    if person.y > 675:
        person.y = 675

    if spawn_protection == False:
        if dead is False:
            for i in range(len(viruses)):
                distance = ((person.x - viruses[i].x) ** 2 + (person.y - viruses[i].y) ** 2) ** 0.5
                if distance <= 200:
                    score += 2


def on_update(delta_time):
    global play_screen, player_y, player_x, up_pressed, down_pressed, right_pressed, left_pressed, WIDTH, HEIGHT, player_speed
    if play_screen:
        if up_pressed:
            person.y += player_speed
        if down_pressed:
            person.y -= player_speed
        if right_pressed:
            person.x += player_speed
        if left_pressed:
            person.x -= player_speed

    global dead, start_screen, load_screen, viruses, spawn_protection, respawn, score, virus_speed_x, virus_speed_y, game_timer
    if dead:
        if respawn is True:
            viruses = []
            for i in range(2):
                viruses.append(
                    Virus(random.randint(25, 1080), random.randint(25, 700), virus_image.width, virus_image.height,
                          virus_image, virus_speed_x, virus_speed_y))
            person.x = WIDTH/2
            person.y = HEIGHT/2
            up_pressed = False
            down_pressed = False
            right_pressed = False
            left_pressed = False
            spawn_protection = True
            dead = False
            respawn = False
            score = 0
            game_timer = 0
    global loading_timer
    if load_screen:
        loading_timer += delta_time
        if loading_timer >= 8:
            load_screen = False
            play_screen = True
    if spawn_protection == False and dead == False:
        game_timer += delta_time
        if game_timer >= 30:
            dead = True


def on_draw():
    arcade.start_render()

    if start_screen:
    #   DRAW START HERE
        game_start_screen()
    elif play_screen:
    #   DRAW GAME HERE
        game_play_screen()
    elif load_screen:
        game_load_screen()
    elif end_screen:
        game_end_screen()

    if dead:
        arcade.draw_text("You died, your score was "+ str(score) +  "\n press 'f' to reset", title_x, title_y, (210, 255, 248), 30, font_name='CONSOLAS')

def on_key_press(key, modifiers):
    global start_screen, play_screen, load_screen
    if load_screen:
        if key == arcade.key.E:
            start_screen = False
            load_screen = False
            play_screen = True


    if play_screen:
        global up_pressed, down_pressed, right_pressed, left_pressed, player_y, player_x, spawn_protection, score, dead, viruses, respawn, game_timer
        if key == arcade.key.W:
            up_pressed = True
        if key == arcade.key.S:
            down_pressed = True
        if key == arcade.key.D:
            right_pressed = True
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
        if key == arcade.key.R:
            play_screen = False
            start_screen = True
            person.x = WIDTH/2
            person.y = HEIGHT/2
            viruses = []
            for i in range(2):
                viruses.append(
                    Virus(random.randint(25, 1080), random.randint(25, 700), virus_image.width, virus_image.height,
                          virus_image,virus_speed_x ,virus_speed_y))
            dead = False
            score = 0
            game_timer = 0
            spawn_protection = True
        if key == arcade.key.T:
            spawn_protection = False

        if dead:
            if key == arcade.key.F:
                respawn = True


def on_key_release(key, modifiers):
    if play_screen:
        global up_pressed, down_pressed, left_pressed, right_pressed
        if key == arcade.key.W:
            up_pressed = False
        if key == arcade.key.S:
            down_pressed = False
        if key == arcade.key.D:
            right_pressed = False
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


def on_mouse_press(x, y, button, modifiers):
    global start_screen, play_screen, button_video, load_screen, easy_button, medium_button, hard_button, easy, medium, hard, mode, virus_speed_y, virus_speed_x, player_speed, trace_virus_speed
    if start_screen:
        if (x > 800 - (button_1.width)/2 and x < 800 + (button_1.width)/2 and y > 400 - (button_1.height)/2 and y < 400 + (button_1.height)/2):
            print("click")
            player_speed = 5
            trace_virus_speed = 2.5
            start_screen = False
            load_screen = True
        if (x > 750 - (easy_button.width)/2 and x < 800 + (easy_button.width)/2 and y > 300 - (easy_button.height)/2 and y < 300 + (easy_button.height)/2):
            print("yes")
            player_speed = 9
            trace_virus_speed = 1.2
            start_screen = False
            load_screen = True
        if (x > 750 - (medium_button.width)/2 and x < 800 + (medium_button.width)/2 and y > 200 - (medium_button.height)/2 and y < 200 + (medium_button.height)/2):
            player_speed = 7
            trace_virus_speed = 2.2
            start_screen = False
            load_screen = True
        if (x > 750 - (hard_button.width) / 2 and x < 800 + (hard_button.width) / 2 and y > 100 - (hard_button.width) / 2 and y < 100 + (hard_button.height) / 2):
            player_speed = 5
            trace_virus_speed = 2.7
            start_screen = False
            load_screen = True

def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1 / 240)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
