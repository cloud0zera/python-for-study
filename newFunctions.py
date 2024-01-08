import mariadb
import json

class initJson():
     def connectJson():
         # Segundo Metodo Puxar Algo especifico
          with open('settings.json', 'r') as f:
           data = json.load(f)

          version = data['ApplicationVersion']
          name = data['ApplicationName']
          Apptype = data['ApplicationID']
          
          print("Application Version:",version,"\nApplication Name:",name, "\nID:",Apptype)

class App():
    def __init__(self):
        self.conn = mariadb.connect(user='root',database='codestack',password='32512302',port=3306)
        self.cursor = self.conn.cursor()
        #self.get_data("SELECT * FROM user;")

    def get_data(self,query):
            # Pegar resultados da db
            try:
                statement = query
                self.cursor.execute(query)
                results = self.cursor.fetchall()
                for result in results:
                    print(result)
            except mariadb.Error as e:
                 print(f"Error: {e}")
 # tu tava chamando o método dentro do construtor, logo ele só vai executar se tu criar um objeto newFunctions (ou vulgo app q é a classe)

    def add_data(self, login, senha, email, code):
         try:
              statement = "INSERT INTO user (login, senha, email, code) VALUES (%s, %s, %s, %s)"
              data = (login, senha, email, code)
              self.cursor.execute(statement, data)
              self.conn.commit()
              print(f"Usuário inserido, {data}")
         except mariadb.Error as e:#vsf identação
               print(f"Error: {e}")

    def remove_data(self, id):
         try:
              statement = f"DELETE FROM user WHERE ID={id}"
              self.cursor.execute(statement) #isso aq fica mto estranho, 1 parâmetro e ele pede uma lista: self.cursor.execute(statement, id)
              self.conn.commit()
              print(f"Usuario com id {id} removido com sucesso!")
         except mariadb.Error as e:
              print(f"Error: {e}")

    def get_id(self, login): # Isso aq é pq o id vem como uma lista no get_data ent da erro
         try:
              statement = "SELECT id FROM user WHERE `login`=%s"
              self.cursor.execute(statement,(login,))
              result = self.cursor.fetchone()
              if result:
                   return result[0]
              else:
                   print(f"Usuário com login {login} não encontrado.")
                   return None
         except mariadb.Error as e:
              print(f"Error: {e}")
              return None
         
    #O último agr pra terminar o crud
    def update_user(self, user_id, new_login=None, new_password=None, new_email=None): #Usar só esses 3 por agr
         try:
              if not new_login and not new_password and not new_email:
                   print("Nenhum dado para atualizar.")
                   return
              
              update_data = []
              values = []

              if new_login:
                   update_data.append('login=%s')
                   values.append(new_login)
              if new_password:
                   update_data.append('senha=%s')
                   values.append(new_password)
              if new_email:
                   update_data.append('email=%s')
                   values.append(new_email)
              values.append(user_id)

              #Update_data é o nosso sql Set login=tal,senha=tal
              #Values é os dados
              statement = f'UPDATE user SET {', '.join(update_data)} WHERE id=%s'

              self.cursor.execute(statement, tuple(values))
              self.conn.commit()

              print(f"Usuário com id {user_id} atualizado com sucesso!")
         except mariadb.Error as e:
              print(f"Erro: {e}")
              
         

