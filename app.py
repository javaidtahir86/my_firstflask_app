# Import Flask
from flask import Flask, render_template,request

# Create a Flask app
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def home():

    return render_template('home.html')

# Define the route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Define the route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

#route for calculator

@app.route('/calculator')
def calculator():
    return render_template('Calculator.html')
@app.route("/sum" ,methods=['GET','POST'])
def sum():
     if request.method =="POST":
        num1 = int(request.form.get("num1"))
        num2 = int(request.form.get("num2"))
        result= num1+num2
        return render_template('Result.html',result={'result':result})
# Run the app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
