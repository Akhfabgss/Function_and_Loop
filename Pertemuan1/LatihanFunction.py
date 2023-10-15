# Konverrsi Celcius ke fahrenheit dengan fungs

def konversi_suhu(suhu, skala_awal, skala_tujuan):

    
    if skala_awal == 'C' and skala_tujuan == 'F':
        hasil_konversi = (suhu * 9/5) + 32
    elif skala_awal == 'F' and skala_tujuan == 'C':
        hasil_konversi = (suhu - 32) * 5/9
    else:
        raise ValueError("Skala awal atau skala tujuan tidak valid. Gunakan 'C' untuk Celsius atau 'F' untuk Fahrenheit.")
    
    return hasil_konversi

# Contoh penggunaan:
try:
    suhu_celsius = float (input("Masukan suhu anda dalam celcius : "))
    suhu_fahrenheit = konversi_suhu(suhu_celsius, 'C', 'F')
    print(f"{suhu_celsius} Celsius setara dengan {suhu_fahrenheit} Fahrenheit.")
    
    suhu_fahrenheit = float (input("Masukan suhu anda dalam fahrenheit : "))
    suhu_celsius = konversi_suhu(suhu_fahrenheit, 'F', 'C')
    print(f"{suhu_fahrenheit} Fahrenheit setara dengan {suhu_celsius} Celsius.")
except ValueError as e:
    print(e)