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