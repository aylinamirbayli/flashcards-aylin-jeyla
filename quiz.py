import random

# Git flashcards: (question, answer)
git_cards = [
    ("Which command shows the history, one line per commit?", "git log --oneline"),
    ("Which command creates a branch and moves to it?", "git switch -c <name>"),
    ("Which command shows what changed but is not staged yet?", "git diff"),
]

def print_random_card():
    """Print a random flashcard: the question, then the answer."""
    question, answer = random.choice(git_cards)
    print(f"Q: {question}")
    print(f"A: {answer}")

if __name__ == "__main__":
    print("Flashcards for the course")
    print_random_card()
