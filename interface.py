import PySimpleGUI as sg 

def interface():
    layout = [
        [sg.Text('Deseja iniciar a automação agora?')],
        [
            sg.Button('Iniciar', button_color='green', size=(8,1)), 
            sg.Button('Cancelar',button_color='red',  size=(8,1))
        ],
        [sg.Output(size=(40,7))],
        [sg.Button('Finalizar', button_color='black',  size=(8,1), disabled=True)]
    ]

    return sg.Window('Download de vídeo MP4', layout=layout)
