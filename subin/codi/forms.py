from django.forms import inlineformset_factory
from .models import *

CodiInlineFormSet=inlineformset_factory(Category,
                                         Codi,
                                         fields=['image', 'title', 'description'],
                                         extra=2
                                         )