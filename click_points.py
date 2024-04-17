import time
from random import shuffle
import pynput.mouse as mouse

# Função para clicar nos pontos listados
def click(x, y):
    mouse_controller = mouse.Controller()
    mouse_controller.position = (x, y)
    mouse_controller.click(mouse.Button.left)
    print(f"Clicando em {x}, {y}")

# Função para clicar em pontos específicos da lista
def click_points(points, click_interval):
    shuffle(points)
    time.sleep(click_interval)   # Intervalo para inicio dos clicks
    for point in points:
        x, y = point
        click(x, y)
        time.sleep(click_interval)  # Intervalo entre os cliques

# Função para clicar no ponto específico Y vezes
def click_specific_point_Yx(specific_point, click_interval, qty_points):
    time.sleep(click_interval)
    for _ in range(qty_points): # Clique Y vezes
        x, y = specific_point
        click(x, y)
        time.sleep(click_interval)

# Executar o processo
def main(points, specific_point, click_interval, wait_time, repetitions):
    try:
        # Clique em cada ponto específico aleatoriamente
        click_points(points, click_interval)

        # Clique no ponto específico Y vezes
        click_specific_point_Yx(specific_point, click_interval, repetitions)

        # Aguardar um determinado tempo
        time.sleep(wait_time * 60)  # Convertendo minutos para segundos

    except Exception as e:
        print(f"Erro: {e}")
