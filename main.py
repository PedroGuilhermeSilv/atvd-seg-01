def encrypt_letter(letter, k):
    """Encripta uma letra usando a chave k no módulo 26"""
    # Converter letra para número (A=0, B=1, ..., Z=25)
    x = ord(letter.upper()) - ord('A')
    # Aplicar encriptação
    y = (x + k) % 26
    # Converter de volta para letra
    return chr(y + ord('A'))

def decrypt_letter(letter, k):
    """Descripta uma letra usando a chave k no módulo 26"""
    # Converter letra para número (A=0, B=1, ..., Z=25)
    y = ord(letter.upper()) - ord('A')
    # Aplicar decriptação
    x = (y - k) % 26
    # Converter de volta para letra
    return chr(x + ord('A'))

def encrypt_text(text, k):
    """Encripta um texto usando a chave k no módulo 26"""
    encrypted_text = ""
    for letter in text:
        if letter.isalpha():
            encrypted_text += encrypt_letter(letter, k)
        else:
            encrypted_text += letter  # Manter caracteres não alfabéticos inalterados
    return encrypted_text

def decrypt_text(text, k):
    """Descripta um texto usando a chave k no módulo 26"""
    decrypted_text = ""
    for letter in text:
        if letter.isalpha():
            decrypted_text += decrypt_letter(letter, k)
        else:
            decrypted_text += letter  # Manter caracteres não alfabéticos inalterados
    return decrypted_text

# Exemplo de uso
original_text = "Hello, World!"  # Texto original
k = 3  # Chave de deslocamento

# Encriptação
encrypted_text = encrypt_text(original_text, k)
print("Texto original:", original_text)
print("Texto encriptado:", encrypted_text)

# Decriptação
decrypted_text = decrypt_text(encrypted_text, k)
print("Texto decriptado:", decrypted_text)
