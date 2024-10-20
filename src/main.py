from watermark import Watermark


def main():
    watermark = Watermark()

    # Configurações do watermark
    watermark.configure_watermark(
        space_between=0,
        resize_percentage=10,
        padding=40,
        rotate_angle=45,
        watermark_opacity=10
    )

    # Adiciona watermark a uma única imagem
    watermark.add_watermark_to_image(
        input_image='imgs/main.jpg',
        watermark_image='imgs/watermark.png',
        output_image='imgs/output_image.png',
        format=watermark.Formats.PNG
    )

    # Adiciona watermark a todas as imagens de uma pasta
    watermark.add_watermark_to_images_folder(
        input_images_folder='input_images_folder',
        watermark_image='watermark_image.png',
        output_image_folder='output_images_folder',
        format=watermark.Formats.PNG
    )


if __name__ == "__main__":
    main()
