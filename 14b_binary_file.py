f = open("number.bin", "wb") # w for write and b for binary
d=1024
f.write(int.to_bytes(d,16, 'big'))
f.close()

