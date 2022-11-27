from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__) 
    
@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/chat')#, methods==['POST'])
def chat_page():
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)
