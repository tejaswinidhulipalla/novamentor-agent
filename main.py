from flask import Flask, request, jsonify
from tools import project_idea_tool

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "NovaMentor Agent is running on Cloud Run!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json

    branch = data.get("branch")
    skills = data.get("skills")
    level = data.get("level")
    goal = data.get("goal")

    ideas = project_idea_tool(branch, skills, level, goal)

    return jsonify({"ideas": ideas})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)