#cronometro
import PySimpleGUI as sg
from time import *
sg.theme('DarkGrey5')
sg.theme_background_color('#e89a80')

layout = [
    [sg.Text('',size=(15,1), justification='center', font=('Helvetica', 40), key='timer',background_color='#e89a80')],
    [sg.Button('Começar',size=(15,1), button_color='#e89a80'), sg.Button('Parar', size=(15,1), button_color='#e89a80'),sg.Button('Continuar', size=(15,1), button_color='#e89a80')]
]
tela1 = sg.Window('Cronometro', layout, finalize=True)
inicio = None
while True:
    eventos, valores = tela1.read(timeout=1000)
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Começar' and inicio is None:
        inicio = time() - (tempodecorrido if inicio is not None else 0)
    if eventos == 'Parar' and inicio is not None:
        inicio = None
    if eventos == 'Continuar' and inicio is None:
        inicio = time() - tempodecorrido
    if inicio is not None:
        tempodecorrido = time() - inicio
        minutos, segundos = divmod(tempodecorrido, 60)
        horas, minutos = divmod(minutos, 60)
        tela1['timer'].update('{:.0f}h;{:.0f}m;{:.0f}s'.format(horas, minutos, segundos))