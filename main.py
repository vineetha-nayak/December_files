import json
import os
import random

FLASHCARD_FILE = "flashcards.json"

# Load flashcards from file
def load_flashcards():
    if os.path.exists(FLASHCARD_FILE):
        with open(FLASHCARD_FILE, "r") as file:
            return json.load(file)
    return []

# Save flashcards to file
def save_flashcards(flashcards):
    with open(FLASHCARD_FILE, "w") as file:
        json.dump(flashcards, file, indent=2)

# Add a new flashcard
def add_flashcard(flashcards):
    question = input("Enter the question: ").strip()
    answer = input("Enter the answer: ").strip()
    flashcards.append({"question": question, "answer": answer})
    print("✅ Flashcard added!")

# Practice flashcards randomly
def practice_flashcards(flashcards):
    if not flashcards:
        print("⚠️ No flashcards available. Please add some first.")
        return

    random.shuffle(flashcards)
    for card in flashcards:
        input(f"\n🧠 Q: {card['question']}\n(Press Enter to see the answer)")
        print(f"💡 A: {card['answer']}")
        input("Press Enter to continue...")

# Main menu
def main():
    flashcards = load_flashcards()

    while True:
        print("\n📚 Flashcard Learning App")
        print("1. Add Flashcard")
        print("2. Practice Flashcards")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            add_flashcard(flashcards)
        elif choice == "2":
            practice_flashcards(flashcards)
        elif choice == "3":
            save_flashcards(flashcards)
            print("💾 Flashcards saved. Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()