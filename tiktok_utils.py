from TikTokApi import TikTokApi
import asyncio
import os

ms_token = os.getenv("TIKTOK_MS_TOKEN")
if not ms_token:
    raise ValueError("TIKTOK_MS_TOKEN is not set. Please set it in your environment variables.")

LAST_URL_FILE = "last_url.txt"

async def get_last_video():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, browser=os.getenv("TIKTOK_BROWSER", "chromium"))
        user = 'ismil0u'
        async for video in api.user(user).videos():
            video = video.as_dict
            url = f"https://www.tiktok.com/@{video['author']['uniqueId']}/video/{video['id']}"
            return url  # Retourne l'URL de la vidéo

        print("Finished fetching trending videos.")
        return None  # Si aucune vidéo n'est trouvée, retourne None
    
def load_last_url():
    try:
        with open(LAST_URL_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""
    
def save_last_url(url):
    with open(LAST_URL_FILE, "w") as f:
        f.write(url)

async def check_new_video():
    try:
        current_url = load_last_url()
        new_url = await get_last_video()
        if new_url and new_url != current_url:
            save_last_url(new_url)
            return True
    except Exception as e:
        print(f"Erreur dans check_new_video : {e}")
    return False

def get_video_url():
    return load_last_url()

if __name__ == "__main__":
    # Exemple d'utilisation
    for i in range(3):
        if check_new_video():
            print("Nouvelle vidéo trouvée !")
            print("URL de la vidéo :", get_video_url())
        else:
            print("Aucune nouvelle vidéo.")
