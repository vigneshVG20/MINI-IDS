from scapy.all import *


def packet_show(packet):
    suspicious_ports = [80, 443]

    if packet.haslayer(IP):

        protocol = packet[IP].proto

        if protocol == 6:
            protocol_name = f"Tcp "

        elif protocol == 17:
            protocol_name=f"UDP "
        elif protocol == 1:
            protocol_name = f"ICMP "
        elif protocol == 2:
            protocol_name = f"IGMP"
        
        else:
            protocol_name = f"UNKNOWN protocol{protocol}"
        log_data=""
        log_data+= f"Source IP: {packet[IP].src}\n"
        log_data+= f"Destination IP: {packet[IP].dst}\n"
        log_data+= f"Protocol: {protocol_name}\n"
        log_data+= "----------------------------\n"
        if packet.haslayer(TCP):
            log_data += f"Source Port:{packet[TCP].sport}\n"
            log_data += f"Destination port:{packet[TCP].dport}\n"
            if packet[TCP].dport in suspicious_ports :
                log_data += "[ALERT] Suspicious Port Detected\n"
                print(f"[ALERT] Suspicious Port Detected\n Source IP: {packet[IP].src}\n Destination IP: {packet[IP].dst}\nProtocol: {protocol_name}\n")
                if packet[TCP].dport == 80:
                    log_data += "[Alert] http Traffic detected\n"
                    print("[Alert] http Traffic detected\n")
                elif packet[TCP].dport == 443:
                    log_data += "[Alert] https Traffic detected\n"
                    print("[Alert]  https detected\n")
        elif packet.haslayer(UDP):
            log_data += f"Source Port:{packet[UDP].sport}\n"
            log_data += f"Destination Port: {packet[UDP].dport}\n"
        elif packet.haslayer(ICMP):
            log_data += "ICMP ports"
            
        else:
            log_data += f"[Alert] Unknown Ports Detected:{protocol}\n"

        
        
        with open("packet_anlysys.txt","a") as f:
            f.write(log_data)

        


            
            

            
            

sniff(prn=packet_show, store=False)
