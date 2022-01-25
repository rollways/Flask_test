from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)



#@app.route('/')
#def index():
#    return render_template('index.html')

#@app.route('/base')
#def base():
#    return render_template('base.html')


@app.route('/')
def input_customer():
    return render_template('input_customer.html')

@app.route('/result', methods=['Get','POST'])
def result():
    if request.method == 'POST':
        member_code = request.values["Name"]
    return render_template('result.html',member_code=member_code)

if __name__ == '__main__':
    app.run()
