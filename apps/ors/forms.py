from django import forms
from django.core.exceptions import ValidationError

from .models import Order, Customer, Pizza, Rating, Coupon, Ingredient


#### form Validator ####

def validate_coupon(value) -> float:
    discount = 0
    try:
        coupon = Coupon.objects.get(code=value)
        discount = coupon.discount
    except Coupon.DoesNotExist:
        raise ValidationError('El cupón ingresado no existe')
    else:
        if coupon.status == 'CANJEADO':
            raise ValidationError('El cupón ingresado ya fue canjeado')
        elif coupon.status == 'DISPONIBLE':
            return discount


#### Forms ####
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        labels = {
            'name': 'Nombre completo*',
            'cedula': 'Cédula*',
            'address': 'Dirección de entrega*',
            'phone_number': 'Número de teléfono*',
        }


class CouponForm(forms.Form):
    code = forms.CharField(
        max_length=7,
        min_length=7,
        validators=[validate_coupon],
        label='Código de cupón',
        required=False,
    )


class OrderForm(forms.ModelForm):
    coupon_code = CouponForm()

    class Meta:
        model = Order

        fields = ['payment_method']

        labels = {
            'payment_method': 'Método de pago',
        }


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza

        fields = ['size', 'mass_type', 'ingredients']

        labels = {
            'size': 'Tamaño',
            'mass_type': 'Masa',
            'ingredients': 'Ingredientes',
        }

        ingredients = forms.ModelMultipleChoiceField(
            queryset=Ingredient.objects.all()
        )

        widgets = {
            'ingredients': forms.CheckboxSelectMultiple(),
        }


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating

        exclude = ['order']

        labels = {
            'rating_value': 'Calificación',
            'message': 'Mensaje (opcional)',
        }