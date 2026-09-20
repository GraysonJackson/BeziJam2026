# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define w = Character("Winston")
define d = Character("Dhampir")
define i = Character("Ica")
define m = Character("Madeline")
define r = Character("Razzle Dazzle")
define n = Character("Nicky")
define u = Character("Ulysses")
define f = Character("Freddy")
define v = Character("Victor")
define j = Character("Jeramiah")
define b = Character("Barry")
define c = Character("Carl")
define t = Character("Tucker")
define e = Character("Edgar")
define s = Character("Simon")
define k = Character("Kyle")
define a = Character("Alan")


# The game starts here.

label start:

    # # Show a background. This uses a placeholder by default, but you can
    # # add a file (named either "bg room.png" or "bg room.jpg") to the
    # # images directory to show it.

    # scene bg sky

    # # This shows a character sprite. A placeholder is used, but you can
    # # replace it by adding a file named "eileen happy.png" to the images
    # # directory.

    # # show eileen happy
    # show kibby at truecenter

    # # These display lines of dialogue.

    # k "Did you change the name and save directory of the game in options.rpy?"

    # $ answer = renpy.input("Did you change the values at the top of options.rpy?").strip().lower()

    # if answer == "yes":
    #     k "Good job"
    # else:
    #     k "If not, you should do so right away! Saves will not work properly until you do."

    # $ renpy.notify("This is a notification")

    # menu:
    #     "This is a sample choice menu"
    #     "Choice 1":
    #         pass
    #     "Choice 2":
    #         pass

    "The year is 1996. You have been hired to assist the ATLAS superhero team in their investigation into a recent murder case, but you only have one week to solve it. While you need to solve the crime, it's also a great time to get to know the ATLAS team. Who knows? Maybe as you spend time with them throughout the week, you may even fall in love..."
    "To introduce you to the team, here's Freddy!"
    f "Hey there! I'm Freddy, one of the members of ATLAS! I wanted to help you meet the team and get an idea of them before you have to get right into the thick of it. Each member of the team has their own personality and cool power! For example, as you may be able to tell, I have super hearing, but I can also release sonic screams. Here, let's meet the others. "

    # Ulysses
    f "Ulysses Umbral. Co-leader of the team. He's a bit of a stern face guy who comes off a bit serious (and maybe a hardass), but he just wants what's best for the team. His power is he can see the future, but he isn't able to tell others, otherwise he may die. The good news is that he's still a great guide for the team, and is our team's strategist!"

    # Razzle Dazzle
    f "Razzle Dazzle. She's one of the original members of the team, and is a bright spirit for ATLAS. While she may not be the smartest, she brings a lot of energy and fun to the team! As you can likely tell, her power is flame cloaking and flame projectiles."

    # Madeline
    f "Madeline Taylors. Another one of the great minds on the team. She's a bit quiet and rude at first, but the moment you get her talking you'll see how... uh... passionate she can be about what she thinks. Her power is superintelligence, which she uses to help her create powerful suits of armor that can do all kinds of things!"

    # Winston
    
    # Nicky

    # Ica

    # This ends the game.
    return
