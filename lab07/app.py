from flask import Flask, request, render_template, flash, redirect, url_for
import os
from werkzeug.utils import secure_filename
from datetime import datetime
import pickle
app = Flask('lab07')

UPLOAD_FOLDER = './static/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
imageInfo = []

if os.path.isfile('data.pickle'):
    with open('data.pickle', 'rb') as file:
        imageInfo = pickle.load(file)
else:
    imageInfo = []

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def render_index():
    return render_template('index.html', 
                           info=imageInfo,
                           len=len(imageInfo))

def delete_image(delIndex):
    path = imageInfo[delIndex][0]
    if os.path.isfile(path):
        os.remove(path)
    else:
        print("File not exists")
    imageInfo.pop(delIndex)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'GET':
        print(f'images info:{imageInfo}')
        print(f'last image info: {imageInfo[-1]}')
        return render_index()
    
    delValue = request.form.get("delValue")
    if delValue != None:
        print(delValue)
        delIndex = int(delValue)
        delete_image(delIndex)
        return render_index()
    
    fileName = request.form.get('fileName')
    file = request.files['file']
    name = request.form.get('name')
    meaning = request.form.get('meaning')
    star = request.form.get('star')
    appeared = request.form.get('appeared')
    timeToSee = request.form.get('timeToSee')
    area = request.form.get('area')
    hemisphere = request.form.get('hemisphere')

    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == None:
        return render_template("error.html", errorMessage="Select file!")
    if not (file and allowed_file(file.filename)):
        return render_template("error.html", errorMessage="Wrong format")

    if fileName == "":
            fileName = secure_filename(file.filename)   

    path = os.path. os.path.join(app.config['UPLOAD_FOLDER'], fileName)
    file.save(path)

    imageInfo.append([path, fileName, name, meaning, star, appeared, timeToSee, area, hemisphere, datetime.now()])
    print(f'image info: {imageInfo[-1][0]}')

    with open('data.pickle', 'wb') as file:
        pickle.dump(imageInfo, file)

    return render_index()
