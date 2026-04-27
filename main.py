from services.pdf_loader import load_pdf_text
from services.section_splitter import split_sections
from services.tutor import teach
from services.evaluator import evaluate
from services.quiz_generator import generate_quiz
from services.quiz_evaluator import evaluate_quiz


def run():

    print("📄 Loading PDF...")
    text = load_pdf_text("data/retail.pdf")

    print("🧠 Splitting sections...")
    sections = split_sections(text)

    # Show sections
    print("\n📚 Available Sections:\n")
    for i, key in enumerate(sections.keys()):
        print(f"{i+1}. {key}")

    # Select section
    choice = int(input("\nSelect a section: ")) - 1
    section_title = list(sections.keys())[choice]
    section_content = sections[section_title]

    print(f"\n📘 Teaching: {section_title}\n")

    # Teach
    explanation = teach(section_content)
    print(explanation)

    # User understanding
    user_answer = input("\n📝 Explain what you understood:\n")

    print("\n📊 Evaluating your understanding...\n")
    result = evaluate(section_content, user_answer)
    print(result)

    # Generate Quiz
    print("\n🧪 Generating Quiz...\n")
    quiz = generate_quiz(section_content)

    print("\n🧪 QUIZ:\n")
    print(quiz)

    # 🧠 Take user answers
    print("\n✍️ Answer the MCQs (format: 1-a, 2-b, 3-c)")
    mcq_answers = input("Your MCQ answers: ")

    print("\n✍️ Answer subjective questions:")
    sub1 = input("Q1: ")
    sub2 = input("Q2: ")

    # Combine answers
    user_answers = f"""
MCQ Answers:
{mcq_answers}

Subjective Answers:
1. {sub1}
2. {sub2}
"""

    # Evaluate Quiz
    print("\n📊 Evaluating Quiz...\n")
    quiz_result = evaluate_quiz(section_content, quiz, user_answers)

    print(quiz_result)

    print("\n✅ Session Complete!\n")


if __name__ == "__main__":
    run()