      from flask  import Flask, jsonify, request

postys= []

app=Flask(__name__)



@app.route('/')
def ping():
    return jsonify({'responce': 'pong'})

@app.route('/posty',methods=['POST'])
def create_posty():
    '''("body":"Helo World","author":"vita1923")
    '''
    posty_json=request.get_json()
    posty=posty(posty_json['body'],posty_json['author'])
    postys.append(posty)
    return jsonify({'status':'succsess'})



@app.route('/posty',methods=['GET'])         
def read_posty():
    return jsonify({'postys':'postys'})




# Включает режим дебага при изменение файла автоматически подтягивает изменения(чвще всего)
if  __name__ =='__main__':
    app.run (debug=True)  
     






