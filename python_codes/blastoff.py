import time
n = int(input ("Enter your countdown: \n"))
while n > 0:
    print (n)
    n -= 1
    time.sleep(1)
print ('Blastoff!')