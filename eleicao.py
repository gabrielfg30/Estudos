print('Você tem que digitar a sua nacionalidade')  
nacionalide = input('Coloque b (brasileiro) ou q (caso não seja):') #se não for brasileiro (b) não votará 
if nacionalide == 'q': 
    print('Você não pode votar')
    exit()
else: 
    idade = eval(input('Entre com sua idade: ')) 
if idade < 16: 
    print('Você não é eleitor') 
elif idade >= 18 and idade<= 65: 
    print("Você é eleitor obrigatório") 
elif (idade >=16 and idade <18) or idade > 65: 
    print("Você é eleitor facultativo") 
else: 
    print("Erro") #por via das duvidas mas acho que nem precisava
print("Obrigada por usar nossos serviços")  