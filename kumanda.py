import random
import time 
class Kumanda(): 
    def __init__(self, tv_durum = "Kapalı", tv_ses = 0, kanal_listesi = ["TRT","SHOW TV"], kanal = "TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi 
        self.kanal = kanal 
    def tv_ac(self): 
        if(self.tv_durum == "Açık"):
            print("TV zaten açık")
        else:
            print("TV açılıyor")
            self.tv_durum = "Açık"
    def tv_kapat(self): 
        if(self.tv_durum == "Kapalı"):
            print("TV zaten kapalı")
        else: 
            print("Tv kapanıyor")
            self.tv_durum = "Kapalı"
    def ses_ayarlari(self): 
        while True:
            cevap = input("Sesi azalt: '<' \nSesi artır: '>'\nÇıkış: çıkış" )
            if (cevap == '<'): 
                self.tv_ses -= 1 
                print("Ses",self.tv_ses)
            elif(cevap == '>'): 
                if(self.tv_ses != 31):
                    self.tv_ses +1
                    print("Ses: ", self.tv_ses)
            else:
                print("Ses güncellendi: ", self.tv_ses)
                break
    def kanal_ekle(self, kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(3)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanale eklendi....")
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi) - 1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu an ki Kanal: ", self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "TV Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\n Şu anki kanal: {}\n".format(self.tv_durum, self.tv_ses, self.kanal_listesi,self.kanal)
    def kanal_sil(self, kanal_ismi):
        if kanal_ismi in self.kanal_listesi:
            self.kanal_listesi.remove(kanal_ismi)
            print("{} kanalı silindi.".format(kanal_ismi))
        else:
            print("{} kanalı bulunamadı.".format(kanal_ismi))
    
    def __del__(self): 
        print("Kanal siliniyor...")
        time.sleep(3)
    def kanala_git(self, kanal_ismi):
        if kanal_ismi in self.kanal_listesi:
            self.kanal = kanal_ismi
            print("Şu anki Kanal: ", self.kanal)
        else:
            print(f"{kanal_ismi} kanalı bulunamadı.")

kumanda = Kumanda()
print("""
      
Televizyon uygulaması
      
1. TV Aç
      
2. TV Kapat
      
3. Ses Ayarları 
      
4. Kanal Ekle
      
5. Kanal Sayısını Öğrenme
      
6. Rastgele Kanal Geçme
      
7. TV bilgileri
    
8. Kanal sil
      
9. Gitmek istediğiniz kanalı seçiniz
      
Çıkmak için 'q' basınız.
       
""")

while True:
    islem = input("İşleminzi Seçiniz: ")
    if (islem == 'q'): 
        print("Program Sonlandırılıyor...")
        break
    elif (islem == "1"):
        kumanda.tv_ac()
    elif(islem == "2"): 
        kumanda.tv_kapat()
    elif(islem == "3"):
        kumanda.ses_ayarlari()
    elif(islem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak giriniz")
        kanal_isimleri = kanal_isimleri.split(',')
        for eklenenecekler in kanal_isimleri: 
            kumanda.kanal_ekle(eklenenecekler)     
    elif(islem == "5"):
        print ("Kanal Sayısı: ", len(kumanda))
    elif (islem == "6"):
        kumanda.rastgele_kanal() 
    elif (islem == "7"):
        print(kumanda)
    elif (islem == "8"):
        kanal_ismi = input("Silmek istediğiniz kanalı giriniz: ")
        kumanda.kanal_sil(kanal_ismi)
    elif(islem == "9"):
        kanal_ismi = input("Gitmek istediğimiz kanalı giriniz: ")
        kumanda.kanala_git(kanal_ismi)

    else:
        print("Geçersiz işlem...")