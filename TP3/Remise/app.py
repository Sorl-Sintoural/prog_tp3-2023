from flask import Flask, render_template
from flask_mail import Mail, Message
import TP3_complete as tp3
print(" - - - Library Import Complete")

app = Flask(__name__)
app.config['MAIL_SERVER'] = "smtp.office365.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "trashccount02@outlook.com"
app.config['MAIL_PASSWORD'] = "retna47$"
app.config['DEBUG'] = True
print(" - - - Email Settings Complete")

mail = Mail(app)
house_status = "gone"

temperature , humidity , pressure , light = tp3.read_capt()

@app.route('/')
def send_email():

    
    global temperature, humidity, pressure, light
    
    
    if temperature < -15:
        house_status = "freezing"
    elif temperature < 0:
        house_status = "Cold"
    elif temperature < 10:
        house_status = "Cool"
    elif temperature < 20:
        house_status = "Warm"
    elif temperature < 30:
        house_status = "Hot"
    elif temperature > 30:
        house_status = "burning"

    try:
        msg = Message(str("Status update: your house is "+house_status), sender="trashccount02@outlook.com", recipients=["EquipeBme_@outlook.com"])
        msg.body = "Your house is currently "+house_status+"\n\r Temperature: "+str(temperature)+"°C\r Relative Humidity: "+str(humidity)+"%\n\r Thank you for your patronage\n\r\n\rAutohome check-ups"
        mail.send(msg)
        print("Email sent")
    except Exception as e:
        app.logger.error(str(e))
        print( "Error: " + str(e))
    return render_template('info.html',temp=temperature,press=pressure,humi=humidity,lumi=light) 

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0' , debug=True)
