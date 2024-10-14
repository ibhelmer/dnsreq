from scapy.all import *

# Sæt domænenavnet, som du ønsker at lave DNS-forespørgsel på
domain_name = "ibhelmer.dk"

# Opret en DNS-forespørgselspakke
dns_request = IP(dst="8.8.8.8") / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=domain_name))

# Send forespørgslen og modtag svaret
dns_response = sr1(dns_request, verbose=0)

# Udskriv DNS-svaret
if dns_response and dns_response.haslayer(DNS):
    for i in range(dns_response[DNS].ancount):
        print(dns_response[DNS].an[i].rdata)
else:
    print("Ingen DNS-svar modtaget.")

