# codeAlpha - Network Sniffer (Tâche 1)
Ce projet est un sniffer réseau développé avec Python et la bibliothèque Scapy.  
Il s'inscrit dans le cadre du stage de cybersécurité chez CodeAlpha.

Il permet de :
- Capturer des paquets réseau en temps réel
- Afficher les adresses IP source et destination
- Identifier le protocole utilisé (TCP/UDP)
- Afficher les ports utilisés
- Lire le contenu du paquet (payload) si lisible

## Technologies utilisées
- Python 3.12
- Scapy (`pip install scapy`)
- Npcap (pour le sniffing réel sur Windows)

## Utilisation
1. Ouvrir PowerShell **en mode administrateur**
2. Aller dans le dossier du script
3. Lancer :
python task1.py
