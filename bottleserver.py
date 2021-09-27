from bottle import run, get, post, request # or route
from sha1password import make

@get('/')
def index():
    return '''
        <form action="/" method="post">
            Input seed to generate passwords: <input name="seed" type="text" />
            <input value="Submit" type="submit" />
        </form>
    '''

@post('/')
def gen():
    seed = request.forms.get('seed')
    password = make(seed)
    password=password.replace('<','&lt;').replace('>','&gt').replace('\n','<br>')
    return'''seed= {}<br><br>passwords=<br><br>{}'''.format(seed,password)

if __name__ == '__main__':
    run(host="0.0.0.0",port=80,debug=True,reloader=True)