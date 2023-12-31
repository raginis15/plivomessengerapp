# app.py
from flask import Flask, render_template, request
import plivo
import datetime

app = Flask(__name__)

# In-memory storage for messages (replace this with a database in production)
messages = []

auth_id = 'Enter Id'
auth_token = 'Enter Token'
plivo_client = plivo.RestClient(auth_id=auth_id, auth_token=auth_token)

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send_message():
    to_number = request.form['to_number']
    message = request.form['message']

    # Send message using Plivo API
    response = plivo_client.messages.create(
        src="+12028993116",  # Replace with your Plivo phone number
        dst=to_number,
        text=message
    )

    print("Plivo API Response:", response)

    # Append the message to the in-memory storage
    messages.append({
        'to_number': to_number,
        'message': message,
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

    return index()  # Redirect back to the index page

@app.route('/receive', methods=['GET'])
def receive_message():
    # Get the necessary data from the incoming request
    from_number = request.form.get('From', '')
    received_message = request.form.get('Text', '')
    
    # Append the received message to the in-memory storage
    messages.append({
        'to_number': '+12028993116',  # Replace with your Plivo phone number
        'message': received_message,
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'received_from': from_number

    
    
    })

    # Trigger PHLO when receiving SMS
    phlo_response = phlo_client.phlo('8dcfccfa-2235-4af3-a3b6-ec36404d1689').run()
    print("PHLO API Response:", phlo_response)
    
    return "Message received successfully"


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host="127.0.0.1", port=8080, debug=True)
