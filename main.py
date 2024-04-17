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
        if repetitions.strip() == "":
            repetitions = 1000
        else:
            repetitions = int(repetitions)
        
        print("Iniciando cliques nos pontos capturados...")
        # Solicitar que seja pressionada uma tecla para continuar
        input("Pressione qualquer tecla para continuar...")
        
        # Executar os cliques
        for _ in range(repetitions):
            click_points.click_points(points, click_interval)
            click_points.click_specific_point_Yx(specific_point, click_interval, qty_points)
            print("Aguarde {} minutos até a proxima rodada...".format(wait_time))
            time.sleep(wait_time * 60)

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
