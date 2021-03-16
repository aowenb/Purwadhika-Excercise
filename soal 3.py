x = list(map(int,input('masukkan angka : ').split(' ')))
print(x)

def sortit(x):
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    return(x)

print('hasil sorting : ', sortit(x))
print('nilai terbesar adalah : ',sortit(x)[-1])
print('nilai terendah adalah : ',sortit(x)[0])