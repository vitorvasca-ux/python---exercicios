from DataBase import conn, cursor


    
# Cadastro de Produtos


def cadastrar_produto():

     nome = input(("Digite o nome do produto: "))
     categoria = (input("Digite a categoria do produto: "))
     preço = float(input("Digite o preço do produto: "))
     estoque_atual = int(input("Qual o estoque Atual do produto?: "))
     estoque_minimo = int(input("Qual o estoque mínimo do produto?: "))


     while estoque_atual < estoque_minimo:
        print("O estoque atual precisa ser acima do estoque mínimo!!!")
        estoque_atual = int(input("Qual o estoque inicial do produto?: "))
 
         
     cursor.execute("""

INSERT INTO produtos(NOME, PRECO_ATUAL, CATEGORIA, ESTOQUE_ATUAL, ESTOQUE_MINIMO)VALUES (?,?,?,?,?)
    
 """, (nome, preço, categoria, estoque_atual, estoque_minimo))

     conn.commit()

    

# Listagem de Produtos

def listar_produto():
   cursor.execute("SELECT * FROM produtos")
   produtos = cursor.fetchall()
   for produto in produtos:
      print(produto)




def buscar_produto():
     id_produto = int(input("Digite o ID do produto desejado: "))
     cursor.execute("SELECT * FROM produtos WHERE ID = ?", (id_produto,))
     produtos = cursor.fetchone()

     if produtos is not None:
          print(produtos)
     else:
          print("Produto não encontrado. ")




      
# Menu

def menu():
    
    while True:
       print(" ---- BEM VINDO A LOJA VASCA ----")
       print("1 - Cadastrar Produto")
       print("2 - Listar Produtos ")
       print("3 - Buscar produtos ")
       print("4 - Sair ")
       opcao = input(("Qual opção você deseja?: "))
       if opcao == "1":
        cadastrar_produto()
       elif opcao == "2":
          listar_produto()
       elif opcao == "3":
          buscar_produto()
       elif opcao == "4":
        print("Até a próxima!")
        break
       else:
        print("Opção Inválida")
      

menu()





    
