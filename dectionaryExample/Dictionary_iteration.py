d = {1:"one", 2:"Two",3:"Thress","key":"value", "hello":"Hi" }
for k,v in d.items():
    if k == "key" or k == 1:
        continue
    if(k != 3):
        print(">>",v)
    print(k, " - ", v)

