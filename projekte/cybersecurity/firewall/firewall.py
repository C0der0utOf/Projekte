import random

def generate_random_ip():
    # Generates a random IP in the 192.168.1.0/24 subnet
    return f"192.168.1.{random.randint(0, 20)}"

def check_firewall_rules(ip, rules):
    # Checks if the IP is in the firewall rules
    for blocked_ip, action in rules.items():
        if ip == blocked_ip:
            return action
    return "allow"

def main():
    # Define firewall rules: block specific IPs
    firewall_rules = {
        "192.168.1.5": "block",
        "192.168.1.10": "block",
        "192.168.1.15": "block",
        "192.168.1.18": "block",
        "192.168.1.19": "block",
        "192.168.1.20": "block"
    }

    # Simulate 12 packets
    for _ in range(12):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        unique_id = random.randint(0, 99999)
        print(f"Packet from {ip_address}: {action.upper()} (ID: {unique_id})")

if __name__ == "__main__":
    main()
