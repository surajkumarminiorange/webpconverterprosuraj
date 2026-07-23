from pathlib import Path
from PIL import Image

import pillow_avif
from pillow_heif import register_heif_opener

register_heif_opener()


SUPPORTED_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".bmp",
    ".tiff",
    ".tif",
    ".gif",
    ".avif",
    ".heic",
    ".heif",
    ".ico"
}


def convert_image(image_path, output_folder=None, quality=80):
    """
    Converts a single image to WebP.

    Returns:
        (success, message)
    """

    try:

        image_path = Path(image_path)

        if image_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            return False, "Unsupported"

        img = Image.open(image_path)

        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGBA")

        if output_folder:

            output_folder = Path(output_folder)
            output_folder.mkdir(parents=True, exist_ok=True)

            output_file = output_folder / f"{image_path.stem}.webp"

        else:

            output_file = image_path.with_suffix(".webp")

        img.save(
            output_file,
            "WEBP",
            quality=int(quality),
            method=6
        )

        return True, output_file

    except Exception as e:

        return False, str(e)