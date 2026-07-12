def pin_extractor(poems):
    secret_codes = []  # Lista vacía para guardar los PINs finales de todos los poemas
    for poem in poems:  # Recorre los poemas de la lista uno por uno
        secret_code = ''  # Cadena vacía para construir el PIN del poema actual
        lines = poem.split('\n')  # Rompe el poema en una lista de líneas usando el salto de línea
        for line_index, line in enumerate(lines):  # Recorre las líneas dándonos su índice (0, 1, 2...) y el texto
            words = line.split()  # Rompe la línea actual en una lista de palabras separadas por espacios
            if len(words) > line_index:  # Seguridad: comprueba si la línea tiene suficientes palabras para la posición que toca
                secret_code += str(len(words[line_index]))  # Cuenta las letras de la palabra en diagonal y añade el número al PIN
            else:
                secret_code += '0'  # Si la línea es muy corta y no tiene esa palabra, añade un '0' por defecto
        secret_codes.append(secret_code)  # Guarda el PIN completado de este poema en la lista de resultados
    return secret_codes  # Devuelve la lista con todos los PINs extraídos


# --- Zona de pruebas con tus ejemplos ---

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

# Ejecuta la función y muestra el resultado en la consola: ['5202', '3342', '50000']
print(pin_extractor([poem, poem2, poem3]))
