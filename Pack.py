def IpFinder(hostname):

    import PySimpleGUI as Pysg
    import socket
    
    hostname = hostname
    local_ip = socket.gethostbyname(hostname)

    Pysg.theme('DarkBlue16')
    layout = [
        [Pysg.Text("O Nome do seu Computador é: {}".format(hostname))],
        [Pysg.Text("E o seu Ip é: {}".format(local_ip))]
        ]
    janela = Pysg.Window('Ip Finder', layout)

    while True:
        desenhar, atualizar = janela.read()

        if desenhar == Pysg.WINDOW_CLOSED or desenhar == 'Quit':
            Pysg.Popup('Tchau até a proxima!',auto_close = True, auto_close_duration=(2) )
            break
