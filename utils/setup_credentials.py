import getpass
import keyring

SERVICE_NAME = "mintaka_api"

username = input("Username: ").strip()
password = getpass.getpass("Password: ")

keyring.set_password(
    SERVICE_NAME,
    "username",
    username
)

keyring.set_password(
    SERVICE_NAME,
    "password",
    password
)

print(f"Credentials updated for service '{SERVICE_NAME}'")