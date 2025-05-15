import socket

def scan_ports(target, port_range):
    open_ports = []
    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Set a timeout for the connection attempt
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    target = "127.0.0.1"  # Replace with the IP address you want to scan
    ports = range(1, 1025)  # Scan ports 1 through 1024
    found_ports = scan_ports(target, ports)
    print(f"Open ports on {target}: {found_ports}")
