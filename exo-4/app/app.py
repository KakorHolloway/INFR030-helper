from flask import Flask, request, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None  # Initialize the message variable
    if request.method == 'POST':
        host = request.form['host']
        port = request.form['port']
        username = request.form['username']
        password = request.form['password']
        database = request.form['database']

        connection_string = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'
        app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
        db = SQLAlchemy(app)

        try:
            db.engine.execute('SELECT 1')
            message = "Connexion réussie"
        except Exception as e:
            message = f"Erreur de connexion : {e}"

    return render_template_string(TEMPLATE, message=message)


TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tester la connexion à une base de données</title>
</head>
<body>
    <h1>Tester la connexion à une base de données</h1>
    <form method="post">
        <label for="host">Hôte:</label>
        <input type="text" id="host" name="host" required><br>

        <label for="port">Port:</label>
        <input type="text" id="port" name="port" required><br>

        <label for="username">Nom d'utilisateur:</label>
        <input type="text" id="username" name="username" required><br>

        <label for="password">Mot de passe:</label>
        <input type="password" id="password" name="password" required><br>

        <label for="database">Nom de la base de données:</label>
        <input type="text" id="database" name="database" required><br>

        <input type="submit" value="Tester la connexion">
    </form>

    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
