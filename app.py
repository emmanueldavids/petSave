from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/')
def index():
    return render_template('frontend/index.html')

@app.route('/about')
def about():
    return render_template('frontend/about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('frontend/contact.html')

@app.route('/home')
def home():
    return render_template('backend/home.html')

@app.route('/registration-forms')
def form():
    return render_template('backend/basic_elements.html')

@app.route('/main')
def main():
    return render_template('frontend/main.html')

@app.route('/service')
def service():
    return render_template('frontend/service.html')

@app.route('/login')
def login():
    return render_template('frontend/login.html')

@app.route('/register')
def register():
    return render_template('frontend/register.html')



# @app.route('/register', methods=['POST'])
# def register():
#     if 'file' not in request.files:
#         return redirect(request.url)

#     file = request.files['file']

#     if file.filename == '':
#         return redirect(request.url)

#     if file:
#         filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(filename)
#         # Save other registration details to the database here
#         # You can use a database library like SQLAlchemy for this

#         return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
