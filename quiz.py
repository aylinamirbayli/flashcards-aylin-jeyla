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

def print_random_card(topic=None):
    """Print a random flashcard with its label from the chosen topic or both."""
    if topic == "git":
        deck = [("[GIT]", q, a) for q, a in git_cards]
    elif topic == "terminal":
        deck = [("[TERMINAL]", q, a) for q, a in terminal_cards]
    else:
        deck = [("[GIT]", q, a) for q, a in git_cards] + [("[TERMINAL]", q, a) for q, a in terminal_cards]
    
    label, question, answer = random.choice(deck)
    print(f"{label} Q: {question}")
    print(f"{label} A: {answer}")

if __name__ == "__main__":
    print("Flashcards for the course")
    print_random_card()
    print_random_card(topic="git")
    print_random_card(topic="terminal")
