# Let's create two sample text files: "ip_addresses.txt" and "routing_table.txt"
# For demonstration purposes, these files will contain simple, simulated content.

# Content for "ip_addresses.txt"
ip_addresses_content = """192.168.1.1
172.16.0.1
10.0.0.1
192.168.1.2
172.16.0.1  # Duplicate
10.0.0.2
192.168.1.3"""

# Content for "routing_table.txt"
routing_table_content = """Destination        Gateway            Flags   Refs      Use   Netif
default            192.168.1.1        UGSc       45        0     en0
10.0.0.0/24        link#2             UCSc        2        0     en1
172.16.0.0/16      172.16.0.1         UGSc        0        0     en2
192.168.1.0/24     link#6             UCSc       10        0     en0"""

# Create and write to "ip_addresses.txt"
with open("ip_addresses.txt", "w") as file:
    file.write(ip_addresses_content)

# Create and write to "routing_table.txt"
with open("routing_table.txt", "w") as file:
    file.write(routing_table_content)
