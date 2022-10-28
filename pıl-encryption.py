import numpy as np
from PIL import Image

def Encode(src, message, dest):

    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    totalPik = array.size//n
        
    message += "$t3g0"
    b_message = ''.join([format(ord(i), "08b") for i in message])
    reqPik = len(b_message)

    if reqPik > totalPik:
        print("HATA: Daha Büyük Boyutlu Bir Dosya Kullanın")

    else:
        index=0
        for p in range(totalPik):
            for q in range (0,3):
                if index < reqPik:
                    array [p] [q] = int(bin(array [p] [q]) [2:9] +b_message[index], 2)
                    index += 1

    array=array.reshape(height, width, n)
    enc_img = Image.fromarray(array.astype('uint8'),img.mode)
    enc_img.save(dest)
    print("Görsel Şifreleme Tamamlandı")

def Decode(src):

    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if "$t3g0" in message:
        print("Görsel İçerisine Gizlenmiş Mesaj:", message[:-5])
    else:
        print("Gizli Bir Mesaj Bulunamadı")
            
def Stego():
    print("--$t3g0'a Hoşgeldiniz")
    print("1: Encode")
    print("2: Decode")
    
    func = input()
    
    if func == '1':
        print("Resmin Kaynak Dizinin Giriniz:")
        src = input()
        print("Gizlemek İstediğiniz Mesajı Giriniz:")
        message = input()
        print("Çıktı Görsel Nereye Kaydedilsin:")
        
        dest =input()
        print("Encoding...")
        Encode(src, message, dest)
        
    elif func == '2':
        print("Şifrelemesi Çözülecek Resmin Kaynak Dizinin Giriniz")
        src = input()
        print("Decoding...")
        Decode(src)
        
    else:
        print("HATA1: Geçersiz Opsiyon Seçildi")
        
Stego()