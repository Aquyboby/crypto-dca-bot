from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Crypto DCA Bot est actif."

@app.route('/run')
def run_script():
    from main import main
    main()
    return "Script exécuté."

def keep_alive():
    Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 8080}).start()


