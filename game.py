import arcade

WIDTH = 800
HEIGHT = 600
TITLE = "THE BEST GAME"

window = arcade.open_window(WIDTH, HEIGHT, TITLE)

arcade.start_render()
arcade.draw_circle_filled(400, 300, 150, arcade.color.GREEN)
arcade.draw_circle_filled(400, 300, 130, arcade.color.BLUE)
arcade.draw_circle_filled(400, 300, 110, arcade.color.WHITE)
arcade.draw_circle_filled(400, 300, 95, arcade.color.BLACK)
arcade.draw_ellipse_filled(390, 250, 70, 50, arcade.color.WHITE)
arcade.draw_ellipse_filled(430, 340, 50, 70, arcade.color.WHITE)
arcade.finish_render()

arcade.run()