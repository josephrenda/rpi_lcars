from screens.authorize import ScreenAuthorize
from ui.ui import UserInterface

# global config
UI_PLACEMENT_MODE = True
RESOLUTION = (800, 480)
FPS = 30
DEV_MODE = False

if __name__ == "__main__":
    firstScreen = ScreenAuthorize()
    ui = UserInterface(firstScreen, RESOLUTION, UI_PLACEMENT_MODE, FPS, DEV_MODE)

    while (True):
        ui.tick()
