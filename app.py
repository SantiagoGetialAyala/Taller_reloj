from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

class CircularList:
    def __init__(self, max_value):
        self.max_value = max_value
        self.value = 0
    
    def increment(self):
        self.value = (self.value + 1) % self.max_value
        return self.value

@app.route('/')
def index():
    # listas circulares 
    hour_list = CircularList(12)  
    minute_list = CircularList(60) 
    second_list = CircularList(60)  

    timezone = pytz.timezone("America/Bogota")
    now = datetime.now(timezone)

    hour_list.value = now.hour % 12 or 12  
    minute_list.value = now.minute
    second_list.value = now.second

    current_time = now.strftime("%H:%M:%S %p")
    return render_template('index.html', current_time=current_time, timezone="America/Bogota")

if __name__ == '__main__':
    app.run(debug=True)
