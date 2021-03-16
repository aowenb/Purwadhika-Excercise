x = input('masukkan sebuah kalimat : ')
print('kalimat original : ',x)

def counter(x):
    up = []
    low = []
    for i in x[::1]:
        if i.isupper() == True:
            up.append(i)
        else:
            low.append(i)
    for i in low:
        if i == ' ':
            low.remove(' ')
    return len(up), len(low)

# 0 adalah Kapital dan 1 adalah non kapital

print('banyaknya Jumlah Huruf Kapital Di Kalimat adalah ', counter(x)[0])
print('banyaknya Jumlah Huruf Kapital Di Kalimat adalah ', counter(x)[1])
