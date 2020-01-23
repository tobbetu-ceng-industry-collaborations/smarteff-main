from app import app

@app.route("/list")
def list():
    return "Hello, tables will be listed here soon!"
