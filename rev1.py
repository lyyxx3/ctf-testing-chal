input = b'fZjkMyeQWVmmbk'
key = b'123456789'

def xor(input_bytes, key_bytes):
    decrpyted_bytes = bytearray()
    key_len = len(key)
    
    for i in range(len(input_bytes)):
        decrpyt = input_bytes[i] ^ key_bytes[i % key_len]
        decrpyted_bytes.append(decrpyt)
    
    return decrpyted_bytes.decode('utf-8', errors='ignore') 


result = xor(input, key) #input and key is both converted into bytes, for input the read() make it into bytes
print (result)