import json
import os
import sys

class Flashcard:
    def __init__(self, front, back):
        self.front = front
        self.back = back

class Deck:
    def __init__(self, filename="deck.json"):
        self.filename = filename
        self.cards = self.load_deck()

    def load_deck(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    raise ValueError("Deck JSON must be a list of flashcards.")
                return [Flashcard(card["front"], card["back"]) for card in data]
        except FileNotFoundError:
            print(f"❌ File '{self.filename}' not found.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"❌ Invalid JSON format in '{self.filename}'.")
            sys.exit(1)
        except (KeyError, ValueError) as e:
            print(f"❌ Error loading deck: {e}")
            sys.exit(1)

class FlashcardSession:
    def __init__(self, deck):
        self.queue = deck.cards.copy()
        self.remembered = set()

    def run(self):
        self.clear_screen()
        print("📚 Welcome to the Flashcard Session!\n")
        print("You will be shown questions. Press Enter to flip and answer.\n")

        while self.queue:
            card = self.queue.pop(0)
            self.present_card(card)

        print("\n🎉 Session complete!")
        print(f"✅ You remembered {len(self.remembered)} cards.")

    def present_card(self, card):
        print(f"\n📝 {card.front}")
        input("Press Enter to see the answer...")
        print(f"💡 {card.back}")

        while True:
            remembered = input("Did you remember this? (y/n): ").strip().lower()
            if remembered == 'y':
                self.remembered.add((card.front, card.back))
                break
            elif remembered == 'n':
                self.queue.append(card)
                break
            else:
                print("Please enter 'y' or 'n'.")

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

def main():
    deck = Deck("deck.json")
    session = FlashcardSession(deck)
    session.run()

if __name__ == "__main__":
    main()