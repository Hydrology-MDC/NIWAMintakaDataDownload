import yaml
import keyring


def load_config():
    with open("config/config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    service = config["api"]["api_credential"]

    config["api"]["username"] = keyring.get_password(service, "username")

    config["api"]["password"] = keyring.get_password(service, "password")

    if not config["api"]["username"]:
        raise ValueError(f"Username not found in keyring service '{service}'")

    if not config["api"]["password"]:
        raise ValueError(f"Password not found in keyring service '{service}'")

    return config