peso = float(input('Dame tu peso en kilogramos: '))
altura = float(input('Dame tu altura en metros: '))
imc = peso / (altura * altura)
print(imc)

if imc < 18.5:
    print('Bajo peso.')
if imc >= 18.5 <= 24.9:
    print('Normal.')
elif imc >= 25 <= 29.9:
    print('Sobrepeso.')
elif imc > 29.9:
    print('Obesidad.')