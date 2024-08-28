## BEST APPROACH

a = [6,7,3,2,2]

index = [0,2,4,3]

dp = [0] * len(a)

i = 0

while i < len(a):
    if i == 0:
        dp[i] = a [i]
    else:
        dp[i] = a[i] + dp[i-1]
    i = i + 1

for i in index:
    print(dp[i])


## TC --> O( A + INDEX)


# ----------------------------------------------------------------------------------------

## Brutee Force Approch

# a = [6,7,3,2,2]

# index = [0,2,4,3]

# for i in index:
#     result = 0
#     for j in range(0,i+1):
#         result = result + a[j]
#     print(result)

# TC --> O( A * INDEX)