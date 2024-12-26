from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

poll_data = {
    "question": "What is your favorite programming language?",
    "fields": ["Python", "JavaScript", "Java", "C++"]
}

votes = {language: 0 for language in poll_data["fields"]}

@app.route('/')
def index():
    return render_template('index.html', data=poll_data)

@app.route('/vote', methods=['POST'])
def vote():
    voted_option = request.json['option']
    if voted_option in votes:
        votes[voted_option] += 1
    return jsonify(votes)

if __name__ == '__main__':
    app.run(debug=True)
