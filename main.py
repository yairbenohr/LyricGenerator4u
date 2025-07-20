from lyric_generator import LyricGenerator

def main():
    generator = LyricGenerator("data/wordbanks.json")

    print("🎤 Welcome to LyricGenerator4u 🎤")

    while True:
        print("\nAvailable genres: pop, rap, indie, synthpop")
        genre = input("Choose a genre: ").strip().lower()

        print("Available moods: hopeful, melancholy, dark, trippy, romantic")
        mood = input("Choose a mood: ").strip().lower()

        print("\n Generating your lyrics...\n")
        lyrics = generator.generate_lyrics(genre, mood)

        for line in lyrics:
            print(line)

        again = input("\nWould you like to generate more lyrics? (Y/N): ").strip().lower()
        if again != 'y':
            print("\nThanks for using LyricGenerator4u. Goodbye! ")
            break

if __name__ == "__main__":
    main()




