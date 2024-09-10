import odrive
from odrive.enums import *
import time

def main():
    print("Recherche de l'ODrive...")
    odrv0 = odrive.find_any()
    print("ODrive trouvé. Configuration des calibrations")


    # Calibration du moteur
    print("Calibration du moteur...")
    odrv0.axis1.requested_state = AXIS_STATE_MOTOR_CALIBRATION #calibration du moteur
    for i in range(1, 10):
        print(str(i))
        time.sleep(1)
    odrv0.axis1.motor.config.pre_calibrated = True #pré-calibre pour ne plus avoir a le faire
    
    print("Calibration du moteur terminée.")
    
    # Calibration de l'encodeur
    print("Calibration de l'encodeur...")
    odrv0.axis1.requested_state = AXIS_STATE_ENCODER_OFFSET_CALIBRATION#calibre l'encodeur
    for i in range(1, 15):
        print(str(i))
        time.sleep(1)
    odrv0.axis1.config.startup_encoder_offset_calibration = True#pré-calibre pour ne plus avoir a le faire
    
    print("Calibration de l'encodeur terminée.")
    
    # Passage en mode fermé pour le contrôle en vitesse
    odrv0.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL#passe en mode controle fermer, le moteur tiendra sa position
    odrv0.axis1.config.startup_closed_loop_control = True#pré-calibre pour ne plus avoir a le faire

    odrv0.save_configuration()
     


if __name__ == "__main__":
    main()
