# nilai = int(input("masukkan nilai: "))

# if (nilai > 90 and nilai <= 100):
#     print("selamat anda lulus, dengan nilai yang memuaskan")
# elif (nilai > 80):
#     print("selamat anda lulus")
# elif (nilai > 70):
#     print("lulus tapi pinggir jurang")
# else:
#     print("anda masih belum lulus tes, semangat dan coba lagi")

#for loop
# for i in range (2, 10, 1):
#     print(i)

# angka = 30

# while (angka > 1):
#     print(angka)
#     angka -= 1

#function
def Sayhello():
    print("hello world")

Sayhello()
Sayhello()

def Sayhello(param_nama):
     print(f"hello {param_nama}")
   

fungsi_kurang4 = lambda param_angka : param_angka - 4
angka = 10
print(fungsi_kurang4(angka))