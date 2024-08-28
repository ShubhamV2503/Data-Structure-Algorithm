

a = [3,1,2,3,2]

hashmap = {}

k = 1
bool = False
for i in range(len(a)):
    if a[i] not in hashmap:
        hashmap[a[i]] = hashmap.get(0 ,i)
    else:
        hashmap[a[i]] = i -  hashmap[a[i]]

        if hashmap[a[i]] ==



bool = False
for i in hashmap.values():

    if i <= k:
        bool = True
if bool:
    print("yes")
else:
    print("no")
