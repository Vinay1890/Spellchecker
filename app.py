from spellchecker import SpellChecker

class SpellcheckerApp:
    def __init__(self):
        self.spell = SpellChecker()


    def correct_text(self,text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_words != word.lower():
                print(f'Correcting "{word}" to "{corrected_word}"')
            corrected_words.append(corrected_word)
        # Return the coreect text
        return ' '.join(corrected_words)

# step-5 running the app

    def run(self):
        print("\n--- Spell checker ----")


        while  True:
          text = input('Enter text to check (or type "exit" to quit): ')

          if text.lower() == 'exit':
             print('closing the program....')
             break

          Corrected_text = self.correct_text(text)
          print(f'Corrected Text : {Corrected_text}')


if __name__ == "__main__":
    SpellcheckerApp().run()