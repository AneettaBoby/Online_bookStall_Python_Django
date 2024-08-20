from PIL import Image
import os


def combine_images(image_path1, image_path2, output_path):
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

    width1, height1 = image1.size
    width2, height2 = image2.size

    combined_width = width1 + width2
    combined_height = max(height1, height2)

    combined_image = Image.new('RGB', (combined_width, combined_height))

    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (width1, 0))

    combined_image.save(output_path)
# your_app/utils.py
from django.utils.text import slugify

def generate_unique_slug(model_instance, slug_field, slug_base):
    """
    Generate a unique slug for a given model instance.
    """
    slug = slugify(slug_base)
    model_class = model_instance.__class__

    # Check if the slug is unique
    if not model_class.objects.filter(**{slug_field: slug}).exists():
        return slug

    # If not unique, append a number and check again
    counter = 1
    while model_class.objects.filter(**{slug_field: f"{slug}-{counter}"}).exists():
        counter += 1

    return f"{slug}-{counter}"
