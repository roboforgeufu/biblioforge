# 🔧 Motor EV3 – LEGO Mindstorms

> Documentação técnica do motor EV3 utilizado em projetos de robótica educacional e competições como a OBR.

---

## 📌 Sobre o projeto

Este repositório contém informações técnicas e práticas sobre o motor EV3, componente amplamente utilizado em kits LEGO Mindstorms. O objetivo é fornecer uma visão geral de suas características, funcionamento e aplicações em projetos de robótica.

---

## ⚙️ Especificações técnicas

| Característica        | Detalhes                        |
|-----------------------|---------------------------------|
| Tipo                  | Motor DC com encoder            |
| Tensão nominal        | 9V                              |
| Torque máximo (Large) | ~40 mNm                         |
| RPM (Large)           | ~160                            |
| Interface de conexão  | Conector padrão LEGO EV3        |
| Sensoriamento         | Encoder rotativo embutido       |

*Fonte: [Datasheet oficial da LEGO](https://le-www-live-s.legocdn.com/sc/media/images/resource-site/files/ev3_chromebook_userguide_us_motors-f19da6c7dld9blafld6b8c9e8359fllc.pdf)*

---

## 🚀 Aplicações

- Robôs móveis com controle de locomoção precisa
- Braços robóticos e mecanismos de levantamento
- Acionamento de engrenagens e catapultas em desafios da OBR
- Projetos educacionais com feedback de posição via encoder

---

## 🧠 Funcionamento

O motor EV3 é controlado pelo brick LEGO EV3, que se comunica com o motor utilizando dois fios principais para energia e dois para leitura do encoder. O controle de velocidade é realizado via PWM, e o encoder envia sinais para o brick medir deslocamento e direção.

> Embora o motor EV3 seja normalmente usado com o brick da LEGO, também pode ser controlado por microcontroladores como Arduino utilizando uma ponte H. Isso é útil quando se deseja integrar o motor a sistemas fora do ecossistema LEGO.

---

## 📚 Referências

- [Datasheet oficial da LEGO](https://le-www-live-s.legocdn.com/sc/media/images/resource-site/files/ev3_chromebook_userguide_us_motors-f19da6c7dld9blafld6b8c9e8359fllc.pdf)
- Experimentos realizados com kits LEGO Mindstorms EV3 durante treinamentos da Roboforge
- Documentação de apoio da OBR e da LEGO Education

---

📚 Por [Maria Clara] 
