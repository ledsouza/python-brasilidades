from validate_docbr import CPF, CNPJ

class Documento:
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
    