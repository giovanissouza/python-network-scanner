# Scanner de Rede em Python

## Objetivo

Desenvolver um scanner de rede robusto e modular em Python, capaz de:

1.  **Descobrir hosts ativos** na rede local.
2.  **Realizar varredura de portas** em hosts específicos para identificar serviços em execução.
3.  **Identificar serviços** básicos em portas abertas.

## Funcionalidades Principais

-   **Descoberta de Hosts (Host Discovery):** Utilizar técnicas como ARP Ping ou ICMP Echo Request para identificar dispositivos ativos na rede.
-   **Varredura de Portas (Port Scanning):** Implementar diferentes tipos de varredura (e.g., TCP SYN, TCP Connect) para determinar o estado das portas (aberta, fechada, filtrada).
-   **Identificação de Serviços (Service Identification):** Tentar banner grabbing ou outras técnicas para inferir o tipo de serviço rodando em uma porta aberta.
-   **Interface de Usuário:** Uma interface de linha de comando (CLI) simples para interação.
-   **Geração de Relatórios:** Apresentar os resultados de forma clara e organizada.

## Tecnologias

-   **Linguagem:** Python 3.x
-   **Bibliotecas:**
    -   `socket`: Para operações de rede de baixo nível (TCP/UDP).
    -   `scapy` (opcional, para funcionalidades mais avançadas como ARP/ICMP a nível de pacote).
    -   `ipaddress`: Para manipulação de endereços IP e redes.
    -   `argparse`: Para parsing de argumentos de linha de comando.

## Estrutura do Projeto

network_scanner/
├── main.py             # Ponto de entrada principal do scanner
├── host_discovery.py   # Módulo para descoberta de hosts
├── port_scanner.py     # Módulo para varredura de portas
├── service_identifier.py # Módulo para identificação de serviços
├── utils.py            # Funções utilitárias (e.g., validação de IP)
└── README.md           # Documentação do projeto

## Como Usar

1.  **Salve os arquivos:** Baixe todos os arquivos (`README.md`, `main.py`, `host_discovery.py`, `port_scanner.py`, `service_identifier.py`, `utils.py`) em uma mesma pasta.
2.  **Instale as dependências:** Certifique-se de ter o Python 3.x instalado. Não há dependências externas além das bibliotecas padrão do Python e do comando `ping` (que pode precisar ser instalado no seu sistema operacional).
3.  **Execute o scanner:** Abra um terminal na pasta onde você salvou os arquivos e use os seguintes comandos:

    *   **Para descobrir hosts na rede local:**
        ```bash
        python main.py --discover
        ```

    *   **Para escanear portas em um host específico (ex: 192.168.1.1) no intervalo padrão (1-1024):**
        ```bash
        python main.py --scan 192.168.1.1
        ```

    *   **Para escanear portas em um host específico com um intervalo de portas personalizado (ex: 80-443):**
        ```bash
        python main.py --scan 192.168.1.1 --ports 80-443
        ```

    *   **Para ajustar o timeout da conexão (em segundos):**
        ```bash
        python main.py --scan 192.168.1.1 --timeout 2
        ```
