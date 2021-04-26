# Decoratorler kodun okunabilirliğini arttırır.
# DRY (Dont repeat yourself) prensibinin uygulanmasını sağlar.

#  @decorator
#  def fonksiyon():
#      pass

# tüm işlemler tek tek yapılabilir lakin bir sayının
# (fark(ikikat)) değerini bulmak için 2 fonksiyonu da
# yazmak gerekir.

def fark(x):
    return x - 5

fark(10)

def ikikat(x):
    return x * 2

ikikat(5)

# iki fonksiyon yazılır.
fark(ikikat(4))

# Tümünü tek bir fonksiyon ile yazma işlemi decorator mantığı ile gerçekleşir.
# Parametre olarak fonksiyon alır. Decorators fonksiyonu farklı bir fonksiyon tarafından
# çağırıldığında ise decorators' da yazılan tüm işlevler çalışır.
def fark(func):
    print("Hi!") # print fonksiyonu decorators farklı bir fonksiyonda çağırıldığında da çalışır.
    return lambda x: func(x) - 5

@fark       # decorator çağırma
def ikikat(x):
    return x * 2

# Tek bir fonksiyon çağırılarak iki fonksiyon da çalıştırılmış olur.
# Önce iki katını sonra farkını alır. Print de çıktı verir.
ikikat(3)


# Hesap makinesi decorator fonksiyonu oluşturarak farklı bir
# fonksiyon içerisinde çalıştırmak

def hesap_makinesi(func):
    def islem(a,b,secenek):
        if secenek == "+":
            print(f"Toplam = {a+b}")
        elif secenek == "-":
            print(f"Fark = {a-b}")
        else:
            print("Tanımsız")
        func(a,b)
    return islem

@hesap_makinesi
def hesap(a,b):
    pass

hesap(4,2,"-")
hesap(3,1,"+")

# Higher order functions
# Argüman olarak fonksiyon alan fonksiyonlara denir.

def arttır(x):
    return x+1

def azalt(x):
    return x-1

def degistir(func,x):
    return func(x)

degistir(azalt,5)
degistir(arttır,5)
