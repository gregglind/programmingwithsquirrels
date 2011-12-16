def div2(ii):
    return ii %2 == 0

def div3(ii):
    return ii %3 == 0

def main():
    ii = 1
    while ii <= 15:
        if div2(ii):
            print ii, "FIZZ"
        
        if div3(ii):
            print ii, "BUZZ"
        
        ii+=1

main()  # start off the whole thing.



