import pyautogui as pg
import pyperclip
from random import randint
from time import sleep 



def clicar(x: int, y:int):
    pg.click(x=x, y=y, duration=2)
    sleep(1)


def pressionar_botao(botao:str):
    if botao in pg.KEYBOARD_KEYS:
        pg.press(botao)
        sleep(1)
    else: 
        raise Exception('Botão inválido. Esse botão não existe na biblioteca')


def digitar_texto(texto: str): 
    pyperclip.copy(texto)
    pg.hotkey('ctrl', 'v')
    sleep(1)


def esperar_pagina_carregar():
    sleep(40)


# Abrindo o navegador:
pressionar_botao('win')
digitar_texto('Google Chrome')
pressionar_botao('enter')
clicar(x=302, y=643)

# Acessando o site: https://file-examples.com/
digitar_texto('https://file-examples.com/')
pressionar_botao('enter')
esperar_pagina_carregar()
clicar(x=733, y=478)

