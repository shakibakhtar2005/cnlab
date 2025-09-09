import dns.resolver

def dns_demo():
    domain = "example.com"

    try:
        # A record
        result = dns.resolver.resolve(domain, "A")
        for ip in result:
            print("A record:", ip.to_text())

        # MX record
        result = dns.resolver.resolve(domain, "MX")
        for mx in result:
            print("MX record:", mx.to_text())

        # CNAME record
        try:
            result = dns.resolver.resolve(domain, "CNAME")
            for cname in result:
                print("CNAME record:", cname.to_text())
        except:
            print("No CNAME record found.")

    except Exception as e:
        print("DNS query failed:", e)

dns_demo()
