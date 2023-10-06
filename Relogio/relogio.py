import PySimpleGUI as sg
from time import *

sg.theme('DarkGrey5')
sg.theme_background_color(color='#C71585')

layout = [
    [sg.Text('Olá Gabriel',size=(22,1), justification='center',font=('Helvetica', 15), background_color='#C71585')],
    [sg.Text('',size=(15,1), justification='center', font=('Helvetica', 20), key='data', background_color='#C71585')],
    [sg.Text('',size=(13,1),justification='center',font=('Helvetica', 24), key='hora', background_color='#C71585')],
    [sg.Button('fechar', button_color='#C71585', )]
]
tela = sg.Window('Relogio', layout, finalize=True)

while True:
    eventos, valores = tela.read(timeout=1000)
    if eventos == 'fechar' or eventos == sg.WIN_CLOSED:
        break
    data = strftime('%d/%m')
    hora = strftime('%H:%M:%S')
    tela['data'].update(data)
    tela['hora'].update(hora)
tela.close()


        