from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from . import models


class AddFeedForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddFeedForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field('feed_url', placeholder="Feed address"),
            Submit('add_feed', 'Add Feed',
                   css_class="btn btn-lg btn-primary btn-block"),
            )

    class Meta:
        model = models.Feed
        fields = ['feed_url']
