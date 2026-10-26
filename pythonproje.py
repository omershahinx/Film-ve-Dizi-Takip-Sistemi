def film_dizi_sistemi():
    yapimlar = []

    while True:
        print("\n FILM VE DIZI TAKIP SISTEMI ")
        print("1 - Yeni film/dizi ekle")
        print("2 - Tum yapimlari listele")
        print("3 - Film/dizi ara")
        print("4 - Izleme durumunu guncelle")
        print("5 - Film/dizi sil")
        print("6 - Istatistikleri goster")
        print("0 - Programdan cik")

        secim = input("Seciminiz: ").strip()

        if secim == "0":
            print("Programdan cikiliyor.")
            break

        elif secim == "1":
            ad = input("Film/dizi adi: ").strip()

            if ad == "":
                print("Yapim adi bos birakilamaz.")
                continue

            if any(y["ad"].lower() == ad.lower() for y in yapimlar):
                print("Bu yapim zaten kayitli.")
                continue

            kategori = input("Film mi, dizi mi? ").strip().lower()

            if kategori not in ["film", "dizi"]:
                print("Lutfen film veya dizi yazin.")
                continue

            tur = input("Turu (Komedi, Aksiyon, Dram vb.): ").strip()

            durum = input("Izlendi mi? (evet/hayir): ").strip().lower()

            if durum not in ["evet", "hayir"]:
                print("Lutfen evet veya hayir yazin.")
                continue

            yapim = {
                "ad": ad,
                "kategori": kategori,
                "tur": tur,
                "durum": durum
            }

            yapimlar.append(yapim)
            print("Yapim basariyla eklendi.")

        elif secim == "2":
            if not yapimlar:
                print("Henuz kayitli yapim yok.")
            else:
                print("\n--- KAYITLI YAPIMLAR ---")

                for sira, yapim in enumerate(yapimlar, 1):
                    print(
                        f"{sira}. {yapim['ad']} | "
                        f"Kategori: {yapim['kategori']} | "
                        f"Tur: {yapim['tur']} | "
                        f"Izlendi: {yapim['durum']}"
                    )

        elif secim == "3":
            aranan = input("Aranacak film/dizi adi: ").strip().lower()

            bulunanlar = [
                y for y in yapimlar
                if aranan in y["ad"].lower()
            ]

            if bulunanlar:
                print("\n--- ARAMA SONUCLARI ---")

                for yapim in bulunanlar:
                    print(
                        f"{yapim['ad']} | "
                        f"{yapim['kategori']} | "
                        f"{yapim['tur']} | "
                        f"Izlendi: {yapim['durum']}"
                    )
            else:
                print("Aranan yapim bulunamadi.")

        elif secim == "4":
            ad = input("Durumunu guncellemek istedigin yapim: ").strip().lower()

            bulunan = None

            for yapim in yapimlar:
                if yapim["ad"].lower() == ad:
                    bulunan = yapim
                    break

            if bulunan is None:
                print("Yapim bulunamadi.")
            else:
                print("Mevcut durum:", bulunan["durum"])
                yeni_durum = input("Yeni durum (evet/hayir): ").strip().lower()

                if yeni_durum in ["evet", "hayir"]:
                    bulunan["durum"] = yeni_durum
                    print("Izleme durumu guncellendi.")
                else:
                    print("Gecersiz durum girdiniz.")

        elif secim == "5":
            ad = input("Silmek istedigin yapim: ").strip().lower()

            bulunan = None

            for yapim in yapimlar:
                if yapim["ad"].lower() == ad:
                    bulunan = yapim
                    break

            if bulunan is None:
                print("Yapim bulunamadi.")
            else:
                yapimlar.remove(bulunan)
                print("Yapim basariyla silindi.")

        elif secim == "6":
            toplam = len(yapimlar)
            izlenen = 0
            bekleyen = 0
            film_sayisi = 0
            dizi_sayisi = 0

            for yapim in yapimlar:
                if yapim["durum"] == "evet":
                    izlenen += 1
                else:
                    bekleyen += 1

                if yapim["kategori"] == "film":
                    film_sayisi += 1
                else:
                    dizi_sayisi += 1

            print("\n--- ISTATISTIKLER ---")
            print("Toplam yapim:", toplam)
            print("Izlenen yapim:", izlenen)
            print("Izlenecek yapim:", bekleyen)
            print("Film sayisi:", film_sayisi)
            print("Dizi sayisi:", dizi_sayisi)

        else:
            print("Gecersiz secim. Tekrar deneyin.")


if __name__ == "__main__":
    film_dizi_sistemi()






