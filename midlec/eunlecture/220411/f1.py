import random
ab= ['1','2','3','4','5','6']

a= [1,2,3,4,5,6]



print(random.randrange(1,7))


print(random.randbytes(2))



random.shuffle(ab)
random.shuffle(a)
print(ab)

print(a)

b= random.uniform(1,55)

print(b)


print(random.choice(ab))  #원소 출력.

import time
print(time.time())

