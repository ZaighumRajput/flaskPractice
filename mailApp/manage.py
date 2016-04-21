
from flask import Flask
from flask_mail import Mail, Message
import pdb



app = Flask(__name__)
mail = Mail(app)

@app.route('/')
def index():
    pdb.set_trace()
    msg = Message("Hello",recipients = ["zaighum47@gmail.com"])
       
    msg.body= "testing"
    msg.html="abc"

    mail.send(msg)
    return "This is my index"


app.run(host="0.0.0.0")
