import os
import json
from flask import Flask, render_template, request, jsonify
import anthropic

app = Flask(__name__)

# Initialise Anthropic client using environment variable
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/questions", methods=["POST"])
def generate_questions():
    data = request.get_json()
    job_title = data.get("job_title", "").strip()

    if not job_title:
        return jsonify({"error": "Please provide a job title."}), 400

    if len(job_title) > 100:
        return jsonify({"error": "Job title is too long."}), 400

    prompt = f"""You are an expert hiring manager and interview coach.

Generate exactly 3 thoughtful, specific interview questions for a {job_title} role.

Requirements:
- Each question should be meaningful and tailored to the specific responsibilities and challenges of a {job_title}
- Include a mix of behavioural, situational, and role-specific questions
- Questions should help reveal a candidate's experience, problem-solving ability, and cultural fit
- Do NOT number the questions or add any preamble or explanation
- Return ONLY a JSON array of 3 strings, each being one question

Example format:
["Question one here?", "Question two here?", "Question three here?"]"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=512,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        response_text = message.content[0].text.strip()

        # Parse the JSON array from the response
        questions = json.loads(response_text)

        if not isinstance(questions, list) or len(questions) != 3:
            return jsonify({"error": "Unexpected response format. Please try again."}), 500

        return jsonify({"questions": questions})

    except json.JSONDecodeError:
        return jsonify({"error": "Could not parse AI response. Please try again."}), 500
    except anthropic.APIError as e:
        return jsonify({"error": f"AI API error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": "Something went wrong. Please try again."}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
