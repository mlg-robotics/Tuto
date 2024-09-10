import odrive
from odrive.enums import *
import time

def main():
    print("Recherche de l'ODrive...")
    odrv0 = odrive.find_any()
    
    print("ODrive trouvé.")
    x = input('choisissez la position')
    print("le moteur bouge")
    odrv0.axis1.controller.input_pos = x
    for i in range(1, 4):
           print(str(i))
           time.sleep(1)
    odrv0.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
    
    print("le moteur a fini de bouger")

if __name__ == "__main__":
    main()
