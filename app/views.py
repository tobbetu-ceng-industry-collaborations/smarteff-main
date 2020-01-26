from app import app

# show current DB tables under the route /list
@app.route("/list")
def list():
    return "Hello, tables will be listed here soon!"
