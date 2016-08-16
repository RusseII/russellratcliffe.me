from network_scan.engine import Engine_network_scan
from coin_flip.engine import Engine_coin_flip
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
# import subprocess
# import json

app = Flask(__name__)

#roomate network_scan
@app.route('/',methods=['GET', 'POST'])
def show_page():
    return render_template("roomates.html")


@app.route('/scan',methods=['GET'])
def scan():
    
    return Engine_network_scan().execute()


  


#grace coin_flip
@app.route("/flip")
def hello():
	return render_template("coin_flip.html")

@app.route("/text")
def text():
	return Engine_coin_flip().run()

if __name__ == "__main__":
    app.run(debug=True)
