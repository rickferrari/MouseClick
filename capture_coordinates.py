from pynput.mouse import Listener, Button
from pynput import keyboard

# Variável global para indicar se o listener do mouse deve parar
should_stop = False

# Lista para armazenar as coordenadas dos cliques do mouse
click_coordinates = []

# Função para capturar as coordenadas do mouse quando ocorre um clique
def on_click(x, y, button, pressed):
    if pressed:
        print('Clique detectado! Coordenadas do mouse: {0}, {1}'.format(x, y))
        click_coordinates.append((x, y))

        global should_stop
        if should_stop:
            return False

# Função para encerrar o programa quando uma tecla específica é pressionada
def on_press(key):
    global should_stop
    try:
        if key.char == 'x' or key.char == 't':
            print("Tecla de encerramento pressionada. Encerrando o programa...")
            should_stop = True
            return False  # Retorna False para encerrar o listener de teclado
    except AttributeError:
        pass


def start_capture():
    global click_coordinates
    
    mouse_listener = Listener(on_click=on_click)     # Criar um listener para o mouse
    keyboard_listener = keyboard.Listener(on_press=on_press)    # Criar um listener para o teclado
    
    # Iniciar os listeners em threads separadas
    mouse_listener.start()
    keyboard_listener.start()

    try:
        # Aguardar até que o listener de teclado termine
        keyboard_listener.join()
    except KeyboardInterrupt:
        # Encerrar o listener de mouse
        mouse_listener.stop()

    return click_coordinates
