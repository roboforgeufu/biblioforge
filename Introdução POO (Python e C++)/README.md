# Programação Orientada a Objetos para Robótica - Introdução Python e C++

A programação orientada a objetos (POO) é um paradigma de programação que organiza o código em torno de objetos que possuem características (atributos) e comportamentos (métodos).

Nesse tutorial vamos estar explorando os conceitos básicos da POO tanto para o Python quanto para o C++ (voltado para microcontroladores), no contexto da robótica. Para isso, vamos primeiro definir uma classe `Robo` com os atributos pertinentes à um robô genérico.

# Classes:

Uma classe é um tipo de dados definido pelo usuário que podemos usar em nosso programa. Classes atuam como um gabarito para a definição de objetos. Através da definição de uma classe, descreve-se que propriedades -- ou **atributos** -- o objeto terá.

### Python:

```python
class Robo:  #identificador da classe
    velocidade = 100  #atributos
```

### C++:

```cpp
class Robo  //identificador da classe
{
    public:  //especificador de acesso
        int velocidade = 100;  //atributos
};
```

# Objetos:

Após a definição da classe, podemos criar objetos a partir desta. Na programação orientada a objetos, uma classe define um conjunto de atributos e métodos que caracterizam um tipo particular de objeto. Quando um objeto é criado a partir dessa classe, ele herda a estrutura e o comportamento especificados na classe, mas possui seus próprios valores únicos para os atributos.

### Python:

```python
class Robo:  #identificador da classe
    velocidade = 100  #atributos

roboSumo = Robo()  #criacao do objeto roboSumo
print(roboSumo.velocidade)  #print do atributo velocidade do objeto criado
```

### C++ (Arduino UNO*):

```cpp
class Robo  //identificador da classe
{
    public:  //especificador de acesso
        int velocidade = 100;  //atributos
};

Robo roboSeguidor;  //criacao do objeto roboSeguidor

void setup() 
{
    Serial.begin(9600);  //*iniciando o monitor serial a 9600 baudrate (UNO)
    Serial.print(roboSeguidor.velocidade);  //print do atributo velocidade do objeto criado
}

void loop()
{

}
```

# Construtores:

Um construtor é um método especial definido dentro de uma classe que é automaticamente invocado quando um novo objeto dessa classe é criado. O principal objetivo do construtor é inicializar o novo objeto, geralmente configurando os valores iniciais de seus atributos ou executando qualquer outra configuração necessária. Construtores podem aceitar parâmetros, permitindo que os atributos do objeto sejam definidos no momento da criação. Eles asseguram que o objeto comece em um estado válido e pronto para uso. No caso do Python, o construtor é definido com a sintaxe `def __init__(self, atributo1, atributo2):` enquanto no C++, chamamos o mesmo nome dado para a classe, seguido de parênteses com os atributos e seus tipos especificados.

### Python:

```python
class Robo:  #identificador da classe
    def __init__(self, velocidade, diametro_roda, distancia_rodas): #chamada do construtor
        self.velocidade = velocidade        #alteração dos atributos no momento
        self.diametro_roda = diametro_roda  #da criacao do objeto
        self.distancia_rodas = distancia_rodas
        self.comprimento_roda = diametro_roda * 3.1415
    
roboSumo = Robo(100, 5, 15)  #criacao do objeto roboSumo com atributos personalizados
print(roboSumo.comprimento_roda)  #print do atributo comprimento_roda do objeto criado
```

### C++:

```cpp
class Robo  //identificador da classe
{
    public:  //especificador de acesso
        int velocidade;  //atributos
        float diametro_roda;
        float distancia_rodas;
        float comprimento_roda;
        Robo(int velocidade, float diametro_roda, float distancia_rodas) //chamada do construtor
        {  
            velocidade = velocidade;        //alteração dos atributos no momento
            diametro_roda = diametro_roda;  //da criacao do objeto
            distancia_rodas = distancia_rodas;
            comprimento_roda = diametro_roda * 3.1415;
        }
};

Robo roboSeguidor(100, 5, 15);  //criacao do objeto roboSeguidor
                                //com atributos personalizados
void setup() 
{
    Serial.begin(9600);  //*iniciando o monitor serial a 9600 baudrate (UNO)
    Serial.print(roboSeguidor.comprimento_roda);  //print do atributo comprimento_roda
}                                                 //do objeto criado

void loop() 
{

}
```

# Métodos:

Um método é uma função definida dentro de uma classe que descreve um comportamento que os objetos daquela classe podem executar. Métodos podem operar sobre os dados armazenados nos atributos do objeto (instância da classe) e podem realizar ações como modificar esses dados, realizar cálculos ou interagir com outros objetos. Estes podem ser chamados em objetos individuais, permitindo que cada objeto possa realizar ações conforme sua própria configuração e estado.

### Python:

```python
class Robo:  #identificador da classe
    def __init__(self, velocidade, diametro_roda, distancia_rodas): #chamada do construtor
        self.velocidade = velocidade        #alteração dos atributos no momento
        self.diametro_roda = diametro_roda  #da criacao do objeto
        self.distancia_rodas = distancia_rodas
        self.comprimento_roda = diametro_roda * 3.1415
    
    def hello_world(self):  #metodo da classe
        print("Oi, eu sou um robo!")  #comandos do metodo
    
roboSumo = Robo(100, 5, 15)  #criacao do objeto roboSumo com atributos personalizados
print(roboSumo.comprimento_roda)  #print do atributo comprimento_roda do objeto criado

while True:  #loop principal
    roboSumo.hello_world()  #chamada do metodo hello_world() do objeto criado
```

### C++:

```cpp
class Robo  //identificador da classe
{
    public:  //especificador de acesso
        int velocidade;  //atributos
        float diametro_roda;
        float distancia_rodas;
        float comprimento_roda;
        Robo(int velocidade, float diametro_roda, float distancia_rodas)  //chamada do construtor
        {
            velocidade = velocidade;        //alteração dos atributos no momento
            diametro_roda = diametro_roda;  //da criacao do objeto
            distancia_rodas = distancia_rodas;
            comprimento_roda = diametro_roda * 3.1415;
        }
		
        void hello_world()  //metodo da classe
        {
            Serial.println("Oi, eu sou um robo!");  //comandos do metodo
        }		
};

Robo roboSeguidor(100, 5, 15);  //criacao do objeto roboSeguidor
                                //com atributos personalizados
void setup() 
{
    Serial.begin(9600);  //*iniciando o monitor serial a 9600 baudrate (UNO)
    Serial.print(roboSeguidor.comprimento_roda);  //print do atributo comprimento_roda
}                                                 //do objeto criado

void loop()  //loop principal
{
    roboSeguidor.hello_world();  //chamada do metodo hello_world() do objeto criado
}
```

# Repositórios da Forge:

Repositórios do GitHub da equipe de robótica **Roboforge** com alguns exemplos de aplicações da programação orientada a objetos para a robótica:

- https://github.com/roboforgeufu/larc-sek-2023/blob/main/src/robot.py
- https://github.com/roboforgeufu/torc-2023/blob/main/src/main.cpp

# Referências:

- https://www.w3schools.com/python/python_classes.asp
- https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes
- https://www.w3schools.com/cpp/cpp_oop.asp
- https://docs.arduino.cc/language-reference/
