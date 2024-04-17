# MouseClick

# Documentação do Projeto

Este projeto consiste em um conjunto de scripts Python para capturar coordenadas de cliques do mouse e realizar cliques em pontos específicos, com a capacidade de repetir os cliques várias vezes.

## Scripts Incluídos

1. **capture_coordinates.py**: Este script captura as coordenadas dos cliques do mouse em tempo real e armazena em uma lista.
2. **click_points.py**: Este script contém funções para realizar cliques em pontos específicos do mouse, bem como funções auxiliares para realizar cliques repetidos.
3. **main.py**: O script principal que integra os dois scripts anteriores para capturar coordenadas e realizar cliques em pontos específicos.

## Como Usar

### 1. Capture Coordenadas

Para capturar coordenadas de cliques do mouse, execute o script `capture_coordinates.py`. Este script iniciará um ouvinte de mouse e teclado. Pressione a tecla 'x' ou 't' para encerrar a captura de coordenadas. As coordenadas capturadas serão exibidas na saída padrão.

```bash
python capture_coordinates.py
```

### 2. Realize Cliques em Pontos Específicos

Após capturar as coordenadas desejadas, você pode executar cliques nos pontos específicos utilizando o script click_points.py. Este script permite clicar em uma lista de pontos aleatórios e clicar repetidamente em um ponto específico.

```bash
python click_points.py
```

### 3. Executar o Processo Principal

Para integrar a captura de coordenadas e os cliques em pontos específicos em um processo contínuo, execute o script principal main.py. Este script irá solicitar o número desejado de repetições e executar os cliques nos pontos capturados.

```bash
python main.py
```

Certifique-se de ter todas as dependências instaladas antes de executar os scripts. Você pode instalá-las usando o pip:

```bash
pip install pynput
```


- Ao executar o main.py, você deve clicar no local onde deseja registrar o ponto de click.
- Quando terminar, pressione 'x' ou 't' do teclado para finalizar a captura. O console mostrará os pontos registrados.
- Digite o número de repetições que vai executar.
- Pressione qualquer tecla para iniciar.