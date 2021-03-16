def multiply(x):
    return x * 5

while True:
    try:
        x = list(map(int,input('masukan angka : ').split(' ')))
    except len(x) > 6:
        print('maksimal input 6 integer')
        continue
    print('angka sebelumdi filter : ', x),print('angka sesudah di filter : ',list(map(multiply,x)))
    break
