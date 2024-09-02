import requests

SOCIAL_MEDIA_PLATFORMS = [
    ("Facebook", "https://www.facebook.com/{}"),
    ("Twitter", "https://twitter.com/{}"),
    ("Instagram", "https://www.instagram.com/{}"),
    ("LinkedIn", "https://www.linkedin.com/in/{}"),
    ("Pinterest", "https://www.pinterest.com/{}"),
    ("GitHub", "https://github.com/{}"),
    ("Reddit", "https://www.reddit.com/user/{}"),
    ("TikTok", "https://www.tiktok.com/@{}"),
    ("YouTube", "https://www.youtube.com/{}"),
    ("Medium", "https://medium.com/@{}"),
    ("Tumblr", "https://{}.tumblr.com"),
    ("VK", "https://vk.com/{}"),
    ("SoundCloud", "https://soundcloud.com/{}"),
    ("Flickr", "https://www.flickr.com/people/{}"),
    ("Steam", "https://steamcommunity.com/id/{}"),
    ("Blogger", "https://{}.blogspot.com"),
    ("WordPress", "https://{}.wordpress.com"),
    ("DeviantArt", "https://www.deviantart.com/{}"),
    ("Twitch", "https://www.twitch.tv/{}"),
    ("StackOverflow", "https://stackoverflow.com/users/{}"),
    ("Patreon", "https://www.patreon.com/{}"),
    ("Quora", "https://www.quora.com/profile/{}"),
    ("AngelList", "https://angel.co/{}"),
    ("Behance", "https://www.behance.net/{}"),
    ("Dribbble", "https://dribbble.com/{}"),
    ("500px", "https://500px.com/{}"),
    ("ProductHunt", "https://www.producthunt.com/@{}"),
    ("Mixcloud", "https://www.mixcloud.com/{}"),
    ("Bandcamp", "https://bandcamp.com/{}"),
    ("WeHeartIt", "https://weheartit.com/{}"),
    ("About.me", "https://about.me/{}"),
    ("LiveJournal", "https://{}.livejournal.com"),
    ("Goodreads", "https://www.goodreads.com/{}"),
    ("Gumroad", "https://gumroad.com/{}"),
    ("Scribd", "https://www.scribd.com/{}"),
    ("Wattpad", "https://www.wattpad.com/user/{}"),
    ("SlideShare", "https://www.slideshare.net/{}"),
    ("Kaggle", "https://www.kaggle.com/{}"),
    ("Bitbucket", "https://bitbucket.org/{}"),
    ("Trello", "https://trello.com/{}"),
    ("OkCupid", "https://www.okcupid.com/profile/{}"),
    ("ResearchGate", "https://www.researchgate.net/profile/{}"),
    ("Bit.ly", "https://bit.ly/{}"),
    ("AngelFire", "https://www.angelfire.com/{}"),
    ("LiveLeak", "https://www.liveleak.com/c/{}"),
    ("Imgur", "https://imgur.com/user/{}"),
    ("Diigo", "https://www.diigo.com/profile/{}"),
    ("Dailymotion", "https://www.dailymotion.com/{}"),
    ("Vimeo", "https://vimeo.com/{}"),
    ("Periscope", "https://www.pscp.tv/{}"),
    ("Discord", "https://discord.com/users/{}"),
    ("Gitee", "https://gitee.com/{}"),
    ("HackerRank", "https://www.hackerrank.com/{}"),
    ("Hashnode", "https://hashnode.com/@{}"),
    ("Dev.to", "https://dev.to/{}"),
    ("Couchsurfing", "https://www.couchsurfing.com/people/{}"),
    ("CodePen", "https://codepen.io/{}"),
    ("Instructables", "https://www.instructables.com/member/{}"),
    ("ReverbNation", "https://www.reverbnation.com/{}"),
    ("BandLab", "https://www.bandlab.com/{}"),
    ("Weibo", "https://weibo.com/{}"),
    ("Renren", "http://www.renren.com/{}"),
    ("MySpace", "https://myspace.com/{}"),
    ("Xing", "https://www.xing.com/profile/{}"),
    ("VK", "https://vk.com/{}"),
    ("AskFM", "https://ask.fm/{}"),
    ("Ello", "https://ello.co/{}"),
    ("MeWe", "https://mewe.com/i/{}"),
    ("Flipboard", "https://flipboard.com/@{}"),
    ("Meetup", "https://www.meetup.com/members/{}"),
    ("Snapchat", "https://www.snapchat.com/add/{}"),
    ("Badoo", "https://badoo.com/profile/{}"),
    ("Friendster", "http://www.friendster.com/{}"),
    ("WeChat", "https://weixin.qq.com/r/{}"),
    ("Telegram", "https://t.me/{}"),
    ("Mastodon", "https://mastodon.social/@{}"),
    ("Gaia Online", "https://www.gaiaonline.com/profiles/{}"),
    ("Xanga", "https://www.xanga.com/{}"),
    ("BlackPlanet", "https://www.blackplanet.com/{}"),
    ("Tagged", "https://www.tagged.com/{}"),
    ("Habbo", "https://www.habbo.com/user/{}"),
    ("Friendica", "https://friendica.com/{}"),
    ("Diaspora", "https://diaspora.com/{}"),
    ("Hubzilla", "https://hubzilla.com/{}"),
    ("Minds", "https://www.minds.com/{}"),
    ("Mix", "https://mix.com/{}"),
    ("Ello", "https://ello.co/{}"),
    ("Plurk", "https://www.plurk.com/{}"),
    ("MyHeritage", "https://www.myheritage.com/member-{}"),
    ("Genealogy", "https://www.geni.com/profile/{}"),
    ("Ancestry", "https://www.ancestry.com/family-tree/tree/{}"),
    ("Doxbin", "https://doxbin.com/user/{}"),
    ("Exploit.in", "https://exploit.in/user/{}"),
    ("Pastebin", "https://pastebin.com/u/{}"),
    ("PublicWWW", "https://publicwww.com/websites/{}"),
    ("Cracked", "https://cracked.io/u/{}"),
    ("0day.today", "https://0day.today/user/{}"),
    ("Forum", "https://forum.{}"),
    ("Cryptome", "https://cryptome.org/{}"),
    ("Mega", "https://mega.nz/fm/{}"),
    ("AnonFiles", "https://anonfiles.com/u/{}"),
    ("SecLists", "https://seclists.org/{}"),
    ("HackerOne", "https://hackerone.com/{}"),
    ("Bugcrowd", "https://bugcrowd.com/{}"),
    ("ExploitDB", "https://www.exploit-db.com/author/{}"),
    ("Malshare", "https://malshare.com/profile/{}"),
    ("MalwareBazaar", "https://bazaar.abuse.ch/author/{}"),
    ("Any.run", "https://app.any.run/{}"),
    ("JoeSandbox", "https://www.joesandbox.com/reports/{}"),
]

def search(username):
    print(f"\nSearching for username '{username}' on social media platforms...\n")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    for platform_name, url_template in SOCIAL_MEDIA_PLATFORMS:
        url = url_template.format(username)
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print(f"[+] {platform_name}: Found! URL: {url}")
            else:
                print(f"[-] {platform_name}: Not found.")
        except requests.RequestException as e:
            print(f"[!] {platform_name}: Error occurred - {e}")

if __name__ == "__main__":
    user = input("Enter the username to search: ")
    search(user)

