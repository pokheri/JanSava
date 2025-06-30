from django import forms 

from .models  import (
    Complaint
)



class ComplaintForm(forms.ModelForm):

    
    class Meta: 
        model = Complaint
        fields = '__all__'
        exclude = ['citizen', 'vote']

    def clean(self):
        cd =  super().clean()
        origin = cd.get('origin',None)
        location = cd.get('location')

        if any([origin, location]):
            return cd
        else: 
            self.add_error('location','Please add the location ')
        return cd 
    


    