import socket

def get_ip_by_hostname(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror as e:
        print(f"Error resolving hostname: {e}")
        return None

hostname = "www.example.com"
ip_address = get_ip_by_hostname(hostname)

if ip_address:
    print(f"The IP address for {hostname} is: {ip_address}")
    import socket

def get_ip_by_hostname(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror as e:
        print(f"Error resolving hostname: {e}")
        return None

# Example usage
hostname = "www.example.com"
ip_address = get_ip_by_hostname(hostname)

if ip_address:
    print(f"The IP address for {hostname} is: {ip_address}")