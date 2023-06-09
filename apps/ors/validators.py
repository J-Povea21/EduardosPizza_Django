from django.core.exceptions import ValidationError


def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError('El número de teléfono debe contener solo números')
    elif len(value) < 10:
        raise ValidationError('El número de teléfono debe contener al menos 10 dígitos')


def validate_cedula(value):
    if value < 0:
        raise ValidationError('La cédula debe ser un número positivo')

def validate_price(value):
    if value < 0:
        raise ValidationError('El precio debe ser positivo')
