class LDR{
    private:
        int pin;

    public:
        LDR(int sensorPin){
            pin = sensorPin;
            pinMode(sensorPin, INPUT);
        }

        int getValue(){
            int valor_sensor = analogRead(pin);

            // Arduino
            return map(valor_sensor, 0, 1023, 0, 100);

            // ESP32
            //return map(valor_sensor, 0, 4095, 0, 100);
        }
};
