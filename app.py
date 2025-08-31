from flashcard_data import load_flashcards

def run_flashcard_app():
    flashcards = load_flashcards()
    score = 0

    print("🧠 Welcome to the Python Flashcard Learning App!")
    
    for i, card in enumerate(flashcards, 1):
        print(f"\nQ{i}: {card.question}")
        user_input = input("Your answer: ")

        if card.check_answer(user_input):
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! Correct answer: {card.answer}")

    print(f"\n🎉 Final Score: {score} out of {len(flashcards)}")

if __name__ == "__main__":
    run_flashcard_app()