from django.core.exceptions import ValidationError

def validate_image(image):
    # Boyut kontrolü (maksimum 5MB)
    filesize = image.size
    megabyte_limit = 5
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Maksimum dosya boyutu: {megabyte_limit}MB")

    # Uzantı kontrolü (sadece .jpg, .jpeg, .png)
    valid_extensions = ['.jpg', '.jpeg', '.png']
    if not any(image.name.lower().endswith(ext) for ext in valid_extensions):
        raise ValidationError("Sadece .jpg, .jpeg ve .png dosyalarına izin verilir.")
