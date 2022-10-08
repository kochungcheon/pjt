from platform import release
from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    Choice = (
        ('comedy', '코미디'),
        ('action', '액션'),
        ('romance', '로맨스'),
        ("horror", '공포'),
        ("animation", '호러'),
        ("fantasy", '판타지')
    )   

    genre = forms.ChoiceField(choices=Choice)
    
    score = forms.FloatField(
        widget=forms.NumberInput
        (
        attrs = {
            'min': 0,
            'max': 5,
            'step': 0.5,
        }    
        )
        
    )

    release_date = forms.DateField(
        widget=forms.DateInput(

            attrs = {
                'type': 'date',
            }
        )




    )
        

    class Meta:
        model = Movie
        fields = '__all__'