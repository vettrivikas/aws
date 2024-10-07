from flask import Flask, render_template, request

import os

# Automatically set the template folder to the "templates" directory in the current folder
current_folder = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(current_folder, 'templates')

app = Flask(__name__, template_folder=template_folder)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        # You can process the email here (e.g., save it to a database)
        return f'Thank you for submitting your email: {email}'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
