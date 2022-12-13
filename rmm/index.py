import os
from flask import Flask, jsonify,json


app = Flask(__name__)
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, 'static', 'data.json')
data = json.load(open(json_url))
real_data = data['ResultData']


def json_extract_all(obj, key):
    arr = []

    def extract(obj, arr, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    if k==key:
                        arr.append(v)
                    else:
                        extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values

def json_search_all(obj,val):
    arr = []

    def search(obj, arr, val):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    if val in str(v):
                        arr.append(v)
                    else:
                        search(v, arr, val)
        elif isinstance(obj, list):
            for item in obj:
                search(item, arr, val)
        return arr

    values = search(obj, arr, val)
    return values


#get all 
@app.get('/data')
def get_data():
    return jsonify(real_data)

#get by key and value
@app.get('/data/<key>/<id>')
def get_id(key,id):
    return jsonify(list(filter(lambda x:x[key]==id,real_data)))

#get all val for key
@app.get('/getall/<key>')
def get_all_val(key):
    tmp=json_extract_all(real_data,key)
    return jsonify(tmp)
    

#search in word and find all occurences #key
@app.get('/searchkey/<key>')
def search_key(key):
    tmp=json_search_all(real_data,key)
    return jsonify(tmp)

#search in word and find all occurences #all dict
@app.get('/searchall/<key>')
def search_all(key):
    var = []
    for i in real_data:
        if isinstance(i,dict):
            tmp=[]
            tmp=json_search_all(i,"Matt")
            if tmp!=[]:
                var.append(i)
    return jsonify(var)


#sort json by a key
@app.get('/sortall/<var>')
def sort_all(var):
    real_data.sort(key=lambda x:x[var])
    return jsonify(real_data)

#sort values of a key
@app.get('/sortkey/<var>')
def sort_key(var):
    var=json_extract_all(real_data,var)
    var.sort()
    return jsonify(var)

    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
    