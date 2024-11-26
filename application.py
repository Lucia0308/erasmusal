from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
@application.route('/home')
def home():
  return render_template('home.html')

@application.route('/business')
def business():
  return render_template('business.html', title='business')

@application.route('/ERASMUSAL')
def ERASMUSAL():
    return render_template('ERASMUSAL.html', title='ERASMUSAL')

if __name__=='__main__':
  application.run(debug=True)  