balance = 10

def pembayaran():
    print("Pilih Pembayaran")
    print("""
        1. Balance
        2. Dana
        3. Ovo
        """)
    pilihan = int(input())
    
    if pilihan == 1:
        print("Pesanan Telah diterima, mohon tunggu informasi paket lewat SMS Anda")
    elif pilihan == 2:
        nomor_dana = int(input("Masukkan nomor Dana Anda:"))
        print("Permintaan anda telah di terima, mohon tunggu dari SMS anda untuk melanjutkan pembelian lewat DANA")
    elif pilihan == 3:
        nomor_ovo = int(input("Masukkan nomor Ovo Anda:"))
        print("Permintaan anda telah di terima, mohon tunggu dari SMS anda untuk melanjutkan pembelian lewat OVO")
    else:
        print("Pilihan tidak valid")

def beli_pulsa():
    global balance

    beli = int(input("Masukkan nomor:"))
    harga = float(input("Beli berapa?: Rp"))

    print("Pilih Pembayaran")
    print("""
        1. Dana
        2. Ovo
    """)
    pilihan = int(input())
    
    if pilihan == 1:
        nomor_dana = int(input("Masukkan nomor Dana Anda:"))
        print("Permintaan anda telah di terima, mohon tunggu dari SMS anda untuk melanjutkan pembelian lewat DANA")
    elif pilihan == 2:
        nomor_ovo = int(input("Masukkan nomor Ovo Anda:"))
        print("Permintaan anda telah di terima, mohon tunggu dari SMS anda untuk melanjutkan pembelian lewat OVO")
    else:
        print("Pilihan tidak valid")

    balance += harga

    print(f"Pembelian pulsa ke nomor {beli} sebesar {harga} telah masuk ke akun anda, total pulsa anda sekarang adalah {balance}")

def cek_pulsa():
    global balance
    print("Pulsa anda saat ini adalah: Rp", balance)
    print("Ingin beli pulsa? (y/t):")
    pilihan = input().lower()

    if pilihan == "y":
        beli_pulsa()
    elif pilihan == "t":
        print("Terima kasih telah menggunakan layanan kami")
    else:
        print("Menu tidak valid")

    print("Ingin membeli kuota? (y/t)")
    lanjut = input()

    if lanjut.lower() == "y":
        menu_utama()
    elif lanjut.lower() == "t":
        print("Terima kasih telah menggunakan layanan kami")
    else:
        print("Menu tidak valid")

def info():
    print("""
        1. Cek Pulsa
        2. Beli Pulsa
          """)
    pilihan = input()

    if pilihan == "1":
        cek_pulsa()
    elif pilihan == "2":
        beli_pulsa()
    else:
        print("Pilihan tidak valid")

def uh():
    global balance

    print("""
    1. Unlimited Harian 9rb 1gb/1 hari (1gb/hari)
    2. Unlimited Harian 27k 7gb/7 hari (1gb/hari)
    3. Unlimited Harian 48k 14gb/14 hari (1gb/hari)
    4. Unlimited Harian 70k 20gb/30 hari (700mb/hari)
    98. Next
    """)
    pilihan = int(input())

    if pilihan == 1:
        print("Makin enak internetan dengan unlimited harian. Tetap bisa internetan walaupun kuota harian habis")
        print("")
        harga = 9000
    elif pilihan == 2:
        print("Makin enak internetan dengan unlimited harian. Tetap bisa internetan walaupun kuota harian habis")
        print("")
        harga = 27000
    elif pilihan == 3:
        print("Makin enak internetan dengan unlimited harian. Tetap bisa internetan walaupun kuota harian habis")
        print("")
        harga = 48000
    elif pilihan == 4:
        print("Makin enak internetan dengan unlimited harian. Tetap bisa internetan walaupun kuota harian habis")
        print("")
        harga = 70000
    elif pilihan == 98:
        print("""
        5. Unlimited Harian 80k 30gb/30 hari (1gb/hari)
        6. Unlimited Harian 120k 60gb/40 hari (2gb/hari)
        7. Unlimited Harian 150k 90gb/45 hari (3gb/hari)
        8. Unlimited Harian 200k 120gb/60 hari (4gb/hari)
        99. Back
        """)
        p = int(input())

        if p == 5:
            print("Makin enak internetan dengan unlimited harian. Tetap bisa internetan walaupun kuota harian habis")
            print("")
            harga = 80000
        elif p == 6:
            print("Makin enak internetan dengan unlimited harian. Tetap bisa internetan walaupun kuota harian habis")
            print("")
            harga = 120000
        elif p == 7:
            print("Makin enak internetan dengan unlimited harian. Tetap bisa internetan walaupun kuota harian habis")
            print("")
            harga = 150000
        elif p == 8:
            print("Makin enak internetan dengan unlimited harian. Tetap bisa internetan walaupun kuota harian habis")
            print("")
            harga = 200000
        elif p == 99:
            uh()

        else:
            print("pilihan tidak valid")

    else:
        print("pilihan tidak valid")

    if harga > balance:
        print("Maaf saldo tidak cukup","saldo anda sekarang adalah",balance)
        print("Ingin beli pulsa? (y/t):")
        
        pilihan=input()
        
        if pilihan.lower() == "y":
            beli_pulsa()
        elif pilihan.lower() == "t":
            print("Terima kasih telah menggunakan layanan kami")
        else:
            print("Menu tidak valid")
            
        print("Lanjut pembelian? (y/t):")
        
        lanjut=input()
        
        if lanjut.lower() == "y":
            uh()
        else:
            print("Terima kasih telah menggunakan layanan kami")
        
    else:
        pembayaran()

def un():
    global balance

    print("""
    1. Unlimited Nonstop 12gb / 30 hari
    2. Unlimited Nonstop 18gb / 30 hari
    3. Unlimited Nonstop 24gb / 30 hari
    4. Unlimited Nonstop 32gb / 35 hari
    98. Next
    """)
    
    pilihan= int(input())

    if pilihan == 1:
        print("Makin hemat dengan kuota nonstop hanya dengan 30k untuk kuota internet 12gb berlaku 30 hari")
        print("")
        harga = 30000
    elif pilihan == 2:
        print("Makin hemat dengan kuota nonstop hanya dengan 40k untuk kuota internet 18gb berlaku 30 hari")
        print("")
        harga = 40000
    elif pilihan == 3:
        print("Makin hemat dengan kuota nonstop hanya dengan 55k untuk kuota internet 24gb berlaku 30 hari")
        print("")
        harga = 55000
    elif pilihan == 4:
        print("Makin hemat dengan kuota nonstop hanya dengan 69k untuk kuota internet 32gb berlaku 35 hari")
        print("")
        harga = 69000

    elif pilihan == 98:
        print("""
        5. Unlimited Nonstop 45gb / 40 hari 
        6. Unlimited Nonstop 60gb / 40 hari 
        7. Unlimited Nonstop 80gb / 60 hari 
        99. Back
        """)
        p = int(input())

        if p == 5:
            print("Makin hemat dengan kuota nonstop hanya dengan 95k untuk kuota internet 45gb berlaku 40 hari")
            print("")
            harga = 95000
        elif p == 6:
            print("Makin hemat dengan kuota nonstop hanya dengan 120k untuk kuota internet 60gb berlaku 40 hari")
            print("")
            harga = 120000
        elif p == 7:
            print("Makin hemat dengan kuota nonstop hanya dengan 150k untuk kuota internet 80gb berlaku 60 hari")
            print("")
            harga = 150000
        elif p == 99:
            un()
        else:
            print("Pilihan tidak valid")
    else:
        print("pilihan tidak valid")

    if harga > balance:
        print("Maaf saldo tidak cukup","saldo anda sekarang adalah",balance)
        print("Ingin beli pulsa? (y/t):")
        
        pilihan=input()
        
        if pilihan.lower() == "y":
            beli_pulsa()
        elif pilihan.lower() == "t":
            print("Terima kasih telah menggunakan layanan kami")
        else:
            print("Menu tidak valid")
            
        print("Lanjut pembelian? (y/t):")
        
        lanjut=input()
        
        if lanjut.lower() == "y":
            un()
        else:
            print("Terima kasih telah menggunakan layanan kami")
    else:
        pembayaran()

def kuota():
    global balance

    print("""
    1.Kuota 10gb 18k
    2.Kuota 12gb 20k
    3.Kuota 15gb 25k
    4.Kuota 25gb 38k
    """)
    
    pilihan= int(input())

    if pilihan == 1:
        print("Makin betah internetan dengan total kuota 10gb, 3gb kuota utama, 2gb kuota chat 5gb kuota malam")
        print("")
        harga = 18000
    elif pilihan == 2:
        print("Makin betah internetan dengan total kuota 12gb, 4gb kuota utama, 2gb kuota chat 6gb kuota malam")
        print("")
        harga = 20000
    elif pilihan == 3:
        print("Makin betah internetan dengan total kuota 15gb, 5gb kuota utama, 4gb kuota chat 6gb kuota malam")
        print("")
        harga = 25000
    elif pilihan == 4:
        print("Makin betah internetan dengan total kuota 25gb, 8gb kuota utama, 5gb kuota chat 12gb kuota malam")
        print("")
        harga = 38000
    else:
        print("Pilihan tidak valid")
    
    if harga > balance:
        print("Maaf saldo tidak cukup","saldo anda sekarang adalah",balance)
        print("Ingin beli pulsa? (y/t):")
        
        pilihan=input()
        
        if pilihan.lower() == "y":
            beli_pulsa()
        elif pilihan.lower() == "t":
            print("Terima kasih telah menggunakan layanan kami")
        else:
            print("Menu tidak valid")
            
        print("Lanjut pembelian? (y/t):")
        
        lanjut=input()
        
        if lanjut.lower() == "y":
            kuota()
        else:
            print("Terima kasih telah menggunakan layanan kami")
    else:
        pembayaran()

def menu_utama():
    print("""
        1. Unlimited Harian
        2. Unlimited Nonstop
        3. Kuota
        4. Informasi Layanan
        """)
    print("")
        
    pilihan = input()
    
    if pilihan == "1":
        uh()
    elif pilihan == "2":
        un()
    elif pilihan == "3":
        kuota()
    elif pilihan == "4":
        info()    
    else:
        print("Menu tidak valid")

def telepon():
    kode = input()
    
    if kode == "*123#":
        menu_utama()
    else:
        print("Kode telah diganti ke *123#")
        telepon()

telepon()

