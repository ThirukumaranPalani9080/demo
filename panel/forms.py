from django import forms  
from .models import Myuser  
class userform(forms.ModelForm):  
    class Meta:  
        model = Myuser  
        fields = "__all__"  