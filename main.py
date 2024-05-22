import capture_coordinates
import click_points
import time
import json
import os

# Função para salvar os dados em um arquivo JSON
def save_to_json(data):
    with open('coordinates.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Função para carregar os dados de um arquivo JSON existente
def load_from_json():
    if os.path.exists('coordinates.json'):
        with open('coordinates.json', 'r') as json_file:
            return json.load(json_file)
    else:
        return []
def run_clicks(points, specific_point, qty_points, click_interval, wait_time, repetitions):
    for i in range(1, repetitions + 1):
        print(f"Rodada {i}:")
        click_points.click_points(points, click_interval)
        click_points.click_specific_point_Yx(specific_point, click_interval, qty_points)
        print(f"Aguarde {wait_time} minutos até a próxima rodada...")
        time.sleep(wait_time * 60)


# Função para coletar as coordenadas
def collect_coordinates():
    print("Capturando coordenadas...")
    return capture_coordinates.start_capture()

# Função principal
def main():
    collected_data = load_from_json()  # Carregar dados existentes, se houver
    count = len(collected_data) + 1  # Determinar o próximo número de chave
    while True:
        click_coordinates = collect_coordinates()
        if click_coordinates:
            specific_point = click_coordinates[0]
            qty_points = len(click_coordinates)
            data_entry = {
                "key": count,
                "coordinates": click_coordinates,
                "specific_point": specific_point,
                "qty_points": qty_points
            }
            collected_data.append(data_entry)
            save_to_json(collected_data)  # Salvar os dados atualizados
            count += 1
            continue_collecting = input("Deseja continuar a coleta? (Y/N): ")
            if continue_collecting.lower() not in ['y', 's']:
                break
        else:
            print("Nenhum clique foi capturado.")
            break

if __name__ == "__main__":
    main()
