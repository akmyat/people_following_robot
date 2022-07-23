from flask import Flask
from flask import render_template, redirect
from rc_control import RCcontrol

# Motor 1
motor1_pin1 = 20
motor1_pin2 = 21
motor1_en = 12

# Motor 2
motor2_pin1 = 6
motor2_pin2 = 5
motor2_en = 19

# Define RC control
control = RCcontrol(motor1_pin1, motor1_pin2, motor1_en, motor2_pin1, motor2_pin2, motor2_en)

app = Flask(__name__)
title = "Raspberry PI Car"

@app.route('/')
def index():
	return render_template("index.html")

@app.route("/forward")
def forward():
	control.forward(0.15)
	return redirect("/")

@app.route("/backward")
def backward():
	control.backward(0.15)
	return redirect("/")

@app.route("/left")
def left():
	control.left(0.15)
	return redirect("/")

@app.route("/right")
def right():
	control.right(0.15)
	return redirect("/")

@app.route("/stop")
def stop():
	control.stop()
	return redirect("/")
	
if __name__ == "__main__":
	app.run(debug=True, port=80, host="0.0.0.0")
