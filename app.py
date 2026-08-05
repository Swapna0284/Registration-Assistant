from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Store registrations in memory
registrations = []

def detect_intent(message):
    message = message.lower()

    if any(word in message for word in ["hello", "hi", "hey"]):
        return "greeting"

    elif "register" in message:
        return "register"

    elif "eligibility" in message or "eligible" in message:
        return "eligibility"

    elif "course" in message:
        return "course"

    elif "thanks" in message or "thank you" in message:
        return "thanks"

    return "unknown"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    user_message = data["message"]

    intent = detect_intent(user_message)

    if intent == "greeting":
        response = "Hello! Welcome to the AI Registration Assistant."

    elif intent == "register":
        response = "Please provide your Full Name, Email and Course."

    elif intent == "eligibility":
        response = "Eligibility depends on the selected course. Please mention your course."

    elif intent == "course":
        response = "We currently support AI, Data Science, Python and Web Development."

    elif intent == "thanks":
        response = "You're welcome! Happy to help."

    else:
        response = "Sorry, I couldn't understand. Please ask about registration or eligibility."

    return jsonify({"reply": response})


if __name__ == "__main__":
    app.run(debug=True)
