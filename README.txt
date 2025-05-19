Controle de Pátio - Mottu

Este projeto faz parte da disciplina Disruptive Architectures: IoT, IoB & Generative IA, com o objetivo de desenvolver um sistema de controle de pátio utilizando ESP32, sensores IoT, visão computacional simulada e comunicação via MQTT com um painel de monitoramento no Node-RED.


Estrutura do Repositório:

esp32:
main.ino Código do ESP32 para leitura de sensores e envio via MQTT

images:
circuito_montado.png - Imagem do circuito montado

node-red:
fluxo-node-red.json - Fluxo exportado da interface Node-RED

python:
mqtt_client.py - Cliente Python para leitura de mensagens MQTT (monitoramento/testes)
detect_motos.py - Script de visão computacional simulada

README - Este arquivo


Tecnologias Utilizadas:

- ESP32** com IDE Arduino
- Sensor Ultrassônico HC-SR04
- Sensor de temperatura e umidade DHT22
- LED de sinalização
- Python (para simulação de visão computacional e cliente MQTT)
- Node-RED (para painel de monitoramento e controle)
- MQTT (broker público: broker.hivemq.com)**


Objetivo do Projeto:

Criar um sistema funcional de controle de entrada e saída de motocicletas do pátio da empresa Mottu. O sistema é composto por:

- Detecção de motos via sensor ultrassônico (HC-SR04)
- Sinalização com LED quando uma moto entra ou sai
- Envio de dados para o Node-RED via MQTT
- Simulação de detecção de motos com visão computacional em Python
- Monitoramento via painel Node-RED


Instruções de Uso:

1. Circuito com ESP32

- Monte o circuito conforme a imagem "images/circuito_montado.png"
- Carregue o código "main.ino" na ESP32 via Arduino IDE
- Certifique-se de que os sensores estão ligados corretamente:
  - HC-SR04: VCC, GND, TRIG, ECHO
  - DHT22: VCC, GND, DATA
  - LED com resistor em GPIO de saída

2. Execução do Node-RED

- Acesse [http://localhost:1880](http://localhost:1880)
- Importe o fluxo contido em `node-red/fluxo-node-red.json`
- Configure o nó MQTT com o broker `broker.hivemq.com` e porta `1883`
- Visualize os dados em tempo real do ESP32

3. Execução do Python (opcional)

- Acesse a pasta "python"
- Instale dependências (se necessário):
  pip install paho-mqtt opencv-python

- Execute o script de simulação de visão computacional:
  python detect_motos.py

- Execute o cliente MQTT (para testes):
  python mqtt_client.py


Resultados Parciais:

- Comunicação funcional entre ESP32 e Node-RED via MQTT

- Leitura de sensores (distância e temperatura/umidade)

- Acionamento de LED com base em eventos (moto detectada)

- Simulação da detecção de motos com Python

- Interface no Node-RED com exibição em tempo real


Link para o Repositório:
https://github.com/Guusthy/controle-patio-mottu

Equipe:

Gustavo Roberto do Nascimento - 558033
Cauan Matos Moura - 558821
Thiago Renatino - 556934


