import tkinter as tk
from scapy.all import *

# Funktion til at udføre DNS-forespørgsel og vise resultat
def dns_query():
    domain_name = entry.get()
    if domain_name:
        try:
            # DNS forespørgsel til Google's DNS server (8.8.8.8)
            dns_request = IP(dst="8.8.8.8") / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=domain_name))
            dns_response = sr1(dns_request, verbose=0)

            # Hvis der er et DNS-svar
            if dns_response and dns_response.haslayer(DNS):
                results = ""
                for i in range(dns_response[DNS].ancount):
                    results += str(dns_response[DNS].an[i].rdata) + "\n"
                result_label.config(text=results)
            else:
                result_label.config(text="Ingen DNS-svar modtaget.")
        except Exception as e:
            result_label.config(text=f"Fejl: {str(e)}")
    else:
        result_label.config(text="Indtast et domænenavn!")

# Opret GUI vinduet
root = tk.Tk()
root.title("DNS Forespørgsel")

# Label for domænenavn indtastning
label = tk.Label(root, text="Indtast domænenavn:")
label.pack(pady=5)

# Entry widget til domænenavn
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Knap til at udføre DNS-forespørgsel
query_button = tk.Button(root, text="Forespørg DNS", command=dns_query)
query_button.pack(pady=10)

# Label til at vise resultaterne af DNS-forespørgslen
result_label = tk.Label(root, text="", wraplength=400, justify="left")
result_label.pack(pady=10)

# Start GUI hovedløkke
root.mainloop()
