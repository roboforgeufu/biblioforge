# ROS - Robot Operating System

![alt text](image.png)

É um _conjunto de bibliotecas de software_ feitas para a construção de aplicações robóticas. Desde drivers até algoritmos no estado da arte, com ferramentas de desenvolvimento poderosas, o ROS tem "tudo que você precisa para seu próximo projeto de robótica", e é completamente _open source_.

O ROS é um conjunto de ferramentas muito robusto, amplamente utilizado em _projetos de pesquisa e desenvolvimento_, tanto _acadêmicos_ quanto da _indústria_, nas áreas de robótica e automação.

Define, para o desenvolvimento de robôs avançados:

- Componentes
- Interfaces
- Ferramentas

Desenvolvedores podem, de forma facilitada e modular, integrar motores, sensores e controladores.

Feito na intenção de funcionar bem com qualquer tipo de dispositivo de hardware que tenha alguma interface de software.

> Além disso tudo, o ROS traz ferramentas de visualização, teleoperação, e funciona muito bem com [Simuladores](/Simuladores/README.md)

Também existe uma variação, [microROS](https://micro.ros.org), feita para rodar nativamente em sistemas embarcados rodando em sistemas operacionais em tempo real (`real-time`).

> :ferris_wheel: A ideia é que o ROS ajude desenvolvedores a focarem nos seus problemas específicos, e passarem menos tempo "reinventando a roda".

# Instalar ROS

É recomendável instalar ROS num sistema operacional que seja altamente compatível com ele, como é uma estrutura de software que trabalha de forma muito próxima com o sistema operacional e as bibliotecas do sistema.

Em geral, os sistemas operacionais recomendados para instalação do ROS são Ubuntu e Windows. Cada versão do ROS vai ter uma compatibilidade maior com uma versão específica do sistema operacional. Por exemplo, _ROS 2 Humble Hawksbill_ funciona melhor no _Ubuntu 22.04 Jammy Jellyfish_, e _Windows 10_. Se você tentar instalar em outros sistemas operacionais, pode ser que você encontre dificuldades e problemas, e a documentação do ROS não recomenda essa alternativa para usuários novos.

# Sobre versões

**Resposta curta**: escolha a versão LTS (_long term support_) atual, instale na versão LTS correspondente do Ubuntu e seja feliz! Grandes chances de não ter problemas por conta da escolha de versão.

**Resposta longa**:

É legal sempre dar uma pesquisada sobre como está o suporte das bibliotecas mais famosas / mais utilizadas às novas versões do ROS antes de escolher a mais recente pra trabalhar.

Como é um sistema de software open source, nem tudo vai estar tão robusto / amadurecido nas versões mais recentes o tempo todo. Usar versões mais antigas que tenham mais recursos online (wikis mais completas, tutoriais, canais com dúvidas e erros resolvidos) pode ser uma boa ideia, dependendo do que você quer.

Como dito acima, muitas vezes isso vai significar baixar a versão LTS do ROS, ainda que tenham versões mais recentes já disponíveis (geralmente _short-term releases_, por exemplo).

> Leia mais sobre isso [aqui](https://docs.ros.org/en/jazzy/Releases.html).

# Conceitos principais

> Leia mais sobre os conceitos principais do ROS [aqui](https://docs.ros.org/en/jazzy/Concepts/Basic.html).

- Nós (_nodes_) e o _ROS Graph_
- Interfaces
- Tópicos e mensagens
- Services
- Actions
- Logs e bag files

# Comunidade

Uma parte importante do ROS é a sua [comunidade](https://www.ros.org/blog/community)! Desde fóruns e grupos online até conferências ao redor do mundo, várias pessoas contribuem com o ecossistema ao redor dessa ferramenta open source.

![ROSCon 2025](image-1.png)

> Poster da [ROSCon](https://roscon.ros.org) 2025, uma das maiores conferências de robótica do mundo, organizada pela comunidade do ROS.

# Tutoriais

Alguns dos tutoriais que podem ser bons pra começar no ROS.

- https://docs.ros.org/en/jazzy/Tutorials.html

# Referências

- https://www.ros.org
- https://micro.ros.org
- https://www.ros.org/blog/community
- https://roscon.ros.org
- https://docs.ros.org/en/jazzy/Installation.html
- https://wiki.ros.org
