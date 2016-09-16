import json, os

dirname = os.path.join(os.path.dirname(__file__), '../_data')

def load(store_name):
    create_dir_if_nonexistant(store_name)
    path = os.path.join(dirname, store_name+'.json') 
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    else:
        with open(path, 'w+') as f:
            f.write(json.dumps({}))
            return json.dumps({})

def save(store_name, obj):
    create_dir_if_nonexistant(store_name)
    path = os.path.join(dirname, store_name+'.json')
    with open(path, 'w+') as f:
        f.write(json.dumps(obj))

def create_dir_if_nonexistant(store_name):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
