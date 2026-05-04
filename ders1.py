print("Merhaba Ben Yaren")
isim = "Yaren"
yas = 111111
universite = "Çanakkale Onsekiz Mart"

print("Adım:" , isim)
print("yaşım:",yas)
print("okuduğum üniversite:",universite)
    
    #şimdi ise değişkenlerin türlerini gösteren bir kodd yazalım.

isim="Yaren"
yas=19
boy=1.65
universiteli_mi= True

print(type(isim))
print(type(yas))
print(type(boy))
print(type(universiteli_mi))

#adın,soyadın,yaşın,okuduğun bölüm ve kaçıncı sınıf olduğunu ekrana yazdıran bir kod yaz

isim="Yaren"
soyisim="xxxxx"
yas=11111
bolum="Bilgisayar_muhendisligi"
sinif="1. sınıf"

print("Adım:",isim)
print("Soyadım:",soyisim)
print("Yaş:",yas)
print("Okuduğum bölüm:",bolum)
print("sınıf:",sinif)

#kullanıcıdan veri almak için kod yazınız

isim= input("Adın ne?")
print("merhaba,",isim)

#input() kullanarak kullanıcıdan isim, yaş ve şehir alan, sonra hepsini güzel bir cümleyle yazdıran bir kod yaz.
isim= "Yaren"
yas=11111
sehir="Çanakkale"

print(f"Merhaba ben {isim}.{sehir}'de yaşıyorum ve {yas} yaşındayım")

# iki sayı alan ve bu iki sayının toplamını ekrana yazdıran kodu yazınız

a =5
b =8
toplam =a+b

print("ilk sayıyı giriniz:",a)
print("ikinci sayıyı giriniz:",b)
print(f"İki sayının toplamı {a}+{b}={toplam}") 

#kullanıcıdan iki sayı alan ve toplamını ekrana yazdıran kodu giriniz.

a=int(input("ilk sayıyı giriniz:"))
b=int(input("ikinci sayıyı giriniz:"))
toplam=a+b

print(f"{a}+{b}={toplam}")
