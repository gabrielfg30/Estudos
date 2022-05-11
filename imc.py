altura = eval(input('Entrar com a altura ')) 

peso = eval(input('Entrar com o peso ')) 

imc = peso / (altura*altura) 

if imc < 18: 

     print('Abaixo do peso normal, com IMC:', imc) 

elif imc >= 18 and imc <= 25: 

     print('Peso normal, com IMC:', imc) 

elif imc > 25 and imc <= 30: 

     print('Excesso de peso, com IMC:', imc) 

elif imc > 30 and imc <= 35: 

     print('Obesidade classe 1, com IMC:', imc) 

elif imc > 35 and imc <= 40: 

     print('Obesidade classe 2, com IMC:', imc) 

else: 

     print('Obesidade classe 3, com IMC:', imc) 