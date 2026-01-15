![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Tool](https://img.shields.io/badge/PySimpleGUI-8A2BE2)
![Status](https://img.shields.io/badge/Status-Completed-success)

# 📡 LTE Network Dimensioning Application
<p align="center">
  <img src="captures/index.png" alt="Page d'accueil de l'application LTE Dimensioning">
</p>

## Description

Ce projet est une application desktop destinée au dimensionnement d'un réseau LTE. Elle a été réalisée dans le cadre du projet "Ingénierie Planification Réseaux" pour l'année scolaire 2022/2023 en classe INGC3 à l'École Supérieure Multinationale Des Télécommunications (ESMT).

L'objectif principal est de fournir un outil permettant de calculer le trafic (Internet, VPN, signalisation) et de dimensionner les nœuds et interfaces du réseau (Plan Usager et Plan de Contrôle).

## 🚀 Fonctionnalités

L'application propose les modules de calcul suivants :

### 1. Calcul du Trafic

* **Trafic Utilisateur :** Estimation du trafic Internet et VPN généré par les "Data Cards" et les Smartphones LTE (en Uplink/Downlink).


* **Trafic Total :** Calcul du trafic total VPN et Internet à l'heure chargée (HC).



### 2. Calcul du Trafic de Signalisation

* Estimation du nombre total d'opérations pour chaque procédure de signalisation.



### 3. Dimensionnement

* **Nœuds LTE :** Calcul du nombre de nœuds requis (MME, SGW, PGW).


* **Plan Usager & Contrôle :** Dimensionnement des plans et calcul des capacités des interfaces S1U et S8 (trafic utilisateur).



## 🛠 Technologies Utilisées

* **Langage :** Python (orienté objet, typage dynamique).
* **Interface Graphique (GUI) :** `PySimpleGUI` (basé sur Tkinter).
* **IDE recommandé :** PyCharm Community.

* **Stockage de données :** Utilisation de dictionnaires Python pour la sauvegarde temporaire et la réutilisation des résultats de calcul.



## 📂 Structure du Projet

L'application est structurée autour de plusieurs modules Python interconnectés. Le schéma ci-dessous illustre l'architecture des paquets et leurs dépendances :

<p align="center">
  <img src="images/packages%20architecture.png" alt="Architecture des paquets et imports du projet">
</p>

Le projet est composé de 9 fichiers principaux:

* `main.py` : Point d'entrée principal, inclut tous les autres fichiers.
* `main_windows.py` : Interface de récupération des paramètres globaux (nombre d'abonnés, % smartphones, etc.).


* `dataCards_smartphones_trafic.py` : Module de calcul trafic terminaux.
* `trafic_total_internet_vpn.py` : Module de calcul trafic global.
* `signaling_traffic_windows.py` : Module pour le trafic de signalisation.
* `nombre_de_noeuds_requis.py` : Calcul du nombre d'équipements.
* `dimensionnement_noeuds_lte.py` : Dimensionnement spécifique des nœuds.
* `dimensionnement_plan_controle.py` : Dimensionnement du plan de contrôle.
* `dimensionnement_plan_usager.py` : Dimensionnement du plan usager.

## ⚙️ Installation et Utilisation

### Prérequis

* Python 3.x installé sur votre machine.
* Bibliothèque `PySimpleGUI`.

```bash
pip install PySimpleGUI

```

### Lancement

Exécutez le fichier principal pour démarrer l'application :

```bash
python main.py

```

### ⚠️ Notes Importantes pour l'Utilisateur

Pour garantir le bon fonctionnement des calculs :

1. **Format des données :** Évitez d'entrer des chaînes de caractères dans les champs numériques pour ne pas causer de dysfonctionnement.


2. **Pourcentages :** Les valeurs en pourcentage doivent impérativement être converties en décimales (divisées par 100).
*Exemple :* Pour **60%**, saisissez **0.6**.