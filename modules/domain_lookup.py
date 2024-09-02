import whois

def lookup(domain):
    try:
        domain_info = whois.whois(domain)
        print("\nDomain Lookup Result:")
        print(f"Domain Name: {domain_info.domain_name}")
        print(f"Registrar: {domain_info.registrar}")
        print(f"Creation Date: {domain_info.creation_date}")
        print(f"Expiration Date: {domain_info.expiration_date}")
        print(f"Updated Date: {domain_info.updated_date}")
        print(f"Name Servers: {', '.join(domain_info.name_servers)}")
        print(f"Status: {', '.join(domain_info.status)}")
        print(f"Registrant Country: {domain_info.country}")
    except Exception as e:
        print(f"Error: {e}")

