import math
limit = int(input('masukkan banyaknya data : '))
data = []

for i in range(0,limit):
    for j in range(0,limit):
        print('masukkan data ke', j+1 ,'=',)
        data.append(int(input()))
    break
print(data)

def mean(x):
    return sum(x)/len(x)

def var(x):
    log = []
    for i in x:
        log.append((i - mean(x))**2)
    return sum(log)/len(x)

def stan_dev(x):
    return math.sqrt(var(x))

print('rata ratanya adalah ', mean(data))
print('variancenya adalah ', var(data))
print('standard deviation adalah ', stan_dev(data))

