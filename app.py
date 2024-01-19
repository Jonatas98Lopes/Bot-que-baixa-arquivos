import pyautogui as pg
import pyperclip
from random import randint
from time import sleep 



def clicar(x: int, y:int):
    pg.click(x=x, y=y, duration=2)
    sleep(2)


def pressionar_botao(botao:str):
    if botao in pg.KEYBOARD_KEYS:
        pg.press(botao)
        sleep(2)
    else: 
        mensagem = 'Botão inválido. Esse botão não existe na biblioteca.\n'\
            f' Lista de botões válidos abaixo:\n{pg.KEYBOARD_KEYS}'
        raise Exception(mensagem)


def digitar_texto(texto: str): 
    pyperclip.copy(texto)
    executar_atalho('ctrl', 'v')
    sleep(2)


def esperar_pagina_carregar():
    sleep(40)


def executar_atalho(botao1: str, botao2:str):
    if (botao1 in pg.KEYBOARD_KEYS) and (botao2 in pg.KEYBOARD_KEYS):
        pg.hotkey(botao1, botao2)
        sleep(2)
    else: 
        mensagem = 'Um ou mais botões inválidos. Digite botões válidos.\n'\
            f' Lista de botões válidos abaixo:\n{pg.KEYBOARD_KEYS}'
        raise Exception(mensagem)


def rolar_pagina(pixels: int):
    if type(pixels) == int:
        pg.scroll(pixels)
    else:
        raise Exception("Valor informado inválido. Valor digitado não é do tipo 'int'.")

# Abrindo o navegador:
pressionar_botao('win')
digitar_texto('Google Chrome')
pressionar_botao('enter')
clicar(x=302, y=643)
executar_atalho('alt', 'space')
[pressionar_botao('up') for i in range(7)]
pressionar_botao('enter')

# Acessando o site: https://file-examples.com/
digitar_texto('https://file-examples.com/')
pressionar_botao('enter')
esperar_pagina_carregar()
clicar(x=733, y=478)

# Acessando a página: https://file-examples.com/index.php/sample-video-files/
rolar_pagina(-2100)
clicar(x=301, y=58)
digitar_texto('https://file-examples.com/index.php/sample-video-files/')
pressionar_botao('enter')
esperar_pagina_carregar()

# Acessando a página de vídeo MP4
clicar(x=733, y=478)
rolar_pagina(-2100)
clicar(x=960, y=157)


