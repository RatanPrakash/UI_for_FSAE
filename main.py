from runpy import run_module
import pygame , sys
import subprocess
from button import Button

# todo Initializing PyGame and Joystick
pygame.init()
pygame.joystick.init()
_joystick = pygame.joystick.Joystick(0)
_joystick.init()


SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("TDR-SDC FSAE Italy")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play(mission):
    process = subprocess.Popen("./accBash.bash", shell = True) 
    while True:
        SCREEN.fill("black")
        runStr = "Mission {0} is now running...".format(mission)
        PLAY_TEXT = get_font(25).render(runStr, True, "Green")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 360),
                            text_input="End this Mission", font=get_font(20), base_color="White", hovering_color="Red")
        
        PLAY_MOUSE_POS = (640, 360)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if _joystick.get_button(0):
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    subprocess.run("pkill ros", shell=True)
                    _joystick.rumble(0.3,0.9,1500)
                    SCREEN.fill("black")
                    endStr = "Mission {0} is now CLOSING...".format(mission)
                    waitStr = "PLEASE WAIT!!!"
                    END_TEXT = get_font(25).render(endStr, True, "Green")
                    END_RECT = PLAY_TEXT.get_rect(center=(640, 260))
                    WAIT_TEXT = get_font(30).render(waitStr, True, "Red")
                    WAIT_RECT = WAIT_TEXT.get_rect(center = (640, 320))
                    SCREEN.blit(END_TEXT, END_RECT)
                    SCREEN.blit(WAIT_TEXT,WAIT_RECT)
                    pygame.display.update()
                    pygame.time.delay(9000)
                    main_menu()
                    
        pygame.display.update()
        


def main_menu():
    x, y = 640, 200          ##Initial mouse position
    MENU_MOUSE_POS = (x, y)  ## Initialised to 1st option
    while True:
        MENU_MOUSE_POS = (x, y)
        SCREEN.blit(BG, (0, 0))

        MENU_TEXT = get_font(60).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 70))

        ACCELERATION = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 200),
                             text_input="Acceleration", font=get_font(35), base_color="#0d0d0d", hovering_color="White")
        TRACK_DRIVE = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 270),
                            text_input="TrackDrive", font=get_font(35), base_color="#0d0d0d", hovering_color="White")
        SKID_PAD = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 340),
                                text_input="Skid-Pad", font=get_font(35), base_color="#0d0d0d", hovering_color="White")
        AUTOCROSS = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 410),
                          text_input="Autocross", font=get_font(35), base_color="#0d0d0d", hovering_color="White")
        EBS_TEST = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 480),
                          text_input="EBS test", font=get_font(35), base_color="#0d0d0d", hovering_color="White")
        INSPECTION = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 550),
                          text_input="Inspection", font=get_font(35), base_color="#0d0d0d", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 620),
                             text_input="Quit", font=get_font(35), base_color="#0d0d0d", hovering_color="White")


        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [ACCELERATION, SKID_PAD, TRACK_DRIVE, AUTOCROSS, EBS_TEST, INSPECTION, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)

        hat = _joystick.get_hat(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if hat[1] == -1:
                # if event.key == pygame.K_DOWN:
                if y >= 620:
                    y = 200
                else:
                    y = y + 70

            if hat[1] == 1:
                if y <= 200:
                    y = 620
                else:
                    y = y - 70
    

            if _joystick.get_button(0):
                
                if ACCELERATION.checkForInput(MENU_MOUSE_POS):
                    _joystick.rumble(0.3,0.9,500)
                    play("Acceleration")
                if SKID_PAD.checkForInput(MENU_MOUSE_POS):
                    _joystick.rumble(0.3,0.9,500)
                    play("Skid-Pad")
                if TRACK_DRIVE.checkForInput(MENU_MOUSE_POS):
                    _joystick.rumble(0.3,0.9,500)
                    play("TrackDrive")
                if AUTOCROSS.checkForInput(MENU_MOUSE_POS):
                    _joystick.rumble(0.3,0.9,500)
                    play("Autocross")
                if EBS_TEST.checkForInput(MENU_MOUSE_POS):
                    _joystick.rumble(0.3,0.9,500)
                    play("EBS Test")
                if INSPECTION.checkForInput(MENU_MOUSE_POS):
                    _joystick.rumble(0.3,0.9,500)
                    play("Inspection")
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    _joystick.rumble(0.3,0.9,500)
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
