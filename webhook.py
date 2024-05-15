from flask import Flask, request, make_response

app = Flask('')

@app.get('/')
def home():
    print(request.headers)
    resp = make_response({})
    resp.headers["X-AdobeSign-ClientId"]=request.headers.get("X-AdobeSign-ClientId")
    return resp