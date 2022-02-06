import tkinter as tk
import requests

from flask import Flask
import json

app = Flask(__name__)
@app.route('/', methods=['GET'])


def home_page():
    data_set = { 'firstname': 'Semanur', 'lastname': 'GOLET'}
    json_dump = json.dumps(data_set)

    return json_dump

@app.route('/temperature', methods=['GET'])

def temperature(canvas):

    
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=6338d4738b07bea572b9bde7277a826a"
    
    json_data = requests.get(api).json()
  
    temp = int(json_data['main']['temp'] - 273.15)
 

    city1 = "\n" "temperature:" + str(temp) + " "
      
    label1.config(text = city1)

    firstname_lastname= "firstname: Semanur , lastname: GOLET"
    label3.config(text=firstname_lastname)
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("BCFM_CASE API")
f = ("Courier New", 10, "normal")
t = ("Courier New", 10, "normal")

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', temperature)
label3= tk.Label(canvas,font=f)
label3.pack()
label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()

if __name__ == '__main__':

  app.run(port=5000)