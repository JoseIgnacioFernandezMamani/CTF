from pwn import xor

# Cadena de entrada (puedes cambiar esto por la cadena que necesites)
input_string = "label"  # Reemplaza "label" con tu cadena real
key = 13

# Usando pwntools para realizar la operación XOR
result = xor(input_string.encode(), key)

# Imprimir el resultado en el formato requerido
print("crypto{" + result.decode() + "}")
