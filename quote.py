import random

quotes = {
    "Steve Jobs": [
        "The only way to do great work is to love what you do.",
        "Your time is limited, so don’t waste it living someone else’s life.",
        "Innovation distinguishes between a leader and a follower.",
        "I’m convinced that about half of what separates successful entrepreneurs from the non-successful ones is pure perseverance."
    ],
    "Albert Einstein": [
        "Life is like riding a bicycle. To keep your balance, you must keep moving.",
        "Imagination is more important than knowledge.",
        "Strive not to be a success, but rather to be of value.",
        "The important thing is not to stop questioning. Curiosity has its own reason for existing."
    ],
    "Maya Angelou": [
        "I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.",
        "You may not control all the events that happen to you, but you can control your attitude toward them.",
        "If you don't like something, change it. If you can't change it, change your attitude.",
        "Nothing will work unless you do."
    ],
    "Mark Twain": [
        "The two most important days in your life are the day you are born and the day you find out why.",
        "The secret of getting ahead is getting started.",
        "Courage is resistance to fear, mastery of fear, not absence of fear.",
        "Life is short, and it is up to you to make it sweet."
    ],
    "Babe Ruth": [
        "Never let the fear of striking out keep you from playing the game.",
        "It’s hard to beat a person who never gives up.",
        "Every strike brings me closer to the next home run.",
        "I’d play for half my salary if I could hit in this dump all the time."
    ],
    "Nelson Mandela": [
        "It always seems impossible until it’s done.",
        "Education is the most powerful weapon which you can use to change the world.",
        "For to be free is not merely to cast off one’s chains, but to live in a way that respects and enhances the freedom of others.",
        "What counts in life is not the mere fact that we have lived. It is what difference we have made to the lives of others."
    ],
    "Confucius": [
        "It does not matter how slowly you go as long as you do not stop.",
        "Our greatest glory is not in never falling, but in rising every time we fall.",
        "Life is really simple, but we insist on making it complicated.",
        "Wherever you go, go with all your heart."
    ],
    "Oscar Wilde": [
        "Be yourself; everyone else is already taken.",
        "To live is the rarest thing in the world. Most people exist, that is all.",
        "We are all in the gutter, but some of us are looking at the stars.",
        "Experience is simply the name we give our mistakes."
    ],
    "Winston Churchill": [
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "If you're going through hell, keep going.",
        "To improve is to change; to be perfect is to change often.",
        "Courage is what it takes to stand up and speak; courage is also what it takes to sit down and listen."
    ],
    "Helen Keller": [
        "Life is either a daring adventure or nothing at all.",
        "The only thing worse than being blind is having sight but no vision.",
        "Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence.",
        "Alone we can do so little; together we can do so much."
    ],
    "Ralph Waldo Emerson": [
        "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.",
        "The only person you are destined to become is the person you decide to be.",
        "What lies behind us and what lies before us are tiny matters compared to what lies within us.",
        "For every minute you are angry you lose sixty seconds of happiness."
    ],
    "Eleanor Roosevelt": [
        "The future belongs to those who believe in the beauty of their dreams.",
        "No one can make you feel inferior without your consent.",
        "You gain strength, courage, and confidence by every experience in which you really stop to look fear in the face.",
        "Do what you feel in your heart to be right – for you’ll be criticized anyway."
    ],
    "Henry Ford": [
        "Whether you think you can or you think you can’t, you’re right.",
        "Failure is simply the opportunity to begin again, this time more intelligently.",
        "Coming together is a beginning; keeping together is progress; working together is success.",
        "You can’t build a reputation on what you are going to do."
    ],
    "Vincent Van Gogh": [
        "I dream my painting, and then I paint my dream.",
        "What would life be if we had no courage to attempt anything?",
        "The more I read, the more I acquire, the more certain I am that I know nothing.",
        "Great things are not done by impulse, but by a series of small things brought together."
    ],
    "Jim Rohn": [
        "Don’t wish it was easier, wish you were better.",
        "Success is nothing more than a few simple disciplines, practiced every day.",
        "The book you don’t read won’t help.",
        "Your life does not get better by chance, it gets better by change."
    ],
    "Tony Robbins": [
        "The only limit to your impact is your imagination and commitment.",
        "Setting goals is the first step in turning the invisible into the visible.",
        "It is in your moments of decision that your destiny is shaped.",
        "Stay committed to your decisions, but stay flexible in your approach."
    ]
}

def random_quote(author):
    if author in quotes:
        quote = random.choice(quotes[author])
        print(f"{author}: {quote}")
    else:
        print("Author not found. Please select a valid author.")

def list_authors():
    print("Available authors:")
    for author in quotes.keys():
        print(f"- {author}")

if __name__ == "__main__":
    list_authors()
    selected_author = input("Select an author: ")
    random_quote(selected_author)
