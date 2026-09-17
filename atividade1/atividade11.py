nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
total_aulas = float(input("total de aulas do aluno: "))
total_faltas = float(input("total de faltas: "))
soma = (nota1 + nota2 + nota3)/3
faltas = (total_faltas * 100) / total_aulas

if faltas >= 25 :
    print("Reprovado! por faltas")

elif soma >= 9 and faltas <= 10:
    print("Aprovado com louvor!")
elif soma >= 7:
    print("Aluno Aprovado!")
elif soma < 7:
    print("Recuperação!")
elif soma < 5:
    print("Reprovado!")
