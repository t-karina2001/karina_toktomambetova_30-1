from django import forms


class ProductCreateForm(forms.Form):
    image = forms.ImageField(required=False)
    title = forms.CharField(max_length=128)
    rate = forms.FloatField()
    description = forms.CharField(widget=forms.Textarea())
    price = forms.FloatField()


class CategoryCreateForm(forms.Form):
    title = forms.CharField(max_length=64)


class ReviewCreateForm(forms.Form):
    user_name = forms.CharField(max_length=128)
    e_mail = forms.CharField(max_length=128)
    description = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField()
