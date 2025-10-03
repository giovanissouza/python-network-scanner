import socket

def identify_service(host, port, timeout=1):
    """Tenta identificar o serviço em uma porta aberta através de banner grabbing."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((host, port))
            # Tenta receber dados do serviço
            banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
            if banner:
                return banner
            else:
                return "Nenhum banner recebido"
    except socket.timeout:
        return "Timeout ao tentar obter banner"
    except ConnectionRefusedError:
        return "Conexão recusada (porta pode ter fechado ou serviço não respondeu)"
    except Exception as e:
        return f"Erro ao identificar serviço: {e}"

if __name__ == "__main__":
    # Exemplo de uso
    target_host = "127.0.0.1"
    target_port = 22 # Porta SSH, geralmente tem um banner

    print(f"Tentando identificar serviço em {target_host}:{target_port}...")
    service_info = identify_service(target_host, target_port)
    print(f"Serviço em {target_host}:{target_port}: {service_info}")

    target_port_http = 80 # Porta HTTP, se houver um servidor web
    print(f"Tentando identificar serviço em {target_host}:{target_port_http}...")
    service_info_http = identify_service(target_host, target_port_http)
    print(f"Serviço em {target_host}:{target_port_http}: {service_info_http}")

