import requests

from consts import access_token, base_url

def get_headers():
    header = {
        "Authorization": f"Bearer {access_token}",
        "accept": "application/json"
    }

    return header

def autenticar():
    header = get_headers()
    resultado = requests.get(f"{base_url}/3/authentication", headers=header)
    print(resultado.json())
    return resultado.json()