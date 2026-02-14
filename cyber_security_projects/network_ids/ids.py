from scapy.all import sniff
from collections import defaultdict
from datetime import datetime

ip_count = defaultdict(int)

LOG_FILE = "ids_log.txt"

def detect(packet):
    if packet.haslayer("IP"):
        src = packet["IP"].src
        ip_count[src] += 1
        
        if ip_count[src] > 20:
            alert = f"[ALERT] {datetime.now()} Possible port scan from {src}"
            print(alert)

            with open(LOG_FILE, "a") as f:
                f.write(alert + "\n")

print("Monitoring network traffic...")
sniff(prn=detect)
