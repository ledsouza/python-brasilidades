import re

class TelefonesBr:
    """Representa um número de telefone brasileiro.

    Esta classe permite validar e formatar números de telefone no formato brasileiro.
    O padrão considerado é o seguinte: DDD (opcional) + Número com 8 ou 9 dígitos.

    Args:
        telefone (str): O número de telefone a ser validado e formatado.

    Raises:
        ValueError: Se o número de telefone fornecido não estiver no formato correto.

    Attributes:
        numero (str): O número de telefone formatado, incluindo o DDD quando presente.

    Methods:
        valida_telefone(telefone): Verifica se o número de telefone fornecido é válido.
        format_numero(): Formata o número de telefone no padrão com DDD e hífen.

    """
    def __init__(self, telefone) -> None:
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError('Número incorreto!')
        
    def __str__(self) -> str:
        return self.format_numero()
    
    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False
        
    def format_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.numero)
        numero_formatado = '+{}({}){}-{}'.format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
        return numero_formatado