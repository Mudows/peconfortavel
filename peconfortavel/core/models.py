from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator, RegexValidator
from django.contrib.auth.hashers import make_password

class Fabricante(models.Model):
  codigo = models.IntegerField(
    unique=True,
    verbose_name='Código'
  )
  nome = models.CharField(
    max_length=70,
    verbose_name='Nome'
  )

  def __str__(self):
    return self.nome
  
class Produto(models.Model):
  CORES = [
    ('AZ', 'Azul'),
    ('VD', 'Verde'),
    ('VM', 'Vermelho'),
    ('AM', 'Amarelo'),
    ('PR', 'Preto'),
    ('BR', 'Branco'),
    ('MR', 'Marrom'),
  ]
  codigo = models.IntegerField(
    unique=True,
    verbose_name='Código'
  )
  nome = models.CharField(
    max_length=70,
    verbose_name='Nome'
  )
  preco_compra = models.FloatField(
    verbose_name='Preço de Compra'
  )
  preco_venda = models.FloatField(
    verbose_name='Preço de Venda'
  )
  cor = models.CharField(
    max_length=2,
    choices=CORES,
    verbose_name='Cor'
  )
  fabricante = models.ForeignKey(
    Fabricante,
    on_delete=models.CASCADE,
    verbose_name='Fabricante'
  )
  imagem = models.ImageField(
    upload_to='produtos/',
    null=True,
    blank=True,
    verbose_name='Imagem'
  )

  def __str__(self):
    return self.nome
  
class Cliente(models.Model):
  ESTADOS = [
    ('RJ', 'Rio de Janeiro'),
    ('SP', 'São Paulo'),
    ('MG', 'Minas Gerais'),
    ('ES', 'Espírito Santo'),
    ('BA', 'Bahia'),
    ('RS', 'Rio Grande do Sul'),
    ('PR', 'Paraná'),
  ]
  
  GENEROS = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outro'),
  ]
  CONTATO = [
    ('EMAIL', 'Email'),
    ('TELEFONE', 'Telefone'),
    ('CELULAR', 'Celular'),
  ]

  cpf = models.CharField(
    max_length=11, 
    unique=True, 
    validators=[
      RegexValidator(r'^\d{11}$', 'CPF deve conter 11 números')
    ], 
    verbose_name='CPF'
  )

  nome = models.CharField(
    max_length=70,
    validators=[
      MinLengthValidator(25, 'O nome deve conter entre 25 e 70 caracteres')
    ],
    verbose_name='Nome'
  )

  endereco = models.CharField(
    max_length=100,
    verbose_name='Endereço'
  )

  telefone = models.CharField(
    max_length=11,
    validators=[
      RegexValidator(r'^\d{10,11}$', 'Telefone deve conter 10 ou 11 números')
    ],
    verbose_name='Telefone'
  )

  estado = models.CharField(
    max_length=2,
    choices=ESTADOS,
    verbose_name='Estado'
  )

  cidade = models.CharField(
    max_length=50,
    verbose_name='Cidade'
  )

  genero = models.CharField(
    max_length=1,
    choices=GENEROS,
    verbose_name='Gênero'
  )

  contato_pref = models.CharField(
    max_length=10,
    choices=CONTATO,
    verbose_name='Contato Preferencial'
  )

  email = models.EmailField(
    max_length=100,
    unique=True,
    verbose_name='Email'
  )

  usuario = models.CharField(
    max_length=100,
    verbose_name='Usuário'
  )

  senha = models.CharField(
    max_length=256,
    verbose_name='Senha'
  )

  def save(self, *args, **kwargs):
    self.usuario = self.email
    if not self.senha.startswith('pbkdf2_sha256$'):
      self.senha = make_password(self.senha)
    super().save(*args, **kwargs)

  def __str__(self):
    return self.nome
  