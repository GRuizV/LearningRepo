import flask, json

# CONSTANS
JSON_FILE_ROUTE = r'C:\Users\USUARIO\GR\Software Development\Learning\APIs\Whatsapp Chat Bot\Twilio API Test\test.json'

# Flask app setting
app = flask.Flask(__name__)

# Home page definition
@app.route('/')
def home(): 
    
    # HTML content with embedded URL
    html_content = f"""
    <html>
    <body>
    <h1>Server to receive Twilio callbacks</h1>
    <p>This was made to wait for twilio responses</p>
    </body>
    </html>
    """
    return html_content


# Callback page definition
@app.route('/callback', methods=['POST'])
def callback():

    # Log the request data for debugging purposes
    print("Received callback from Twilio")
    print(f"Request headers: {flask.request.headers}")
    print(f"Request data: {flask.request.get_data()}")



    # Check if the request contains JSON data
    if flask.request.is_json:
        
        # Get the JSON data sent by twilio
        data = flask.request.json
    
    else:
        data = flask.request.form.to_dict() # Capture form data if not JSON

    
    # Save the JSON data to a file 
    with open(JSON_FILE_ROUTE, 'w') as file:
        json.dump(data, file, indent=2)
    
    # Respond with a success message
    return 'Received Twilio callback successfully'
            



if __name__ == '__main__':
    app.run(port=5000)
