import socket

def scan_port(host, port, timeout=1):
    """Tenta conectar a uma porta específica em um host."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            if result == 0:
                return True  # Porta aberta
            else:
                return False # Porta fechada ou filtrada
    except socket.gaierror:
        print(f"Host {host} não encontrado.")
        return None
    except socket.error as e:
        # print(f"Erro de conexão com {host}:{port} - {e}")
        return None

def scan_ports_on_host(host, start_port, end_port, timeout=1):
    """Varre um intervalo de portas em um host específico."""
    print(f"Varrendo portas de {start_port} a {end_port} em {host}...")
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(host, port, timeout):
            print(f"Porta {port} aberta em {host}")
            open_ports.append(port)
    return open_ports

if __name__ == "__main__":
    target_host = "127.0.0.1"  # Exemplo: localhost
    # target_host = "169.254.0.22" # Exemplo: um host descoberto anteriormente
    start_port = 1
    end_port = 1024

    print(f"Iniciando varredura de portas em {target_host}...")
    open_ports = scan_ports_on_host(target_host, start_port, end_port)

    print("\n--- Portas Abertas Encontradas ---")
    if open_ports:
        for port in open_ports:
            print(f"Porta {port} está aberta")
    else:
        print("Nenhuma porta aberta encontrada no intervalo especificado.")

