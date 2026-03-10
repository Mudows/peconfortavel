from django import forms
from .models import Cliente, Produto, Fabricante
from django.core.validators import EmailValidator, MinLengthValidator
import re

class ClienteForm(forms.ModelForm):
    # Campo senha com widget de password e validação de tamanho
    senha = forms.CharField(
        widget=forms.PasswordInput(),
        validators=[MinLengthValidator(8, 'A senha deve ter exatamente 8 caracteres')],
        label='Senha'
    )
    # Confirmar senha (opcional, mas bom)
    confirmar_senha = forms.CharField(widget=forms.PasswordInput(), label='Confirmar senha')

    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'endereco', 'telefone', 'estado', 'cidade',
                  'genero', 'contato_pref', 'email', 'senha']
        widgets = {
            'cpf': forms.TextInput(attrs={'placeholder': 'Apenas números'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Apenas números'}),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if not cpf.isdigit():
            raise forms.ValidationError('CPF deve conter apenas números')
        return cpf

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if not telefone.isdigit():
            raise forms.ValidationError('Telefone deve conter apenas números')
        return telefone

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) < 25 or len(nome) > 70:
            raise forms.ValidationError('Nome deve ter entre 25 e 70 caracteres')
        return nome

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar = cleaned_data.get('confirmar_senha')
        if senha and confirmar and senha != confirmar:
            self.add_error('confirmar_senha', 'Senhas não conferem')
        # usuario será igual ao email, mas não precisa validar aqui
        return cleaned_data

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['codigo', 'nome', 'preco_compra', 'preco_venda', 'cor', 'fabricante', 'imagem']
        # imagem não é obrigatória, mas se for enviada será tratada

class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = ['codigo', 'nome']