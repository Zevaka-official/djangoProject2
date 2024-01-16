from django import forms

from main.models import Product, ProductVersion


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.ChoiceField):
                field.widget.attrs['class'] = 'form-select'
            elif isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control mt-2 mb-2'


class ProductForm(StyleFormMixin, forms.ModelForm):
    RESTRICTED_WORDS = [
        'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
        'дёшево', 'бесплатно', 'обман', 'полиция', 'радар'
    ]

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        for word in name.split():
            if word.lower() in self.RESTRICTED_WORDS:
                raise forms.ValidationError('Недопустимое название')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        for word in description.split():
            if word.lower() in self.RESTRICTED_WORDS:
                raise forms.ValidationError('Недопустимое описание')
        return description


