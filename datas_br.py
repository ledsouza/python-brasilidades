from datetime import datetime, timedelta

class Cadastro:
    def __init__(self) -> None:
        self.data_cadastro = datetime.today()
        
    def __str__(self) -> str:
        return self.format_data()
    
    def format_data(self):
        data_formatada = self.data_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada
    
    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        
        mes_cadastro = self.data_cadastro.month
        return meses_do_ano[mes_cadastro - 1]
    
    def dia_semana_cadastro(self):
        dias_semana = [
            "segunda", "terça",
            "quarta", "quinta", "sexta",
            "sábado", "domingo"
        ]
        
        dia_semana_cadastro = self.data_cadastro.weekday()
        return dias_semana[dia_semana_cadastro]
        
    def tempo_cadastro(self):
        agora = datetime.today() + timedelta(days=15, minutes=20, seconds=30)
        return agora - self.data_cadastro