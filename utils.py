import ipaddress

def is_valid_ip(ip_address):
    """Verifica se a string fornecida é um endereço IP válido."""
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False

