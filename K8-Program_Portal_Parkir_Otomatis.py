# PROGRAM PORTAL PARKIR OTOMATIS
import time

#Deklarasi Awal 
platmobil = ["" for i in range(100)]  #Plat mobil
waktumasuk_mobil = ["" for i in range(100)]  #Waktu masuk mobil
platmotor = ["" for i in range(100)]  #Plat motor
waktumasuk_motor = ["" for i in range(100)]  #Waktu masuk motor
tanggalmasuk_mobil = ["" for i in range(100)] #Tanggal masuk mobil
tanggalmasuk_motor = ["" for i in range(100)] #Tanggal masuk motor
n = 0 #index kendaraan masuk
tarif = 0 #set tarif
portal = ""

#Gambar
mobil = """
                  _________________
              _.-'_____  _________ _`.
            .` ,'      ||         | `.`.
          .` ,'        ||         |   `.`.
        .`  /          ||         |  ,' ] `....___
      _`__.'''''''''''''''''''''''`''''''''|..___ `-.._
    .'                  [='                '     `'-.._`.
 ,:/.'''''''''''''''''''|''''''''''''''''''|'''''''''''\||'
  //||    _..._         |                  '    _..._  |)|
 /|//   ,',---.`.       |                  |  .',---.`.\>|
(':/   //' .-. `\\      \_________________/  '/' .-. `\\|_)
 `-...'||  '-'  ||________,,,,,,,,,,,,,,,__.'||  '-'  ||-'
       '.'.___.','                           '.'.___.','
      '-.m.-'                               '-.m.-'
"""
motor = """
                                    ,-~ |
       ________________          o==]___|
      |                |            \\
      |________________|            /\\
 __  /  _,-----._      )           |  \ \.
|_||/_-~         `.   /()          |  /|]_|_____
  |//              \ |              \/ /_-~     ~-_
  //________________||              / //___________\\
 //__|______________| \____________/ //___/-\ \~-_
((_________________/_-o___________/_//___/  /\,\  \\
 |__/(  ((====)o===--~~                 (  ( (o/)  )
      \  ``==' /                         \  `--'  /
       `-.__,-'      _______________      `-.__,-'
"""
portalmasuk = """
||==========||
||== P  M ==||
||== O  A ==||=======================
||== R  S ==||=======================
||== T  U ==||
||== A  K ==||
||== L    ==||
||==========||
"""
portalkeluar = """
||==========||
||== P  K ==||
||== O  E ==||============================
||== R  L ==||============================
||== T  U ==||
||== A  A ==||
||== L  R ==||
||==========||
"""

#Subprogram Masuk Parkir
def masuk(platmobil,waktumasuk_mobil,platmotor,waktumasuk_motor,tanggalmasuk_mobil,tanggalmasuk_motor): 
    #Jenis Kendaraan
    jenis = str(input("Apa jenis kendaraan Anda ('mobil' atau 'motor') ? "))
    while jenis not in ("mobil","motor","Mobil","Motor"):
        jenis = str(input("Apa jenis kendaraan Anda ('mobil' atau 'motor') ? "))
    if jenis == "Mobil":
        jenis = "mobil"
    elif jenis == "Motor":
        jenis = "motor"
    #Mengecek slot parkir kendaraan, kendaraan tidak dapat masuk jika parkiran penuh
    for i in range (100):
        if platmobil[i] == "" and jenis=="mobil":
            n=i
            break
        elif platmotor[i] == "" and jenis=="motor":
            n=i
            break
        elif i == 99 : #Tidak ditemukan index dengan data kosong pada array
            print("MAAF PARKIRAN PENUH. PARKIRLAH DI AREA PARKIR LAIN.")
            return platmobil,waktumasuk_mobil,platmotor,waktumasuk_motor,tanggalmasuk_mobil,tanggalmasuk_motor
        
    #Kendaraan menekan tombol
    print(portalmasuk)
    print("Selamat Datang. Silahkan tekan tombol tiket.\n")
    tombol = str(input("Tekan huruf 'O': "))
    while tombol not in ('O','o'):
        tombol = str(input("Tekan huruf 'O': "))

    #Sistem portal mengisi data kendaraan
    plat = str(input("Plat Kendaraan: "))
    tanggal = "DD/MM/YYYY"
    while (tanggal[0] + tanggal[1] + tanggal[3] + tanggal[4] + tanggal[6] + tanggal[7] + tanggal[8] + tanggal[9]).isdigit()!=True:  #Cek format input tanggal
        tanggal = str(input("Tanggal Masuk(DD/MM/YYYY): "))
        if len(tanggal) != 10:
            tanggal = "DD/MM/YYYY"
        elif tanggal[2] == "/" and tanggal[5] == "/":
            tanggal = tanggal
        else: 
            tanggal = "DD/MM/YYYY"
    if jenis == "mobil": 
        tanggalmasuk_mobil[n] = tanggal
    else: 
        tanggalmasuk_motor[n] = tanggal

    waktu="JJ.MM"
    while (waktu[0]+waktu[1]+waktu[3]+waktu[4]).isdigit()!=True:    #Cek format input waktu
        waktu = str(input("Waktu Masuk (JJ.MM): "))
        if len(waktu)==5 and waktu[2]=="." :
            waktu = waktu
        else : 
            waktu = "JJ.MM"

    #Print struk parkir
    spasi = ""
    spasi1 = ""
    spasi2 = ""
    for i in range (0,len("+ tanggal+str(spasi")-len(tanggal)+1):
        spasi += " "
    for i in range (0,len("+ plat+str(spasi1)+")-len(plat)+1):
        spasi1 += " "
    for i in range (0,len("+ waktu+str(spasi2)+")-len(waktu)):
        spasi2 += " "
    #Masukkan data parkir motor ke sistem dan print struk
    if jenis == "motor":
        platmotor[n] = plat
        waktumasuk_motor[n] = waktu
        print()
        print("  -----------------------------------------")
        print("|| UPT Parkir Institut Teknologi Bandung   ||")
        print("||    Jalan Ganesa no. 10, Bandung         ||")
        print("||                                         ||")
        print("||  ----------TIKET PARKIR----------       ||")
        print("||                                         ||")
        print("||  Tanggal          : "+ tanggal+str(spasi)+"||")
        print("||  Plat Kendaraan   : "+ plat+str(spasi1)+"||")
        print("||  Waktu Masuk      : "+ waktu+str(spasi2)+"||")
        print("||                                         ||")
        print("||    ----------------------------         ||")
        print("||  Tarif Utama      : Rp2.000             ||")
        print("||  Tarif Tambahan   : Rp1.000/Jam         ||")
        print("||  Denda            : Rp250.000           ||")
        print("||  Berlaku satu kali parkir               ||")
        print("||                                         ||")
        print("||            Terima Kasih                 ||")
        print("  ---------------------------------------\n")    
    #Masukkan data parkir mobil ke sistem dan print struk
    else: 
        platmobil[n]=plat
        waktumasuk_mobil[n]=waktu
        print()
        print("  -----------------------------------------")
        print("|| UPT Parkir Institut Teknologi Bandung   ||")
        print("||    Jalan Ganesa no. 10, Bandung         ||")
        print("||                                         ||")
        print("||  ----------TIKET PARKIR----------       ||")
        print("||                                         ||")
        print("||  Tanggal          : "+ tanggal+str(spasi)+"||")
        print("||  Plat Kendaraan   : "+ plat+str(spasi1)+"||")
        print("||  Waktu Masuk      : "+ waktu+str(spasi2)+"||")
        print("||                                         ||")
        print("||    ----------------------------         ||")
        print("||  Tarif Utama      : Rp5.000             ||")
        print("||  Tarif Tambahan   : Rp2.000/Jam         ||")
        print("||  Denda            : Rp250.000           ||")
        print("||  Berlaku satu kali parkir               ||")
        print("||                                         ||")
        print("||            Terima Kasih                 ||")
        print("  ---------------------------------------\n")

    #Buka portal
    print("🚗 Portal terbuka. Silakan Masuk.🚗\n")
    e = str(input("Tekan 'M' untuk masuk portal: "))
    while e not in ('M','m'):
        e = str(input("Tekan 'M' untuk masuk portal: \n"))
    if jenis == "mobil":
        print(mobil)
    else: 
        print(motor)
    time.sleep(1)
    print("=========Portal Ditutup=========")
    return platmobil,waktumasuk_mobil,platmotor,waktumasuk_motor,tanggalmasuk_mobil,tanggalmasuk_motor

#Subprogram Keluar Parkir
def keluar(platmobil,waktumasuk_mobil,platmotor,waktumasuk_motor,tanggalmasuk_mobil,tanggalmasuk_motor):
    print(portalkeluar)
    print("Silahkan scan tiket.")
    scan = str(input("\nTekan huruf 'S': "))
    while scan not in ('S','s'):
        scan = str(input("Tekan huruf 'S': "))
    #Input Data Kendaraan
    plat = str(input("Plat Kendaraan: "))
    jenis=""
    for i in range (100):
        if platmobil[i] == plat :      #Mencari indeks parkir mobil
            jenis="mobil"
            n=i
            break
        elif platmotor[i] == plat :     #Mencari indeks parkir motor
            jenis="motor"
            n=i
            break
        elif i == 99 :     #Tidak ditemukan plat pada kedua list
            print("\nKendaraan belum terdata")
            return platmobil,waktumasuk_mobil,platmotor,waktumasuk_motor,tanggalmasuk_mobil,tanggalmasuk_motor
        
    tanggal = "DD/MM/YYYY"
    while (tanggal[0] + tanggal[1] + tanggal[3] + tanggal[4] + tanggal[6] + tanggal[7] + tanggal[8] + tanggal[9]).isdigit()!=True:  #Cek format input tanggal
        tanggal = str(input("Tanggal Keluar(DD/MM/YYYY): "))
        if len(tanggal)!=10:
            tanggal = "DD/MM/YYYY"
        elif tanggal[2]=="/" and tanggal[5]=="/":
            tanggal = tanggal
        else: 
            tanggal ="DD/MM/YYYY"

    waktu = "JJ.MM"
    while (waktu[0]+waktu[1]+waktu[3]+waktu[4]).isdigit()!= True:    #Cek format input waktu
        waktu = str(input("Waktu Keluar (JJ.MM): "))
        if len(waktu) == 5 and waktu[2] == ".":
            waktu = waktu
        else: 
            waktu = "JJ.MM"

    if platmobil[n] == plat :  #menentukan tarif untuk mobil
        J   = waktumasuk_mobil[n][0]+waktumasuk_mobil[n][1]
        M   = waktumasuk_mobil[n][3]+waktumasuk_mobil[n][4]
        J2  = waktu[0]+waktu[1]
        M2  = waktu[3]+waktu[4]
        H   = tanggalmasuk_mobil[n]
        H2  = tanggal

        #Penentuan tarif
        if int(M2) <int (M):
            tarif=int(J2)-int(J)-1
        else: 
            tarif=int(J2)-int(J)
        harga = 5 + (2*tarif)
        #Jika melewati hari masuk, dikenakan denda
        if H !=H2:   #jika tanggal keluar berbeda dengan tanggal masuk maka dikenai denda
            harga = 250
        #Pemberitahuan tarif dan pembayaran
        print("Tarif parkir yang harus Anda bayarkan adalah Rp"+str(harga)+".000")
        bayar = str(input("\nMasukkan metode pembayaran: "))
        platmobil[n] = ""     # Clear data kendaraan keluar
        waktumasuk_mobil[n] = ""
        tanggalmasuk_mobil[n] = ""

    elif platmotor[n] == plat:  #menentukan tarif untuk motor
        J   = waktumasuk_motor[n][0]+waktumasuk_motor[n][1]
        M   = waktumasuk_motor[n][3]+waktumasuk_motor[n][4]
        J2  = waktu[0]+waktu[1]
        M2  = waktu[3]+waktu[4]
        H   = tanggalmasuk_motor[n]
        H2  = tanggal
        if int(M2) < int(M):
            tarif = int(J2)-int(J)-1
        else: 
            tarif = int(J2)-int(J)
        harga = 2 + (1*tarif)
        if H !=H2 :   #jika tanggal keluar berbeda dengan tanggal masuk maka dikenai denda
            harga = 250
        print("Tarif parkir yang harus Anda bayarkan adalah Rp"+str(harga)+".000")
        bayar = str(input("\nMasukkan metode pembayaran: "))
        platmotor[n] = ""     # Clear data kendaraan keluar
        waktumasuk_motor[n] = ""
        tanggalmasuk_motor[n] = ""
    #Buka portal
    print("\n🚗 Portal terbuka🚗\n")
    print("Terima kasih. Sampai jumpa lagi.")   
    e = str (input("\nTekan 'K' untuk keluar portal: "))
    while e not in ('K','k'):
        e = str(input("\nTekan 'K' untuk keluar portal: "))
    if jenis == "mobil": 
        print(mobil)
    else: 
        print(motor)
    time.sleep(1)
    print("=========Portal Ditutup=========")
    return platmobil,waktumasuk_mobil,platmotor,waktumasuk_motor,tanggalmasuk_mobil,tanggalmasuk_motor

#Program Utama
while True : #Looping program
    portal = str(input("\nApa kendaraan akan 'masuk' atau 'keluar'? "))
    if portal == "masuk":   #Subprogram masuk
        masuk(platmobil,waktumasuk_mobil,platmotor,waktumasuk_motor,tanggalmasuk_mobil,tanggalmasuk_motor)
    elif portal == "info":
        print(platmobil)
        print(platmotor)
    elif portal == "keluar":  #Subprogram keluar
        keluar(platmobil,waktumasuk_mobil,platmotor,waktumasuk_motor,tanggalmasuk_mobil,tanggalmasuk_motor)
    elif portal != "stop":
        print("Tolong masukkan input yang benar !!!")
    else :    #Stop looping
        print("Operasi Portal Dimatikan")
        break
