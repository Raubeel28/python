def netprice(listprice,discount=0,tax=0.05):
    return listprice*(1-discount)*(1+tax)

print(netprice(450))
import time
def count(end,start=0):
    for x in range(start,end,-1):
        print(x)
        time.sleep(1)
    print("DONE!!")

print(count(10,15))
