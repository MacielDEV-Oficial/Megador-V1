import os


class Megador:
    def __init__(self):
        self.iniciar_loop = True
        pass
    def sistema_de_comandos(self):
        match self.comando:
            case 'start server':
                print("Iniciando servidor na porta << 789 >>")
                os.system('nc -nvlp 789')
    def criar_pyload(self):
        pass

    def carregar_logo_megador(self):
        self.logo = """
  __  __ ______ _____          _____   ____  _____  
 |  \/  |  ____/ ____|   /\   |  __ \ / __ \|  __ \ 
 | \  / | |__ | |  __   /  \  | |  | | |  | | |__) |
 | |\/| |  __|| | |_ | / /\ \ | |  | | |  | |  _  / 
 | |  | | |____ |__| |/ ____ \| |__| | |__| | | \ \ 
 |_|  |_|______\_____/_/    \_\_____/ \____/|_|  \_/
                                                    
                                                    
        """
        print(self.logo)
    
    def mainloop(self):
        try:
            self.carregar_logo_megador()
            while self.iniciar_loop:
                self.comando = input("|Megador-V1> ")
        except:
            pass
    def Update(self):
        self.mainloop()

if __name__=="__main__":
    mg = Megador()
    mg.Update()