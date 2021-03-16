x = list(input('masukkan sebuah kalimat : ').split(' '))
def reverse_word(x):
    return x[::-1]
new = list(map(reverse_word,x))
for i in new:
    print(i,end=' ')