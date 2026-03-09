import os
import sys
import time
import webbrowser
import json
import requests
import socket
import socketserver
import http.server
from typing import Dict, Any

# --- STYLING ---
GREEN = "\033[1;32m"
RED = "\033[1;31m"
BLUE = "\033[1;34m"
YELLOW = "\033[1;33m"
WHITE = "\033[1;37m" 
CYAN = "\033[1;36m"
RESET = "\033[0m"

# --- SYSTEM INITIALIZATION ---
LOOT_DIR = "brahmastra_loot"
if not os.path.exists(LOOT_DIR):
    os.makedirs(LOOT_DIR)

# --- ETHICAL VIRUS BUILDER CLASS ---
class EthicalVirusBuilder:
    def __init__(self):
        self.platforms = {
            '1': ('windows', 'Windows Meterpreter RAT'),
            '2': ('linux', 'Linux Reverse Shell'), 
            '3': ('android', 'Android RAT APK'),
            '4': ('macos', 'macOS Keylogger'),
            '5': ('custom', 'Custom Webhook')
        }
    
    def virus_menu(self):
        print(f"{GREEN}\n=== VIRUS BUILDER - AUTHORIZED PENTEST ONLY ==={RESET}")
        for key, (plat, desc) in self.platforms.items():
            print(f"{WHITE}{key}. {desc} → {plat}{RESET}")
        
        choice = input(f"{BLUE}Target Platform > {RESET}").strip()
        if choice not in self.platforms: return
        
        device, desc = self.platforms[choice]
        
        print(f"\n{CYAN}=== TARGET CONSENT REQUIRED ==={RESET}")
        consent = input(f"{RED}Type 'I CONSENT' to verify authorization > {RESET}").strip().upper()
        
        if consent == "I CONSENT":
            print(f"{YELLOW}[*] Compiling {desc} payload...{RESET}")
            time.sleep(1.5)
            filename = os.path.join(LOOT_DIR, f"payload_{device}_{int(time.time())}.json")
            data = {"type": desc, "platform": device, "status": "Ready", "timestamp": time.time()}
            with open(filename, "w") as f:
                json.dump(data, f, indent=4)
            print(f"{GREEN}✅ Payload Generated: {filename}{RESET}")
        else:
            print(f"{RED}[!] ABORTED: Consent not verified.{RESET}")

# --- CORE UTILITIES ---
def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{GREEN}")
    print(r"""
    __________                           .__                               
    \______   \____________  |  |__  _____ _____    ____ |  |_____________ 
     |    |  _/\_  __ \__  \ |  |  \ /     \\__  \  / ___\|  |\_  __ \__  \
     |    |   \ |  | \// __ \|  Y  \  Y Y  \/ __ \_\  \___|  |_|  | \// __ \_
     |______  / |__|  (____  /___|  /__|_|  (____  /\___  >____/__|  (____  /
            \/             \/     \/      \/     \/    \/                \/
                    [ V11.5 - THE OMNI-PENETRATION & FORENSIC SUITE ]
                    [ Created by: @thesudosiuu | GitHub: shouryacr7 ]
    """)
    print(f"{RESET}")

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# --- MODULES ---

def digital_footprint():
    target = input(f"{BLUE}Enter Target Username/Email: {RESET}").strip()
    print(f"{YELLOW}[*] Running Sherlock Scan on {target}...{RESET}")
    os.system(f"sherlock {target}")

def google_dorks():
    domain = input(f"{BLUE}Enter Target Domain (e.g., target.com): {RESET}").strip()
    print(f"{YELLOW}[*] Opening Admin & Vulnerability Dorks...{RESET}")
    webbrowser.open(f"https://www.google.com/search?q=site:{domain}+inurl:admin+OR+inurl:login")
    webbrowser.open(f"https://www.google.com/search?q=site:{domain}+ext:php+id=")

def ip_tracker():
    ip = input(f"{BLUE}Enter IP Address: {RESET}").strip()
    try:
        data = requests.get(f"http://ip-api.com/json/{ip}").json()
        print(f"{GREEN}\n[+] IP Results:")
        print(f"{WHITE}City: {data.get('city')}\nCountry: {data.get('country')}\nISP: {data.get('isp')}{RESET}")
    except:
        print(f"{RED}[!] Error fetching IP data.{RESET}")

def wordlist_generator():
    print(f"{CYAN}\n--- HIGH-END WORDLIST GENERATOR ---{RESET}")
    name = input(f"{BLUE}Target Name: {RESET}").strip().lower()
    dob = input(f"{BLUE}DOB (DDMMYYYY): {RESET}").strip()
    special = input(f"{BLUE}Special Character: {RESET}").strip()
    
    if not name: return
    
    words = [name+dob, name+special+dob[-4:] if len(dob)>4 else name+special, name.capitalize()+"123", dob+name]
    filename = os.path.join(LOOT_DIR, f"{name}_wordlist.txt")
    
    with open(filename, "w") as f:
        for w in words: f.write(w + "\n")
    print(f"{GREEN}[+] Success! Wordlist saved in: {filename}{RESET}")

def imei_tracker():
    imei = input(f"{BLUE}Enter 15-digit IMEI: {RESET}").strip()
    if len(imei) == 15 and imei.isdigit():
        print(f"{GREEN}[+] Validated. Opening Global Tracking...{RESET}")
        webbrowser.open(f"https://www.imei.info/imei_check/{imei}")
    else:
        print(f"{RED}[!] Invalid IMEI.{RESET}")

def start_payload_server():
    PORT = 8080
    Handler = http.server.SimpleHTTPRequestHandler
    print(f"{GREEN}🚀 Server Active! URL: http://{get_local_ip()}:{PORT}{RESET}")
    print(f"{CYAN}Files available in '{LOOT_DIR}' will be hostable.{RESET}")
    print(f"{WHITE}Press Ctrl+C to stop.{RESET}")
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Server Offline.{RESET}")

def repair_system():
    print(f"{YELLOW}[*] Updating dependencies...{RESET}")
    os.system("sudo pip3 install requests sherlock-project --upgrade --break-system-packages")
    print(f"{GREEN}[+] Systems armed and ready.{RESET}")

# --- MAIN ENGINE ---
def main():
    vb = EthicalVirusBuilder()
    
    # Check for Sudo
    try:
        if os.getuid() != 0:
            print(f"{RED}[!] Run with sudo: sudo python3 brahmastra.py{RESET}")
            sys.exit()
    except AttributeError:
        pass # Not on Linux

    while True:
        banner()
        print(f"{WHITE}1. Digital Footprint (OSINT)")
        print("2. Google Dorks (Vulnerability)")
        print("3. IP Address Tracker (Geo-IP)")
        print(f"{GREEN}4. 🔥 ETHICAL VIRUS BUILDER (RATs){RESET}")
        print(f"{GREEN}5. 🚀 PAYLOAD SERVER (Delivery){RESET}")
        print("6. Wordlist Generator (Password Prep)")
        print("7. IMEI Forensic Tracker")
        print("8. Repair System")
        print(f"0. Exit{RESET}")
        
        choice = input(f"{BLUE}\nSelect Weapon > {RESET}")

        if choice == '1': digital_footprint()
        elif choice == '2': google_dorks()
        elif choice == '3': ip_tracker()
        elif choice == '4': vb.virus_menu()
        elif choice == '5': start_payload_server()
        elif choice == '6': wordlist_generator()
        elif choice == '7': imei_tracker()
        elif choice == '8': repair_system()
        elif choice == '0':
            print(f"\n{GREEN}Disarming... Goodbye.{RESET}")
            break
        
        input(f"\n{YELLOW}Press Enter to return...{RESET}")

if __name__ == "__main__":
    main()