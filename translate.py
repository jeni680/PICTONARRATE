""" from googletrans import Translator

class EnglishToMalayalam:
    English to Malayalam translation class.

    @staticmethod
    def translate_story(story):
       
        Translate the given English story to Malayalam.
        Args:
            story (str): The English story to translate.
        Returns:
            str: Translated story in Malayalam.
        
        translator = Translator()
        sentences = story.split('. ')  # Split the story into sentences
        translated_sentences = []

        for sentence in sentences:
            if sentence.strip():  # Skip empty sentences
                try:
                    translation = translator.translate(sentence.strip(), dest="ml")
                    translated_sentences.append(translation.text)
                except Exception as e:
                    print(f"Translation failed for sentence: {sentence}\nError: {e}")
                    translated_sentences.append(sentence)  # Fallback to original text

        return '. '.join(translated_sentences)
"""


from deep_translator import GoogleTranslator

def translate_story(story, target_language="ml"):
    try:
        translation = GoogleTranslator(source='auto', target=target_language).translate(story)
        return translation
    except Exception as e:
        print(f"Translation failed: {e}")
        return story  # Fallback to the original story



"""# Example usage
english_story = "Aarav loved exploring his grandmother’s old room. It was filled with dusty books, antique furniture, and forgotten treasures. One evening, while rummaging through an old trunk, he found a small, framed painting of a beautiful garden with a stone bench in the middle. Strangely, the colors in the painting looked fresh, as if they had been painted yesterday.Curious, Aarav showed it to his grandmother. Her eyes widened in shock. This painting belonged to my mother, she whispered.She always said it was special, but no one believed her.That night, unable to shake his curiosity, Aarav hung the painting on his bedroom wall. As he stared at it, he felt a strange pull—like the garden in the painting was calling to him. Suddenly, the air shimmered, and before he could react, he found himself sitting on the stone bench inside the painting."
malayalam_story = translate_story(english_story)
print("Translated Story (Malayalam):")
print(malayalam_story)
"""