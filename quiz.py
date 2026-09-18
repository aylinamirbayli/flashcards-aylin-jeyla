import random

# Git flashcards: (question, answer)
git_cards = [
    ("Which command shows the history, one line per commit?", "git log --oneline"),
    ("Which command creates a branch and moves to it?", "git switch -c <name>"),
    ("Which command shows what changed but is not staged yet?", "git diff"),
]

def print_random_card(topic="git"):
    """Print a random flashcard with a topic label."""
    if topic == "git":
        question, answer = random.choice(git_cards)
        print(f"[GIT] Q: {question}")
        print(f"[GIT] A: {answer}")

if __name__ == "__main__":
    print("Flashcards for the course")
    print_random_card(topic="git")
