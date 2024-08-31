from tkinter import*
from tkinter import Tk, ttk
from tkinter import messagebox

# cores

cor0 = "#f0f3f5"  # Preta / black
cor1 = "#feffff"  # branca / white
cor2 = "#3fb5a3"  # verde / green
cor3 = "#38576b"  # valor / value
cor4 = "#403d3d"   # letra / letters

#criando janela

janela =Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)

#dividindo a janela

Frame_cima = Frame(janela, width=310, height=50, bg=cor1,relief='flat')
Frame_cima.grid(row=0, column=0, pady=1, padx=0,sticky=NSEW)

Frame_baixo = Frame(janela, width=310, height=250, bg=cor1,relief='flat')
Frame_baixo.grid(row=1, column=0, pady=1, padx=0,sticky=NSEW)

#configurando o frame cima
l_nome =Label(Frame_cima, text='LOGIN', anchor=NE, font=('ivy 25'), bg=cor1, fg=cor4)
l_nome.place(x=5, y=5)

l_linha =Label(Frame_cima, text='', width=275 , anchor=NW, font=('Ivy 1'), bg=cor2, fg=cor4)
l_linha.place(x=10, y=45)


credenciais= ['Thais', '123456']


#função para verificar senha:

def verificar_senha():
     nome = e_nome.get()
     senha= e_pass.get()

     if nome =='admin' and senha == 'admin':
          messagebox.showinfo('Login', 'Seja bem vindo Admin !!!')
     elif  credenciais[0] == nome and credenciais[1] ==senha:
          messagebox.showinfo('Login', 'Seja bem vindo de volta ' + credenciais[0])
     else:
          messagebox.showwarning('Erro', 'Verifique o nome e a senha')

#função após verificação

def nova_janela(): 
   #configurando o frame cima
    l_nome = Label(Frame_cima, text='Usuario: ' + credenciais[0], anchor=NE, font=('ivy 20'), bg=cor1, fg=cor4)
    l_nome.place(x=5, y=5)

    l_linha =Label(Frame_cima, text='', width=275 , anchor=NW, font=('Ivy 1'), bg=cor2, fg=cor4)
    l_linha.place(x=10, y=45)

    l_nome = Label(Frame_baixo, text='Seja bem vindo: ' + credenciais[0], anchor=NE, font=('ivy 20'), bg=cor1, fg=cor4)
    l_nome.place(x=5, y=105)


         

#configurando o frame baixo
l_nome =Label(Frame_baixo, text='Nome *', anchor=NW, font=('ivy 10'), bg=cor1, fg=cor4)
l_nome.place(x=10, y=20)
e_nome =Entry(Frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_nome.place(x=14,y=50)

l_pass =Label(Frame_baixo, text='Palavra pass *', anchor=NW, font=('ivy 10'), bg=cor1, fg=cor4)
l_pass.place(x=10, y=95)
e_pass =Entry(Frame_baixo, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
e_pass.place(x=14,y=130)


b_confirmar =Button(Frame_baixo, command=verificar_senha,text='Entrar *', width=39, height=2, font=('ivy 8 bold'), bg=cor2, fg=cor1, relief= RAISED, overrelief=RIDGE)
b_confirmar.place(x=15, y=180)



janela.mainloop()