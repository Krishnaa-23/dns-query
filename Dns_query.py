import socket

domain = "www.kame.net"

try:
    # IPv4
    ipv4 = socket.getaddrinfo(domain, None, socket.AF_INET)
    ipv4_addresses = [result[4][0] for result in ipv4]
    print("IPv4 addresses:", list(set(ipv4_addresses)))

    # IPv6
    ipv6 = socket.getaddrinfo(domain, None, socket.AF_INET6)
    ipv6_addresses = [result[4][0] for result in ipv6]
    print("IPv6 addresses:", list(set(ipv6_addresses)))

except socket.gaierror as e:
    print(f"Error resolving {domain}: {e}")
