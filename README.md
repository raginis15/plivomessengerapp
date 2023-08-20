<h1> Flask SMS Handling App </h1>
This is a Flask application that allows you to send and receive SMS messages using the Plivo API. The app provides a simple web interface to send SMS messages and displays received SMS messages. Additionally, it is integrated with a Plivo PHLO to trigger a specific workflow upon receiving an SMS.

## Prerequisites

* Python 3.6+
* Flask
* Plivo Account (for sending and receiving SMS)
* Plivo PHLO ID (for workflow integration)



## Configuration

*Import the required libraries
* auth_id: Your Plivo authentication ID.
* auth_token: Your Plivo authentication token.
* src: Your Plivo phone number.
* Plivo PHLO ID (for workflow integration)
* Update the PHLO ID in the receive_message route to trigger the desired PHLO workflow.
* Run the flask app locally using  python main.py


## Deployment

### Deploying on Google Cloud

1. Set up a Google Cloud account and project.
2. Install the Google Cloud SDK.
3. Deploy the app to Google Cloud App Engine
4. Access the deployed app at https://flask-webapp-396515.el.r.appspot.com

