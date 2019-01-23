''
    else:
        tentativas -= 1
        print("Errado! %s, ainda lhe restam %d tentativas" %(name_player, tentativas))
        if palpite > numero_secreto:
            print("Sua tentativa era maior que o numero secreto")
        else:
            print("Seu palpite era menor que o numero secreto")
