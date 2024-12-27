from django import forms    
from velas.models import Clientes

class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['Nome', 'Email', 'Número', 'Mensagem']

        def clean_numero(self):
            Número = self.cleaned_data.get('Número')

            if not (10 <= len(Número) <= 11):
                raise forms.ValidationError('Digite o número de telefone com o DDD (10 ou 11 dígitos).')
            return Número   