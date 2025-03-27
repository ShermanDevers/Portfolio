api_key = input("Your discord api key: ")

with open(".env", "a+") as env:
    env.write(f"AUTH_T={api_key}\n")
