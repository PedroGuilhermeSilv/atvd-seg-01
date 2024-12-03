# Criptografia de Substituição no Módulo 26

Este projeto implementa um algoritmo de criptografia de substituição baseado no módulo 26, permitindo encriptar e descriptar letras e textos completos. É especialmente útil para lidar com o alfabeto inglês (A-Z).

---

## Como funciona?

O algoritmo utiliza operações matemáticas no **módulo 26** para deslocar letras dentro do alfabeto. 

### Encriptação
Para cada letra:
1. Converter a letra para um valor numérico:  
   \( A=0, B=1, ..., Z=25 \).
2. Adicionar a chave (\(k\)) e calcular o resultado no módulo 26:  
   \( y = (x + k) \mod 26 \).
3. Converter o valor resultante de volta para uma letra.

### Decriptação
Para cada letra:
1. Converter a letra criptografada para um valor numérico.
2. Subtrair a chave (\(k\)) e calcular o resultado no módulo 26:  
   \( x = (y - k) \mod 26 \).
3. Converter o valor resultante de volta para uma letra.

### Tratamento de caracteres especiais
Os caracteres não alfabéticos (como números, espaços, e pontuações) são mantidos inalterados durante o processo.

---

## Estrutura do Código

### Funções
1. **`encrypt_letter(letter, k)`**  
   Encripta uma única letra usando a chave \(k\).

2. **`decrypt_letter(letter, k)`**  
   Descripta uma única letra usando a chave \(k\).

3. **`encrypt_text(text, k)`**  
   Encripta um texto completo, aplicando a encriptação em cada letra alfabética.

4. **`decrypt_text(text, k)`**  
   Descripta um texto completo, aplicando a decriptação em cada letra alfabética.

---

## Exemplo de Uso

```python
# Texto original
original_text = "Hello, World!"
k = 3  # Chave de deslocamento

# Encriptação
encrypted_text = encrypt_text(original_text, k)
print("Texto original:", original_text)
print("Texto encriptado:", encrypted_text)

# Decriptação
decrypted_text = decrypt_text(encrypted_text, k)
print("Texto decriptado:", decrypted_text)
```

### Saída esperada:
```
Texto original: Hello, World!
Texto encriptado: Khoor, Zruog!
Texto decriptado: Hello, World!
```

---

## Aplicações
- Simulação de criptografia básica.
- Exercícios educacionais para entender operações de substituição no módulo.
- Introdução à criptografia e segurança da informação.

---

## Observações
Este algoritmo **não é seguro** para uso em sistemas modernos, pois pode ser facilmente quebrado com análise de frequência. É apenas um exemplo didático.