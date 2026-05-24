# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

num = input().strip()
pp = []
for x in num.strip():
     if x.isdigit():
          pp.append(int(x))
re_shape = np.array(pp)
reree = re_shape.reshape(3,3)
print(reree)
