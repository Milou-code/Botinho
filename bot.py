# Importation des bibliothèques
import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
from tiktok_utils import check_new_video, get_video_url

load_dotenv()
token_bot = os.getenv('DISCORD_TOKEN')

print("Lancement du bot...")
bot = commands.Bot(command_prefix = '!', intents = discord.Intents.all())

@tasks.loop(seconds=60) # Vérifie toutes les 5 minutes
async def check_tiktok():
    print("⏳ [Tâche] Vérification TikTok en cours...")
    channel_id = 1364302377590456391 # Remplace avec l'ID du salon où envoyer le lien
    channel = bot.get_channel(channel_id)
    if channel:
        if await check_new_video():
            print("✅ Nouvelle vidéo détectée ! Envoi du lien...")
            url = get_video_url()
            await channel.send(f"📢 Nouvelle vidéo TikTok ! {url}")
        else :
            print("🔍 Aucune nouvelle vidéo.")
    else:
        print(f"❌ Salon non trouvé (ID: {channel_id})")

@bot.event
async def on_ready():
    print("Bot allumé !")
    #Synchronisation des commandes
    try : 
        synced = await bot.tree.sync()
        print(f"Nombre de commandes synchronisées : {len(synced)}")
    except Exception as e :
        print(e)
    check_tiktok.start()
    print("🚀 Tâche de vérification TikTok démarrée.")

@bot.event
async def on_message(message: discord.Message):
    msg = message.content.lower()
    if 'lien pour' in msg or 'liens pour' in msg :
        channel = message.channel
        await channel.send("**Tu peux retrouver tous les liens du jour ici -->** https://discord.com/channels/1232443169132773478/1348337167423770644")

@bot.tree.command(name="tiktok", description="Lien vers notre chaine tiktok")
async def tiktok(interaction: discord.Interaction):
    print("📱 Commande /tiktok utilisée")
    await interaction.response.send_message("**Voici notre chaîne tiktok :** https://www.tiktok.com/@ismil0u \n N'hésite pas à aller t'abonner :)")

@bot.tree.command(name="twitter", description="Lien vers notre page X (twitter)")
async def twitter(interaction: discord.Interaction):
    print("🐦 Commande /twitter utilisée")
    await interaction.response.send_message("**Voici notre page X (Twitter) :** https://x.com/le12_homme \n N'hésite pas à aller t'abonner :)")

@bot.tree.command(name="ping", description="Vérifier le ping du bot sur le serveur")
async def ping(interaction: discord.Interaction):
    print("🏓 Commande /ping utilisée")
    await interaction.response.send_message(f"**Ping :** {round(bot.latency * 1000)}ms")

bot.run(token_bot)
