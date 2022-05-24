import pygame
import sys
import subprocess
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("TDR-SDC FSAE Italy")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play(mission):
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        runStr = "Mission {0} is now running...".format(mission)
        PLAY_TEXT = get_font(25).render(runStr, True, "Green")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 360),
                            text_input="End this Mission", font=get_font(20), base_color="White", hovering_color="Red")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(60).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 70))

        ACCELERATION = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 200),
                             text_input="Acceleration", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        TRACK_DRIVE = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 270),
                            text_input="TrackDrive", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        SKID_PAD = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 340),
                                text_input="Skid-Pad", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        AUTOCROSS = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 410),
                          text_input="Autocross", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        EBS_TEST = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 480),
                          text_input="EBS test", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        INSPECTION = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 550),
                          text_input="Inspection", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 620),
                             text_input="Quit", font=get_font(35), base_color="#d7fcd4", hovering_color="White")


        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [ACCELERATION, SKID_PAD, TRACK_DRIVE, AUTOCROSS, EBS_TEST, INSPECTION, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ACCELERATION.checkForInput(MENU_MOUSE_POS):
                    play("Acceleration")
                if SKID_PAD.checkForInput(MENU_MOUSE_POS):
                    play("Skid-Pad")
                if TRACK_DRIVE.checkForInput(MENU_MOUSE_POS):
                    play("TrackDrive")
                if AUTOCROSS.checkForInput(MENU_MOUSE_POS):
                    play("Autocross")
                if EBS_TEST.checkForInput(MENU_MOUSE_POS):
                    play("EBS Test")
                if INSPECTION.checkForInput(MENU_MOUSE_POS):
                    play("Inspection")
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()