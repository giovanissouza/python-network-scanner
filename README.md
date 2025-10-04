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

