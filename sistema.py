from menu.bib.interface import *
from menu.bib.arq import *
from time import sleep

while True:
    resposta = menu(['Usuários Cadastrados', 'Cadastrar Usuário', 'Atualizar Usuário', 'Deletar Usuário', 'Sair do Sistema'])

    if resposta == 1:
        result = select('nome, datanasc, endereco, cidade, uf, cpf', 'alunos')
        id = int(input('ID do aluno: '))
        print(f'Nome: {result[id - 1]["nome"]}')
        print(f'Nascimento: {result[id - 1]["datanasc"]}')
        print(f'Endereço: {result[id - 1]["endereco"]}')
        print(f'Cidade: {result[id - 1]["cidade"]}')
        print(f'UF: {result[id - 1]["uf"]}')
        print(f'CPF: {result[id - 1]["cpf"]}')

    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        datanasc = str(input('Nascimento: '))
        endereco = str(input('Endereço: '))
        cidade = str(input('Cidade: '))
        uf = str(input('Uf: '))
        cpf = str(input('Cpf: '))
        values = [f"DEFAULT,'{nome}', '{datanasc}', '{endereco}', '{cidade}', '{uf}', '{cpf}' "]
        insert(values, 'alunos')

    elif resposta == 3:
        print('O que deseja atualizar?')
        res = atu(['nome', 'datanasc', 'endereco', 'cidade', 'uf', 'cpf'])

        if res == 1:
            nome = str(input('Nome: '))
            id = int(input('ID do aluno: '))
            update({'nome': nome}, "alunos", f'id_aluno = {id}')

        elif res == 2:
            nasc = str(input('Nascimento: '))
            id = int(input('ID do aluno: '))
            update({'datanasc': nasc}, "alunos", f'id_aluno = {id}')

        elif res == 3:
            end = str(input('Endereço: '))
            id = int(input('ID do aluno: '))
            update({'endereco': end}, "alunos", f'id_aluno = {id}')

        elif res == 4:
            cid = str(input('Cidade: '))
            id = int(input('ID do aluno: '))
            update({'cidade': cid}, "alunos", f'id_aluno = {id}')

        elif res == 5:
            uf = str(input('Uf: '))
            id = int(input('ID do aluno: '))
            update({'uf': uf}, "alunos", f'id_aluno = {id}')

        elif res == 6:
            cpf = str(input('CPF: '))
            id = int(input('ID do aluno: '))
            update({'datanasc': cpf}, "alunos", f'id_aluno = {id}')

    elif resposta == 4:
        id = int(input('Id do Usuário: '))
        delete("alunos", f'id_aluno = {id}')

    elif resposta == 5:
        cabecalho('Sistema Encerrado...\033[m')
        break

    else:
        print('Digite uma opção válida\033[m')
        sleep(1.5)
