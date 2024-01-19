import pyautogui as pg
import pyperclip
from time import sleep
import PySimpleGUI as sg 




def print_personalizado(texto):
    print(30 * '=')
    print(texto)
    print(30 * '=')
    print()


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


def clica_imagem_detectada(image_path: str):
    image_position = pg.locateCenterOnScreen(image_path)
    clicar(image_position[0], image_position[1])
    sleep(2)


def main(window: sg.Window):
    # Abrindo o navegador:
    print_personalizado('Abrindo o navegador...')
    pressionar_botao('win')
    digitar_texto('Google Chrome')
    pressionar_botao('enter')
    clicar(x=302, y=643)

    print_personalizado('Maximizando a tela...')
    executar_atalho('alt', 'space')
    try:
        clica_imagem_detectada('maximizar-janela.png')
    except: pass
    pressionar_botao('enter') 
    pressionar_botao('enter') 

    print_personalizado('Acessando o site: https://file-examples.com/...')
    # Acessando o site: https://file-examples.com/
    digitar_texto('https://file-examples.com/')
    pressionar_botao('enter')
    esperar_pagina_carregar()
    clicar(x=733, y=478)

    # Acessando a página: https://file-examples.com/index.php/sample-video-files/
    print_personalizado('Acessando a página de tipo de vídeo...')
    rolar_pagina(-2100)
    clicar(x=301, y=58)
    digitar_texto('https://file-examples.com/index.php/sample-video-files/')
    pressionar_botao('enter')
    esperar_pagina_carregar()

    # Acessando a página de vídeo MP4
    print_personalizado('Acessando a página de MP4...')
    clicar(x=733, y=478)
    rolar_pagina(-2100)
    clicar(x=960, y=157)
    esperar_pagina_carregar()
    try:
        clica_imagem_detectada('fechar-propaganda.png')
    except:
        clicar(x=1077, y=204)


    print_personalizado('Acessando a página de vídeos de 10MB...')
    # Acessando a página de vídeo de 10MB
    clicar(x=733, y=478)
    rolar_pagina(-700)
    clicar(x=987,y=306)
    esperar_pagina_carregar()

    # Fazendo download do vídeo.
    print_personalizado('Fazendo download do vídeo...')
    clicar(x=1228, y=675)
    clicar(x=1139, y=585)
    pressionar_botao('enter')
    pressionar_botao('enter')
    sleep(10)
    clicar(x=733, y=478)
    executar_atalho('alt', 'f4')
    window.write_event_value('encerrado', '')
    print_personalizado('Automação encerrada...')


