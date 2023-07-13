def main():
    input_email = input('Input your email address: ')

    (username, domain) = input_email.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)

while True:
    main()