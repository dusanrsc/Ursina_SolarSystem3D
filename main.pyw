# importing modules and sub-modules
from ursina import *
import random

# special variables
# meta data
__name__ = "Solar System 3D"
__version__ = "v1.0"

# solar system info
info = """
• Sun (central star):
  Diameter: ~1,391,000 km

• Mercury:
  Distance from Sun: ~0.39 AU (57.9 million km)
  Diameter: ~4,880 km

• Venus:
  Distance from Sun: ~0.72 AU (108.2 million km)
  Diameter: ~12,104 km

• Earth:
  Distance from Sun: ~1 AU (149.6 million km)
  Diameter: ~12,742 km

• Mars:
  Distance from Sun: ~1.52 AU (227.9 million km)
  Diameter: ~6,779 km

• Jupiter:
  Distance from Sun: ~5.2 AU (778.6 million km)
  Diameter: ~139,820 km

• Saturn:
  Distance from Sun: ~9.5 AU (1.429 billion km)
  Diameter (excluding rings): ~120,536 km

• Uranus:
  Distance from Sun: ~19.2 AU (2.871 billion km)
  Diameter: ~50,724 km

• Neptune:
  Distance from Sun: ~30.1 AU (4.498 billion km)
  Diameter: ~49,244 km
"""

# variables
orbit_radius = 10
orbit_speed = -0.05
angle = 5

quit_question_counter = 0

# color constants
RED = color.rgb(200, 0, 0)
GREEN = color.rgb(0, 200, 0)
BLUE = color.rgb(0, 0, 200)

BLACK = color.black
WHITE = color.white

BACKGROUND = color.rgba(0, 0, 200, 200)

ALPHA = GREEN

# creating main app window
app = Ursina()

# window settings
window.exit_button.enabled = False
window.fps_counter.enabled = False
window.entity_counter.enabled = False
window.collider_counter.enabled = False
window.fullscreen = False

# help message
def help_message():
	help_message = Button(parent=camera.ui, scale=(.25, .1), text="[MOUSE] Camera\n [F] Fullscreen\n [ESC] Quit", position=(-.73, .42), color=BACKGROUND)
	
	# destroy help message entities
	def destroy_help_message():
		destroy(help_message)

	# destroying help message on exit button click 
	help_message.on_click = destroy_help_message

# info message
def info_message():
	info_message = Button(parent=camera.ui, scale=(0.65, 0.95), text=info, position=(0, 0), color=BACKGROUND)

	# destroy info message entities
	def destroy_info_message():
		destroy(info_message)

	# destroying info message on exit button click 
	info_message.on_click = destroy_info_message

# quit app message
def quit_message():
	# abort quit function
	def abort_quit():
		global quit_question_counter
		quit_question_counter = 0

		# destroying quit message entities
		destroy(question)
		destroy(yes_answer)
		destroy(no_answer)

	# question
	question = Button(parent=camera.ui, text=f"Quit {__name__}?", scale=(.5, .2), position=(0, .05), color=BACKGROUND)

	# answer positive
	yes_answer = Button(parent=camera.ui, text="Yes", scale=(.15, .055), position=(-.1, -.05, 0), color=RED, collider="mesh")
	yes_answer.on_click = application.quit

	# answer negative
	no_answer = Button(parent=camera.ui, text="No", scale=(.15, .055), position=(.1, -.05, 0), color=GREEN, collider="mesh")
	no_answer.on_click = abort_quit

# input function
def input(key):
	# fullscreen or window
	if key == "f" and window.fullscreen == False:
		window.fullscreen = True
	elif key == "f" and window.fullscreen == True:
		window.fullscreen = False

# update function
def update():
	# exit app
	if held_keys["escape"]:
		# restricting quit question more than one
		global quit_question_counter
		quit_question_counter += 1

		# condition for showing only one message
		if quit_question_counter <= 1:
			quit_message()
		else:
			pass

	# importing variables
	global angle

	# circular movement
	# circular movement for mercury
	mercury.x = orbit_radius * math.cos(angle)
	mercury.z = orbit_radius * math.sin(angle)

	# circular movement for venus
	venus.x = 20 * math.cos(angle)
	venus.z = 20 * math.sin(angle)

	# circular movement for earth
	earth.x = 30 * math.cos(angle)
	earth.z = 30 * math.sin(angle)

	# circular movement for earth moon
	earth_moon.x = 32 * math.cos(angle)
	earth_moon.z = 32 * math.sin(angle)

	# circular movement for mars
	mars.x = 40 * math.cos(angle)
	mars.z = 40 * math.sin(angle)

	# circular movement for jupiter
	jupiter.x = 50 * math.cos(angle)
	jupiter.z = 50 * math.sin(angle)

	# circular movement for saturn and saturn ring
	saturn.x = 60 * math.cos(angle)
	saturn.z = 60 * math.sin(angle)
	saturn_ring.x = 60 * math.cos(angle)
	saturn_ring.z = 60 * math.sin(angle)

	# circular movement for uranus
	uranus.x = 70 * math.cos(angle)
	uranus.z = 70 * math.sin(angle)

	# circular movement for neptune
	neptune.x = 80 * math.cos(angle)
	neptune.z = 80 * math.sin(angle)

	# angle changing
	angle += orbit_speed * time.dt

	# rotating animation
	sun.rotation_y += 0.1
	mercury.rotation_x += 0.1
	venus.rotation_z += 0.2
	earth.rotation_x -= 0.2
	earth_moon.rotation_y -= 0.1
	mars.rotation_z -= 0.2
	jupiter.rotation_x += 0.1
	saturn.rotation_y += 0.1
	saturn_ring.rotation_y += 0.1
	uranus.rotation_x -= 0.3
	neptune.rotation_y -= 0.3

# help message at the start
help_message()

# editor camera
EditorCamera()

# creating objects
# creating space
space = Sky(color=WHITE, texture="textures/8k_stars_milky_way")

# creating stars
for i in range(1000):
	star = Button(parent=scene, model="sphere", color=WHITE, scale=0.5, position=(random.randint(-1000, 1000), random.randint(-1000, 1000), random.randint(-1000, 1000)))

# creating planets
# creating sun
sun = Button(parent=scene, model="sphere", texture="textures/8k_sun", color=WHITE, scale=13.910, collider="mesh")
sun.on_click = info_message

# creating mercury
mercury = Button(parent=scene, model="sphere", texture="textures/8k_mercury", color=WHITE, scale=0.488, collider="mesh")

# creating venus
venus = Button(parent=scene, model="sphere", texture="textures/8k_venus_surface", scale=1.210, color=WHITE, collider="mesh")

# creating earth
earth = Button(parent=scene, model="sphere", texture="textures/8k_earth_daymap", color=WHITE, scale=1.274, collider="mesh")

# creating earth moon
earth_moon = Button(parent=scene, model="sphere", texture="textures/8k_moon", color=WHITE, scale=0.347, collider="mesh")

# creating mars
mars = Button(parent=scene, model="sphere", texture="textures/8k_mars", color=WHITE, scale=0.677, collider="mesh")

# creating jupiter
jupiter = Button(parent=scene, model="sphere", texture="textures/8k_jupiter", color=WHITE, scale=1.398, collider="mesh")

# creating saturn
saturn = Button(parent=scene, model="sphere", texture="textures/8k_saturn", color=WHITE, scale=1.164, collider="mesh")

# creating saturn ring
saturn_ring = Button(parent=scene, model="sphere", texture="textures/8k_saturn_ring_alpha", color=WHITE, scale=(2.820, 0.005, 2.820), rotation=(0, 0, 15), collider="mesh")

# creating uranus
uranus = Button(parent=scene, model="sphere", texture="textures/2k_uranus", color=WHITE, scale=0.507, collider="mesh")

# creating neptune
neptune = Button(parent=scene, model="sphere", texture="textures/2k_neptune", color=WHITE, scale=0.492, collider="mesh")

# running the app
app.run()