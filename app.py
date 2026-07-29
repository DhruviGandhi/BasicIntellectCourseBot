from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
courses = {
    "python": {
        "duration": "3 Months",
        "fees": "₹10,000"
    },
    "c": {
        "duration": "2 Months",
        "fees": "₹6,000"
    },
    "java": {
        "duration": "3 Months",
        "fees": "₹12,000"
    },
    "cyber security": {
        "duration": "4 Months",
        "fees": "₹15,000"
    },
    "bca": {
        "duration": "3 Years",
        "fees": "As per University"
    }
}

def chatbot(message):

    msg = message.lower()

    if "hello" in msg or "hi" in msg:
        return "Welcome to Intellect Computers."

    if "contact" in msg:
        return """Contact Us

📍 City Light, Surat

📞 9876543210"""

    for course in courses:

        if course in msg:

            return f"""
Course : {course.title()}

Duration : {courses[course]['duration']}

Fees : {courses[course]['fees']}
"""

    return "Sorry, I didn't understand."

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])

def chat():

    user = request.json['message']

    reply = chatbot(user)

    return jsonify({"reply": reply})

if __name__=="__main__":
    app.run(debug=True)