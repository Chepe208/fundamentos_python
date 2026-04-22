#kilometers = 12.25
#miles = 7.38

#miles_to_kilometers = miles * 1.61
#kilometers_to_miles = kilometers / 1.61

#print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
#print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

usd = 100
tipo_cambio = 0.92
eur = usd * tipo_cambio
print(usd, "USD son", round(eur, 2), "EUR")

celsius = 25
fahrenheit = celsius * 9/5 + 32
print(celsius, "°C son", round(fahrenheit, 1), "°F")

numero = 3.14159
print("Original:", numero)
print("Redondeado a 0 decimales:", round(numero))
print("Redondeado a 2 decimales:", round(numero, 2))
print("Redondeado a 3 decimales:", round(numero, 3))

total_apples = 14
print("Número total de manzanas:", total_apples)
print("Total: " + str(total_apples) + " manzanas")   
print(f"Tenemos {total_apples} manzanas")     