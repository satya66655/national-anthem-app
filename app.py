from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
nano templates/index.html
<html>
<head><title>National Anthem</title></head>
<body>
  <h1>Jana Gana Mana</h1>
  <p>Stanzas coming soon.</p>
</body>
</html>

