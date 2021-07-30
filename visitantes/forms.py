from django import forms
from visitantes.models import Visitante

class VisitanteForm(forms.ModelForm):
  class Meta:
    model = Visitante
    fields =  [
      "nome_completo",
      "cpf",
      "data_nascimento",
      "numero_casa",
      "placa_veículo",
    ]
    error_messages = {
      "nome_completo" : {
        "required": "O nome do completo do visitante é obrigatório para o registro"
      },
      "cpf" : {
        "required": "O CPF do visitante é obrigatório para o registro"
      },
      "data_nascimento" : {
        "required": "A data de nascimento do visitante é obrigatório para o registro",
        "invalid" : "Por favor informe uma data válida de nascimento para o visitante (DD/MM/AAAA)"
      },
      "numero_casa" : {
        "required": "Por favor informe o número da casa a ser visitada"
      },
    }