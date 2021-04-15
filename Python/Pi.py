import time
import math

def Viete(iterations):
    start=time.time()
    root = math.sqrt(2)
    p = root / 2
    for i in range(1, iterations + 1):
        root = math.sqrt(2 + root)
        p = p * (root / 2)
    print('Viete: {:.50f} | time={:.4f}'.format(2/p,(time.time() - start)))




def Wallis(iterations):
    start = time.time()
    p = 1
    for i in range(1, iterations + 1):
        p = p * (2 * i) / (2 * i - 1) * (2 * i) / (2 * i + 1)
    print('Wallis: {:.50f} | time={:.4f}'.format(p * 2,(time.time() - start)))


def Leibniz(iterations):
    start = time.time()
    p=0
    for i in range (1, iterations+1):
        if i%2==1:
            p=p+4/(2*i-1)
        else:
            p=p-4/(2*i-1)
    print('Leibniz: {:.50f} | time={:.4f}'.format(p,(time.time() - start)))

def Nilakantha(iterations):
    start = time.time()
    p = 3
    for i in range(1, iterations + 1):
        if i % 2 == 1:
            p = p + 4 / ((2 * i) * (2 * i + 1) * (2 * i + 2))
        else:
            p = p - 4 / ((2 * i) * (2 * i + 1) * (2 * i + 2))
    print('Nilakantha: {:.50f} | time={:.4f}'.format(p,(time.time() - start)))

print("Iteration = 100000")
Viete(100000)
Wallis(100000)
Leibniz(100000)
Nilakantha(1000000)
print("================================================================================")
print("Iteration = 500000")
Viete(500000)
Wallis(500000)
Leibniz(500000)
Nilakantha(5000000)
print("================================================================================")
print("Iteration = 1000000")
Viete(100000)
Wallis(1000000)
Leibniz(1000000)
Nilakantha(10000000)



