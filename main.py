from cpf_cnpj import Documento

cpf = 87596504000

cpf_formatado = Documento.criar_novo(cpf)
print(cpf_formatado)