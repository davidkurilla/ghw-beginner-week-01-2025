from flask import Flask, render_template, request
import requests

app = Flask(__name__)

base_url = "https://pokeapi.co/api/v2/"

@app.route("/", methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        name = request.form.get('name').lower()
        pokemon_info = get_pokemon(name)
        return render_template("index.html", info=pokemon_info)

    return render_template("index.html")

def get_pokemon(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        return None

if __name__ == "__main__":
    app.run(debug=True)