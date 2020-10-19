# import dependencies
import os
import json
from flask import Flask

# bootstrap the app
app = Flask(__name__)

# set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '3000'))

# our base route which just returns a string
@app.route('/')
def hello_world():
    return 'Congratulations! Welcome to the KubeCF Hands on Lab at EU Cloud Foundry Summit.'

@app.route('/create')
def create():
    data = json.loads(os.environ['VCAP_SERVICES'])
    print(data)
    print(data["volume_mount"]["container_id"])
    mountPath = data["volume_mount"]["container_id"]
    open(mountPath + "volumeTest.txt","x")
    return "Created volumeTest.txt file in " + str(mountPath)

# start the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)