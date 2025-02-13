def madlibs():
    print("\n🏏 Welcome to the Virat Kohli Mad Libs Game! 🏏\n")
    
    # Collecting user inputs
    adjective1 = input("Enter an adjective: ")
    stadium_name = input("Enter a stadium name: ")
    adjective2 = input("Enter another adjective: ")
    adjective3 = input("Enter one more adjective: ")
    team_name = input("Enter a cricket team name: ")
    animal = input("Enter an animal: ")
    adjective4 = input("Enter an adjective: ")
    verb_past = input("Enter a past-tense verb: ")
    number1 = input("Enter a number: ")
    phrase = input("Enter a chant or phrase: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    nickname = input("Enter a nickname for Virat Kohli: ")
    adjective5 = input("Enter an adjective: ")
    cricket_shot = input("Enter a type of cricket shot (e.g., cover drive, pull shot): ")
    adjective6 = input("Enter an adjective: ")
    number2 = input("Enter another number: ")
    emotion = input("Enter an emotion: ")
    verb_past2 = input("Enter another past-tense verb: ")
    number3 = input("Enter a number: ")
    country_name = input("Enter a country name: ")
    adjective7 = input("Enter an adjective: ")
    quote = input("Enter a funny or inspirational quote: ")
    title_nickname = input("Enter a title/nickname for Virat Kohli: ")

    # Story template with placeholders
    story = f"""
    It was a {adjective1} day at the {stadium_name}, and the crowd was roaring with excitement. 
    Virat Kohli walked onto the field with his {adjective2} bat, ready to face the {adjective3} bowlers of {team_name}. 
    The tension was high as he took his stance, eyes focused like a {animal} hunting its prey.

    The bowler ran in and delivered a {adjective4} ball. With a swift movement, Kohli {verb_past} it for a glorious {number1}-run shot! 
    The crowd erupted, chanting "{phrase}" in unison. His teammates on the sidelines were {verb_ing}, knowing that he was once again proving 
    why he is called {nickname}.

    As the innings progressed, Kohli displayed his {adjective5} skills, executing perfect {cricket_shot} and outsmarting the fielders 
    with his {adjective6} running between the wickets. With just {number2} runs needed to reach his century, he took a deep breath 
    and prepared for the next ball.

    The bowler charged in, and in a moment of pure {emotion}, Kohli {verb_past2} the ball out of the stadium! A stunning {number3}-run shot! 
    His century was complete, and the entire {country_name} celebrated his {adjective7} performance.

    At the post-match interview, when asked about his innings, Kohli smiled and said, "{quote}."

    And that’s how Virat Kohli once again proved why he is a true {title_nickname} of cricket! 🏏🔥
    """

    # Print the final story
    print("\n🏆 Here’s Your Virat Kohli Mad Libs Story! 🏆\n")
    print(story)

# Run the Mad Libs game
if __name__ == "__main__":
    madlibs()
