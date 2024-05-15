from flask import Flask, request, make_response
from json import dumps, loads
from datetime import datetime
from os import remove

app = Flask('')

@app.get('/')
def home():
    print(request.headers)
    resp = make_response({})
    resp.headers["X-AdobeSign-ClientId"]=request.headers.get("X-AdobeSign-ClientId")
    return resp

@app.post('/')
def hook():
    try:
        with open('hook.log', 'a') as l:
            try:
                record = {
                    'time': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                    'headers': dict(request.headers),
                    'body': loads(request.data.decode())
                }
                l.write(dumps(record)+'\n')
            except Exception as e:
                record = {
                    'time': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                    'error': str(e)
                }
                l.write(dumps(record)+'\n')
                return str(e), 500
        resp = make_response({})
        resp.headers["X-AdobeSign-ClientId"]=request.headers.get("X-AdobeSign-ClientId")
        return resp
    except Exception as e:
        return str(e), 500

@app.get('/log')
def log():
    try:
        with open('hook.log', 'r') as l:
            return l.read()
    except Exception as e:
        return ''
    
@app.delete('/log')
def delete():
    try:
        remove('hook.log')
    except:
        pass
    return ''