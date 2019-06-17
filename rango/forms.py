from django import forms
from rango.models import Page, Category

# Use Django's ModelForm as base for our customized form
class CategoryForm(forms.ModelForm):
    name= forms.CharField(max_length = 128,
                            help_text = "Please enter the category name.")
    views = forms.IntegerField(widget = forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget = forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget = forms.HiddenInput(), required = False)

    # Associates ModelForm to our model
    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length = 128,
                            help_text = "Please enter the title of the page.")
    url = forms.URLField(max_length = 200,
                            help_text = "Please enter the URL of the page.")
    views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)

    class Meta:
        model = Page
        exclude = ('category',)

    # Override clean()
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data
