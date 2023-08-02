import requests

class BuscaEndereco:
    """Classe que realiza busca de informações de endereço através de um CEP.

    Args:
        cep (str): O CEP (Código de Endereçamento Postal) a ser buscado.

    Raises:
        ValueError: Se o CEP fornecido não tiver exatamente 8 dígitos.

    Attributes:
        cep (str): O CEP válido para busca.

    Methods:
        __str__(): Retorna o CEP formatado como uma string.
        validar_cep(cep): Valida se o CEP fornecido possui 8 dígitos.
        format_cep(): Formata o CEP para o padrão XXXXX-XXX.
        acessa_via_cep(): Acessa a API ViaCEP para obter informações de endereço.

    """
    def __init__(self, cep) -> None:
        cep = str(cep)
        if self.validar_cep(cep):
            self.cep = cep
        else:
            raise ValueError('CEP inválido!')
        
    def __str__(self) -> str:
        return self.format_cep()
    
    def validar_cep(self, cep) -> bool:
        if len(cep) == 8:
            return True
        else:
            return False
        
    def format_cep(self) -> str:
        return f'{self.cep[0:5]}-{self.cep[5:]}'
    
    def acessa_via_cep(self) -> tuple:
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )