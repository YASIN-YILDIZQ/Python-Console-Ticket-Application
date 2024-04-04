import datetime

class BiletAlimUygulamasi:
    def __init__(self):
        self.koltuklar = [i for i in range(1, 23)]
        self.secilen_koltuklar = []
        self.ad = ""
        self.soyad = ""
        self.kalkis_yeri = ""
        self.varis_yeri = ""
        self.tarih = ""
        self.saat = ""
        self.kart_bilgileri = {}

    def koltuk_goster(self):
        print("Mevcut Koltuklar:", self.koltuklar)

    def koltuk_sec(self):
        while True:
            secilen_koltuklar = input("Lütfen koltuk numaralarını virgülle ayırarak girin (örn. 1,3,5): ")
            secilen_koltuklar_list = [int(koltuk) for koltuk in secilen_koltuklar.split(",") if koltuk.strip().isdigit()]

            if not secilen_koltuklar_list:
                print("Geçersiz koltuk numarası. Lütfen sayısal değerler girin.")
                continue

            secilen_koltuklar_set = set(secilen_koltuklar_list)

            invalid_koltuklar = secilen_koltuklar_set - set(self.koltuklar)
            if invalid_koltuklar:
                print(f"Geçersiz koltuk numaraları: {', '.join(map(str, invalid_koltuklar))}")
                continue

            self.koltuklar = list(set(self.koltuklar) - secilen_koltuklar_set)
            self.secilen_koltuklar.extend(secilen_koltuklar_list)
            print("Seçilen koltuklar:", self.secilen_koltuklar)
            return True

    def kalkis_varis_tarih_saat(self):
        self.kalkis_yeri = input("Kalkış Yeri: ")
        self.varis_yeri = input("Varış Yeri: ")
        self.tarih = input("Tarih (YYYY-MM-DD): ")
        self.saat = input("Saat (HH:MM): ")

    def odeme_ekrani(self):
        print("\nÖdeme Ekranı")
        self.kisi_bilgileri_gir()
        self.kart_bilgileri_gir()

    def kisi_bilgileri_gir(self):
        while True:
            self.ad = input("Adınız: ")
            if not self.ad.strip():
                print("Lütfen geçerli bir ad girin.")
            else:
                break

        while True:
            self.soyad = input("Soyadınız: ")
            if not self.soyad.strip():
                print("Lütfen geçerli bir soyad girin.")
            else:
                break

    def kart_bilgileri_gir(self):
        print("Kart Bilgilerinizi Girin:")
        while True:
            kart_numarasi = input("Kart Numarası: ")
            if not kart_numarasi.isdigit():
                print("Kart numarası sadece rakamlardan oluşmalıdır.")
            else:
                self.kart_bilgileri['kart_numarasi'] = kart_numarasi
                break

        while True:
            son_kullanim_tarihi = input("Son Kullanma Tarihi (MM/YY): ")
            if not son_kullanim_tarihi.count("/") == 1 or not son_kullanim_tarihi.replace("/", "").isdigit():
                print("Geçersiz son kullanma tarihi formatı. Lütfen MM/YY formatında girin.")
            else:
                self.kart_bilgileri['son_kullanim_tarihi'] = son_kullanim_tarihi
                break

        while True:
            guvenlik_kodu = input("Güvenlik Kodu: ")
            if not guvenlik_kodu.isdigit():
                print("Güvenlik kodu sadece rakamlardan oluşmalıdır.")
            else:
                self.kart_bilgileri['guvenlik_kodu'] = guvenlik_kodu
                break

    def bilgileri_goster(self):
        print("\nBilet Bilgileri")
        print("Ad:", self.ad)
        print("Soyad:", self.soyad)
        print("Kalkış Yeri:", self.kalkis_yeri)
        print("Varış Yeri:", self.varis_yeri)
        print("Tarih:", self.tarih)
        print("Saat:", self.saat)
        print("Seçilen Koltuklar:", self.secilen_koltuklar)
        print("Sistem Saati:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def bilet_al(self):
        while self.koltuklar:
            self.koltuk_goster()
            while not self.koltuk_sec():
                pass
            self.kalkis_varis_tarih_saat()
            self.odeme_ekrani()
            self.bilgileri_goster()
            print("\n\nYeni bir bilet alabilirsiniz.\n")

if __name__ == "__main__":
    bilet_alim = BiletAlimUygulamasi()
    bilet_alim.bilet_al()
    print("Bilet alımı tamamlandı. Teşekkür ederiz!")
