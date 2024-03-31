import requests

def query_ip():
    ip = input("IP adresini girin: ")
    if not ip:
        print("Geçersiz IP adresi!")
        return
    
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        
        if data["status"] == "fail":
            print("IP sorgusu başarısız oldu.")
        else:
            print(f"""
                IP Adresi: {data["query"]}
                Ülke: {data["country"]}
                Şehir: {data["city"]}
                Konum: {data["lat"]}, {data["lon"]}
                ISP: {data["isp"]}
            """)
    except Exception as e:
        print("Bir hata oluştu:", e)

print("\033[91m" + "İP CHECK")
query_ip()

print("\nMade By Veraildez")
print("Instagram: veraildez_v33")
print("İP CHECK")
