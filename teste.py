print("bem vindo ao calculo de media")
name = input("Digite seu nome: ")
matter = input("digite o nome da materia: ")
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
nota4 = float(input("digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4

if media > 7:
    print("PARABÈNS! %s, você foi aprovado! Sua media é %f" %(name, media))
else:
    print("REPROVADO! %s, sua media foi %f" %(name, media))
