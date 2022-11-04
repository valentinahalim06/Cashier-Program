import os
os.system('cls')

print('==================== Welcome to the Scent of Heaven ================')
print('===== We will provide you with the largest selection of perfumes at the lowest price =====')
print('')

parfum = {
    'Fallen Angel 50 ml' :70000,
    'Garden of Eden 50 ml':80000,
    'Hidden Gem 50 ml':90000,
    'Angel Eyes 50 ml'  :100000,
    'Goddess Angel 50 ml':110000,
}
print('================ Grab yours now! ================')
for i in parfum :
    print('Varian Perfume : ' , i,'\t > Price :' , parfum[i],)
    
#Mohon masukkan nama perfume dengan lengkap
#Contoh > Varian Perfume: Fallen Angel 50 ml
 
print('================================================')   
print('Pembelian di Atas 120 ribu Mendapatkan Diskon 15%')
print('================================================')
print('')

print('>>> Please choose your favorite perfume to order <<<')
nama_Parfum = input('Varian Perfume:')
jumlah = int(input('Jumlah Pesanan:'))
bayar = jumlah * parfum[nama_Parfum]

if bayar > 120000:
    diskon= bayar*15/100
    total= bayar - diskon
else:
    total= bayar

print('')
print('================ Detail Pembayaran ================')
print('Perfume yang Dipesan     :', nama_Parfum)
print('Jumlah yang Dipesan      :', jumlah)
print('Total Biaya              :', bayar)
print('Total yang Harus Dibayar :', total)

print('')
print('========== Thank you for your order! ==========')
