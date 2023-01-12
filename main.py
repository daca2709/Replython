#APP igual a meu sistema, e é necessário nomear ele.
#@app.route fica em cima de DEF, tirando o DEF como função e colocando como uma ROTA!!!!!!
#As rotas não precisam estar em 'Ordem'
#Flask PRECISA da criação de uma pasta chamada 'templates', para colocar o código html la dentro
#Isso serve para o Flask procurar o HTML q precisa estar dentro da pasta templat
#METHODS ---> GET = Quando busca no 'google' a barra de pesquisa fica escrita com meu usuario e senha.
#POST = Já quando é post, não aparece o usuario na barra de pesquisa

from flask import Flask, redirect , url_for, request, render_template

app = Flask(__name__)






@app.route('/entrar/')
def admin_index():
  return render_template('login.html')

@app.route('/login/', methods=['POST', 'GET'])
def login():
  if request.method == 'POST':
    usuario = request.form['c_usuario']
    senha = request.form['c_senha']
    if usuario == 'daca' and senha == 2709:
      return redirect(url_for('admin' , nome=usuario, senha=senha))
    else:
      return redirect(url_for('login'))
  else:
    usuario = request.args.get('c_usuario')
    senha = request.args.get('c_senha')
    if usuario == 'daca' and senha == 2709:
      return redirect(url_for('admin', nome=usuario, senha=senha))
    else:
      #return redirect(url_for('login'))
      return redirect(url_for('admin', nome=usuario, senha=senha))
      
@app.route('/admin/<nome>/<senha>')
def admin(nome, senha):
  frase = '<b> bem vindo </b>' + nome + 'sua senha é:' + senha
  return frase

      

if __name__ == '__main__':
  app.run('0.0.0.0')
  

