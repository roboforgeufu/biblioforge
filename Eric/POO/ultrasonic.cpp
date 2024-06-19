/*
    Eric Martins
    Classe Sensor Ultrassônico
*/

// Velocidade do som em mm/us 
#define SOUND_SPEED 0.343



class Ultrasonic{
    private:
        int triggerPin, echoPin;
    
    public:
        Ultrasonic(int trigger, int echo) {
            triggerPin = trigger;
            echoPin = echo;

            pinMode(triggerPin, OUTPUT);
            pinMode(echoPin, INPUT);
        }

        float get_distance(){
            digitalWrite(triggerPin, LOW);
            delayMicroseconds(2);

            digitalWrite(triggerPin, HIGH);
            delayMicroseconds(10);
            digitalWrite(triggerPin, LOW);
            float duration = pulseIn(echoPin, HIGH);

            return (duration * SOUND_SPEED) / 2;
        }


};
