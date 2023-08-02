from datetime import datetime, timedelta

class Cadastro:
    """
    Classe para representar um cadastro com informações de data e tempo.

    Atributos:
        data_cadastro (datetime): A data e hora do cadastro, definida como o momento da criação do objeto.

    Métodos:
        __str__(): Retorna a representação formatada da data de cadastro.
        format_data(): Formata a data de cadastro para o formato "dd/mm/aaaa hh:mm".
        mes_cadastro(): Retorna o nome do mês em que o cadastro foi realizado.
        dia_semana_cadastro(): Retorna o dia da semana em que o cadastro foi realizado.
        tempo_cadastro(): Retorna a diferença entre a data atual e a data de cadastro como um objeto timedelta.
    """
    def __init__(self) -> None:
        self.data_cadastro = datetime.today()
        
    def __str__(self) -> str:
        return self.format_data()
    
    def format_data(self) -> str:
        data_formatada = self.data_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada
    
    def mes_cadastro(self) -> list[str]:
        meses_do_ano = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        
        mes_cadastro = self.data_cadastro.month
        return meses_do_ano[mes_cadastro - 1]
    
    def dia_semana_cadastro(self) -> list[str]:
        dias_semana = [
            "segunda", "terça",
            "quarta", "quinta", "sexta",
            "sábado", "domingo"
        ]
        
        dia_semana_cadastro = self.data_cadastro.weekday()
        return dias_semana[dia_semana_cadastro]
        
    def tempo_cadastro(self) -> datetime:
        agora = datetime.today() + timedelta(days=15, minutes=20, seconds=30)
        return agora - self.data_cadastro