from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def hello():
    return 'Hello, World!'
 
@app.route('/about')
def about():
    return 'This is the about page.'
 
@app.route('/contact')
def contact():
    return 'Contact us at example@example.com'
 
@app.route('/user/<username>')
def user_profile(username):
    return f'User Profile: {username}'
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 80)