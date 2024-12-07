from django import forms

class ProductosMasVendidosForm(forms.Form):
    semanas_antes = forms.IntegerFIeld(label="Hace cuántas semanas", min_value=1)
