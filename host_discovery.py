import ipaddress
import subprocess
import platform
import socket

def get_local_ip_and_subnet():
    """Obtém o endereço IP local e a máscara de sub-rede."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Conecta a um IP externo para obter o IP local
        local_ip = s.getsockname()[0]
        s.close()

        # Tenta obter a máscara de sub-rede (pode variar entre OS)
        # Uma abordagem mais robusta seria usar 'ip -o -f inet addr show' no Linux
        # ou 'ipconfig' no Windows e parsear a saída.
        # Por simplicidade, vamos assumir uma máscara /24 para o IP local por enquanto.
        # Isso precisaria ser melhorado para redes mais complexas.
        network = ipaddress.ip_network(f'{local_ip}/24', strict=False)
        return str(local_ip), str(network.network_address), str(network.netmask)
    except Exception as e:
        print(f"Erro ao obter IP local e sub-rede: {e}")
        return None, None, None

def discover_hosts_ping(network_address, netmask):
    """Descobre hosts ativos na rede usando ping."""
    active_hosts = []
    try:
        network = ipaddress.ip_network(f'{network_address}/{netmask}', strict=False)
        print(f"Varrendo a rede: {network}")

        for host in network.hosts():
            host_str = str(host)
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, '1', '-W', '1', host_str] # -W 1 para timeout de 1 segundo
            
            try:
                output = subprocess.run(command, capture_output=True, text=True, timeout=2)
                if "ttl=" in output.stdout.lower() or "tempo de vida" in output.stdout.lower():
                    print(f"Host ativo encontrado: {host_str}")
                    active_hosts.append(host_str)
            except subprocess.TimeoutExpired:
                # print(f"Ping para {host_str} expirou.")
                pass
            except Exception as e:
                print(f"Erro ao pingar {host_str}: {e}")

    except Exception as e:
        print(f"Erro na descoberta de hosts: {e}")
    return active_hosts

if __name__ == "__main__":
    local_ip, network_address, netmask = get_local_ip_and_subnet()
    if local_ip and network_address and netmask:
        print(f"IP Local: {local_ip}")
        print(f"Endereço de Rede: {network_address}")
        print(f"Máscara de Sub-rede: {netmask}")
        
        print("Iniciando descoberta de hosts...")
        active_hosts = discover_hosts_ping(network_address, netmask)
        print("\n--- Hosts Ativos Encontrados ---")
        if active_hosts:
            for host in active_hosts:
                print(host)
        else:
            print("Nenhum host ativo encontrado (além do próprio dispositivo).")
    else:
        print("Não foi possível determinar as informações da rede local.")

