import json
import random

class LyricGenerator:
    def __init__(self, wordbank_file):
        self.wordbank = self.load_wordbank(wordbank_file)

    def load_wordbank(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: {file_path} not found.")
            return {}

    def generate_lyrics(self, genre, mood, num_lines=4):
        words = self.wordbank.get(genre, {}).get(mood, [])
        if not words:
            return ["[No words found for that genre/mood]"]

        templates = {
            "pop": [
                "I feel the {w1} when you {w2} my {w3}",
                "You're the {w1} in my {w2}, shining so {w3}",
                "Every {w1} leads me back to your {w2}",
                "We dance through the {w1}, chasing our {w2}"
            ],
            "rap": [
                "{w1} in my mind, can't {w2} the {w3}",
                "Drop a {w1}, hit the {w2}, stack the {w3}",
                "Through the {w1}, I see your {w2} burn",
                "Riding with a {w1}, heart cold like {w2}"
            ],
            "indie": [
                "The {w1} waits beneath your {w2}",
                "Quiet like {w1}, we drift in {w2}",
                "A {w1} painted on your {w2}, soft as {w3}",
                "I write your name in {w1}, chasing {w2}"
            ],
            "synthpop": [
                "We ride the {w1}, fading into {w2}",
                "Your {w1} echoes through the {w2} light",
                "Caught in a {w1} loop with you",
                "Neon {w1} under midnight {w2}"
            ]
        }

        selected_templates = templates.get(genre, [])
        if not selected_templates:
            return ["[No templates found for that genre]"]

        lyrics = []
        for _ in range(num_lines):
            template = random.choice(selected_templates)
            # Use 3 words no matter how many placeholders the template has
            chosen_words = random.choices(words, k=3)
            line = template.format(w1=chosen_words[0], w2=chosen_words[1], w3=chosen_words[2])
            lyrics.append(line.capitalize())

        return lyrics


