import capture_coordinates
import click_points
import time

def main():
    try:
        # Parte do capture_coordinates.py
        print("Capturando coordenadas...")
        click_coordinates = capture_coordinates.start_capture()

        # Exibindo as coordenadas capturadas
        print("\nCoordenadas dos cliques capturados:")
        if click_coordinates:
            for i, coord in enumerate(click_coordinates, 1):
                print(f"Clique {i}: {coord}")
        else:
            print("Nenhum clique foi capturado.")

        # Parte do click_points.py
        points = click_coordinates
        specific_point = click_coordinates[0]
        qty_points = len(click_coordinates) + 1
        click_interval = 1.2
        wait_time = 5.2

        # Solicitar a quantidade de repetições desejadas
        repetitions = input("Digite o número de repetições desejadas (padrão: 1000): ")
        repetitions = int(repetitions.strip()) if repetitions.strip() else 1000

        print("Iniciando cliques nos pontos capturados...")
        # Solicitar que seja pressionada uma tecla para continuar
        input("Pressione qualquer tecla para continuar...")
        
        # Executar os cliques
        run_clicks(points, specific_point, qty_points, click_interval, wait_time, repetitions)

    except Exception as e:
        print(f"Erro: {e}")

def run_clicks(points, specific_point, qty_points, click_interval, wait_time, repetitions):
    for i in range(1, repetitions + 1):
        print(f"Rodada {i}:")
        click_points.click_points(points, click_interval)
        click_points.click_specific_point_Yx(specific_point, click_interval, qty_points)
        print(f"Aguarde {wait_time} minutos até a próxima rodada...")
        time.sleep(wait_time * 60)

if __name__ == "__main__":
    main()
