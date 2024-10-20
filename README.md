# Watermark Project

Este projeto é uma ferramenta para adicionar marcas d'água a imagens individuais ou a todas as imagens em uma pasta.

## Funcionalidades

- Adicionar marca d'água a uma única imagem.
- Adicionar marca d'água a todas as imagens de uma pasta.
- Configurar a marca d'água com opções como espaço entre marcas, porcentagem de redimensionamento, padding, ângulo de rotação e opacidade.

## Instalação

1. Clone o repositório:
  ```sh
  git clone https://github.com/PedroNeto05/watermark.git
  ```
2. Navegue até o diretório do projeto:
  ```sh
  cd watermark
  ```
3. Instale as dependências:
  ```sh
  pip install -r requirements.txt
  ```

## Uso

### Configuração da Marca d'Água

No arquivo `main.py`, configure as opções da marca d'água:
```python
watermark.configure_watermark(
  space_between=0,
  resize_percentage=10,
  padding=40,
  rotate_angle=45,
  watermark_opacity=10
)
```

### Adicionar Marca d'Água a uma Única Imagem

Para adicionar uma marca d'água a uma única imagem, use:
```python
watermark.add_watermark_to_image(
  input_image='imgs_examples/main.jpg',
  watermark_image='imgs_examples/watermark.png',
  output_image='imgs_examples/output_image.png',
  format=watermark.Formats.PNG
)
```

### Adicionar Marca d'Água a Todas as Imagens de uma Pasta

Para adicionar uma marca d'água a todas as imagens de uma pasta, use:
```python
watermark.add_watermark_to_images_folder(
  input_images_folder='input_images_folder',
  watermark_image='watermark_image.png',
  output_image_folder='output_images_folder',
  format=watermark.Formats.PNG
)
```

### Executar o Script

Para executar o script, use:
```sh
python main.py
```

## Dependências

- Python 3.x
- Pillow
- NumPy

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.
