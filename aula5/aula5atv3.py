# TODO

# EM SQUADS

# Leiam o texto abaixo e resolvam.

# Na "JUNTOFIT", se um aluno tiver frequência de 21 vezes, sem interrupções, ele ganha um mês de aulas gratuitas para presentear um acompanhante. Caso contrário, ele não se qualifica para o benefício.

# Na catraca de acesso, haverá uma tela voltada para o cliente. Todos os dias, quando ele passar, deve aparecer a mensagem "VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO"

# Quando ele completar 21 identificações seguidas, deve aparecer a mensagem "UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ".

# Caso o cliente tenha uma certa frequência, mas falte algum dia, quando retornar, deve aparecer "QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO."

# dias_consecutivos = 0

# while True:
#     input("Pressione Enter para simular a passagem na catraca (ou 'q' para sair): ")
#     dias_consecutivos += 1

#     mensagem = "VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO"

#     if dias_consecutivos == 21:
#         mensagem = "UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ."
#         dias_consecutivos = 0
#     elif dias_consecutivos > 1:
#         mensagem = "QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO."
#         dias_consecutivos = 0

#     print(mensagem)

#     if input("Deseja sair? (Digite 'sair' para sair, Enter para continuar): ").lower() == 'sair':
#         break


# frequencia = int(input("INFORME SUA FREQUÊNCIA: "))

# if frequencia < 21 and frequencia > 0:
#     print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO.")

# elif frequencia >= 21:
#     print("UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ.")

# else:
#     print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")


dias_consecutivos = 0

while dias_consecutivos < 21:
    input("Pressione Enter para simular a passagem na catraca (ou 'q' para sair): ")
    dias_consecutivos += 1

    if dias_consecutivos == 21:
        print("UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ.")
    else:
        print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO")

    if input("Deseja sair? (Digite 'q' para sair, Enter para continuar): ").lower() == 'q':
        break

    # Reinicie a contagem se o aluno perder um dia
    if input("Você perdeu um dia? (Digite 's' para sim, Enter para não): ").lower() == 's':
        dias_consecutivos = 0
