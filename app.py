from automacao_site import *
from interface import *
from time import sleep




window = interface()
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancelar', 'Finalizar'): 
        break

    elif event == 'Iniciar':
        window['Iniciar'].update(disabled=True)

        sg.popup('⚠ATENÇÃO! APÓS CLICAR EM "OK" A AUTOMAÇÃO VAI COMEÇAR. NÃO MOVA O'\
            ' MOUSE OU USE TECLADO ATÉ QUE A AUTOMAÇÃO ESTEJA COMPLETA.⚠')
        sleep(3)
        

        main(window)

    elif event == 'encerrado':
        window['Finalizar'].update(disabled=False)


    