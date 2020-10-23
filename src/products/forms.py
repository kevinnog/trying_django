from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={"placeholder": "Your Title"}))

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "placeholder": "Your description",
            "rows": 20,
            "cols": 80
        })
    )
    price = forms.DecimalField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not "Brain" in title:
            raise forms.ValidationError('Title must contain the word "Brain"')
        return title


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={"placeholder": "Your Title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "placeholder": "Your description",
            "rows": 20,
            "cols": 80
        })
    )
    price = forms.DecimalField()
