This project is a tool to add watermarks to individual images or all images in a folder.

## Features

- Add watermark to a single image.
- Add watermark to all images in a folder.
- Configure the watermark with options such as space between marks, resize percentage, padding, rotation angle, and opacity.

## Installation

1. Clone the repository:
  ```sh
  git clone https://github.com/PedroNeto05/watermark.git
  ```
2. Navigate to the project directory:
  ```sh
  cd watermark
  ```
3. Install the dependencies:
  ```sh
  pip install -r requirements.txt
  ```

## Usage

### Watermark Configuration

In the `main.py` file, configure the watermark options:
```python
watermark.configure_watermark(
  space_between=0,
  resize_percentage=10,
  padding=40,
  rotate_angle=45,
  watermark_opacity=10
)
```

### Add Watermark to a Single Image

To add a watermark to a single image, use:
```python
watermark.add_watermark_to_image(
  input_image='imgs_examples/main.jpg',
  watermark_image='imgs_examples/watermark.png',
  output_image='imgs_examples/output_image.png',
  format=watermark.Formats.PNG
)
```

### Add Watermark to All Images in a Folder

To add a watermark to all images in a folder, use:
```python
watermark.add_watermark_to_images_folder(
  input_images_folder='input_images_folder',
  watermark_image='watermark_image.png',
  output_image_folder='output_images_folder',
  format=watermark.Formats.PNG
)
```

### Run the Script

To run the script, use:
```sh
python main.py
```

## Dependencies

- Python 3.x
- Pillow
- NumPy

## Contribution

Contributions are welcome! Feel free to open issues and pull requests.