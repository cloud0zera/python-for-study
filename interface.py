import customtkinter as ctk
import tkinter as tk
#from main import *
#from newFunctions import *
from tkinter import PhotoImage

class Interface(ctk.CTk):
    def __init__(self,):
        super().__init__()
        self.title("VitalClinMed - Acesso:")
        self.geometry("500x350")
        self.resizable(False, False)
        self.frameLogin()
        self.labelInterface()
        
        
    def frameLogin(self):
        self.frm_login = ctk.CTkFrame(self,width=300, height=100)
        self.frm_login.place(x=20, y=40)

    def labelInterface(self):
        #Aqui são todas as Labels da interface
        #como criar uma label com customtkinter?
        self.LabelLogin = ctk.CTkLabel(self, text="Criando sistema.", font=("Arial", 12))
        self.LabelLogin.pack(padx=10, pady=10)
        self.LabelLogin.place(x=15,y=2)
        
    #def buttonsInterface(self):
        #Aqui são todos os Botões da interface
         # pass

    #def entryInterface(self):
        #Aqui é o Entry para inserir texto na tela
       # pass 

    #def logoImagem(self):
     #   pass

if __name__=="__main__":
    app = Interface()
    app.mainloop()


  # class interface_Build(ctk.CTk):
  #   def __init__(self,):
  #      super().__init__()
  #      self.title("Building the User Interface...")
  #      self.geometry("450x275")

  # if __name__=="__main__":
  #  app = interface_Build()
  #  app.mainloop()