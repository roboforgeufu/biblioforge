# Herança

Herança permite a reutilização do código para classes com comportamentos semelhantes, essas semelhanças podem ser armazenadas em uma classe mãe que é base para as outras classes. Classes mãe podem ter construtores e métodos que serão herdados pelas classes filhas. As classes filhas herdam tudo da classe mãe e podem ter seus próprios métodos e construtores.

---

**Python:**

```python
class Robo: #classe mãe (base)
    def __init__(self, nome): #construtor
        self.nome = nome

    def apresentar(self): #método comum
        print("Oi, eu sou o robo", self.nome)

class RoboLinha(Robo): #classe filha (herda de Robo)
    def seguir_linha(self):  #novo método da filha
        print("Estou seguindo a linha!")

meu_robo = RoboLinha("Seguidor") #criação do robo com herança
meu_robo.apresentar() #método da classe mãe
meu_robo.seguir_linha() #método da classe filha
```
---

**C++:**

```cpp
#include <iostream>
using namespace std;

//classe mãe (base)
class Robo{
    public:
        string nome;

        Robo(string nome){ //construtor
            this->nome = nome;
        }

        void apresentar(){ //método da classe mãe
            cout << "Oi, eu sou o robo " << nome << endl;
        }
};

//classe filha (herda de Robo)
class Seguidor_Linha : public Robo{
    public:
        Seguidor_Linha(string nome) : Robo(nome) {} //construtor da classe filha

        void seguir_linha(){ //método da classe filha
            cout << "Estou seguindo a linha!" << endl;
        }
};

int main(){
    Seguidor_Linha meuRobo("Seguidor"); //criação do robo com herança
    meuRobo.apresentar(); //método da classe mãe
    meuRobo.seguir_linha(); //método da classe filha
    return 0;
}
```



