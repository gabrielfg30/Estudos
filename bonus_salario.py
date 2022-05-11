salario = int(input('Digite o salario: ')) 

tempoCasa = int(input('Digite o tempo em anos que está na empresa: ')) 

 

if tempoCasa >= 5: 

    bonus =  salario * 20 / 100 

else: 

    bonus =  salario * 10 / 100 

print('O bonus é R$: ',bonus)   

print('O salário é R$: ',salario+bonus) 