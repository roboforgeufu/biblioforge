class LDR {
  public:
    // construtor que aceita o pino analógico como parâmetro
    LDR(int pin, int adcResolution, float refVoltage) {
      sensorPin = pin; // configura o pino analógico
      resolution = adcResolution;
      voltage = refVoltage;
      threshold = (1 << resolution) / 2; // limite para distinguir entre preto e branco
      gndPin = 0; //configura o pino GND (padrão)
    }

    // método para ler o valor do sensor e converter para qualitativo
    int readSensor() {
      sensorValue = analogRead(sensorPin); // lê o valor do pino analógico
      if (sensorValue < threshold) {
        return 0; // cor preta
      } else {
        return 1; // cor branca
      }
    }

    // método para retornar a leitura do sensor em porcentagem
    float percentageSensor() {
      sensorValue = analogRead(sensorPin); // lê o valor do pino analógico
      return (sensorValue / float(1 << resolution)) * 100; // retorna o valor em porcentagem
    }

  private:
    int sensorPin; // pino analógico do sensor
    int gndPin; // pino GND (padrão)
    int resolution; // resolução ADC (bits)
    float voltage; // tensão de referência
    int threshold; // limite para distinguir entre preto e branco
    int sensorValue; // valor lido do sensor
};

// instancia o sensor LDR esquerdo no pino A0
LDR sensorTeste(A0, 10, 5.0);

void setup() {
  Serial.begin(9600); // inicia a comunicação serial a 9600 bps - ARDUINO UNO (?)
}

void loop() {
  int bin = sensorTeste.readSensor(); // lê o valor qualitativo do sensor
  float percentage = sensorTeste.percentageSensor(); // lê a porcentagem do sensor
  Serial.println(bin); // imprime o resultado (0 ou 1) no monitor serial
  Serial.println(percentage); // imprime a porcentagem no monitor serial
  delay(300); // espera 0,3 segundos antes de ler novamente
}
