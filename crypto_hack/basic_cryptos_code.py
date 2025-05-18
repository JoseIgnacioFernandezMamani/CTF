#!/usr/bin/env python3

import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("Here is your flag:")
# descencriptado XOR
## ^ es la funcion xor en python
## 0x32 es 50, 0x32 0x indica que el siguiente es un valor hexadecimal, 32 hexadecimal en decimal es 3x16^1 + 2x16^0=50
## 81 = 01010001 (binario)
## 50 = 00110010
## resultado: 01100011 que se convierte directamente a un valor ascci con ayuda de chr es c de crypto{ ...
print("".join(chr(o ^ 0x32) for o in ords))



# hex to byte

my_hex= "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
# python transalate to text automatically
print(bytes.fromhex(my_hex))

# hex to base64
import base64

my_base64 = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
print(base64.b64encode(bytes.fromhex(my_base64)))
