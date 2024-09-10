import odrive #on importe la bibliotheque odrive.
from odrive.enums import *#depuis la bibliotheque, on recupère tout les enumeration(les commandes)

def main():# debut de la fonction main
    print("Recherche de l'ODrive...")
    odrv0 = odrive.find_any()#definir n'importe quelle odrive trouver comme odrv0
    
    print("ODrive trouvé. Configuration de l'axe 1...")
    print("Configuration des paramètre.")
    # Configuration des paramètrest et de la resistance
    odrv0.config.brake_resistance = 2.0 # Configuration de la resistance
    odrv0.config.dc_bus_undervoltage_trip_level = 8.0 # Défini le seuil minimum de tension
    odrv0.config.dc_bus_overvoltage_trip_level = 56.0 # Défini le seuil maximum de tension
    odrv0.config.dc_max_positive_current = 15.0 # le maximum de courrant que peut fournir l'alimentation
    odrv0.config.dc_max_negative_current = -3.0 # Courant maximum que l'alimentation peut absorber.
    odrv0.config.max_regen_current = 0 #Courant maximal autoriser avant d'activer la resistance
    
    print("Configuration du moteur.")
    # Configuration du moteur
    odrv0.axis1.motor.config.pole_pairs = 20 #nombre de poles magnetique du  moteur
    odrv0.axis1.motor.config.calibration_current = 5 #courant utiliserr pour la calibration
    odrv0.axis1.motor.config.resistance_calib_max_voltage = 2#voltage maximum pendant la calibration
    odrv0.axis1.motor.config.motor_type = MOTOR_TYPE_HIGH_CURRENT#type de moteur
    odrv0.axis1.motor.config.current_lim = 15  # Limite de courant en Amperes
    odrv0.axis1.motor.config.requested_current_range = 20 #La plage minimale de courant de phase

    print("Configuration de l'encodeur.")
    #Configuration de l'encodeur
    odrv0.axis1.encoder.config.mode = ENCODER_MODE_INCREMENTAL#mode de l'encodeur
    odrv0.axis1.encoder.config.cpr = 20480#cpr de mon encodeur
    odrv0.axis1.encoder.config.bandwidth = 1000#bande passante pour l'encodeur
    odrv0.axis1.config.calibration_lockin.current = 5                         
    odrv0.axis1.config.calibration_lockin.ramp_time = 0.4
    odrv0.axis1.config.calibration_lockin.ramp_distance = 3.1415927410125732         #valeur utiliser pendant la caibration
    odrv0.axis1.config.calibration_lockin.accel = 20
    odrv0.axis1.config.calibration_lockin.vel = 40

    print("Configuration du mode de controle.")
    #configuration du mode de controle
    odrv0.axis1.controller.config.control_mode = CONTROL_MODE_POSITION_CONTROL#mode de controle
    odrv0.axis1.controller.config.vel_limit = 50#velociter limite
    odrv0.axis1.controller.config.pos_gain = 30#gain de position
    odrv0.axis1.controller.config.vel_gain = 0.02#gain de vitesse 				
    odrv0.axis1.controller.config.vel_integrator_gain = 0.2#gain intégral de la boucle de vitesse
    odrv0.axis1.controller.config.input_mode = INPUT_MODE_TRAP_TRAJ
    odrv0.axis1.trap_traj.config.vel_limit = 30
    odrv0.axis1.trap_traj.config.accel_limit = 5                      #configure le mode de controle par trajectoire(set point)
    odrv0.axis1.trap_traj.config.decel_limit = 5
    odrv0.save_configuration()#enregistre
    
if __name__ == "__main__":#lance la fonction principale
    main()
