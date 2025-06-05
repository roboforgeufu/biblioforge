## Polimorfismo

O polimorfismo permite que objetos de diferentes classes usem o mesmo método, mas com comportamentos diferentes. Isso oferece flexibilidade no código, pois podemos tratar objetos de tipos diferentes de forma uniforme.

Na prática, o polimorfismo ocorre principalmente por meio da **sobrescrição de métodos** (method overriding), quando uma subclasse redefine um método da superclasse, criando um comportamento específico.

Também existe a **sobrecarga de métodos** (method overloading), que ocorre quando há métodos com o mesmo nome, mas com parâmetros diferentes. O overloading é comum em linguagens como C++, mas não é suportado diretamente em Python. Enquanto o overriding está ligado ao polimorfismo de tempo de execução, o overloading é um polimorfismo de tempo de compilação.

- Em **Python**, o polimorfismo acontece de forma dinâmica. Se diferentes classes tiverem métodos com o mesmo nome, o Python executa o método correspondente ao objeto no momento da execução.

- Em **C++**, é necessário usar a palavra-chave virtual  na superclasse para permitir que o método seja sobrescrito nas subclasses. Assim, mesmo que o objeto seja tratado como uma referência ou ponteiro da superclasse, ele executará o método da subclasse corretamente.

---

### Python:

```python
class Robo:
    def falar(self):
        print("Eu sou um robô genérico.")

class RoboSumo(Robo):
    def falar(self):
        print("Eu sou um robô de sumô.")

class RoboSeguidor(Robo):
    def falar(self):
        print("Eu sou um robô seguidor de linha.")

def apresentar_robo(robo):
    robo.falar()

robo1 = RoboSumo()
robo2 = RoboSeguidor()

apresentar_robo(robo1)  # A saída será: "Eu sou um robô de sumô."
apresentar_robo(robo2)  # A saída será: "Eu sou um robô seguidor de linha."
```

---

### C++:

```cpp
class Robo {
    public:
        virtual void falar() {
            Serial.println("Eu sou um robo generico.");
        }
};

class RoboSumo : public Robo {
    public:
        void falar() override {
            Serial.println("Eu sou um robo de sumo.");
        }
};

class RoboSeguidor : public Robo {
    public:
        void falar() override {
            Serial.println("Eu sou um robo seguidor de linha.");
        }
};

RoboSumo robo1;
RoboSeguidor robo2;

void setup() {
    Serial.begin(9600);
    robo1.falar();  // A saída será: "Eu sou um robo de sumo."
    robo2.falar();  // A saída será: "Eu sou um robo seguidor de linha."
}

void loop() {
  
}
```

## Referências

- https://adrianosantostreina.com.br/blog/poo-3o-pilar-polimorfismo/ 
- https://www-geeksforgeeks-org.translate.goog/polymorphism-in-python/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc
- https://www-geeksforgeeks-org.translate.goog/cpp-polymorphism/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc 

 
