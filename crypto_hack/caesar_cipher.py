import string

def poly(plain: str, key: int) -> str:
    plain = plain.lower()  # Convertir a minúsculas
    letters = string.ascii_lowercase  # Alfabeto en minúsculas
    charset = {}

    # Crear el conjunto de caracteres desplazados
    for i in range(len(letters)):
        charset[letters[i]] = letters[(i + key) % 26]  # Cifrado

    def encdec(plain: str, charset: dict) -> str:
        es = ''
        for char in plain:
            if char in charset:
                es += charset[char]  # Agregar carácter cifrado
            else:
                es += char  # Dejar igual si no está en charset
        return es

    return encdec(plain, charset).upper() 

# Probar todas las claves posibles
for i in range(26):
    possible_answer = poly("NJGYDZM GJPIBZ VPBPNO KVMMJO", i)
    print(f'{possible_answer}, key: {i + 1}')

