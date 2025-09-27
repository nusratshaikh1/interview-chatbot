def get_chatbot_response(user_input, rules):
    user_input = user_input.lower()

    # Match keywords with rules
    if "tip" in user_input or "prepare" in user_input:
        return rules.get("tips", "Prepare well for interviews! Research the company, practice common questions, and be confident.")

    elif "strength" in user_input:
        return rules.get("strengths", "Talk about your strengths confidently, like teamwork, problem-solving, or adaptability.")

    elif "weakness" in user_input:
        return rules.get("weaknesses", "Mention a weakness but show how you are improving it. For example, public speaking → joining workshops.")

    elif "introduce" in user_input or "yourself" in user_input or "tell me about" in user_input:
        return rules.get("introduce", "Start with your background, highlight your skills/achievements, and end with your future goals.")

    elif "why company" in user_input or "why this job" in user_input:
        return rules.get("why company", "Say how your values align with the company, mention culture, growth, and your contribution.")

    # ✅ Python interview questions (specific)
    elif "python" in user_input and "question" in user_input:
        questions = [
            "1. What are Python’s key features that make it different from other languages?",
            "2. Explain the difference between list, tuple, and set in Python.",
            "3. What is the difference between shallow copy and deep copy?",
            "4. How is memory management handled in Python?",
            "5. Explain the concept of decorators in Python with an example.",
            "6. What is the difference between @staticmethod, @classmethod, and normal methods?",
            "7. How does Python handle exceptions? Give an example.",
            "8. What is the purpose of the __init__ method in Python classes?",
            "9. What are Python generators and how are they different from normal functions?",
            "10. Explain the difference between 'is' and '==' operators in Python."
        ]
        # ✅ join with new line for proper display
        return "\n".join(questions)

    # ✅ General interview questions
    elif "question" in user_input or "sample" in user_input or "practice" in user_input:
        general_questions = [
            "🎯 Common Interview Questions:",
            "1. Tell me about yourself.",
            "2. Why should we hire you?",
            "3. What are your strengths?",
            "4. What are your weaknesses?",
            "5. Where do you see yourself in 5 years?",
            "6. Why do you want to work here?",
            "7. Tell me about a challenge you faced and how you solved it."
        ]
        return "\n".join(general_questions)

    elif "resume" in user_input or "cv" in user_input:
        return rules.get("resume", "Keep your resume clear, concise, and highlight achievements with measurable results.")

    elif "dress" in user_input or "attire" in user_input:
        return rules.get("dress", "Dress professionally. For men: formal shirt/pants. For women: formal wear or decent ethnic. Avoid flashy colors.")

    elif "body language" in user_input or "gesture" in user_input:
        return rules.get("body language", "Maintain eye contact, sit straight, give a confident smile, and avoid crossing arms.")

    elif "closing" in user_input or "end interview" in user_input:
        return rules.get("closing", "End positively: thank the interviewer, express enthusiasm, and ask thoughtful questions.")

    else:
        return "I'm not sure about that. Can you ask something related to interview preparation?"
