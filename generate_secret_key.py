# generate_secret_key.py
from django.core.management.utils import get_random_secret_key


if __name__ == "__main__":
    secret_key = get_random_secret_key()


    with open(".env", "w") as env_file:
        env_file.write(f"SECRET_KEY=\"{secret_key}\"\n")

    print("Secret key generated and saved to .env file.")
