import socket

def get_ip_address(url):
    ip_address = socket.gethostbyname(url)
    return ip_address

def print_title():
    print("\033[1m  ______           _              __        __   _")
    print(" |__  (_)_ __   __| | __ _ _ __   \ \      / /__| |__")
    print("   / /| | '_ \ / _` |/ _` | '_ \   \ \ /\ / / _ \ '_ \ ")
    print("  / /_| | | | | (_| | (_| | | | |   \ V  V /  __/ |_) |")
    print(" /____|_|_| |_|\__,_|\__,_|_| |_|    \_/\_/ \___|_.__/ \n")

def print_yellow(text):
    print("\033[93m" + text)

def main_menu():
    print_title()
    print_yellow("1- IP adresini bul")

    choice = input("\nHangi seçeneği kullanmak istersiniz (1): ")
    if choice == "1":
        website_url = input("\nIP adresini bulmak istediğiniz web sitesinin URL'sini girin: ")
        ip_address = get_ip_address(website_url)
        print_yellow("\nGirdiğiniz web sitesinin IP adresi: " + ip_address)
    else:
        print_red("\nGeçersiz seçenek! Lütfen 1'i seçin.")

main_menu()
print("clear")
