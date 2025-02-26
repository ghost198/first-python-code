
print("Bayar utang Brokkk")

while True:
  bayar = input(f"mau bayar utang? (y/n) ")
  if bayar == "n":
    print("bayar dong bosku")
    break

    uang = input("Ada berapa uang kamu ")
    utang = 10000

if int(uang) < utang:
    print("maaf boss uang kamu kurang")
elif int(uang) == utang:
    input("uang kamu cukup nih, yakin mau bayar (y/n)")
else:
    print("uang nya kelebihan")