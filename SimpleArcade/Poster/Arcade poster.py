import arcade

#   DIMENSIONS
WIDTH = 1080
HEIGHT = 785

#   TEXTURES
background = arcade.load_texture("Poster/Textures/background.jpg")
diagram = arcade.load_texture("Poster/Textures/e8938de4688a694c58e9e8389f8e5c18.jpg")
bitdefender = arcade.load_texture("Poster/Textures/LOGO_bitdefender_white_red.png")
norton = arcade.load_texture("Poster/Textures/385-3855769_norton-security-online-norton-antivirus-hd-png-download.png")
star = arcade.load_texture("Poster/Textures/1024px-Antu_bookmarks.svg.png")
#   PICTURE BUTTONS
diagram_x = 160
diagram_y = 350
diagram_delta_x = 0
diagram_delta_y = 0

#   CLICKED DIAGRAM
clicked_diagram = False

#   TITLE END DIMENSIONS
title_x = 230
title_y = 720
title_start_y = 800

delta_x_star = 3
star_x = 20


def make_background():
    arcade.draw_texture_rectangle(WIDTH / 2, HEIGHT / 2, 1.27 * background.width, 1.63 * background.height, background,
                                  0)

def on_draw_shapes():
    point_list_1 = ((0, 700),
                    (0, 625),
                    (450, 625),
                    (550, 700))
    arcade.draw_polygon_filled(point_list_1, arcade.color.LIGHT_BLUE)

    point_list_2 = ((0, 625),
                    (450, 625),
                    (310, 520),
                    (0, 520))
    arcade.draw_polygon_outline(point_list_2, (210, 255, 248), 5)

    point_list_3 = ((1080, 700),
                    (1080, 580),
                    (590, 580),
                    (750, 700))
    arcade.draw_polygon_filled(point_list_3, (210, 255, 248))

    point_list_4 = ((325, 325),
                    (400, 425),
                    (775, 425),
                    (700, 325))
    arcade.draw_polygon_filled(point_list_4, (210, 255, 248))

def on_mouse_press(x,y, button, modifiers):
    global diagram_delta_y, diagram_delta_x, clicked_diagram
    #   DIAGRAM CLICK
    if (x > 0 and x < 320 and y > 190 and y < 510):
        clicked_diagram = True
    else:
        pass



def draw_text():
    global title_start_y, title_x, title_y
    #   Title
    arcade.draw_text("Malware Prevention", title_x, title_start_y, (210, 255, 248), 45, font_name='CONSOLAS')

    #   Subtitle 1
    arcade.draw_text("What is Malware", 75, 650, arcade.color.BLACK, 30, font_name='CONSOLAS')
    arcade.draw_text(
        "Malware is any software intentionally \ndesigned to cause damage to a \ncomputer, server, client, \nor computer network.",
        10, 600, arcade.color.WHITE, 15, font_name='CONSOLAS')

    #   SUBTITLE 2
    arcade.draw_text("How to avoid \nMalware", 415, 390, arcade.color.BLACK, 30, font_name='CONSOLAS')

    #   HOW TO AVOID MALWARE
    arcade.draw_text("Surfing the web smartly, don't download suspicious things", 390, 290, arcade.color.BLUE_VIOLET, 15, font_name='CONSOLAS')
    arcade.draw_text("Install a reputable anti-virus", 390, 250, arcade.color.BLUE_VIOLET, 15, font_name='CONSOLAS')
    arcade.draw_text("If something seems too good to be true, \nit probably is, don't fall for scams", 390, 210, arcade.color.BLUE_VIOLET, 15, font_name='CONSOLAs')
    arcade.draw_text("Regularly update device", 390, 150, arcade.color.BLUE_VIOLET, 15, font_name="CONSOLAS")
    #   HOW TO GET MALWARE?
    arcade.draw_text("How can you get Malware?", 10, 480, arcade.color.BLACK, 17, font_name='CONSOLAS')
    arcade.draw_text("Downloading Free \nsuspicous software programs", 20, 450, arcade.color.WHITE, 12, font_name='CONSOLAS')
    arcade.draw_text("Scareware / pop-ups \nthat say you need a \nantivirus, scaring you \ninto installing a false \nantivirus", 20,400, arcade.color.WHITE, 12, font_name='CONSOLAS')
    arcade.draw_text("Not using an antivirus", 20, 295, arcade.color.WHITE, 12, font_name= 'CONSOLAS')

    #   REPUTABLE ANTIVIRUS
    arcade.draw_text("Good antivirus:",720, 625, arcade.color.BLACK, 30, font_name='CONSOLAS')

def draw_images():
    arcade.draw_texture_rectangle(diagram_x + diagram_delta_x, diagram_y + diagram_delta_y , 0.4*diagram.width, 0.4*diagram.height, diagram, 0)
    arcade.draw_texture_rectangle(675, 500, 0.2*bitdefender.width, 0.2*bitdefender.height, bitdefender,0)
    arcade.draw_texture_rectangle(900, 460, 0.15*norton.width, 0.15*norton.height, norton, 0)


def draw_bullet_points():
    arcade.draw_circle_filled(12,405, 5, arcade.color.PURPLE_NAVY)
    arcade.draw_circle_filled(12, 455,5, arcade.color.PURPLE_NAVY)
    arcade.draw_circle_filled(12, 300,5, arcade.color.PURPLE_NAVY)
    arcade.draw_circle_filled(375, 295, 5, arcade.color.WHITE)
    arcade.draw_circle_filled(375, 255, 5, arcade.color.WHITE)
    arcade.draw_circle_filled(375, 215, 5, arcade.color.WHITE)
    arcade.draw_circle_filled(375, 155, 5, arcade.color.WHITE)

def draw_just_be_smart():
    global delta_x_star, star_x
    star_x += delta_x_star
    if star_x <20:
        delta_x_star *= -1
    if star_x > 740:
        delta_x_star *= -1



    arcade.draw_text("Just be smart!", star_x+ 50,70, arcade.color.WHITE, 30, font_name='CONSOLAS')
    arcade.draw_texture_rectangle(star_x,90, 0.1*star.width, 0.1*star.height, star, 0)

def on_update(delta_time):
    global diagram_delta_y, diagram_delta_x, clicked_diagram
    #   DIAGRAM ANIMATION
    if clicked_diagram:
        diagram_delta_y += 5
        diagram_delta_x -= 5

    global title_y, title_start_y
    if title_start_y >= title_y:
        title_start_y -= 1








def on_draw():
    arcade.start_render()
    make_background()
    draw_bullet_points()
    on_draw_shapes()
    draw_text()
    draw_images()
    draw_just_be_smart()



def setup():
    arcade.open_window(WIDTH, HEIGHT, "Malware prevention")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1 / 120)
    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.make_background = make_background
    window.on_mouse_press = on_mouse_press
    arcade.run()


if __name__ == '__main__':
    setup()
