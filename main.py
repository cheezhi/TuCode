'''
Project Name: TuCode
Author: Tutu (版权所有，请勿外传，否则后果自负)
QQ:2093142951
Blog: www.tutime.cn
'''

from flask import Flask, redirect, url_for, request, session
from wsgiref.simple_server import make_server
from create import create_code

app = Flask(__name__)
app.config["SECRET_KEY"] = 'tutu_owo_uwu_qwq'


@app.route('/')
def log():
    code = create_code()
    session['code'],file_name = str(code[1]),str(code[2])
    return f'''
    <form action = "/check" method = "post">
        <img src="{code[0]}">
        <p>输入验证码（不区分大小写）<br>Enter Code</p>
        <p><input type = "text" name = "cd" /></p>
        <p><input type = "submit" value = "submit" /></p>
    </form>
    '''
    # except Exception as e:
    #     return e
    # return "It's TuCode."

@app.route('/check',methods = ['POST'])
def check():
    if request.method == 'POST':
        get_test = request.form['cd']
        code = session.get('code', None)
        get_test, code = str(get_test), str(code)
        if get_test.upper() == code.upper():
            print(True)
            return 'True'
        else:
            print(False)
            return 'False'
        # return "It's TuCode."
    # except Exception as e:
    #     return e
    # return "It's TuCode."

if __name__ == '__main__':
    server = make_server('', 8824, app)
    server.serve_forever()
    # app.run()