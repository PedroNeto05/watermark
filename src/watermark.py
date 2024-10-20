from enum import Enum
from PIL import Image
import os
import numpy as np


class Watermark:

    class Formats(Enum):
        PNG = 'PNG'
        TIFF = 'TIFF'
        WEBP = 'WEBP'
        GIF = 'GIF'

    def __init__(self):
        self.__configurations: dict[str, int] = {
            'space_between': 0,
            'resize_percentage': 0,
            'padding': 0,
            'rotate_angle': 0,
            'watermark_opacity': 0,
        }

    def add_watermark_to_image(self, input_image: str, watermark_image: str, output_image: str, format: Formats):
        self.__main_image = Image.open(input_image).convert('RGBA')
        self.__watermark_image = Image.open(watermark_image).convert('RGBA')
        self.__output_path = output_image

        main_width, main_height, watermark_width, watermark_height = self.__get_image_sizes()

        new_watermark_width, new_watermark_height = self.__calculate_new_dimensions(
            watermark_width, watermark_height)

        self.__watermark_image = self.__watermark_image.resize(
            (new_watermark_width, new_watermark_height), Image.Resampling.LANCZOS)

        padding = self.__configurations['padding']
        space_between = self.__configurations['space_between']

        num_watermarks_width, num_watermarks_height = self.__determine_num_watermarks(
            main_width, main_height, new_watermark_width, new_watermark_height, padding, space_between)

        transparent_main = Image.new(
            'RGBA', self.__main_image.size, (0, 0, 0, 0))
        transparent_main.paste(self.__main_image, (0, 0))
        self.__main_image = transparent_main

        self.__adjust_watermark_opacity()

        rotate_angle = self.__configurations['rotate_angle']
        self.__watermark_image = self.__watermark_image.rotate(rotate_angle)

        self.__apply_watermarks(new_watermark_width, new_watermark_height,
                                padding, space_between, num_watermarks_width, num_watermarks_height)

        self.__main_image.save(output_image, format.value)

    def __apply_watermarks(self, new_watermark_width: int, new_watermark_height: int, padding: int, space_between: int, num_watermarks_width: int, num_watermarks_height: int):
        for i in range(int(num_watermarks_width)):
            for j in range(int(num_watermarks_height)):
                position = (padding + i * (new_watermark_width + space_between),
                            padding + j * (new_watermark_height + space_between))
                self.__main_image.paste(
                    self.__watermark_image, position, mask=self.__watermark_image)

    def __adjust_watermark_opacity(self):
        watermark_opacity = self.__configurations['watermark_opacity'] / 100
        watermark_array = np.array(self.__watermark_image)
        watermark_array[..., 3] = (
            watermark_array[..., 3] * watermark_opacity).astype(np.uint8)
        self.__watermark_image = Image.fromarray(watermark_array, 'RGBA')

    def __determine_num_watermarks(self, main_width, main_height, new_watermark_width, new_watermark_height, padding, space_between):
        num_watermarks_width = (main_width - 2 * padding +
                                space_between) // (new_watermark_width + space_between)
        num_watermarks_height = (main_height - 2 * padding +
                                 space_between) // (new_watermark_height + space_between)

        return num_watermarks_width, num_watermarks_height

    def __calculate_new_dimensions(self, watermark_width, watermark_height):
        resize_percentage = self.__configurations['resize_percentage']
        new_watermark_width = int(watermark_width * (resize_percentage / 100))
        new_watermark_height = int(watermark_height * (resize_percentage / 100))
        return new_watermark_width, new_watermark_height

    def __get_image_sizes(self):
        main_width, main_height = self.__main_image.size
        watermark_width, watermark_height = self.__watermark_image.size
        return main_width, main_height, watermark_width, watermark_height

    def add_watermark_to_images_folder(self, input_images_folder: str, watermark_image: str, output_image_folder: str, format: Formats):

        if not os.path.exists(output_image_folder):
            os.makedirs(output_image_folder)

        for filename in os.listdir(input_images_folder):
            input_image_path = os.path.join(input_images_folder, filename)
            output_image_path = os.path.join(output_image_folder, filename)

            if os.path.isfile(input_image_path):
                self.add_watermark_to_image(
                    input_image_path, watermark_image, output_image_path, format)

    def configure_watermark(self, space_between: int = 0, resize_percentage: int = 0, padding: int = 0, rotate_angle: int = 0, watermark_opacity: int = 0):
        self.__configurations['space_between'] = space_between
        self.__configurations['resize_percentage'] = resize_percentage
        self.__configurations['padding'] = padding
        self.__configurations['rotate_angle'] = rotate_angle
        self.__configurations['watermark_opacity'] = watermark_opacity
