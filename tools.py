import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def project_idea_tool(branch, skills, level, goal):

    print("🔧 ProjectIdeaTool activated...\n")

    prompt = f"""
You are NovaMentor, an AI career mentor.

Suggest 3 project ideas for:
Branch: {branch}
Skills: {skills}
Level: {level}
Goal: {goal}
"""

    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        print("⚠️ Groq Error:", e)
        print("⚠️ Groq API unavailable. Switching to Offline Mode...\n")

        return f"""
🎯 Offline Project Ideas for {branch} Student

1) AI Resume Analyzer
2) Smart Study Planner Agent
3) Project Recommendation System
"""