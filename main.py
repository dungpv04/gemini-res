from langchain_google_genai import ChatGoogleGenerativeAI
from flask import Flask, request
from flask_cors import CORS
import os
import json
app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def sendMessage():
    #API_KEY = os.getenv("API_KEY")
    llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key="AIzaSyCZ4qM5bJuq9GCOHpTgaY1AqI9kfzSMhlE"
    )

    userMsg = json.loads(request.data)

    messages = [
        (
            "system",
            """You are a chatbot which help user to find information about real estate, house buying, house finding. If user ask another topic or you don't
                know ther answer, just say you don't know or can't answer. Always say thank you for asking""",
        ),
        ("human", f"{userMsg}"),
    ]
    ai_msg = llm.invoke(messages)
    print(ai_msg.content)
    return {"response": ai_msg.content}

if __name__ == '__main__':
    app.run(debug=False)