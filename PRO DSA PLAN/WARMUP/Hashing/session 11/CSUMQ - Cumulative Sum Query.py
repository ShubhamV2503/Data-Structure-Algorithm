
# https://www.spoj.com/submit/CSUMQ/


N = int(input('Size of array'))

a = list(map(int , input('Enter numbers').split()))

q = int(input('enter query'))

while q > 0:
    index  = list(map(int , input('Enter numbers').split()))
    psum = 0
    for i in range(index[0] , index[1]+1):
        psum = psum + a[i]
    print(psum)
    q = q - 1

