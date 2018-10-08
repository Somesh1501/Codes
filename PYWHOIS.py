import whois
data = input("Enter a Domain name.\n")
w = whois.whois(data)
print(w)