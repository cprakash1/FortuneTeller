def main():
    print("🔮 Step into Chandra Prakash's Mystical Fortune Realm (21JE0260) 🔮")
    
    while True:
        mood = input("What's your mood today? (happy/sad/neutral/stressed) or type 'exit' to quit: ").strip().lower()
        
        if mood == "exit":
            print("✨ Thank you for visiting! May your path be bright, Chandra Prakash. ✨")
            break
        elif mood == "happy":
            print("✨ Your fortune: Brilliant paths unfold before you, Chandra Prakash! Let your joy light the way. ✨")
        elif mood == "sad":
            print("✨ Your fortune: Even in shadows, a spark of hope endures. Brighter times are coming soon! ✨")
        elif mood == "neutral":
            print("✨ Your fortune: This day is yours to shape. Dream boldly and take the leap! ✨")
        elif mood == "stressed":
            print("✨ Your fortune: Take a deep breath, for calm waters lie ahead. You’ve got this! ✨")
        else:
            print("✨ Your fortune: The cosmos loves a twist. Welcome each surprise with open arms! ✨")

if __name__ == "__main__":
    main()