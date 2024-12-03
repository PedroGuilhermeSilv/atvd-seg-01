Aqui está a versão detalhada do README explicando o uso de `isalpha` e `ord` no contexto do código:

---

# Criptografia de Substituição no Módulo 26

Este projeto implementa um algoritmo de criptografia de substituição para textos baseados no módulo 26, ideal para trabalhar com o alfabeto inglês (A-Z).

---

## Como funciona?

O algoritmo utiliza operações matemáticas no **módulo 26** para deslocar letras dentro do alfabeto. 

### Encriptação
Para cada letra:
1. Converter a letra em um valor numérico com `ord`:  
   \( A=0, B=1, ..., Z=25 \).
2. Adicionar a chave (\(k\)) e calcular o resultado no módulo 26:  
   \( y = (x + k) \mod 26 \).
3. Converter o valor numérico de volta para uma letra usando `chr`.

### Decriptação
Para cada letra:
1. Converter a letra criptografada em um valor numérico com `ord`.
2. Subtrair a chave (\(k\)) e calcular o resultado no módulo 26:  
   \( x = (y - k) \mod 26 \).
3. Converter o valor numérico de volta para uma letra com `chr`.

### Tratamento de caracteres especiais
Os caracteres não alfabéticos (números, pontuações, espaços, etc.) são mantidos inalterados. Isso é verificado usando a função `isalpha`.

---

## Explicação Detalhada das Funções

### **`isalpha`**
A função `isalpha` verifica se um caractere é uma letra do alfabeto. É usada para:
- Identificar se o caractere deve ser encriptado/descriptado.
- Garantir que caracteres especiais, números e espaços sejam mantidos inalterados.

Exemplo:
```python
letter = 'H'
print(letter.isalpha())  # Saída: True

non_letter = '!'
print(non_letter.isalpha())  # Saída: False
```

No código:
- Se `isalpha` retornar `True`, o caractere é processado.
- Caso contrário, o caractere é simplesmente adicionado ao texto final sem alterações.

### **`ord`**
A função `ord` converte um caractere em seu valor numérico Unicode. Para este algoritmo:
- Subtraímos o valor Unicode de `'A'` (\(65\)) de uma letra maiúscula para normalizar os valores, de forma que \(A=0, B=1, ..., Z=25\).
- Isso permite realizar as operações matemáticas de criptografia e decriptografia.

Exemplo:
```python
letter = 'H'
x = ord(letter) - ord('A')  # H -> 72 - 65 = 7
print(x)  # Saída: 7
```

No código:
- `ord` é usado para transformar letras em números para que possamos aplicar operações no módulo 26.

### **`chr`**
A função `chr` faz o inverso de `ord`: converte um valor numérico de volta em um caractere Unicode.  
No algoritmo:
- Após realizar os cálculos matemáticos no módulo 26, `chr` é usado para reconstruir a letra correspondente.

Exemplo:
```python
x = 7
letter = chr(x + ord('A'))  # 7 -> 7 + 65 = 72 -> H
print(letter)  # Saída: H
```

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
- **`isalpha`** garante que apenas letras sejam processadas. Caracteres especiais e espaços permanecem inalterados.
- **`ord`** e **`chr`** são fundamentais para transformar letras em números e vice-versa, permitindo operações matemáticas simples.