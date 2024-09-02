import requests

# List of websites/platforms for phone number search
PHONE_SEARCH_SITES = [
    ("Truecaller", "https://www.truecaller.com/search/{}"),
    ("Whitepages", "https://www.whitepages.com/phone/{}"),
    ("Spokeo", "https://www.spokeo.com/{}"),
    ("ZabaSearch", "https://www.zabasearch.com/people/{}"),
    ("Intelius", "https://www.intelius.com/people-search/{}"),
    ("BeenVerified", "https://www.beenverified.com/phone/{}"),
    ("Instant Checkmate", "https://www.instantcheckmate.com/search/{}"),
    ("PeopleFinders", "https://www.peoplefinders.com/phone/{}"),
    ("AnyWho", "https://www.anywho.com/phone/{}"),
    ("411.com", "https://www.411.com/phone/{}"),
    ("Pipl", "https://pipl.com/search/?q={}"),
    ("CocoFinder", "https://www.cocofinder.com/reverse-phone-lookup/{}"),
    ("TruthFinder", "https://www.truthfinder.com/reverse-phone-lookup/{}"),
    ("NumLookup", "https://www.numlookup.com/{}"),
    ("WhoCallsMe", "https://whocallsme.com/Phone-Number.aspx/{}"),
    ("NumberGuru", "https://www.numberguru.com/{}"),
    ("SpyDialer", "https://spydialer.com/search?q={}"),
    ("USPhoneBook", "https://www.usphonebook.com/{}"),
    ("Radaris", "https://radaris.com/phone/{}"),
    ("PeopleLooker", "https://www.peoplelooker.com/phone/{}"),
    ("PeekYou", "https://www.peekyou.com/phone/{}"),
    ("FastPeopleSearch", "https://www.fastpeoplesearch.com/phone/{}"),
    ("That’sThem", "https://thatsthem.com/phone/{}"),
    ("SmartBackgroundChecks", "https://www.smartbackgroundchecks.com/phone/{}"),
    ("ReversePhoneLookup.com", "https://www.reversephonelookup.com/{}"),
    ("PhoneNumber.com", "https://phonenumber.com/search/{}"),
    ("USSearch", "https://www.ussearch.com/phone-lookup/{}"),
    ("InfoTracer", "https://infotracer.com/phone-lookup/{}"),
    ("PeoplebyName", "https://peoplebyname.com/search/{}"),
    ("CheckThem", "https://checkthem.com/phone/{}"),
    ("Social Catfish", "https://socialcatfish.com/search/{}"),
    ("PhoneLookup.com", "https://phonelookup.com/phone/{}"),
    ("FindPeopleSearch", "https://findpeoplesearch.com/phone/{}"),
    ("CallerName", "https://callername.com/lookup/{}"),
    ("ReversePhoneReports", "https://reversephonereports.com/phone/{}"),
    ("PhoneDetective", "https://phonedetective.com/{}"),
    ("Kiwi Searches", "https://kiwisearches.com/phone/{}"),
    ("PhoneHistory", "https://phonehistory.com/{}"),
    ("Webmii", "https://webmii.com/people/{}"),
    ("CallerSmart", "https://callersmart.com/lookup/{}"),
    ("OkCaller", "https://okcaller.com/search?q={}"),
    ("Sync.me", "https://sync.me/search/?q={}"),
    ("InstaCheckMate", "https://instacheckmate.com/phone/{}"),
    ("Phonebook.cz", "https://phonebook.cz/search?q={}"),
    ("Telelisting", "https://telelisting.com/phone/{}"),
    ("FindPeopleFree", "https://findpeoplefree.com/phone/{}"),
    ("SearchYellowDirectory", "https://searchyellowdirectory.com/phone/{}"),
    ("Nuwber", "https://nuwber.com/search/phone/{}"),
    ("FindWhitePages", "https://findwhitepages.com/phone/{}"),
    ("Facebook", "https://www.facebook.com/search/top/?q={}"),
    ("Twitter", "https://twitter.com/search?q={}"),
    ("LinkedIn", "https://www.linkedin.com/search/results/people/?keywords={}"),
    ("Instagram", "https://www.instagram.com/explore/tags/{}"),
    ("Google Search", "https://www.google.com/search?q={}"),
    ("Bing Search", "https://www.bing.com/search?q={}"),
    ("Yandex Search", "https://yandex.com/search/?text={}"),
    ("Reddit", "https://www.reddit.com/search/?q={}"),
    ("Pinterest", "https://www.pinterest.com/search/pins/?q={}"),
    ("YouTube", "https://www.youtube.com/results?search_query={}"),
    ("VK", "https://vk.com/search?c%5Bq%5D={}"),
    ("GitHub", "https://github.com/search?q={}"),
    ("Craigslist", "https://{}.craigslist.org/search/sss?query={}"),
    ("Tumblr", "https://www.tumblr.com/search/{}"),
    ("Quora", "https://www.quora.com/search?q={}"),
    ("Pastebin", "https://pastebin.com/search?q={}"),
    ("PublicWWW", "https://publicwww.com/websites/{}"),
    ("TruePeopleSearch", "https://truepeoplesearch.com/results?phoneno={}")
]

def search(phone_number):
    print(f"\nSearching for phone number '{phone_number}' on various websites...\n")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    for site_name, url_template in PHONE_SEARCH_SITES:
        url = url_template.format(phone_number)
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.ok:
                print(f"[+] {site_name}: Check results here - {url}")
            else:
                print(f"[-] {site_name}: Not available (Status code: {response.status_code}).")
        except requests.RequestException as e:
            print(f"[!] {site_name}: Error occurred - {e}")

if __name__ == "__main__":
    phone_number = input("Enter the phone number to search (with country code, e.g., +1XXXXXXXXXX): ")
    search_phone_number(phone_number)

