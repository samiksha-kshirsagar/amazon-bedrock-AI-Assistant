from flask import Flask, render_template, request
from bedrock_client import BedrockClient

app = Flask(__name__)

client = BedrockClient()

@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""

    if request.method == "POST":

        question = request.form["question"]

        answer = client.invoke(question)

    return render_template(
        "index.html",
        answer=answer
    )

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)