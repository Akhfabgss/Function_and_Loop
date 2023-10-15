# Mmebuat Kalkulator dengan fanction

def kalkulator_aritmatika(operator, *args):
    if not args:
        raise ValueError("Tidak ada argumen yang diberikan.")
    
    valid_operators = {'+', '-', '*', '/', '**'}
    if operator not in valid_operators:
        raise ValueError("Operator tidak valid. Gunakan '+', '-', '*', '/', atau '**'.")
    
    result = args[0]
    
    if operator == '+':
        for num in args[1:]:
            result += num
    elif operator == '-':
        for num in args[1:]:
            result -= num
    elif operator == '*':
        for num in args[1:]:
            result *= num
    elif operator == '/':
        for num in args[1:]:
            result /= num
    elif operator == '**':
        for num in args[1:]:
            result **= num
    
    return result

# Contoh penggunaan:
try:
    a = int(input("Masukan Nilai Kamu : "))
    b = int(input("Masukan Nilai Kamu : "))
    c = int(input("Masukan Nilai Kamu : "))

    hasil = kalkulator_aritmatika('+', a, b, c)
    print("Hasil Penjumlahan:", hasil)
    
    hasil = kalkulator_aritmatika('-', a, b, c)
    print("Hasil Pengurangan:", hasil)
    
    hasil = kalkulator_aritmatika('*', a, b, c)
    print("Hasil Perkalian:", hasil)
    
    hasil = kalkulator_aritmatika('/', a, b, c )
    print("Hasil Pembagian:", hasil)
    
    hasil = kalkulator_aritmatika('**', a, b)
    print("Hasil Pemangkatan:", hasil)
    
except ValueError as e:
    print(e)