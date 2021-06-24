aluno = {}
print("CADASTRO DE ALUNO")
while True:
    matricula = int(input("Digite o numero da matricula: "))
    if matricula in aluno:
        print("Matricula ja cadastrada!")
        continue
    elif matricula == 0:
        break
    nome = str(input("Digite o nome do aluno: "))
    idade = int(input("Digite a idade do aluno: "))
    curso = str(input("Digite o curso: "))
    infos = (nome,idade,curso)
    aluno[matricula] = infos
    pergunta = str(input("Gostaria de cadastrar mais um aluno? "))
    if pergunta == 'sim':
        continue
    elif pergunta == 'nao':
        break
print("FIM DO CADASTRO")
for matricula,dados in aluno.items():
    print("Matricula: {} Aluno: {} Idade: {} Curso: {}".format(matricula,dados[0],dados[1],dados[2]))