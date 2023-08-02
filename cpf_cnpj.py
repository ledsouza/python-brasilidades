from validate_docbr import CPF, CNPJ

class Documento:
    """
    Classe Documento: Responsável por criar um objeto específico para CPF ou CNPJ e validar seu formato.

    Métodos:
        criar_novo(documento): Método estático para criar uma instância de DocCpf ou DocCnpj
                              baseado no tamanho do número do documento.

    Raises:
        ValueError: Se o número do documento não tiver o tamanho correto para CPF ou CNPJ.

    Exemplos de Uso:
        # Criando um novo objeto de CPF
        documento_cpf = Documento.criar_novo('12345678900')

        # Criando um novo objeto de CNPJ
        documento_cnpj = Documento.criar_novo('12345678900000')
    """
    @staticmethod
    def criar_novo(documento):
        doc_str = str(documento)
        if len(doc_str) == 11:
            return DocCpf(doc_str)
        elif len(doc_str) == 14:
            return DocCnpj(doc_str)
        else:
            raise ValueError('Documento incorreto!')
        
class DocCpf:
    """
    Classe DocCpf: Representa um número de CPF válido e fornece funcionalidades de validação e formatação.

    Métodos:
        valida(documento): Verifica se o número de CPF fornecido é válido.
        format(): Retorna o número de CPF formatado com a máscara.

    Raises:
        ValueError: Se o número de CPF fornecido for inválido.

    Exemplo de Uso:
        cpf = DocCpf('12345678900')
        print(cpf)  # Output: 123.456.789-00
    """
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido!')
        
    def __str__(self):
        return self.format()
    
    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)
    
    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    
class DocCnpj:
    """
    Classe DocCnpj: Representa um número de CNPJ válido e fornece funcionalidades de validação e formatação.

    Métodos:
        valida(documento): Verifica se o número de CNPJ fornecido é válido.
        format(): Retorna o número de CNPJ formatado com a máscara.

    Raises:
        ValueError: Se o número de CNPJ fornecido for inválido.

    Exemplo de Uso:
        cnpj = DocCnpj('12345678900000')
        print(cnpj)  # Output: 12.345.678/9000-00
    """
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ inválido!')
        
    def __str__(self):
        return self.format()
    
    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)
    
    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cpf)
    