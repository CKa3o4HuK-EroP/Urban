numbers = [i for i in range(1, 16)]
primes = []
not_primes = []
for i in numbers:
    if i == 1: continue
    prime = True
    for j in range(2, round(i ** 0.5 + 1)):
        if i % j == 0: prime = False; break
    if prime: primes.append(i)
    else: not_primes.append(i)

print(f'Primes: {primes}\nNot primes: {not_primes}')
