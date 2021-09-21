import hashlib
import niceware

hash=None
hasha=None
hashb=None
def symbols():
    s1=[i for i in range(0x21,0x30)]
    s2=[i for i in range(0x3a,0x41)]
    s3=[i for i in range(0x5b,0x61)]
    s4=[i for i in range(0x7b,0x7f)]
    s=s1+s2+s3+s4
    return[chr(i) for i in s]
symbols_v=symbols()
def cherry(n):
    s=''
    s+=symbols_v[n%32]
    n=n//32
    s+=chr(0x30+n%10)
    n=n//10
    s+=chr(0x41+n%26)
    return s
def make(u):
    rv=''
    #print('u=',u)
    m = hashlib.sha1()
    m.update(bytes(u,'utf-8'))
    mb=m.digest()#message binary
    hd=m.hexdigest()#hex digest
    #print('SHA-1 hash=',hd)
    for i in range(0,20,4):
        #print('i=',i)
        hash=mb[i:i+4]
        hasha=hash[0:2]
        hashb=hash[2:4]
        #print(type(hash),type(hasha),type(hashb))
        #print('hash=',hd[i*2:i*2+4],hd[i*2+4:i*2+8])
        #b  = int.from_bytes(hash ,byteorder='big')
        ba = int.from_bytes(hasha,byteorder='big')
        bb = int.from_bytes(hashb,byteorder='big')
        rv+= niceware.wordlist[ba]+cherry(bb)+'\n'
    return rv

