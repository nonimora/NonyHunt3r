#make sure u typing the right username 
#no1 is hide :))
#Good luck by Nonitoo



import requests
from colorama import Fore, Style, init
import pyfiglet
import time
import os

init(autoreset=True)

def banner():
    os.system('clear')
    text = pyfiglet.figlet_format("NonyHunt3r", font="slant")
    print(Fore.CYAN + text)
    print(Fore.YELLOW + "="*55)
    print(Fore.GREEN + "  OSINT Username Hunter | by Nonitoo")
    print(Fore.YELLOW + "="*55 + "\n")

def check_username(username):
    sites = {
        "Instagram": f"https://www.instagram.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "X.com": f"https://x.com/{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Spotify": f"https://open.spotify.com/user/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Roblox": f"https://www.roblox.com/user.aspx?username={username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Bitbucket": f"https://bitbucket.org/{username}/",
        "Behance": f"https://www.behance.net/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}",
        "500px": f"https://500px.com/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "Blogger": f"https://{username}.blogspot.com",
        "WordPress": f"https://{username}.wordpress.com",
        "Patreon": f"https://www.patreon.com/{username}",
        "Ko-fi": f"https://ko-fi.com/{username}",
        "BuyMeCoffee": f"https://www.buymeacoffee.com/{username}",
        "PayPal": f"https://www.paypal.me/{username}",
        "CashApp": f"https://cash.app/${username}",
        "Telegram": f"https://t.me/{username}",
        "VK": f"https://vk.com/{username}",
        "Odnoklassniki": f"https://ok.ru/{username}",
        "Wattpad": f"https://www.wattpad.com/user/{username}",
        "Quora": f"https://www.quora.com/profile/{username}",
        "ProductHunt": f"https://www.producthunt.com/@{username}",
        "HackerNews": f"https://news.ycombinator.com/user?id={username}",
        "HackerOne": f"https://hackerone.com/{username}",
        "BugCrowd": f"https://bugcrowd.com/{username}",
        "Replit": f"https://replit.com/@{username}",
        "CodePen": f"https://codepen.io/{username}",
        "StackOverflow": f"https://stackoverflow.com/users/{username}",
        "Kaggle": f"https://www.kaggle.com/{username}",
        "LeetCode": f"https://leetcode.com/{username}",
        "TryHackMe": f"https://tryhackme.com/p/{username}",
        "HackTheBox": f"https://app.hackthebox.com/profile/{username}",
        "Chess.com": f"https://www.chess.com/member/{username}",
        "Lichess": f"https://lichess.org/@/{username}",
        "Duolingo": f"https://www.duolingo.com/profile/{username}",
        "Anilist": f"https://anilist.co/user/{username}/",
        "MyAnimeList": f"https://myanimelist.net/profile/{username}",
        "Letterboxd": f"https://letterboxd.com/{username}/",
        "Goodreads": f"https://www.goodreads.com/{username}",
        "Gravatar": f"https://gravatar.com/{username}",
        "About.me": f"https://about.me/{username}",
        "Keybase": f"https://keybase.io/{username}",
        "Slack": f"https://{username}.slack.com",
        "Notion": f"https://www.notion.so/{username}",
        "Trello": f"https://trello.com/{username}",
        "Fiverr": f"https://www.fiverr.com/{username}",
        "Etsy": f"https://www.etsy.com/people/{username}",
        "Gumroad": f"https://gumroad.com/{username}",
        "Bandcamp": f"https://bandcamp.com/{username}",
        "LastFM": f"https://www.last.fm/user/{username}",
        "MixCloud": f"https://www.mixcloud.com/{username}/",
        "BandsInTown": f"https://www.bandsintown.com/a/{username}",
        "OnlyFans": f"https://onlyfans.com/{username}",
        "Fansly": f"https://fansly.com/{username}",
        "Pornhub": f"https://www.pornhub.com/users/{username}",
        "XVideos": f"https://www.xvideos.com/profiles/{username}",
        "Chaturbate": f"https://chaturbate.com/{username}/",
        "Cameo": f"https://www.cameo.com/{username}",
        "VSCO": f"https://vsco.co/{username}",
        "Disqus": f"https://disqus.com/{username}",
        "Discord": f"https://discord.com/users/{username}",
        "Kick": f"https://kick.com/{username}",
        "Rumble": f"https://rumble.com/c/{username}",
        "Odysee": f"https://odysee.com/@{username}",
        "BitChute": f"https://www.bitchute.com/channel/{username}/",
        "Gab": f"https://gab.com/{username}",
        "Minds": f"https://www.minds.com/{username}",
        "Parler": f"https://parler.com/{username}",
        "Gettr": f"https://gettr.com/user/{username}",
        "TruthSocial": f"https://truthsocial.com/@{username}",
        "Mastodon": f"https://mastodon.social/@{username}",
        "Threads": f"https://www.threads.net/@{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Periscope": f"https://www.pscp.tv/{username}/",
        "Imgur": f"https://imgur.com/user/{username}",
        "Giphy": f"https://giphy.com/{username}",
        "Tenor": f"https://tenor.com/users/{username}",
        "Slack": f"https://{username}.slack.com",
    }

    print(Fore.MAGENTA + f"[*] Hunting for: {username}\n")
    time.sleep(0.5)

    for name, url in sites.items():
        try:
            r = requests.get(url, timeout=5, headers={"User-Agent":"Mozilla/5.0"})
            if r.status_code == 200:
                print(Fore.GREEN + f"[FOUND] {name:12} -> {url}")
            elif r.status_code == 404:
                print(Fore.RED + f"[NOT FOUND] {name:12} -> {url}")
            else:
                print(Fore.YELLOW + f"[UNKNOWN {r.status_code}] {name:12} -> {url}")
        except:
            print(Fore.YELLOW + f"[ERROR] {name:12} -> Could not check")

if __name__ == "__main__":
    banner()
    username = input(Fore.CYAN + "Enter username to hunt > " + Style.RESET_ALL).strip()
    if username:
        check_username(username)
        print(Fore.CYAN + "\n[+] Hunt finished!")
    else:
        print(Fore.RED + "[-] No username entered!")
