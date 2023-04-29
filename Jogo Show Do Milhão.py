import random
r = 0
a = 4
b = 5
c = 5
x = 0
p1 = 'Qual animal da fauna brasileira está retratado na nota de dez reais?\nA) Jabuti\nB) Onça\nC) Arara\nD) Tucano\n'
p2 = 'Quingentésimo corresponde a qual número?'
p3 = 'Quais novas letras foram incorporadas no alfabeto?'
p4 = 'Uma pessoa que é cleptomaníaca é:'
p5 = 'Onde nasceu o pintor Picasso:'
p6 = 'Complete o nome de Dom Pedro I:'
p7 = 'Qual o nome popular da Cannabis Sativa:'
p8 = 'Qual o resultado da expressão: 2+3*(4-1)?'
p9 = 'No futebol americano, o touchdown equivale a quantos pontos?'
p10 = 'Qual a ortografia correta da palavra:'
p11 = 'De onde é a invenção do chuveiro elétrico?'
p12 = 'Quais os principais autores do Barroco no Brasil?'
p13 = 'Qual a tradução da frase “Fabiano cogió su saco antes de salir”?'
p14 = 'Qual das alternativas não é uma linguagem de programação:'
p15 = 'Qual foi a primeira pergunta?\nA) Quingestésimo\nB) Letras no alfabeto\nC) Nota de dez\nD) Cannabis\n'
p16 = 'Se ontem fosse amanhã, hoje seria sexta-feira. Que dia é hoje?\n'
p17 = 'Qual fruta é nativa e exclusiva(tem origem) do Brasil?\n'
p18 = 'Qual é um ano bissexto?\n'
p20 = 'Quantos animais de cada espécie, Moisés colocou em sua arca:'
# ALTERNATIVAS
altAfacil = ['500', 'J, W e Y', 'Colecionadora', 'Espanha', '2022']
altBfacil = ['5000', 'H, K e Y', 'Decoradora', 'Holanda', '2024']
altCfacil = ['50', 'J, K e Y', 'Médica', 'França', '2025']
altDfacil = ['5', 'K, W e Y', 'Doente', 'Bélgica', '2018']

altAmedio = [
    'Pedro de Oliveira Jorge Carlos Leopoldo Salvador Bibiano Francisco Xavier de Paula Leocádio Miguel Gabriel '
    'Rafael Gonzaga de Bragança e Habsburgo',
    'Rivotril', '17', '10', 'Associação', 'Guaraná']
altBmedio = [
    'Pedro de Alcântara João Carlos Leopoldo Salvador Bibiano Francisco Xavier de Paula Leocádio Miguel Gabriel '
    'Rafael Gonzaga de Bragança e Habsburgo',
    'Manga', '10', '3', 'Assossiação', 'Abacaxi']
altCmedio = [
    'Pedro de Alcântara João Carlos Leopoldo Silva Bibiano Francisco Xavier de Paula Leocádio Miguel Gabriel Rafael '
    'Gonzaga de Bragança e Habsburgo',
    'Orquídea', '15', '1', 'Assosciação', 'Caju']
altDmedio = [
    'João Pedro Felitto de Alcântara João Carlos Leopoldo Salvador Borges Francisco Xavier de Paula Leocádio Miguel '
    'Gabriel Rafael Gonzaga de Bragança e Habsburgo',
    'Maconha', '11', '7', 'Assossiassão', 'Abacate']

altAdificil = ['Brasil', 'Gregório de Matos, Bento Teixeira e Manuel Botelho de Oliveira',
               'Fabiano fechou o saco antes de sair', 'C', 'Sexta-feira', '0']
altBdificil = ['EUA', 'Miguel de Cervantes, Gregório de Matos e Danthe Alighieri',
               'Fabiano pegou seu paletó antes de sair', 'R', 'Domingo', '1']
altCdificil = ['Alemanha', 'Padre Antônio Vieira, Padre Manuel de Melo e Gregório de Matos',
               'Fabiano cortou o saco antes de cair', 'F#', 'Quarta-feira', '2']
altDdificil = ['China', 'Castro Alves, Bento Teixeira e Manuel Botelho de Oliveira',
               'Fabiano rasgou seu paletó antes de cair', 'G', 'Sábado', '3']

# P1 é fixa para corresponder à última, que é fixa também
listafacil = [p2, p3, p4, p5, p18]
listamedio = [p6, p7, p8, p9, p10, p17]
listadificil = [p11, p12, p13, p14, p16, p20]
gabfacil = ['a', 'd', 'd', 'a', 'b']
gabmedio = ['b', 'd', 'd', 'd', 'a', 'c']
gabdificil = ['a', 'a', 'b', 'd', 'c', 'a']
validar = []  # Vamos utilizar para não repetir a pergunta no sorteio

stop = 0  # stop para parar, se o usuário decidir
lose = 0  # para indicar se o usuario perder
pause = 0  # para demarcar o fim da repetição

# Prêmios
j = 0
premioA = ['1.000', '2.000', '3.000', '4.000', '5.000', '10.000', '20.000', '30.000', '40.000', '50.000', '100.000',
           '200.000', '300.000', '400.000', '500.000', '1.000000']
premioP = ['0', '1.000', '2.000', '3.000', '4.000', '5.000', '10.000', '20.000', '30.000', '40.000', '50.000',
           '100.000', '200.000', '300.000', '400.000', '500.000']
premioE = ['0', '500', '1.000', '1.500', '2.000', '2.500', '5.000', '10.000', '15.000', '20.000', '25.000', '50.000',
           '100.000', '150.000', '200.000', '0']

# Flexibilizar o random:
maxF = 4
maxM = 5
maxD = 5

# Ajudas
skip = 1
Help = 1


def helpp():
    h = 100
    ha = random.randint(0, h)
    h -= ha
    hb = random.randint(0, h)
    h -= hb
    hc = random.randint(0, h)
    h -= hc
    hd = h
    print(f"* Ajuda da Plateia: *\nO que eles acham?\nA) {ha}%\nB) {hb}%\nC) {hc}%\nD) {hd}%\n")


# Entrada/Introdução

print("* BEM-VINDO AO SHOW DO MILHÃO! *")
inic = int(input("1- JOGAR\n2- ADICIONAR PERGUNTAS\n3- AJUDA\n4- Encerrar\n"))
while inic != 1 and inic != 2 and inic != 3 and inic != 4:
    inic = int(input("Digite uma opção válida!\n"))
    print('\n')

while inic != 4:

    # Incluir perguntas
    while inic == 2:
        dificuldade = input("Digite a dificuldade de sua pergunta:\n1- Fácil\n2- Médio\n3- Dificil\n")
        while dificuldade != '1' and dificuldade != '2' and dificuldade != '3':
            dificuldade = input("Digite uma opção válida: ")
        print("\n")
        if dificuldade == '1':
            listafacil.append(input("Digite a pergunta: "))
            altAfacil.append(input("Digite a alternativa A: "))
            altBfacil.append(input("Digite a alternativa B: "))
            altCfacil.append(input("Digite a alternativa C: "))
            altDfacil.append(input("Digite a alternativa D: "))
            gabfacil.append(input("Qual é a alternativa correta (gabarito)? ").lower())
            print("Cadastrado com sucesso!")
            print("\n")
            maxF += 1
            inic = int(input("1- JOGAR\n2- ADICIONAR PERGUNTAS\n3- AJUDA\n"))
            while inic != 1 and inic != 2 and inic != 3:
                inic = int(input("Digite uma opção válida!\n"))

        if dificuldade == '2':
            listamedio.append(input("Digite a pergunta: "))
            altAmedio.append(input("Digite a alternativa A: "))
            altBmedio.append(input("Digite a alternativa B: "))
            altCmedio.append(input("Digite a alternativa C: "))
            altDmedio.append(input("Digite a alternativa D: "))
            gabmedio.append(input("Qual é a alternativa correta (gabarito)? ").lower())
            print("Cadastrado com sucesso!")
            maxM += 1
            print("\n")
            inic = int(input("1- JOGAR\n2- ADICIONAR PERGUNTAS\n3- AJUDA\n"))
            while inic != 1 and inic != 2 and inic != 3:
                inic = int(input("Digite uma opção válida!\n"))

        if dificuldade == '3':
            listadificil.append(input("Digite a pergunta: "))
            altAdificil.append(input("Digite a alternativa A: "))
            altBdificil.append(input("Digite a alternativa B: "))
            altCdificil.append(input("Digite a alternativa C: "))
            altDdificil.append(input("Digite a alternativa D: "))
            gabdificil.append(input("Qual é a alternativa correta (gabarito)? ").lower())
            print("Cadastrado com sucesso!")
            print("\n")
            maxD += 1
            inic = int(input("1- JOGAR\n2- ADICIONAR PERGUNTAS\n3- AJUDA\n4- Encerrar\n"))
            while inic != 1 and inic != 2 and inic != 3 and inic != 4:
                inic = int(input("Digite uma opção válida!\n"))

    # GAME

    while inic == 1 and r == 0:
        print("PULAR (digite 'P'): %d | AJUDA (digite 'help'): %d\nQUESTÃO:" % (skip, Help))
        resp = input(p1).lower()
        while resp != 'a' and resp != 'b' and resp != 'c' and resp != 'd' and resp != 'p' and resp != 'help':
            resp = input("Digite uma resposta válida!\n").lower()
            print('\n')
        if resp == 'help' and Help == 1:
            Help -= 1
            helpp()
            resp = input().lower()
        if resp == 'help' and Help == 0:
            resp = input("Você já utilizou esta ajuda!\n").lower()
        if resp == 'p' and skip == 1:
            skip -= 1
            resp = 'c'
        if resp == 'p' and skip == 0:
            resp = input("Você já utilizou esta ajuda!\n").lower()
        if resp == 'c':
            print("Parabéns, você já conquistou R$ %s" % (premioA[0]))
            f = input("Você deseja parar ou continuar?\nP- Parar\nC-Continuar\n").lower()
            while f != 'c' and f != 'p':
                f = input("Digite uma opção válida:\n")
            if f == 'p':
                stop = 1
                print("Muito bem! Hoje você leva pra casa R$ %s" % (premioP[j]))
            r = 1
        else:
            lose = 1
            r = 1

        # Fáceis
        while inic == 1 and r == 1:
            while stop == 0 and lose == 0 and pause == 0:
                for i in range(0, a, 1):
                    if lose == 0 and stop == 0:
                        x = random.randint(0, maxF)
                        while (x in validar) == 1:
                            x = random.randint(0, maxF)
                        validar.append(x)
                        print('\n')
                        print("PULAR (digite 'P'): %d | AJUDA (digite 'help'): %d\nQUESTÃO:" % (skip, Help))
                        print(listafacil[x])
                        print('A) ', end="")
                        print(altAfacil[x])
                        print('B) ', end="")
                        print(altBfacil[x])
                        print('C) ', end="")
                        print(altCfacil[x])
                        print('D) ', end="")
                        print(altDfacil[x])
                        resp = input().lower()
                        while resp != 'a' and resp != 'b' and resp != 'c' and resp != 'd' and resp != 'p' \
                                and resp != 'help':
                            resp = input("Digite uma resposta válida!\n").lower()
                        if resp == 'help' and Help == 1:
                            Help -= 1
                            helpp()
                            resp = input().lower()
                        if resp == 'help' and Help == 0:
                            resp = input("Você já utilizou esta ajuda!\n").lower()
                        if resp == 'p' and skip == 0:
                            resp = input("Você já utilizou esta ajuda!\n").lower()
                        if resp == 'p' and skip == 1:
                            skip -= 1
                            a += 1
                        if resp != gabfacil[x] and resp != 'p':
                            lose = 1
                        if resp == gabfacil[x]:
                            j += 1
                            f = input(
                                "Parabéns! Você conquistou R$ %s\nVocê deseja parar ou continuar?\nP- Parar\n"
                                "C-Continuar\n" % (premioA[j])).lower()
                            while f != 'c' and f != 'p':
                                f = input("Digite uma opção válida:\n")
                            if f == 'p':
                                ctz = input(
                                    "Tem certeza? Se desistir agora você só leva R$ %s... Se conseguir acertar a "
                                    "próxima, garante %s... Quer mesmo desistir?\nS- Sim\nN- Não\n"
                                    % (premioP[j], premioA[j + 1])).lower()
                                while ctz != 's' and ctz != 'n':
                                    ctz = input('Digite uma opção válida!')
                                if ctz == 'n':
                                    print("Então vamos continuar!")
                                else:
                                    stop = 1
                                    print("Muito bem! Hoje você leva pra casa R$ %s" % (premioP[j]))
                pause = 1
            pause = 0
            validar.clear()

            # Médias

            while pause == 0 and stop == 0 and lose == 0:
                for i in range(0, b, 1):
                    if lose == 0 and stop == 0:
                        x = random.randint(0, maxM)
                        while (x in validar) == 1:
                            x = random.randint(0, maxM)
                        validar.append(x)
                        print("PULAR (digite 'P'): %d | AJUDA (digite 'help'): %d\nQUESTÃO:" % (skip, Help))
                        print(listamedio[x])
                        print('A) ', end="")
                        print(altAmedio[x])
                        print('B) ', end="")
                        print(altBmedio[x])
                        print('C) ', end="")
                        print(altCmedio[x])
                        print('D) ', end="")
                        print(altDmedio[x])
                        resp = input().lower()
                        while resp != 'a' and resp != 'b' and resp != 'c' and resp != 'd' and resp != 'p' \
                                and resp != 'help':
                            resp = input("Digite uma resposta válida!\n").lower()
                        if resp == 'help' and Help == 1:
                            Help -= 1
                            helpp()
                            resp = input().lower()
                        if resp == 'help' and Help == 0:
                            resp = input("Você já utilizou esta ajuda!\n").lower()
                        if resp == 'p' and skip == 0:
                            resp = input("Você já utilizou esta ajuda!\n").lower()
                        if resp == 'p' and skip == 1:
                            skip -= 1
                            b += 1
                        if resp != gabmedio[x] and resp != 'p':
                            lose = 1
                        if resp == gabmedio[x]:
                            j += 1
                            f = input(
                                "Parabéns! Você conquistou R$ %s\nVocê deseja parar ou continuar?\n"
                                "P- Parar\nC-Continuar\n" % (premioA[j])).lower()
                            while f != 'c' and f != 'p':
                                f = input("Digite uma opção válida:\n")
                            if f == 'p':
                                ctz = input(
                                    "Tem certeza? Se desistir agora você só leva R$ %s... "
                                    "Se conseguir acertar a próxima, garante %s... Quer mesmo desistir?\n"
                                    "S- Sim\nN- Não\n" % (premioP[j], premioA[j + 1])).lower()
                                while ctz != 's' and ctz != 'n':
                                    ctz = input('Digite uma opção válida!')
                                if ctz == 'n':
                                    print("Então vamos continuar!")
                                else:
                                    stop = 1
                                    print("Muito bem! Hoje você leva pra casa R$ %s" % (premioP[j]))
                pause = 1
            pause = 0
            validar.clear()

            # Difíceis

            while pause == 0 and stop == 0 and lose == 0:
                for i in range(0, c, 1):
                    if lose == 0 and stop == 0:
                        x = random.randint(0, maxD)
                        while (x in validar) == 1:
                            x = random.randint(0, maxD)
                        validar.append(x)
                        print("PULAR (digite 'P'): %d | AJUDA (digite 'help'): %d\nQUESTÃO:" % (skip, Help))
                        print(listadificil[x])
                        print('A) ', end="")
                        print(altAdificil[x])
                        print('B) ', end="")
                        print(altBdificil[x])
                        print('C) ', end="")
                        print(altCdificil[x])
                        print('D) ', end="")
                        print(altDdificil[x])
                        resp = input().lower()
                        while resp != 'a' and resp != 'b' and resp != 'c' and resp != 'd' \
                                and resp != 'p' and resp != 'help':
                            resp = input("Digite uma resposta válida!\n").lower()
                        if resp == 'help' and Help == 1:
                            Help -= 1
                            helpp()
                            resp = input().lower()
                        if resp == 'help' and Help == 0:
                            resp = input("Você já utilizou esta ajuda!\n").lower()
                        if resp == 'p' and skip == 0:
                            resp = input("Você já utilizou esta ajuda!\n").lower()
                        if resp == 'p' and skip == 1:
                            skip -= 1
                            c += 1
                        if resp != gabdificil[x] and resp != 'p':
                            lose = 1
                        if resp == gabdificil[x]:
                            j += 1
                            f = input(
                                "Parabéns! Você conquistou R$ %s\nVocê deseja parar ou continuar?\n"
                                "P- Parar\nC-Continuar\n" % (premioA[j])).lower()
                            while f != 'c' and f != 'p':
                                f = input("Digite uma opção válida:\n")
                            if f == 'p':
                                ctz = input("Tem certeza? Se desistir agora você só leva R$ %s... "
                                            "Se conseguir acertar a próxima, garante %s... Quer mesmo desistir?\n"
                                            "S- Sim\nN- Não\n" % (premioP[j], premioA[j + 1])).lower()
                                while ctz != 's' and ctz != 'n':
                                    ctz = input('Digite uma opção válida!')
                                if ctz == 'n':
                                    print("Então vamos continuar!")
                                else:
                                    stop = 1
                                    print("Tudo bem! Hoje você leva pra casa R$ %s" % (premioP[j]))
                pause = 1
                if stop == 0 and lose == 0:
                    print("* Pergunta do Milhão *")
                    resp = input(p15).lower()
                    while resp != 'a' and resp != 'b' and resp != 'c' and resp != 'd':
                        resp = input("Digite uma resposta válida!\n").lower()
                    if resp == 'c':
                        print("VOCÊ GANHOU!!! PARABÉNS!!!\n 🎉🎉🎉🎉🎉🎉🎉🎉\n")
                        inic = int(input("1- JOGAR NOVAMENTE\n2- ADICIONAR PERGUNTAS\n3- AJUDA\n"))
                        while inic != 1 and inic != 2 and inic != 3:
                            inic = int(input("Digite uma opção válida!\n"))
                    else:
                        lose = 1

                # se perdeu:
            if lose == 1:
                print("Que pena! Você errou!\n😭😭😭😭😭😭\nHoje você só leva R$ %s\n" % (premioE[j]))
                inic = int(input("1- JOGAR NOVAMENTE\n2- ADICIONAR PERGUNTAS\n3- AJUDA\n4- Encerrar\n"))
                if inic == 1:
                    r = 0
                lose = 0
                stop = 0
                pause = 0
                skip = 1
                Help = 1
                j = -1
                validar.clear()
                while inic != 1 and inic != 2 and inic != 3 and inic != 4:
                    inic = int(input("Digite uma opção válida!\n"))
            if stop == 1:
                inic = int(input("1- JOGAR NOVAMENTE\n2- ADICIONAR PERGUNTAS\n3- AJUDA\n4-Encerrar\n"))
                if inic == 1:
                    r = 0
                lose = 0
                stop = 0
                pause = 0
                skip = 1
                Help = 1
                j = -1

    while inic == 3:
        print(
            "\n\n- O jogo do milhão é um game de perguntas e respostas, que testa seus conhecimentos gerais. "
            "O objetivo é simples, acertas todas as perguntas! -\n\n")
        inic = int(input("1- JOGAR\n2- ADICIONAR PERGUNTAS\n3- AJUDA\n4- Encerrar\n"))
        while inic != 1 and inic != 2 and inic != 3 and inic != 4:
            inic = int(input("Digite uma opção válida!\n"))