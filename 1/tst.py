tot = 0



with open("input") as f:
      for line in f:
          k = int(line)
          k= k //3 -2
          while k>0:
              tot+=k
              k=k/  /3-2

print(tot)

