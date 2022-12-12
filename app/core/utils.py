from PIL import Image
import os


def image_directory_path(instance, filename):
    return 'items/{}'.format(filename)


def convert_to_webp(source):
    """Convert image to WebP.

    Args:
        source (pathlib.Path): Path to source image

    Returns:
        pathlib.Path: path to new image
    """
    destination = source.with_suffix(".webp")

    image = Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp

    return destination


def get_filepath_and_extension(filepath):
    source, extension = os.path.splitext(str(filepath))

    formats = [extension, ]
    if extension in (".jpg", ".png"):
        if os.path.exists(source + ".webp"):
            formats.append(".webp")
    return {"path": source, "formats": formats}
