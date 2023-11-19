s = set()

s.add("sai")
s.add(10)
s.add('K')
s.add(123)
s.add(10.5)
s.add(True)
s.add(1+4j)
s.add(bytes(10))
s.add(range(5))
print("Set Values :",s)

for i in s:
    print("Set values iterable ",i)
