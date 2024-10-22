def konversisuhu(temperature, value):
    if value == 'C':        #memeriksa apakah value adalah 'C' atau Celsius
        temperaturesuhu = (temperature - 32) * 5/9      #mengonversi suhu dari Fahrenheit ke Celsius
        return temperaturesuhu, 'C'     #mengembalikan suhu yang dikonversi dan unit 'C'
    else:
        temperaturesuhu = (temperature * 9/5) + 32      #mengonversi suhu dari Celsius ke Fahrenheit
        return temperaturesuhu, 'F'     #mngembalikan suhu yang dikonversi dan unit 'F'
    
#mengonversi 30°C ke Fahrenheit
celcius_temperature = 30
temperaturesuhu, target_value = konversisuhu(celcius_temperature, 'F')
#mencetak hasil konversi dari Celsius ke Fahrenheit
print(f"{celcius_temperature}°C dikonversi ke Fahrenheit adalah {temperaturesuhu}°{target_value}")

#mengonversi 86°F ke Celsius
fahrenheit_temperature = 86
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'C')
#mencetak hasil konversi dari Fahrenheit ke Celsius
print(f"{fahrenheit_temperature}°F dikonversi ke Celcius adalah {temperaturesuhu}°{target_value}")