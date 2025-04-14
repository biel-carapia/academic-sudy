Nota_1 = int(input("Digite a primeira nota:"))
Nota_2 = int(input("Digite a segunda nota:"))
Nota_3 = int(input("Digite a terceira nota:"))
Nota_4 = int(input("Digite a quarta nota:"))
#observe que utilizamos a função int(), pois sem ela, o python entenderia que as nota seriam String


media = (Nota_1 + Nota_2 + Nota_3 + Nota_4)/4

#Condição para aprovação do aluno
if media >=6:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

#dadas as notas a média final e a situação do aluno.
print(f"A média das notas é: {media}")
print(f"Situação do aluno: {situacao}")


