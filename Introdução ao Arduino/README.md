# Iniciação em Arduino

O **Arduino** é uma plataforma de prototipagem eletrônica de código aberto, podendo ser descrito como um pequeno computador (**microcontrolador**). Através de suas portas a placa Arduino consegue interpretar suas entradas e controlar suas saídas para a acionar motores e lâmpadas, monitorar o ambiente através dos sensores, e etc.

Nesse tutorial vamos aprender o básico de Arduino como o entendimento de suas **portas** e como isso influencia na sua **programação**, e algumas formas de programar o Arduino em si no contexto da robótica para as competições das quais participamos.

# Portas:

O Arduino é separado portas de 3 categorias, **portas Analógicas, portas digitais e portas PWM.** Apesar de fazer parte da montagem do robô, é importante se atentar a quais portas os componentes estão conectados, pois isso influencia nas interfaces de entrada e saída da placa. 

### Portas Analógicas:

As portas analógicas podem assumir uma variedade de valores não binários de uma faixa de valores. Servindo para ler sinais que variam de forma continua, como a tensão de um sensor, a posição de um potenciômetro, e também para mandar definir valores de mais precisos de saída como velocidade ou intensidade de um componente, podendo assumir até 1024 valores diferentes. Essas portas são marcadas com a letra A junto do numero como A0, A1, etc.

Os valores variam de **0** á **1023** onde o **0** corresponde a **0v** e **1023** a **5v.** Isso ocorre porque o conversor analógico-digital possui 10 bits de resolução, 2^10 = 1024

E essas portas recebem como funções:

```cpp

analogWrite();

analogRead();
```

<img src = "Imagens informativas\Analógico.png">

### Portas Digitais:

De forma diferente das portas analógicas, as portas digitais podem ser definidas por saltos entre valores vem definidos, e são usadas para valores de entrada e saida em apenas dois estados: Ligado (**HIGH**) ou desligado(**LOW**). Esses valores no **Arduino UNO** são referenciados por **HIGH** sendo **5V** e **LOW 0V.** E podem ser usadas em casos que não precisam de um controle de intensidade tão definido, estando apenas ligado ou desligado.

E essas portas recebem como funções:

```cpp

digitalWrite();

digitalRead();

```

<img src = "Imagens informativas\Digital.png">

### Portas PWM:

Algumas portas digitais são diferentes com outras funcionalidades essas são as portas **PWM,** e sua diferenciação se da pelo símbolo **(~)** ao lado do numero da porta. o nome PWM se traduz como **(Pulse Width Modulation)** que se traduz como modulação por largura de pulso, possuem esse nome pois são capazes de modular sinais digitais em sinais analógicos

Apesar de serem portas digitais, elas conseguem assumir valores entre 0 a 255 modulando o sinal digital. São usadas para controle de intensidade assim como as portas analógicas, e são as mais usadas para controle de velocidade de motores de seguidores de linha

Essas portas recebem como funções:

```cpp
digitalWrite();

digitalRead();

analogWrite();
```

<img src = "Imagens informativas\PWM.png">

# Programação:

Partindo para a programação, o Arduino utiliza uma linguagem baseado no C++ de forma simplificada. Para todos que não conhecem o C++ ainda irão sentir certa familiaridade com a linguagem, pois possui alguns aspectos em comum com a linguagem C, que todos já devem ter visualizado em algum momento.

### Formatação:

```cpp
void setup()
{
/*void setup() é uma das funções obrigatorias do arduino, que são usadas para declarar
ações que são executadas apenas uma vez. Sem a declaração do void setup() seu programa
retornará um erro.
É usado para inicializar variáveis, configuração de pinos, iniciar bibliotecas, e 
declarar entradas e saidas.*/
}

void loop()
{
/*O void loop() assim como a anterior também é uma função obrigatoria do Arduino.
É usada para declarar ações a serem repetidas diversas vezes em loop como o nome diz.
Sem essa função o programa retornará erro.
*/
}
```

### Funções de ações:

```cpp
/*As funções desse bloco são para declaração de pinos (sensores/motores) e como 
enviar ações para esses componentes.*/

pinMode(pin, mode);/* Configura o pino para se comportar como uma entrada 
ou saída, usando a declaração INPUT, ou OUTPUT em letras maiúsculas tem de ser declarada
no void setup()*/ pinMode(A1,INPUT);

digitalWrite(pin, value);/* Escreve um valor HIGH ou LOW (Ligado ou desligado)
 para um pino digital, que foi declarado como OUTPUT*/digitalWrite(8, HIGH);

digitalRead(pin);/* Lê o valor de um pino digital, como HIGH ou LOW (Ligado ou
Desligado) que foi declarado como INPUT*/ digitalRead(8);

analogRead(pin);/* Lê o valor de um pino analógico. Lembrando que assume valores de 
0 a 1023*/ analogRead(A1);

analogWrite(pin, value);/* Escreve um valor analógico para um pino analogico ou um pino
PWM, que foram declarados como OUTPUT.*/analogWrite(A0, vel);
```

### Funções de tempo:

```cpp
/*São funções bloqueantes do programa, que vai parar a execução do codigo pelo tempo 
estipulado, ou contar o tempo de execução*/

delay(ms);/* Pausa o programa por uma quantidade de tempo especificada em milissegundos
*/ delay(1000);

millis();/* Retorna o número de milissegundos desde que o Arduino começou a executar 
o programa atual.*/

delayMicroseconds(us);/* Pausa o programa por uma quantidade de tempo especificada
em microsegundos, pode ser útil para atras mais curtos ou controle dos pulsos PWM*/ 
```

### Funções do terminal:

```cpp
/* Essas são as funções para iniciar a execução do terminal, e como fazer prints. Vai 
ser util para qualquer retorno que quiser pelo terminal */

Serial.begin(speed);/* Para qualquer uso do terminald o Arduino é necessario declarar 
essa função, que inicia e configura a velocidade dos dados em bits por segundo. É
declarada no void setup()*/Serial.begin(9600);

Serial.print(data);/* Imprime os dados na porta serial. após ela ser inicializada. Pode 
ser usada no void loop() Serial.println pula uma linha*/ serial.println("Hello world");
```

### Funções úteis:

```cpp
map(value, fromBottom, fromTop, toBottom, toTop);/*Mapeia do sinal analogico para o sinal
PWM, ou os valores PWM ou analógicos para angulos ou intensidades de um componente
especifico*/ sensor = map(value, 0, 1023, 0, 255);
```

# Considerações finais:

Essa pagina de iniciação em Arduino ainda esta em construção, contamos com seu feedback e opinião para melhoria continua de nosso conteúdo. Posteriormente mais informações podem ser publicadas nessas pagina

# Repositórios da Forge:

Repositórios do GitHub da equipe de robótica **Roboforge** com alguns exemplos de aplicações

- https://github.com/roboforgeufu/torc-2023/blob/main/src/main.cpp

# Referências:

- [**Repositório de aulas IF Expert 2023**](https://drive.google.com/drive/folders/1DA-rg8uTd3A8HfhmdwexOE5E_X44IXML?usp=drive_link)
- https://docs.arduino.cc/language-reference/