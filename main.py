import os
import sys
from modules import (
    domain_lookup, ip_info, email_search, social_media_search,
    search_phone_number, data_breach_search, people_search,
    image_lookup, image_metadata_lookup, email_internet_search
)

def main():
    print(r"""
███╗   ███╗███████╗██╗  ██╗
████╗ ████║██╔════╝██║  ██║
██╔████╔██║█████╗  ███████║
██║╚██╔╝██║██╔══╝  ██╔══██║
██║ ╚═╝ ██║███████╗██║  ██║
╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝

        Created by A.M Pachouri
        YouTube        -- @mastersinethicalhacking
        Instagram      -- @mastersinethicalhacking
        Facebook       -- MastersInEthicalHacking
    """)

    print("Welcome to OSINT Framework in Python")
    print("1. Domain Lookup")
    print("2. IP Information")
    print("3. Email Search")
    print("4. Social Media Search by Username")
    print("5. Indian Phone Number Search")
    print("6. Data Breach Search")
    print("7. Indian People Search by Name and Email ID")
    print("8. Image Lookup")
    print("9. Image Metadata Lookup")
    print("10. Where Email is Used on the Internet")
    print("11. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        domain = input("Enter domain name: ")
        domain_lookup.lookup(domain)
    elif choice == "2":
        ip = input("Enter IP address: ")
        ip_info.lookup(ip)
    elif choice == "3":
        email = input("Enter email address: ")
        email_search.search(email)
    elif choice == "4":
        username = input("Enter social media username: ")
        social_media_search.search(username)
    elif choice == "5":
        phone_number = input("Enter Indian phone number: ")
        search_phone_number.search(phone_number)
    elif choice == "6":
        email = input("Enter email address for breach search: ")
        data_breach_search.search(email)
    elif choice == "7":
        name = input("Enter name: ")
        email = input("Enter email (optional): ")
        people_search.search(name, email)
    elif choice == "8":
        image_path = input("Enter the path to the image: ")
        image_lookup.lookup(image_path)
    elif choice == "9":
        image_path = input("Enter the path to the image: ")
        image_metadata_lookup.lookup(image_path)
    elif choice == "10":
        email = input("Enter email address: ")
        email_internet_search.search(email)
    elif choice == "11":
        sys.exit()
    else:
        print("Invalid choice! Exiting...")
        sys.exit()

if __name__ == "__main__":
    main()
