from newFunctions import *

app = App()
app2 = initJson()
#Buscar todos os usuários
#app.get_data("SELECT * FROM user;") #não aceita parâmetros na consulta

#Adicionar um usuário
#app.add_data("codestack5","325123025","contato@codestack.com", 4)
  
#Buscar geral dps q adicionou
#app.get_data("SELECT * FROM user;")

initJson.connectJson()

#O delete é meio q caso específico, por ex. Tu só usa o delete com valores únicos, como o id. Ai digamos q n aplicação tu não tenha o id, só o login,email etc
#var_login = "Joãozinho"
#var_id = app.get_id(var_login)
#app.remove_data(var_id)

#Buscar geral após remoção
#app.get_data("SELECT * FROM user;")

#app.update_user(1,"cloud","teste","aio@gmail.com")
#app.get_data("SELECT * FROM user;")

