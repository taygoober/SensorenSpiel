import random
import time
from gpiozero import PWMOutputDevice

buzzer = PWMOutputDevice(22, frequency=500, initial_value=0.0)


class RandomSensor:
    def randomchallange(self):
        return random.randint(1, 9)
stage = RandomSensor()

def runde_gewonnen():
    buzzer.value = 0.5 
    
    buzzer.frequency = 600
    time.sleep(0.15)
    buzzer.frequency = 800
    time.sleep(0.3)
    buzzer.value = 0.0

def runde_gewonnen_gross():
    buzzer.value = 0.5

    buzzer.frequency = 1319
    time.sleep(0.125)
    buzzer.frequency = 1568
    time.sleep(0.125)
    buzzer.frequency = 2637
    time.sleep(0.125)
    buzzer.frequency = 2093
    time.sleep(0.125)
    buzzer.frequency = 2349
    time.sleep(0.125)
    buzzer.frequency = 3136
    time.sleep(0.125)
    buzzer.value = 0.0

def runde_verloren():
    buzzer.value = 0.5     
    
    buzzer.frequency = 300
    time.sleep(0.3)
    buzzer.frequency = 150
    time.sleep(0.6)
    buzzer.value = 0.0

def get_multiplikator(runde):
    base_points = 1.5
    growth = 0.5
    return round(base_points ** (runde * growth), 2)

def score_berechnen(Base_points, runde):
    UserScore = Base_points * get_multiplikator(runde)
    return UserScore


def playgame():
    runde = 1
    score = 100
    while True:
        Aufgabe1 = [stage.randomchallange() for i in range(runde)]
        print("Challenge:", Aufgabe1)

        Playerinputs = list(map(int, input("Geben sie die Aufgabe wieder ").split()))
        print(Playerinputs)

        if Aufgabe1 == Playerinputs:
            runde_gewonnen()
            print(f"Glückwunsch, Sie haben Runde {runde} bestanden")
            # 1. Calculate and add the score for the round you just finished
            earned_points = score_berechnen(100, runde)
            score = score + earned_points
            
            print(f"Aktueller Gesamt-Score: {score}")

            runde = runde + 1

            if runde == 5:
                runde_gewonnen_gross
        else:
            runde_verloren()
            print(f"Falsch eingegeben. Ihr Score ist {score}")
            break

playgame()
