import random

# Git flashcards: (question, answer)
git_cards = [
    ("Which command shows the history, one line per commit?", "git log --oneline"),
    ("Which command creates a branch and moves to it?", "git switch -c <name>"),
    ("Which command shows what changed but is not staged yet?", "git diff"),
]

# Terminal flashcards: (question, answer)
terminal_cards = [
    ("Which command shows the current working directory?", "pwd"),
    ("Which command lists all files, including hidden ones?", "ls -a"),
    ("Which command moves or renames a file?", "mv"),
]

def print_random_card():
    """Print a random flashcard from both decks."""
    all_cards = git_cards + terminal_cards
    question, answer = random.choice(all_cards)
    print(f"Q: {question}")
    print(f"A: {answer}")

if __name__ == "__main__":
    print("Flashcards for the course")
    print_random_card()
