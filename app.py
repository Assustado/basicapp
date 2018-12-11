from flask import Flask, render_template, jsonify, request, Blueprint
from flask_mongoengine import MongoEngine
from mongoengine import *
import json
debug = __name__ == '__main__'

db = MongoEngine()

app = Flask(__name__, template_folder="ui/template",static_folder="ui/dist")
app.config['MONGODB_DB'] = 'dbteste-raccoon'
app.config['MONGODB_HOST'] = 'ds127443.mlab.com'
app.config['MONGODB_PORT'] = 27443
app.config['MONGODB_USERNAME'] = 'pedropuzzi'
app.config['MONGODB_PASSWORD'] = 'teste12'
db.init_app(app)


class Script(Document):
    name = StringField(required=True, unique=True)


class Client(Document):
    name = StringField(required=True, unique=True)
    scripts = EmbeddedDocumentListField('Script')


@app.route('/')
def index():
    print('xxxx debug')
    return render_template('index.html', debug=debug)




@app.route('/add', methods=['GET','POST'])
def add():
    x1 = Script("ScriptK");
    if request.method == "POST":
          data = request.get_json()
          name = data["name"]
          x = Client(name, [x1])
          x.save()
    elif request.method == "GET":
        print("tentei dar um get")
    else:
        print("tentei qualquer bosta")

    #nome = request.form["nome"]
    #print("nome passado como parametro:",nome)

    #x = Client(nome, [x1])
    #x.save()
    # print("adicionando")
    # x1 = Script("script1")
    # x2 = Script("script2")
    # x3 = Script("script3")
    # x4 = Script("script4")
    # x5 = Script("script5")
    # x6 = Script("script6")
    # x7 = Script("script7")
    # x8 = Script("script8")
    # x9 = Script("script9")
    # x = Client("joao", [x3, x4])
    # x.save()
    # y = Client("pedro", [x1, x2])
    # y.save()
    # z = Client("julia", [x8, x9])
    # z.save()
    # x10 = Script("ScriptGelaoooo")
    # w = Client("Gelaoooo", [x1,x3,x10])
    # w.  save()
    return json.dumps({'name':x.name, 'scripts': [script.name for script in x.scripts] })


@app.route('/clients/')
def listClients():
    clients = Client.objects.all()
    response = jsonify({'clients': clients})
    httpcode = 200
    return response, httpcode


@app.route('/scripts/')
def listScripts():
    for client in Client.objects:
        print(client.name)
        for script in client.scripts:
            print(script.name)
        #print(client.name, scripts)
    return render_template('index.html', debug=debug)


if __name__ == '__main__':
    app.run(debug=debug, port=5000)
