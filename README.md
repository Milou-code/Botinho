# Botinho ⚽🤖

Botinho est un bot Discord développé en **Python**.  
C’était mon tout premier bot, à la base créé pour un serveur orienté football mais il est surtout destiné aux créateurs de contenus, je cherchais une alternative gratuite à Pingbot.

## 🎯 Objectif du bot

Le bot avait deux fonctionnalités principales :

- répondre à des commandes sur Discord ;
- envoyer une alerte lorsqu’un nouveau TikTok était publié sur un compte suivi.

## 🚀 Fonctionnalités

- Commandes Discord personnalisées
- Système d’alertes TikTok
- Bot simple et léger, parfait pour apprendre les bases de l’automatisation Discord

## 🛠️ Stack technique

- **Langage** : Python (100%)
- **Plateforme** : Discord
- **But** : apprentissage et expérimentation autour des bots communautaires

## 📦 Installation (générique)

> ⚠️ À adapter selon les fichiers présents dans le repo (`requirements.txt`, structure, etc.)

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/Milou-code/Botinho.git
   cd Botinho
   ```

2. (Optionnel mais recommandé) Créer un environnement virtuel :
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux / macOS
   .venv\Scripts\activate     # Windows
   ```

3. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Configurer les variables d’environnement (exemple) :
   ```env
   DISCORD_TOKEN=ton_token_discord
   TIKTOK_ACCOUNTS=compte1,compte2
   ALERT_CHANNEL_ID=id_du_salon_discord
   ```

5. Lancer le bot :
   ```bash
   python main.py
   ```

## 🔐 Configuration

Pour utiliser le bot, il faut généralement :

- créer une application/bot sur le [Discord Developer Portal](https://discord.com/developers/applications) ;
- récupérer le token du bot ;
- inviter le bot sur ton serveur avec les permissions nécessaires ;
- définir le salon où envoyer les alertes TikTok.

## 📚 Contexte du projet

Ce projet représente mes débuts en développement de bots Discord.  
Il m’a permis d’apprendre :

- la gestion d’événements et de commandes ;
- l’intégration de services externes ;
- la structure d’un projet Python orienté automatisation.

## ⚠️ Notes

- Le projet peut contenir du code “première version” (normal pour un premier bot 😊).
- Si le code n’est plus maintenu, certaines APIs ou dépendances peuvent nécessiter une mise à jour.

## 🧑‍💻 Auteur

- GitHub : [@Milou-code](https://github.com/Milou-code)
