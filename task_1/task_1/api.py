from flask import Flask, request
from db_interface import DbInterface

app = Flask(__name__)

@app.route('/api/v1/storage/json/all', methods=['GET'])
def get_all_values():
    db = DbInterface()
    return db.get_all()

@app.route('/api/v1/storage/json', methods=['GET'])
def get_val_by_key():
    db = DbInterface()
    key = request.args.get('key', None)
    
    try:
        res = db.get_val(key)
        return ', '.join(res)
    except Exception as e:
        return str(e)

@app.route('/api/v1/storage/json/write', methods=['POST'])
def add_new_val():
    db = DbInterface()
    data_to_add = request.get_json(force=True)
    for key, value in data_to_add.items():
        db.set_val(key, value)
    
    return 'Succesfully added!'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)