N1,N2,N3,N4 = list(map(float,input().split(" ")))
media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / (2 + 3 + 4 + 1)
print("Media: {:.1f}".format(media))
if(media >= 7.0):
    print("Aluno aprovado.")
elif(media < 5.0):
    print("Aluno reprovado.")
elif(media >= 5.0 and media < 7.0):
    print("Aluno em exame.")
    N5 = float(input())
    print("Nota do exame: {:.1f}".format(N5))
    novmedia = (media + N5) / 2
    if(novmedia >= 5.0):
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(novmedia))
    else:
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(novmedia))