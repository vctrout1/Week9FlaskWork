from flask import Flask, render_template
import requests

weatherapi = "3562c0c6779855696acfd6f49aa67107"
response = requests.get("https://samples.openweathermap.org/data/2.5/weather?zip=94040&appid="+weatherapi)
weather = response.json()
print(weather)
htmlweather = weather["weather"][0]["description"].title()
temp = int((weather["main"]["temp"])-273.15*9/5+32)
print(htmlweather)

app=Flask(__name__)
@app.route('/')
def index():
    weather = "sunny"
    rainy = True
    names = ["Valeri", "Jin", "Bob"]
    return render_template("home.html", users=names, weather=weather, rainy=rainy)

@app.route('/about')
def about():
    return render_template("about.html")

app.run()
