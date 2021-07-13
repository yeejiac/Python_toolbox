import pyautogui
import time
from flask import Flask, jsonify, request, Response, redirect, flash, send_file
import json
import numpy as np
import os
import requests
import configparser
config = configparser.ConfigParser()
config.read("config.ini")



status = True

app = Flask(__name__)

def getScreenShot():
    while status:
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'C:\Users\user\AppData\Local\Temp\test.png')
        time.sleep(5)

def pushMsg(id, url):
    try:
        url = "https://api.line.me/v2/bot/message/push"
        headers = { 
            'content-type': 'application/json',
            "Authorization": "Bearer " + config['line_bot']['LINE_CHANNEL_ACCESS_TOKEN'],
        }
        msg = {
            "to": id,
            "messages": [
                {
                    "type": "image",
                    "originalContentUrl": url,
                    "previewImageUrl": url
                }
            ]
        }
        r = requests.post(url, data=json.dumps(msg), headers=headers)
        print(r.content)
    except:
        print("Push msg failed")


@app.route('/getImage', methods=['GET','POST'])
def getImage():
    if request.method == 'POST' and request.files['image']:
    	img = request.files['image']
    	img_name = img.filename
    	img.save(img_name)
    	return "success"
    else:
    	return send_file("test.png",mimetype='image/gif')


if __name__ == '__main__':
    # app.secret_key = 'super secret key'
    # app.config['SESSION_TYPE'] = 'filesystem'
    # app.run(debug=True)
    pushMsg("U0d44ce039195857a0e0f23413cbb9053", "https://yeejiaclib.herokuapp.com/getImage")


# C:\Users\user\AppData\Local\Temp