import os
import subprocess
import sys
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
logo = """
                                                                                                            MM    ##
                                                                                                            ##    ##
::                                ##        ##                                MM                              ##
########  ##      ##  ########    ##        ##            ##::##    ######    ############  ########    ##    ##    ######    ####::##
##    ::    ##  ##    ##      ####################      ++++      @@##    @@  ##  ##    ##  ##      ##  ##    ##  ##    ##    ##    ::
##    ##    ##  ##    #           ##        ##          ##        ##      ##  ##  ##    ##    ##    ##  ##    ##  ####        ##
##    ##      ##      ##          ##        ##          ##        @@##  ##    ##  ++    ##    ##  ##--  ##    ##  ##      ##  ##
######mm      ##      #                                   ######    ######    ##    ::  ##    ######    ##    ##    ######    ##
##            ##      #                                                                       ##
##            ##      #######                                                                 ##

github - Obentemiller...
"""

print(logo)

#sintaxe de prompt: python pyc++.py nome_do_cpp_a_ser_executado.cpp
if len(sys.argv) != 2:
    print("Por favor, forneça o nome do arquivo a ser compilado.")
    sys.exit(1)
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
nome_do_arquivo = sys.argv[1]
nome_do_exe = os.path.splitext(nome_do_arquivo)[0] + ".exe"
dev_cmd_path = r"C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\Tools\VsDevCmd.bat"
comando_abrir_prompt = f'"{dev_cmd_path}"'
comando_compilacao = f'cl.exe {nome_do_arquivo} -o {nome_do_exe}'
caminho_completo_arquivo = os.path.join(diretorio_atual, nome_do_arquivo)
caminho_completo_exe = os.path.join(diretorio_atual, nome_do_exe)
comando_final = f'cd /D {diretorio_atual} && {comando_abrir_prompt} && {comando_compilacao}'
resultado_compilacao = subprocess.run(comando_final, shell=True)
if resultado_compilacao.returncode == 0:
    print(f"Compilação bem-sucedida. Executável gerado: {caminho_completo_exe}")
    comando_executar_exe = f'{caminho_completo_exe}'
    resultado_execucao = subprocess.run(comando_executar_exe, shell=True)
    if resultado_execucao.returncode == 0:
        print("Execução bem-sucedida.")
    else:
        print("Erro durante a execução.")
else:
    print("Erro durante a compilação.")
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
