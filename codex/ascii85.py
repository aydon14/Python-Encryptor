import base64

def encode(input): 
    output = base64.a85encode(input.encode('utf-8')).decode('utf-8')
    return output

def decode(input):
    output = base64.a85decode(input.encode('utf-8')).decode('utf-8')
    return output