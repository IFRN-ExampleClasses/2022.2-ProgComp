num_primos = list()
print(num_primos)
for x in range(2, 101):
   cnt_div = 0
   for div in range(1, x+1):
      if x % div == 0: cnt_div += 1
      if cnt_div > 2: break
   if cnt_div == 2: num_primos.append(x)
print(num_primos)