import argparse
import sys
from host_discovery import get_local_ip_and_subnet, discover_hosts_ping
from port_scanner import scan_ports_on_host
from service_identifier import identify_service
from utils import is_valid_ip

def main():
    parser = argparse.ArgumentParser(description="Um scanner de rede simples em Python.")
    parser.add_argument("-d", "--discover", action="store_true", help="Descobrir hosts ativos na rede local.")
    parser.add_argument("-s", "--scan", metavar="HOST", help="Escanear portas em um host específico (ex: 192.168.1.1).")
    parser.add_argument("-p", "--ports", metavar="RANGE", default="1-1024", help="Intervalo de portas para escanear (ex: 1-1024). Padrão: 1-1024.")
    parser.add_argument("-t", "--timeout", type=int, default=1, help="Timeout para conexão de porta em segundos. Padrão: 1.")

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
        sys.exit(1)

    if args.discover:
        print("\n--- Descoberta de Hosts ---")
        local_ip, network_address, netmask = get_local_ip_and_subnet()
        if local_ip and network_address and netmask:
            print(f"IP Local: {local_ip}")
            print(f"Endereço de Rede: {network_address}")
            print(f"Máscara de Sub-rede: {netmask}")
            active_hosts = discover_hosts_ping(network_address, netmask)
            print("\n--- Hosts Ativos Encontrados ---")
            if active_hosts:
                for host in active_hosts:
                    print(host)
            else:
                print("Nenhum host ativo encontrado (além do próprio dispositivo).")
        else:
            print("Não foi possível determinar as informações da rede local para descoberta de hosts.")

    if args.scan:
        target_host = args.scan
        if not is_valid_ip(target_host):
            print(f"Erro: '{target_host}' não é um endereço IP válido.")
            sys.exit(1)

        try:
            start_port, end_port = map(int, args.ports.split('-'))
            if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535 and start_port <= end_port):
                raise ValueError
        except ValueError:
            print(f"Erro: Intervalo de portas inválido. Use o formato START-END (ex: 1-1024).")
            sys.exit(1)

        print(f"\n--- Varredura de Portas em {target_host} ---")
        open_ports = scan_ports_on_host(target_host, start_port, end_port, args.timeout)

        print("\n--- Relatório de Portas Abertas ---")
        if open_ports:
            for port in open_ports:
                service_info = identify_service(target_host, port, args.timeout)
                print(f"Porta {port} aberta - Serviço: {service_info}")
        else:
            print(f"Nenhuma porta aberta encontrada em {target_host} no intervalo {args.ports}.")

if __name__ == "__main__":
    main()

