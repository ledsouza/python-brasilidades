from validate_docbr import CPF

class ValidaCpf:
    
    def __init__(self, cpf):
        cpf = str(cpf)
        if self.valida_cpf(cpf):
            self.cpf = cpf
        else:
            raise ValueError('CPF inválido!')
        
    def valida_cpf(self, cpf):
        cpf_validate = CPF()
        return cpf_validate.validate(cpf)
    
    def __str__(self):
        return self.format_cpf()
    
    def format_cpf(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self.cpf)