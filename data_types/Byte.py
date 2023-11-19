import sys
x = [1,2,3,4]
print(type(x), " and length is ", len(x), " Size is ", sys.getsizeof(x) )
byte_obj = bytes(x)
print("Bytes printing : ",byte_obj, " length is ", len(byte_obj), "Size is :", sys.getsizeof(byte_obj))
print(type(byte_obj))
# Convert Byte to List
l = list(byte_obj)
print("Converted List ", l)
