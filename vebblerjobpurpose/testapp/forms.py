from . models import vebbler_jobinfo as v_job,vebblerservice as v_service
from . models import vebbler_ios_services as v_ios,vebbler_coustmer_info as v_info
from django import  forms

class v_serviceinfo(forms.ModelForm):
    class Meta:
        model=v_service
        fields='__all__'
class v_jobinfoo(forms.ModelForm):
    class Meta:
        model=v_job
        fields='__all__'
class v_iosinfoo(forms.ModelForm):
    class Meta:
        model=v_ios
        fields='__all__'
class v_coustmerinfo(forms.ModelForm):
    class Meta:
        model=v_info
        fields='__all__'