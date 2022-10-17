from mailbox import NotEmptyError
import tkinter as tk
import mysql.connector
#from PIL import ImageTk, Image
#from numpy import imag
#pip install mysql-connector (instalar o Mysql, executar no cmd)


class usuarios():
                def __init__(self,id, nome, sobrenome, cidade, estado, data_nascimento):
                        self.id = id
                        self.nome = nome
                        self.sobrenome = sobrenome
                        self.cidade =  cidade
                        self.estado = estado
                        self.data_nascimento = data_nascimento

                def __repr__(self):
                        return 'This is object of usuarios'

                def __str__(self):
                        print('id =', id)
                        print('nome =', nome)
                        print('sobrenome =', sobrenome)
                        print('cidade =', cidade)
                        print('estado =', estado)
                        print('data_nascimento =' data_nascimento)

def desconectar(conexao):
        if conexao:
                conexao.close()

def selecionarUsuarios():
        conn = conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM USUARIOS")
                

def conexao():
        try:
                conexao = mysql.connector.connect(
                        host = "localhost",
                        user = "root",
                        passwd = "",
                        db = "banco_python"
                )
                print("conectado")
                return conexao
        except mysql.connector.Error as e:
                print(f'Erro ao conectar o servidor mysql: {e}')
        #try e o except devem ser executados na mesma linha


def cadastrarUsuarios():
    janelaUsuarios = tk.Toplevel(app)

    lblNome = tk.Label(janelaUsuarios,text="Informe o seu nome: "
            ,font="Times"
            ,foreground="black")
    lblNome.place(x=100,y=50)

    entryNome = tk.Entry(janelaUsuarios)
    entryNome.place(x=230,y=55)
    
    lblSobrenome = tk.Label(janelaUsuarios,text="Informe o seu sobrenome: "
            ,font="Times"
            ,foreground="black")
    lblSobrenome.place(x=100,y=75)
    entrySobrenome = tk.Entry(janelaUsuarios)
    entrySobrenome.place(x=260, y=75)

    lblDataNascimento = tk.Label(janelaUsuarios,text="Informe sua data de nascimento:"
            ,font="Times"
            , foreground="black")
    lblDataNascimento.place(x=100, y=100)
    entryDataNascimento = tk.Entry(janelaUsuarios)
    entryDataNascimento.place(x=300, y=100)

    lblCidade = tk.Label(janelaUsuarios,text="Informe a sua cidade:"
            ,font="Times"
            , foreground="black")
    lblCidade.place(x=100,y=125)
    entryCidade = tk.Entry(janelaUsuarios)
    entryCidade.place(x=230,y=125)

    lblEstado = tk.Label(janelaUsuarios, text="Informe o estado: "
            ,font="Times"
            ,foreground="black")
    lblEstado.place(x=100, y=150)
    entryEstado = tk.Entry(janelaUsuarios)
    entryEstado.place(x=230, y=150)

            

    def salvarUsuario():
        conn = conexao()
        print("O nome informado foi: ",entryNome.get())
        print("O sobrenome informado foi: ", entrySobrenome.get())
        print("A data de nascimento informada foi: ", entryDataNascimento.get())
        print("A cidade informada foi: ", entryCidade.get())
        print("O estado informado foi: ",entryEstado.get())
    btnSalvar = tk.Button(janelaUsuarios,width=20
            ,text="Salvar", command=salvarUsuario)
    btnSalvar.place(x=100,y=175)
    
    #entryNome.insert("end","teste")
    #entryNome.insert("end","tormes")
    
    janelaUsuarios.title("Cadastro de Usuários")
    janelaUsuarios.geometry("800x600")
def cadastrarProdutos():
    janelaProduto = tk.Toplevel(app)
    janelaProduto.title("Cadastro de Produtos")
    janelaProduto.geometry("800x600")
app = tk.Tk()

menuPrincipal = tk.Menu(app)
app.config(menu=menuPrincipal)

fileMenu = tk.Menu(menuPrincipal)
fileMenu.add_command(label="Cadastrar Usuários"
            ,command=cadastrarUsuarios)
fileMenu.add_command(label="Cadastrar Produtos"
            ,command=cadastrarProdutos)
menuPrincipal.add_cascade(label="Funcao"
                        ,menu=fileMenu)

#buttonExample = tk.Button(app, 
#              text="Create new window",
#              command=createNewWindow)
#buttonExample.place(x=100,y=50)
app.title("Sistema Tarumã")
app.geometry("800x600")
app.mainloop()
app.destroy()