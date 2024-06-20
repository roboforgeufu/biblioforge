## Para saber mais sobre o sensor LDR:

- LDR é um componente eletrônico passivo¹, possui apenas dois terminais e não tem polaridade definida;
- Ele funciona como um resistor que varia sua resistência de acordo com a intensidade de luz que incide nele;
- Dentro dele tem um semicondutor de alta resistência;
- O LDR também pode aprensentar uns atrasos para variar sua resistência.

Link para entender melhor como funciona o sensor: https://www.youtube.com/watch?v=XW2ZBwCD9dI&t=6s&ab_channel=MundodaEl%C3%A9trica

Link para acessar o datasheet: https://www.makerhero.com/img/files/download/GL5528-Datasheet.pdf

<div style="text-align: center;">
    <img src="/home/me15degrees/Documents/Roboforge/roboforge/estudos/assets/graphic_ldr.png" alt="Descrição da imagem">
</div>

> Lógica de funcionamento: quanto maior a luminosidade, menor a resistência. Contudo vale lembrar que não são linearmente proporcionais.

¹ Componente passivo: não possuem "jeito correto" de ligar os terminais, pois são bidirecionais. Não tem risco de queimar, como seria em um capacitor.

## Código

Utiliza Programação Orientada à Objetos para criar uma classe para o sensor LDR.

O sensor GL5528 retorna para o microcontrolador uma variação de tensão que é convertida em um valor digital pelo ADC do microcontrolador. 
Esse valor digital é então usado para determinar a intensidade da luz incidente sobre o sensor.

A resolução (r) do ADC interefere, pois os valores podem assumir 2^r distintos.

Considerar a tensão de referência como 5v.