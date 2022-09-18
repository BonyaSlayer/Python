with open('Decode.txt', 'r') as data:
    some_text = data.read()

def encode_rle(data):
    str_code = ''
    prev_char = ''
    count = 1
    for char in data:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code



print(encode_rle(some_text))

with open('Encode.txt', 'r') as data:
    some_text2 = data.read()

def decoding_rle(data:str):
    count = ''
    str_decode = ''
    for char in data:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

print(decoding_rle(some_text2))
