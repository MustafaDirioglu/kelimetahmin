import random

sonliste2,kelliste= [],[]                                               #Boş listeleri oluşturuyoruz

try:
    dosya  = open("kelimetahmin.txt")                                   #Verileri çekeceğimiz dosyayı tanımlıyoruz.                      
    dosya  = dosya.readlines()                                          #readlines() dosyadaki her satırı liste öğesine dönüştürür.
except:
    print("Veri dosyayası bulunamadı.")                                 #Dosya bulunmaz  ise programı kapatmak içindir hataları ayıklamak için de try ve except kulanırız.
    exit()

hsayı = int(input("Tahmin ettiğiniz kelime kaç harften oluşmaktadır:")) #Kelimenin basamak sayısını öğrenmek için kulanıcıdan giriş alıyoruz.

for kelime in dosya:                                                    #Bu işlemlerde kulanıcın tahmin basamağına göre  sonliste ye yazıyoruz.
    kelime = (''.join(x for x in kelime if x not in ['\n']))
    for c in kelime:
        listee = kelime
        ksayı=len(listee)
        
    if ksayı== hsayı:     
        kelliste.append(kelime) 
        sonliste =list(kelliste) 

def ekleme(k):                                                          #İşlem sonunda kulanıcının yeni veri ekleyebilmesini sağlıyoruz
    with open("kelimetahmin.txt", "a") as f:
        f.write(f"{k}\n")

basamak = list(range(hsayı))
a = 0
while True:
    
    say = random.choice(basamak)
    basamak.remove(say)
    l= str(input(f"{say + 1}. Basamaktaki harf nedir:"))                #Kulanıcıdan rastgele basamakdaki harfi istyerek "l" değişkenine yazıyoruz.

    if a>=1 :                           
        sonliste =list(sonliste2)                                       
        sonliste2.clear() 
    a+=1
   
    for z in sonliste:                                                  #"l" ile gelen harfi ve sırasını "sonlist" deki tüm kelimlerdeki harf sırasına göre karşılaştırıyoruz    
        if z[say] == l:
            sonliste2.append(z) 
    
    #print(sonliste2)
    
    if len(sonliste2) == 1:
        print("Buldum sanırım",sonliste2[0],"olabilir mi ?")
        print("Eğer yanlış ise bana doğru olanı söylersen  birdahakine doğru olanı bulabilirim")
        ekleme(input())
        break
                                                                        #Eğer bir seçenek kaldıysa seçeneği yazdırıyoruz veya seçenek yoksa kulanıcıya bunu bildiriyoruz ve 24.satırdaki fonksyona gönderiyoruz 
    if len(sonliste2) == 0:
        print("Gerçekten zor bir tahminmiş üzgünüm ki bulamadım")
        print("Eğer bana tahminini söylersen bidahaki sefere bulacağıma eminim")
        ekleme(input())
        break

    




        
   
    