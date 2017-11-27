#created by Eliel Brisido
#Recebe base de usuario e senha, gera saida com a senha calculada em um dos hashs: MD5,SHA1, SHA256

import hashlib
import time
import string

def hash_md5(x,y):
    hash1 = hashlib.md5(x)
    resmd5 = hash1.hexdigest()
    arquivobasesaidamd5 = open('saidatbasemd5.txt', 'a')
    arquivobasesaidamd5.write(y)
    arquivobasesaidamd5.write("|")
    arquivobasesaidamd5.write(str(resmd5))
    arquivobasesaidamd5.write('\n')
    arquivobasesaidamd5.close()

def hash_sha1(x,y):
    hash2 = hashlib.sha1(x)
    ressha1 = hash2.hexdigest()
    arquivobasesaidasha1 = open('saidatbaseSHA1.txt', 'a')
    arquivobasesaidasha1.write(y)
    arquivobasesaidasha1.write("|")
    arquivobasesaidasha1.write(str(ressha1))
    arquivobasesaidasha1.write('\n')
    arquivobasesaidasha1.close()

def hash_sha256(x,y):
    hash3 = hashlib.sha256(x)
    ressha256 = hash3.hexdigest()
    arquivobasesaidasha256 = open('saidatbaseSHA256.txt','a')
    arquivobasesaidasha256.write(y)
    arquivobasesaidasha256.write("|")
    arquivobasesaidasha256.write(str(ressha256))
    arquivobasesaidasha256.write('\n')
    arquivobasesaidasha256.close()

def submenu():
    print("Escolha em qual modelo deseja buscar:")
    print(" 0 - Sair")
    print(" 1 - MD5")
    print(" 2 - SHA1")
    print(" 3 - SHA256")
    print(" 4 - Base de Senha Original")
    print(" 5 - Voltar ao menu anterior")
    escolha = input("Digite sua opção: ")

    if escolha == '1':
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")
        pipe = "|"
        senhaencoded = senha.encode('utf-8')
        pswhash = hashlib.md5(senhaencoded)
        resmd5 = pswhash.hexdigest()
        userandpsw = usuario+pipe+(str(resmd5))
        arquivomd5 = open('saidatbasemd5.txt', 'r')
        existUserAndPsw = False
        inicio = time.time()
        for line in arquivomd5:
            if userandpsw in line:
                existUserAndPsw = True
                print("Usuario e Senha existem!")
                break;
        fim = time.time()
        if existUserAndPsw != True:
            print("Usuario ou senha invalidos!")
        print(fim - inicio)
        arquivomd5.close()
        submenu()
    elif escolha == '2':
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")
        pipe = "|"
        senhaencoded = senha.encode('utf-8')
        pswhash = hashlib.sha1(senhaencoded)
        ressha1 = pswhash.hexdigest()
        userandpsw = usuario+pipe+(str(ressha1))
        arquivosha1 = open('saidatbaseSHA1.txt', 'r')
        existUserAndPsw = False
        inicio = time.time()
        for line in arquivosha1:
            if userandpsw in line:
                existUserAndPsw =True
                print("Usuario e Senha existem!")
                break;
        fim = time.time()
        if existUserAndPsw != True:
            print("Usuario ou senha invalidos!")
        print(fim - inicio)
        arquivosha1.close()
        submenu()
    elif escolha == '3':
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")
        pipe = "|"
        senhaencoded = senha.encode('utf-8')
        pswhash = hashlib.sha256(senhaencoded)
        ressha256 = pswhash.hexdigest()
        userandpsw = usuario+pipe+(str(ressha256))
        arquivosha256 = open('saidatbaseSHA256.txt', 'r')
        existUserAndPsw = False
        inicio = time.time()
        for line in arquivosha256:
            if userandpsw in line:
                existUserAndPsw = True
                print("Usuario e Senha existem!")
                break;
        fim = time.time()
        if existUserAndPsw != True:
            print("Usuario ou senha invalidos!")
        print(fim - inicio)
        arquivosha256.close()
        submenu()
    elif escolha == '4':
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")
        pipe = "|"
        userandpsw = usuario + pipe + senha
        arquivobaseoriginal = open('base.txt', 'r')
        existUserAndPsw = False
        inicio = time.time()
        for line in arquivobaseoriginal:
            if userandpsw in line:
                existUserAndPsw = True
                print("Usuario e Senha existem!")
                break;
        fim = time.time()
        if existUserAndPsw != True:
            print("Usuario ou senha invalidos!")
        print(fim - inicio)
        arquivobaseoriginal.close()
        submenu()


    elif escolha == '5':
        menu()
    elif escolha == '0':
        print("Saindo...")
    else:
        print("Escolha uma opção valida !")
        submenu()


def menu():
    print("Bem Vindo ao Gerador de Hash !!!")
    print("Escolha as opções de Geração de Hash abaixo : ")
    print(" 0 - Sair")
    print(" 1 - Gerar Hash MD5")
    print(" 2 - Gerar Hash SHA1")
    print(" 3 - Gerar Hash SHA256")
    print(" 4 - Busca par de usuarios e senhas")
    escolha = input("Digite sua opção: ")

    if escolha == '1':
        print("Gerando Hash com MD5...")
        inicio = time.time()
        arquivobasemd5 = open('base.txt', 'r')
        for linha in arquivobasemd5:
            str,str1 = linha.split('|')
            str1 = str1.replace('\n','')
            str1encoded = str1.encode('utf-8')
            hash_md5(str1encoded,str)
        fim = time.time()
        print(fim - inicio)
        arquivobasemd5.close()
        print("Gerado Hash em MD5 !")
        menu()
    elif escolha == '2':
        print("Gerando Hash com SHA1...")
        inicio = time.time()
        arquivobasesha1 = open('base.txt', 'r')
        for linha in arquivobasesha1:
            str,str1 = linha.split('|')
            str1 = str1.replace('\n', '')
            str1encoded = str1.encode('utf-8')
            hash_sha1(str1encoded, str)
        fim = time.time()
        print(fim - inicio)
        arquivobasesha1.close()
        menu()
    elif escolha == '3':
        print("Gerando Hash com SHA256...")
        inicio =time.time()
        arquivobasesha256 =open('base.txt', 'r')
        for linha in arquivobasesha256:
            str, str1 = linha.split('|')
            str1 = str1.replace('\n', '')
            str1encoded =str1.encode('utf-8')
            hash_sha256(str1encoded,str)
        fim = time.time()
        print(fim - inicio)
        arquivobasesha256.close()
        menu()
    elif escolha == '4':
        submenu()

    elif escolha == '0':
        print("Saindo...")
    else :
        print("Escolha uma opção valida !")
        menu()

menu()