import math

import gs
import gs.plus.render as render
import gs.plus.input as input
import gs.plus.scene as scene
import gs.plus.clock as clock
import gs.plus.audio as audio

import globals
import level_game

scn = None
dt_sec = 1.0 / 60.0
screen_clock = 0.0
title_music = None

def setup():
	global scn, title_music
	scn = scene.new_scene()
	scn.Load('@assets/3d/level_title.scn', gs.SceneLoadContext(render.get_render_system()))
	title_music = audio.get_mixer().Stream("@assets/sfx/sfx_cellos_loop.ogg")
	# audio.get_mixer().SetChannelState(title_music, gs.MixerChannelState(0.0, 1.0, gs.MixerRepeat))


def exit():
	audio.get_mixer().Stop(title_music)
	scene.Clear(scn)


def update():
	global dt_sec
	dt_sec = clock.update()
	scene.update_scene(scn, dt_sec)
	if input.key_press(gs.InputDevice.KeyEnter):
		globals.current_scene = level_game


def draw():
	global screen_clock

	def fade_sin(fade):
		return (math.cos(fade * 3.0) + 1.0) * 0.5

	size = render.get_renderer().GetCurrentOutputWindow().GetSize()
	x = size.x * 0.5 - 100.0
	y = size.y * 0.5 - 210.0
	font_size = 80
	screen_clock += dt_sec

	render.text2d(x - size.x * 0.001, y - size.y * 0.001, "Press Enter", font_size, gs.Color(0,0,0, fade_sin(screen_clock) * 0.5),  globals.font_garamond)
	render.text2d(x, y, "Press Enter", font_size, gs.Color(1,1,1, fade_sin(screen_clock)), globals.font_garamond)

	y -= 40
	render.text2d(300, y - 20.0, "The MedieCross Project 2010-2015, made for TigSource.com.", 30, gs.Color.Black, globals.font_garamond)
	render.text2d(350, y - 50.0, "Code : Emmanuel Julien - Art : Francois Gutherz", 30, gs.Color.Black, globals.font_garamond)
	render.text2d(360, y - 80.0, "Animation : Ryan Hagen - Engine : Harfang3D", 30, gs.Color.Black, globals.font_garamond)