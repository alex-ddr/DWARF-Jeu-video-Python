import pygame, ctypes, sys
from functions import store_animations
from Heroes_Dico import *
from level import Level
from settings import screen_width, screen_height, FPS, level_map
    
ctypes.windll.user32.SetProcessDPIAware() 

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED)
pygame.event.set_grab(True)
clock = pygame.time.Clock()
icon = pygame.image.load('DWARF/icon/icon.png')
pygame.display.set_icon(icon)


font = pygame.font.Font(None, 30)
def display_fps():
    fps = clock.get_fps()
    fps_text = font.render("{:.2f}".format(int(fps)), True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))


all_animations = store_animations([santa_dico_v1, minotaur_dico_v1, dwarf_dico_v1, indiana_jones_dico_v1, adventurer_dico_v1, bat_dico_v1, halo_dico_v1, gladiator_dico_v1, demon_dico_v1, cyclop_dico_v1], [hobbit_dico_v2, question_mark_dico_v2])

player1_hero_choice = 'santa'
player2_hero_choice = 'hobbit'

player1_hero = [all_animations[heroes_dico[player1_hero_choice][0]], heroes_dico[player1_hero_choice][1], heroes_dico[player1_hero_choice][2], player1_hero_choice, heroes_dico[player1_hero_choice][3]]
player2_hero = [all_animations[heroes_dico[player2_hero_choice][0]], heroes_dico[player2_hero_choice][1], heroes_dico[player2_hero_choice][2], player2_hero_choice, heroes_dico[player2_hero_choice][3]]

level = Level(level_map, screen, player1_hero, player2_hero)

while True:
    screen.fill((255, 255, 255))
    level.run()
    display_fps()
    pygame.display.update()
    clock.tick(FPS)
