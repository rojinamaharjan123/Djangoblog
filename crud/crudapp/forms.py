from django import forms
from .models import Demo

class DemoCreateForm(forms.ModelForm):
	class Meta:
		model = Demo
		fields = "__all__"
		# fields = ['name', 'image']