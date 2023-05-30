from exercicio113.utilidades113 import leiaint

def linha(tam=42):
    return '-'*tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lst):
    cabecalho('MENU PRICIPAL')
    c = 1
    for item in lst:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('Sua Opção: ')
    return opc

def atu(lst):
    cabecalho('ATUALIZAÇÃO')
    c = 1
    for item in lst:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('Sua Opção: ')
    return opc