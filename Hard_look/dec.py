import binascii
f = open("cip.txt","r")
content=f.readlines()[0]
ch=""
for i in content:
    if i =="-":
        ch+="1"
    elif i =="_":
        ch+="0"
ch="00"+ch
n = int(ch,2)
flag = binascii.unhexlify('%x' % n).decode("hex")
print(flag)
        
