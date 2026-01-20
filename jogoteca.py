from flask import Flask, render_template

# 1. Cria a instância do Flask (o 'coração' do site)
app = Flask(__name__)

# 2. Define a rota (endereço URL) e a função (o que o site faz)
@app.route('/inicio')
def ola():
    # Retorna HTML para o navegador
    return render_template('lista.html')

# 3. Executa o servidor (Modo Debug ativado para facilitar)
if __name__ == '__main__':
    app.run(debug=True)