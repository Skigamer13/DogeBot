from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
    return "There were over a dozen extinction level events before even the dinosaurs got theirs! When the Earth starts to settle, God throws a stone at it. And believe me, He's winding up. We have to evolve. -Ultron"


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
