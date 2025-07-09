from scapy.all import sniff, IP, TCP, UDP, Raw


# creer une fct pour analyser chaque paquet capturé
def analyser_paquet(paquet):
    if IP in paquet:  # Vérifie s’il y a une couche IP
        print("Nouveau paquet capturé !")

        print("IP source       :", paquet[IP].src)
        print("IP destination  :", paquet[IP].dst)

        if TCP in paquet:
            print("Protocole       : TCP")
            print("Port source     :", paquet[TCP].sport)
            print("Port destination:", paquet[TCP].dport)

        elif UDP in paquet:
            print("Protocole       : UDP")
            print("Port source     :", paquet[UDP].sport)
            print("Port destination:", paquet[UDP].dport)
        else:
            print("Protocole       : Autre")

        # Afficher le contenu si disponible
        if Raw in paquet:
            try:
                print("Contenu (payload):", paquet[Raw].load.decode(errors='ignore'))
            except:
                print("Contenu : [données non lisibles]")

        print("=" * 60)


print("Démarrage du sniffer. Appuie sur Ctrl+C pour arrêter.")
sniff(count=10, filter="ip", prn=analyser_paquet, store=0)

