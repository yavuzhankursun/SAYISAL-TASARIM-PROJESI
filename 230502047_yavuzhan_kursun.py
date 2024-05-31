import tkinter as tk
from tkinter import messagebox


class MantikKapi:
    def __init__(self, canvas, x, y, kapi_turu):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.kapi_turu = kapi_turu
        self.girdi_a = None
        self.girdi_b = None
        self.cikti = None
        self.ciz_kapi()

    def ciz_kapi(self):
        if self.kapi_turu == "NOT":
            self.canvas.create_polygon(
                self.x,
                self.y,
                self.x + 30,
                self.y + 15,
                self.x,
                self.y + 30,
                fill="blue",
            )
            self.canvas.create_oval(
                self.x + 30, self.y + 10, self.x + 35, self.y + 20, fill="blue"
            )
        elif self.kapi_turu == "BUFFER":
            self.canvas.create_polygon(
                self.x,
                self.y,
                self.x + 30,
                self.y + 15,
                self.x,
                self.y + 30,
                fill="cyan",
            )
        elif self.kapi_turu == "AND":
            self.canvas.create_rectangle(
                self.x, self.y, self.x + 20, self.y + 30, fill="green"
            )
            self.canvas.create_arc(
                self.x + 10,
                self.y,
                self.x + 30,
                self.y + 30,
                start=270,
                extent=180,
                style=tk.ARC,
                fill="green",
            )
        elif self.kapi_turu == "OR":
            self.canvas.create_arc(
                self.x - 10,
                self.y,
                self.x + 20,
                self.y + 30,
                start=270,
                extent=180,
                style=tk.ARC,
                fill="yellow",
            )
            self.canvas.create_arc(
                self.x,
                self.y,
                self.x + 30,
                self.y + 30,
                start=270,
                extent=180,
                style=tk.ARC,
                fill="yellow",
            )
        elif self.kapi_turu == "NAND":
            self.ciz_kapi("AND")
            self.canvas.create_oval(
                self.x + 30, self.y + 10, self.x + 35, self.y + 20, fill="green"
            )
        elif self.kapi_turu == "NOR":
            self.ciz_kapi("OR")
            self.canvas.create_oval(
                self.x + 30, self.y + 10, self.x + 35, self.y + 20, fill="yellow"
            )
        elif self.kapi_turu == "XOR":
            self.ciz_kapi("OR")
            self.canvas.create_arc(
                self.x - 20,
                self.y,
                self.x + 10,
                self.y + 30,
                start=270,
                extent=180,
                style=tk.ARC,
                fill="red",
            )
        elif self.kapi_turu == "XNOR":
            self.ciz_kapi("XOR")
            self.canvas.create_oval(
                self.x + 30, self.y + 10, self.x + 35, self.y + 20, fill="red"
            )

    def cikti_hesapla(self):
        if self.kapi_turu == "NOT":
            self.cikti = not self.girdi_a
        elif self.kapi_turu == "BUFFER":
            self.cikti = self.girdi_a
        elif self.kapi_turu == "AND":
            self.cikti = self.girdi_a and self.girdi_b
        elif self.kapi_turu == "OR":
            self.cikti = self.girdi_a or self.girdi_b
        elif self.kapi_turu == "NAND":
            self.cikti = not (self.girdi_a and self.girdi_b)
        elif self.kapi_turu == "NOR":
            self.cikti = not (self.girdi_a or self.girdi_b)
        elif self.kapi_turu == "XOR":
            self.cikti = self.girdi_a != self.girdi_b
        elif self.kapi_turu == "XNOR":
            self.cikti = self.girdi_a == self.girdi_b
        return self.cikti


class GirisKutusu:
    def __init__(self, canvas, x, y, deger=0):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.deger = deger
        self.rect = self.canvas.create_rectangle(
            self.x, self.y, self.x + 30, self.y + 30, fill="green"
        )
        self.text = self.canvas.create_text(
            self.x + 15, self.y + 15, text=str(self.deger)
        )

    def degeri_ayarla(self, deger):
        self.deger = deger
        self.canvas.itemconfig(self.text, text=str(self.deger))


class CikisKutusu:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.rect = self.canvas.create_rectangle(
            self.x, self.y, self.x + 30, self.y + 30, fill="red"
        )
        self.text = self.canvas.create_text(self.x + 15, self.y + 15, text="")

    # Çıktı değerini hesaplayqbilmek için
    def degeri_ayarla(self, deger):
        self.canvas.itemconfig(self.text, text=str(int(deger)))


# LED sınıfı
class Led:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.durum = False
        # LED'i çiz
        self.oval = self.canvas.create_oval(
            self.x, self.y, self.x + 30, self.y + 30, fill="grey"
        )

    def durumu_ayarla(self, durum):
        self.durum = durum
        self.canvas.itemconfig(self.oval, fill="yellow" if self.durum else "grey")


class DevreSimulatoru:
    def __init__(self, root):
        self.root = root
        self.root.title("Sayısal Tasarım Projesi")
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack()
        self.bilesenler = []
        self.sonraki_x = 100
        self.sonraki_y = 100
        self.arayuz_olustur()

    def arayuz_olustur(self):
        buton_kutusu = tk.Frame(self.root)
        buton_kutusu.pack()
        butonlar = [
            ("NOT Kapısı", "NOT"),
            ("Buffer", "BUFFER"),
            ("VE Kapısı", "AND"),
            ("VEYA Kapısı", "OR"),
            ("NAND Kapısı", "NAND"),
            ("NOR Kapısı", "NOR"),
            ("XOR Kapısı", "XOR"),
            ("XNOR Kapısı", "XNOR"),
            ("Giriş Kutusu: 0", "GIRIS_0"),
            ("Giriş Kutusu: 1", "GIRIS_1"),
            ("Çıkış Kutusu", "CIKIS"),
            ("LED", "LED"),
            ("Çalıştır", self.simulasyon_calistir),
            ("Reset", self.simulasyon_resetle),
            ("Durdur", self.simulasyon_durdur),
        ]

        # Butonları ekrandaki görünen alana eklemek için
        for yazi, komut in butonlar:
            if callable(komut):
                self.buton_olustur(buton_kutusu, yazi, komut)
            else:
                self.buton_olustur(
                    buton_kutusu, yazi, lambda tur=komut: self.bilesen_ekle(tur)
                )

    def buton_olustur(self, kutu, yazi, komut):
        buton = tk.Button(kutu, text=yazi, command=komut)
        buton.pack(side=tk.LEFT)

    def bilesen_ekle(self, bilesen_turu):
        if bilesen_turu in ["NOT", "BUFFER", "AND", "OR", "NAND", "NOR", "XOR", "XNOR"]:
            bilesen = MantikKapi(
                self.canvas, self.sonraki_x, self.sonraki_y, bilesen_turu
            )
        elif bilesen_turu == "GIRIS_0":
            bilesen = GirisKutusu(self.canvas, self.sonraki_x, self.sonraki_y, deger=0)
        elif bilesen_turu == "GIRIS_1":
            bilesen = GirisKutusu(self.canvas, self.sonraki_x, self.sonraki_y, deger=1)
        elif bilesen_turu == "CIKIS":
            bilesen = CikisKutusu(self.canvas, self.sonraki_x, self.sonraki_y)
        elif bilesen_turu == "LED":
            bilesen = Led(self.canvas, self.sonraki_x, self.sonraki_y)
        self.bilesenler.append(bilesen)
        self.koordinatlari_guncelle()

    # Yeni eklenenlerin üstüste binmesini engellemek için
    def koordinatlari_guncelle(self):
        self.sonraki_x += 50
        if self.sonraki_x > 750:
            self.sonraki_x = 100
            self.sonraki_y += 50
        if self.sonraki_y > 550:
            self.sonraki_y = 100

    def simulasyon_calistir(self):
        for bilesen in self.bilesenler:
            if isinstance(bilesen, MantikKapi):

                # Mantık kapılarının giriş değerleri
                bilesen.girdi_a = 1 if bilesen.girdi_a is None else bilesen.girdi_a
                bilesen.girdi_b = 0 if bilesen.girdi_b is None else bilesen.girdi_b
                bilesen.cikti_hesapla()
            elif isinstance(bilesen, CikisKutusu):
                bilesen.degeri_ayarla(1)
            elif isinstance(bilesen, Led):
                bilesen.durumu_ayarla(True)
        messagebox.showinfo("Simülasyon", "Simülasyon tamamlandı.")

    def simulasyon_resetle(self):
        self.canvas.delete("all")
        self.bilesenler = []
        self.sonraki_x = 100
        self.sonraki_y = 100

    def simulasyon_durdur(self):
        messagebox.showinfo("Simülasyon", "Simülasyon durduruldu.")


if __name__ == "__main__":
    root = tk.Tk()
    app = DevreSimulatoru(root)
    root.mainloop()
