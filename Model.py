import proselint
from textblob import TextBlob
class SpellCheckerModule:
    def __init__(self):
        pass

    def correct_spell(self, text):
        # Correct spelling using TextBlob
        corrected_text = str(TextBlob(text).correct())
        return corrected_text

    def correct_grammar(self, text):
        # Use proselint to check for grammar issues
        result = proselint.tools.lint(text)
        print("Proselint result:", result)  # Print the result to understand its structure

        # Handle the output based on its structure
        if isinstance(result, list):
            found_mistakes = [issue[1] for issue in result if isinstance(issue, tuple) and len(issue) > 1]
        else:
            found_mistakes = []

        found_mistakes_count = len(found_mistakes)
        return found_mistakes, found_mistakes_count

if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "Hello world. I like mashine learning. appple. bananana"
    print("Corrected Spelling:", obj.correct_spell(message))
    grammar_corrections, mistakes_count = obj.correct_grammar(message)
    print(f"Grammar Issues (found {mistakes_count}):")
    for correction in grammar_corrections:
        print(f"  - {correction}")
