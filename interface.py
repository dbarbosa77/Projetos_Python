
from PySimpleGUI import PySimpleGUI as sg

sg.theme("DarkPurple1")

layout = [
    [sg.Text("Login "), sg.Input(key="usuario", size=(20,1)) ],
    [sg.Text("Senha"), sg.Input(key="senha",password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar o acesso?')],
    [sg.Button("Entrar")]
]

janela= sg.Window("Tela de login", layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'douglas' and valores['senha']=='123456':
            variavel=sg.popup_yes_no("Você vem sempre aqui?")
            if variavel == 'Yes':
                sg.popup_ok("Parabéns pelo bom gosto")
            else:
                sg.popup_ok("Por que? nos deixe seu feedback.")
                '''
                sg.theme("DarkPurple1")
                layoutrecusa=[
                    [sg.Text("Por que? nos deixe seu feedback."),sg.Input(key='opinião', size=(20,1))],
                    [sg.Button("Enviar")],
                ]
                janelarecusa=sg.Window("Feedback", layoutrecusa)
                sg.popup_ok(janelarecusa)
                '''
                
        else:
            sg.popup_error("Acesso incorreto")




