## Entendendo o Protocolo ESP-NOW 📡

Este repositório tem como objetivo fornecer uma visão geral do protocolo de comunicação **ESP-NOW**, desenvolvido pela Espressif.


## O que é ESP-NOW? 🤔

ESP-NOW é um protocolo de comunicação sem fio rápido e de *baixa potência* definido pela Espressif. Ele permite que *múltiplos dispositivos* se comuniquem entre si diretamente, sem a necessidade de um roteador Wi-Fi tradicional. É ideal para aplicações que exigem troca de *pequenas quantidades* de dados de forma eficiente e com baixo consumo de energia.

**Principais Características:**

* **Comunicação Direta (Peer-to-Peer):** Dispositivos se comunicam diretamente, reduzindo a latência.
* **Baixa Latência:** Respostas rápidas são possíveis devido à conexão direta.
* **Baixo Consumo de Energia:** O protocolo foi projetado para otimizar o consumo, tornando-o ideal para dispositivos alimentados por bateria.
* **Conexão Unilateral ou Bilateral:** Suporta tanto o envio de dados sem confirmação (unilateral) quanto com confirmação (bilateral).
* **Segurança:** Suporta criptografia para proteger os dados transmitidos.
* **Alcance:** O alcance típico é semelhante ao do Wi-Fi (até algumas dezenas de metros em ambientes internos, e mais em ambientes externos com linha de visada), mas pode variar dependendo do ambiente e das antenas utilizadas.
* **Limite de Pares:** Um dispositivo pode ser pareado com até 20 outros dispositivos no modo criptografado, e um número ilimitado no modo não criptografado (embora haja limitações práticas).

---

## Microcontroladores Compatíveis 칩

O ESP-NOW é uma tecnologia específica da **Espressif Systems**. Portanto, os microcontroladores que podem utilizar essa comunicação são aqueles fabricados pela Espressif, incluindo:

* **ESP8266 Series:** Um microcontrolador Wi-Fi popular e de baixo custo.
* **ESP32 Series:** Uma família de System on a Chip (SoC) mais poderosa, com Wi-Fi e Bluetooth integrados. Isso inclui variações como ESP32-S2, ESP32-C3, ESP32-S3, etc.

É importante notar que, embora ambos suportem ESP-NOW, pode haver pequenas diferenças na implementação ou nas funcionalidades disponíveis entre as séries ESP8266 e ESP32. Consulte sempre a documentação oficial da Espressif para detalhes específicos.

---

## Detalhes Adicionais 📝

* **Não requer Conexão Wi-Fi Ativa:** Embora utilize a frequência de 2.4 GHz (a mesma do Wi-Fi), o ESP-NOW não precisa que os dispositivos estejam conectados a uma rede Wi-Fi ou a um ponto de acesso. Eles podem formar sua própria rede ad-hoc.
* **Endereçamento MAC:** A comunicação ESP-NOW utiliza os endereços MAC dos dispositivos para o envio e recebimento de dados. Cada dispositivo precisa conhecer o endereço MAC do dispositivo com o qual deseja se comunicar.
* **Modos de Operação:**
    * **Controller (Mestre):** Envia dados.
    * **Remote (Escravo):** Recebe dados.
    * Um dispositivo pode atuar como ambos.
* **Callbacks:** A biblioteca ESP-NOW geralmente utiliza funções de callback para notificar a aplicação sobre o status da transmissão (sucesso ou falha) e sobre o recebimento de dados.
* **Payload:** O tamanho máximo do payload (dados úteis) que pode ser enviado em uma única transmissão ESP-NOW é de **250 bytes**.
* **Canais Wi-Fi:** Os dispositivos ESP-NOW devem operar no mesmo canal Wi-Fi para se comunicarem. É responsabilidade do desenvolvedor garantir que os dispositivos estejam configurados para o mesmo canal.

---

## Para descobrir o endereço MAC da placa 🔎
Você precisará do endereço MAC de cada placa para que elas possam se comunicar. Carregue o seguinte código simples em cada ESP8266 para ver o endereço MAC no Monitor Serial: 

```
#include "ESP8266WiFi.h"

void setup(){
  Serial.begin(115200);
  Serial.println();
  Serial.print("Endereço MAC desta placa: ");
  Serial.println(WiFi.macAddress());
}

void loop(){}
```

## Criptografia 👾
 Ambas as placas devem usar a mesma Chave Mestra Primária (PMK) e a mesma Chave Mestra Local (LMK) para que a comunicação criptografada funcione. Mantenha essas chaves em segredo.

## Exemplos
> No ArduinoIDE quando selecionamos a board da ESP32, já aparece exemplos usando o protocolo ESP-NOW, no entanto para a ESP8266 existem algumas adaptações. Por isso, foi gerado os exemplos abaixo. Observe que as bibliotecas chamadas são diferentes (comparando as duas ESP).

### Código para o ESP8266 Transmissor (Sender)
```
#include <ESP8266WiFi.h>
#include <espnow.h>

// SUBSTITUA PELO ENDEREÇO MAC DO ESP8266 RECEPTOR
uint8_t broadcastAddress[] = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF}; // Endereço MAC do receptor

// Defina a mesma PMK (Primary Master Key) em ambos os dispositivos (16 bytes)
const char* pmkKey = "MinhaChavePMK123"; // Mantenha em segredo!

// Defina a mesma LMK (Local Master Key) em ambos os dispositivos (16 bytes)
const char* lmkKey = "MinhaChaveLMK456"; // Mantenha em segredo!

// Estrutura dos dados a serem enviados (deve ser a mesma no receptor)
typedef struct struct_message {
  char texto[32];
  int valor;
  float temperatura;
  bool ligado;
} struct_message;

// Cria uma instância da estrutura
struct_message minhaMensagem;

unsigned long ultimoEnvio = 0;
const int intervaloEnvio = 5000; // Enviar a cada 5 segundos

// Função de callback chamada quando os dados são enviados
void OnDataSent(uint8_t *mac_addr, uint8_t sendStatus) {
  Serial.print("Status do último envio: ");
  if (sendStatus == 0) {
    Serial.println("Entregue com sucesso!");
  } else {
    Serial.println("Falha na entrega.");
  }
}

void setup() {
  Serial.begin(115200);
  Serial.println("\nESP8266 Transmissor ESP-NOW com Criptografia");

  // Coloca o dispositivo no modo Station para ESP-NOW
  WiFi.mode(WIFI_STA);
  WiFi.disconnect(); // Opcional: desconecta de qualquer rede Wi-Fi anterior

  // Inicializa o ESP-NOW
  if (esp_now_init() != 0) { // No ESP8266, 0 significa sucesso
    Serial.println("Erro ao inicializar ESP-NOW");
    return;
  }

  // Define a função de callback para o status do envio
  esp_now_set_self_role(ESP_NOW_ROLE_CONTROLLER); // Define o papel como controlador/transmissor
  esp_now_register_send_cb(OnDataSent);

  // Configura a chave PMK (Primary Master Key)
  // É uma chave global para a interface ESP-NOW.
  if (esp_now_set_pmk((uint8_t *)pmkKey) != 0) {
    Serial.println("Erro ao definir PMK");
    return;
  }
  Serial.println("PMK definida.");

  // Registra o peer (receptor) com criptografia
  // O último parâmetro '1' ou 'true' habilita a criptografia para este peer.
  // A chave LMK é passada aqui.
  if (esp_now_add_peer(broadcastAddress, ESP_NOW_ROLE_SLAVE, 0, (uint8_t *)lmkKey, 16) != 0) {
    Serial.println("Erro ao adicionar peer");
    return;
  }
  Serial.println("Peer adicionado com criptografia.");

  // Preenche a estrutura com dados de exemplo
  strcpy(minhaMensagem.texto, "Ola do ESP8266!");
  minhaMensagem.valor = random(0, 100);
  minhaMensagem.temperatura = 25.5;
  minhaMensagem.ligado = true;
}

void loop() {
  if (millis() - ultimoEnvio > intervaloEnvio) {
    ultimoEnvio = millis();

    // Atualiza algum valor para variar a mensagem
    minhaMensagem.valor = random(0, 100);
    minhaMensagem.temperatura += 0.1;
    if (minhaMensagem.temperatura > 35.0) {
      minhaMensagem.temperatura = 20.0;
    }
    minhaMensagem.ligado = !minhaMensagem.ligado;

    Serial.print("Enviando dados: ");
    Serial.print(minhaMensagem.texto);
    Serial.print(", Valor: ");
    Serial.print(minhaMensagem.valor);
    Serial.print(", Temp: ");
    Serial.print(minhaMensagem.temperatura);
    Serial.print(", Ligado: ");
    Serial.println(minhaMensagem.ligado);

    // Envia a mensagem para o MAC address do receptor
    // O tamanho da mensagem deve ser exato (sizeof(minhaMensagem))
    esp_now_send(broadcastAddress, (uint8_t *) &minhaMensagem, sizeof(minhaMensagem));
  }
}
```
### Código para o ESP8266 Receptor (Receiver)
```
#include <ESP8266WiFi.h>
#include <espnow.h>

// Defina a mesma PMK (Primary Master Key) em ambos os dispositivos (16 bytes)
const char* pmkKey = "MinhaChavePMK123"; // Mantenha em segredo! Deve ser a mesma do transmissor.

// Defina a mesma LMK (Local Master Key) em ambos os dispositivos (16 bytes)
const char* lmkKey = "MinhaChaveLMK456"; // Mantenha em segredo! Deve ser a mesma do transmissor.

// Estrutura dos dados a serem recebidos (deve ser a mesma no transmissor)
typedef struct struct_message {
  char texto[32];
  int valor;
  float temperatura;
  bool ligado;
} struct_message;

// Cria uma instância da estrutura para armazenar os dados recebidos
struct_message dadosRecebidos;

// Função de callback chamada quando dados são recebidos
void OnDataRecv(uint8_t *mac_addr, uint8_t *incomingData, uint8_t len) {
  // Copia os dados recebidos para a estrutura local
  memcpy(&dadosRecebidos, incomingData, sizeof(dadosRecebidos));

  Serial.println("---------------------------------");
  Serial.print("Dados recebidos de: ");
  for (int i = 0; i < 6; i++) {
    Serial.printf("%02X", mac_addr[i]);
    if (i < 5) Serial.print(":");
  }
  Serial.println();

  Serial.print("Texto: ");
  Serial.println(dadosRecebidos.texto);
  Serial.print("Valor: ");
  Serial.println(dadosRecebidos.valor);
  Serial.print("Temperatura: ");
  Serial.println(dadosRecebidos.temperatura);
  Serial.print("Ligado: ");
  Serial.println(dadosRecebidos.ligado ? "SIM" : "NAO");
  Serial.print("Bytes recebidos: ");
  Serial.println(len);
  Serial.println("---------------------------------");
}

void setup() {
  Serial.begin(115200);
  Serial.println("\nESP8266 Receptor ESP-NOW com Criptografia");

  // Coloca o dispositivo no modo Station para ESP-NOW
  WiFi.mode(WIFI_STA);
  WiFi.disconnect(); // Opcional

  // Inicializa o ESP-NOW
  if (esp_now_init() != 0) {
    Serial.println("Erro ao inicializar ESP-NOW");
    return;
  }

  // Define o papel como receptor/escravo
  esp_now_set_self_role(ESP_NOW_ROLE_SLAVE);

  // Configura a chave PMK (Primary Master Key)
  // Deve ser a mesma do transmissor.
  if (esp_now_set_pmk((uint8_t *)pmkKey) != 0) {
    Serial.println("Erro ao definir PMK");
    return;
  }
  Serial.println("PMK definida.");

  // IMPORTANTE: Para que o receptor receba dados criptografados,
  // ele NÃO precisa adicionar o transmissor como peer explicitamente com a LMK aqui,
  // se o transmissor já iniciou a comunicação criptografada com a LMK correta.
  // O receptor apenas precisa ter a PMK correta configurada.
  // Se o receptor também for ENVIAR dados de volta para o transmissor de forma criptografada,
  // aí sim ele precisaria adicionar o transmissor como peer com a LMK.

  // Registra a função de callback para o recebimento de dados
  esp_now_register_recv_cb(OnDataRecv);

  Serial.println("Aguardando dados...");
}

void loop() {
  // Não há nada para fazer no loop principal, tudo é tratado por callbacks
  delay(100); // Pequeno delay para estabilidade
}
```

1. Descubra os Endereços MAC: Carregue o sketch para descobrir o MAC em cada ESP8266 e anote-os.
2. Atualize o Código do Transmissor: No código do Transmissor, substitua uint8_t broadcastAddress[] = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF}; pelo endereço MAC real da sua placa Receptora. Por exemplo: uint8_t broadcastAddress[] = {0x1A, 0x2B, 0x3C, 0x4D, 0x5E, 0x6F};.
3. Chaves de Criptografia: Certifique-se de que pmkKey e lmkKey são idênticos em ambos os sketches (Transmissor e Receptor).
4. Carregue os Códigos: Carregue o sketch do Transmissor em uma ESP8266 e o sketch do Receptor na outra.
5. Abra os Monitores Seriais: Abra o Monitor Serial para ambas as placas (em instâncias separadas da IDE ou em um terminal serial). Você deverá ver o transmissor enviando dados e o receptor recebendo-os e imprimindo no console.

### Observações sobre Criptografia no ESP8266 com ESP-NOW:

- esp_now_set_pmk((uint8_t*)pmkKey): Define a Chave Mestra Primária. Esta chave é usada para derivar chaves de sessão. Ela deve ser a mesma em ambos os dispositivos que desejam se comunicar de forma criptografada.
- esp_now_add_peer(broadcastAddress, ESP_NOW_ROLE_SLAVE, 0, (uint8_t *)lmkKey, 16):
- O broadcastAddress é o MAC do receptor.
- ESP_NOW_ROLE_SLAVE indica o papel do peer.
- 0 é o canal Wi-Fi (0 para usar o canal atual).
- (uint8_t *)lmkKey é a Chave Mestra Local. Esta chave também deve ser a mesma entre o par de dispositivos que desejam se comunicar.
- 16 é o tamanho da LMK em bytes.
- A criptografia é habilitada para este peer quando a LMK é fornecida (não nula). No ESP8266, o parâmetro encrypt (que seria o último) não existe como no ESP32. A presença de uma LMK não nula implica criptografia. No entanto, a documentação mais antiga e a API do ESP8266 podem ser um pouco menos explícitas. O código acima reflete uma prática comum para habilitar a criptografia. Se você encontrar problemas, pode ser necessário verificar a versão específica do SDK do ESP8266 que está usando.
- Atualização com base na API do ESP8266 RTOS SDK: A função esp_now_add_peer no ESP8266 tem a seguinte assinatura: int esp_now_add_peer(u8 *mac_addr, u8 role, u8 channel, u8 *key, u8 key_len). O último parâmetro key_len (comprimento da chave) sendo não zero e key sendo não nulo habilita a criptografia usando essa LMK.

---

## Referências 📚

* **Documentação Oficial ESP-NOW (Espressif):**
    * [ESP-NOW API Guide (para ESP-IDF)](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_now.html)
* **Tutoriais e Exemplos (Comunidade):**
    * [Fernando K Tecnologia - ESP32 com protocolo ESP-NOW](https://youtu.be/JkMOrQ2Occw?si=aix4wBQe7yr5gIcN)
    * [Programming Eletronics Academy - ESPNOW mix with #ESP32 and #ESP8266 ](https://youtu.be/_eHe7ViXyY8?si=fwM4MXuQNISR7DRA)
    * [How to use PS4 Controller with ESP32 ](https://www.youtube.com/watch?v=dRysvxQfVDw)
    * [TUTORIAL: Convierte tu mando de PS4 en control para MINISUMO RC con ESP32](https://youtu.be/Nn53sg2A-YM?si=0x4_UAPHOCL_3M2i)
