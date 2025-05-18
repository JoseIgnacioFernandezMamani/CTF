from Crypto.Util.number import long_to_bytes

# Tu número largo como cadena
message = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"

# Convertir la cadena a un entero
long_number = int(message)

# Convertir el número largo a bytes
byte_representation = long_to_bytes(long_number)

print(byte_representation)  # Esto imprimirá la representación en bytes del número largo

