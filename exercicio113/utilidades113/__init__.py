def leiaint(nu):
    while True:
        try:
            n = int(input(nu))
        except (TypeError, ValueError):
            print('Erro: Digite uma opção válida.\033[m')
        except KeyboardInterrupt:
            print('O usuário não digitou nenhum valor.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            f = float(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mErro: Digite um Real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mO usuário não digitou qualaquer valor\033[m')
            return 0
        else:
            return f

