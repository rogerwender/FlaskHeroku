from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = "Rogerio"
    dados = {"profissao": "Analista de Dados", "canal": "MeuCanal"}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/custoplanosaude')
def custoplanosaude():
    return render_template('custoplanosaude.html')

@app.route("/predict", methods=['POST'])
def predict():
    nome_da_variavel = "minha variavel teste"
    return render_template('custoplanosauderesultado.html', variavel=nome_da_variavel)
    
    
    """
        if request.method == 'POST':
        age = float(request.form['age'])
        
        

        sex = request.form['sex']
        if (sex == 'male'):
            sex_male = 1
            sex_female = 0
        else:
            sex_male = 0
            sex_female = 1

        smoker = request.form['smoker']
        if (smoker == 'yes'):
            smoker_yes = 1
            smoker_no = 0
        else:
            smoker_yes = 0
            smoker_no = 1

        bmi = float(request.form['bmi'])
        children = int(request.form['children'])

        region = request.form['region']
        if (region == 'northwest'):
            region_northwest = 1
            region_southeast = 0
            region_southwest = 0
            region_northeast = 0
        elif (region == 'southeast'):
            region_northwest = 0
            region_southeast = 1
            region_southwest = 0
            region_northeast = 0
        elif (region == 'southwest'):
            region_northwest = 0
            region_southeast = 0
            region_southwest = 1
            region_northeast = 0
        else:
            region_northwest = 0
            region_southeast = 0
            region_southwest = 0
            region_northeast = 1


        values = np.array([[age,sex_male,smoker_yes,bmi,children,region_northwest,region_southeast,region_southwest]])
        prediction = model.predict(values)
        prediction = round(prediction[0],2)
      
    
         return render_template('contato.html', prediction_text='A Estimativa de Custo do Plano de Saúde é de R$ {}'.format(prediction))


   """        