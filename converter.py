from pathlib import Path
from PIL import Image

# Register AVIF support
import pillow_avif


SUPPORTED_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".bmp",
    ".tiff",
    ".tif",
    ".gif",
    ".avif",
    ".ico",
}


def convert_image(image_path, output_folder=None, quality=80, lossless=False):
    """
    Convert a single image to WebP.

    Returns:
        (True, output_path) on success
        (False, error_message) on failure
    """

    try:

        image_path = Path(image_path)

        if image_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            return False, "Unsupported file type"

        img = Image.open(image_path)

        # Preserve transparency where possible
        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGBA")

        if output_folder:

            output_folder = Path(output_folder)
            output_folder.mkdir(parents=True, exist_ok=True)

            output_file = output_folder / f"{image_path.stem}.webp"

        else:

            output_file = image_path.with_suffix(".webp")

        save_kwargs = {
            "quality": int(quality),
            "method": 6,
            "lossless": bool(lossless)
        }

        if getattr(img, "is_animated", False):
            save_kwargs["save_all"] = True

        img.save(
            output_file,
            "WEBP",
            **save_kwargs
        )

        return True, output_file

    except Exception as e:

        return False, str(e)