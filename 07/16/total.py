from time import time

def main():
    start = time()
    total = 0
    l = list(range(1,1000001))
    for num in l:
        total += num
    end = time()
    print('total: %d' % total)
    print('time used: %.3f' % ( end - start))

if __name__ == "__main__":
    main()
