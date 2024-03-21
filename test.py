hangiAy= input("Hangi aydayız? ")
aylar=["ocak", "şubat","mart","nisan","mayıs"]
match hangiAy:
  case"1":
    print(aylar[0])
  case"2":
    print(aylar[1])
  case"3":
    print(aylar[2])
  case"4":
    print(aylar[3])
  case"5":
    print(aylar[4])
  case _:
    print("böyle bir ay bulunamamaktadır.")

    islem = input("işlem tipini giriniz: \n toplama icin 1 \n uslu sayı icin 2 \n carpma icin 3 \n bolme icin 4\n")

match islem:
  case "1":
    sayi1=int(input("1. sayıyı giriniz"))
    sayi2=int(input("2. sayıyı giriniz"))
    print("cevabınız",sayi1+sayi2)
  case "2":
    sayi1=int(input("kuvvetini almak istediginiz sayiyi giriniz"))
    sayi2=int(input("kacinci kuvvetini alacagınızı giriniz"))
    print(sayi1**sayi2)
  case "3":
    print(sayi1*sayi2)
  case "4":
    print(sayi1/sayi2)
  case _:
    print("gecersiz bir islem girdiniz. lütfen yukarıda bahsedildigi gibi bir secim yapınız")
  