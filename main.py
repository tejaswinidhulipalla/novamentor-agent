from flask import Flask, request, render_template_string
from tools import project_idea_tool

app = Flask(__name__)

# Simple Web UI
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>NovaMentor AI</title>
</head>
<body style="font-family: Arial; padding:40px;">
    <h2>🤖 NovaMentor AI Career Mentor</h2>

    <form method="POST">
        <label>Branch:</label><br>
        <input type="text" name="branch"><br><br>

        <label>Skills:</label><br>
        <input type="text" name="skills"><br><br>

        <label>Level:</label><br>
        <input type="text" name="level"><br><br>

        <label>Goal:</label><br>
        <input type="text" name="goal"><br><br>

        <button type="submit">Generate Ideas</button>
    </form>

    {% if ideas %}
        <h3>💡 Suggestions:</h3>
        <pre>{{ ideas }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    ideas = ""
    if request.method == "POST":
        branch = request.form["branch"]
        skills = request.form["skills"]
        level = request.form["level"]
        goal = request.form["goal"]

        ideas = project_idea_tool(branch, skills, level, goal)

    return render_template_string(HTML_PAGE, ideas=ideas)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)