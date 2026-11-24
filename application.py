from flask import Flask
application = Flask(__name__)

@application.route("/")
def home():
    return "Hello from Jenkins + CodePipeline! v1"

@application.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    application.run(port=5000)
