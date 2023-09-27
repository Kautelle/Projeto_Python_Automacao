# Passo a passo do projeto

#passo 01: Entrar no sistema
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui #para intalar - pip install pyautogui 
import time

pyautogui.PAUSE = 0.3
#abrir navegador    
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

#entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#esperar site carregar
time.sleep(3)

#passo 02: Fazer login
pyautogui.click(x=784, y=382)
pyautogui.write("gmail")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")

#passo 03: Importar a base de dados de produtos

import pandas as pd #para instalar - pip install pandas numpy openpyxl

table = pd.read_csv("produtos.csv")

for linha in table.index:
    #passo 04: Cadastrar 1 protduto
    pyautogui.click(x=816, y=272)

    codigo = table.loc[linha, "codigo"] #- forma alternativa

    #preencher os campos

    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "categoria"]))                
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = table.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    #aperta em enviar

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
#passo 05: repetir o cadrastro para todos os produtos








# pyautogui.click - clicar com o mouse (x e y - print(pyautogui.position()) - clicks = numero (para quantidade de clicks))
# pyautogui.write - escrever um texto
# pyautogui.press - apertar 1 tecla
# pyautogui.hotkey - atalho (combinacao de teclas)
# pyautogui.PAUSE = numero - velocidade da execução (numeracao amarecana .)
# time.sleep(numero) - pause de execucao
# pyautogui.scroll(numero) - para dar um scroll na tela numero negativo para baixo ps: tem que fazer teste para ver
# for - tab para identar
#nan = not and number 
# str = string = texto
# pandas = analista

