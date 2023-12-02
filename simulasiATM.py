saldo = 100000

def cek_saldo():
    print('')
    print('========================================')
    print('saldo anda saat ini adalah: Rp',saldo)
    print('========================================')
    
def transfer():
    global saldo
    norek_tujuan=int(input('masukkan nomer rekening tujuan: '))
    if norek_tujuan <=10:
    	print('norek tidak ada')
    else:
    	jumlah=float(input('transfer berapa?: Rp'))
    print('')
    
    if jumlah > saldo:
        print('=========================')
        print('maaf saldo tidak cukup')
        print('=========================')
    else:
        saldo-=jumlah
        print('=========================')
        print('transfer berhasil')
        print('=========================')
        cek_saldo()
        
def tarik_tunai():
    global saldo
    tarik=float(input('Tarik tunai berapa?: Rp'))
    if tarik > saldo:
        print('=========================')
        print('maaf saldo tidak cukup')
        print('=========================')
    else:
        print('=========================')
        print('tarik tunai berhasil')
        print('=========================')
        
        saldo1= saldo - tarik
 
        if saldo1 >=0:
        	saldo = saldo1
        	print('=====================================')
        	print('saldo anda saat ini: Rp',saldo)
        	print('=====================================')
        
def tambah_saldo():
    global saldo
    tambah=float(input('tambah saldo: Rp'))
    saldonew= saldo + tambah
    
    if tambah >0:
        saldo= saldonew
        print('===========================')
        print('saldo berhasil ditambahkan')
        print('===========================')
    cek_saldo()
        
while True:
    print('Menu')
    print('1.Cek saldo')
    print('2.Transfer')
    print('3.Tarik tunai')
    print('4.Tambah saldo')
    print('5.Keluar')
    pilihan=input('pilih menu:')
    
    if pilihan == '1':
        cek_saldo()
    elif pilihan == '2':
        transfer()
    elif pilihan == '3':
        tarik_tunai()
    elif pilihan == '4':
        tambah_saldo()
    elif pilihan == '5':
        print('terima kasih telah menggunakan layanan kami')
    else:
        print('pilihan tidak valid')