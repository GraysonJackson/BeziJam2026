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
default uly = 0
default winn = 0
default dhamp = 0
default ica = 0
default mads = 0
default razz = 0
default nick = 0



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

    '''
    Los Angeles, 1996. 
    
    You have been hired to assist the ATLAS superhero team in their investigation into a recent murder case, but you only have one week to solve it. 
    
    While you need to solve the crime, it's also a great time to get to know the ATLAS team. 
    
    Who knows? Maybe as you spend time with them throughout the week, you may even fall in love...

    To introduce you to the team, here's Freddy!
    '''

    f '''
    Hey there! I'm Freddy, one of the members of ATLAS! 
    
    I wanted to help you meet the team and get an idea of them before you have to get right into the thick of it. 
    
    Each member of the team has their own personality and cool power! 
    
    For example, as you may be able to tell, I have super hearing, but I can also release sonic screams. 
    
    Here, let's meet the others.
    '''

    # Ulysses
    f '''
    Ulysses Umbral, Co-leader of the team. 

    He's a bit of a stern face guy who comes off a bit serious (and maybe a hardass), but he just wants what's best for the team. 
    
    His power is he can see the future, but he isn't able to tell others, otherwise he may die. 
    
    The good news though is that he's still a great guide for the team, and is our team's strategist!
    '''

    # Razzle Dazzle
    f "Razzle Dazzle. She's one of the original members of the team, and is a bright spirit for ATLAS. While she may not be the smartest, she brings a lot of energy and fun to the team! As you can likely tell, her power is flame cloaking and flame projectiles."

    # Madeline
    f "Madeline Taylors. Another one of the great minds on the team. She's a bit quiet and rude at first, but the moment you get her talking you'll see how... uh... passionate she can be about what she thinks. Her power is superintelligence, which she uses to help her create powerful suits of armor that can do all kinds of things!"

    # Winston
    f "Winston Navarro. The other Co-leader of ATLAS. He's an idiot. Most of the time he's slacking off or ordering pizza for the team, but he's smarter than he lets on. His power is power negation, meaning he can cancel your power out and turn a fight into a straight up brawl!"

    # Dhampir
    f "Dhampir, longtime hero, but only a recent addition to the team. Dhampir has had... questionable methods to his heroism but he truly does mean well.  He's a super chill laid back dude, but when on the job, he as an 100 percent mortality rate. His power is complicated, but the general lowdown is he messes with ghosts and souls. He can turn into a ghost but also can trap people's souls into trinkets he keeps as a necklace. He's... not loved by law enforcement, so he's really only protected by the ATLAS team covering him. "

    # Nicky
    f "Nicky Nelson. Techinally not a member of the team, but we treat her like one reagardless. She's pretty serious about her job, but otherwise super fun to be around, normally like to kick back and watch a show and drink a beer when off the clock. Nicky is an LAPD officer who we team up with in regards to criminals and making sure that our hero agency does things by the book (Looking at you Dhampir...). Her power is that she has many of the psycial powers of an ant, meaning she's super strong and very in tune to phermones in environment! She's a great detective and helps the team out a lot. "


    # Ica
    f "Ica, world's biggest bum. I can't really remember the last time Ica has done pretty much anything for the team, but she's here! She like to have fun and spends most time here playing games. Her power is gravity maniuplation, either increasing or decreasing depending on the situation."

    # End intros and start moving scenes
    f "Well that's the team! Hopefully you can spend some quality time with them as you sort this whole mess out. I'll see you at work tomorrow newbie! I'm with you the entire time, so you may see pop up whenever something important needs to be said!"

    # Day 1, starting the meeting before splitting
    "Day One: 6 days left until a culprit is decided on."

    "As you walk your way to work, you wonder how everyone will be in person beyond Freddy's introduction. After all, they all seem pretty cool. And maybe a little cute..."

    "No! You need to focus, there's a murder to solve here. But maybe as long as you solve this, you can time for both... right?"

    "You enter into the building and quickly sit in the briefing room. You seem to be the first one there, but shortly after you sit, you see Ulysses walk into the room"

    u "Hello there. You must be the new hire. I know we've exhanged formalities over the phone a few times, but it's nice to put a face to the voice and name. I'm Ulysses, and I speak for the whole team when I say I'm happy to have you on the team."

    u "While we wait for the others, I'll go ahead and give you a rundown of where we've gotten so far. As of now, we have it down to nine possible suspects that could have killed Enrico Edge, but due to the speed this case has gone, we only have the week to gather any more evidence we can before having to make a call. That's why we called you in, with your reasoning skills, I'm confident we can find the killer. We'll distribute evidence roles to each person once they all get here, but you'll be an overseer like me. That means you can choose who to work with each day in order to gather evidence. After a day's worth of work, you'll report back to me and we'll review everything. That all make sense?"

    menu:
        "That all make sense?"
        "Yes sir.":
            $ uly += 1
            "Perfect!"
            pass
        "Uhhh repeat all that again for me please":
            $ uly -= 1
            u "Sure... I was saying that you'll be helping with the investigation and work with a different person each day. You can work with the same as well if you want."
            u "You read the briefing right? You should already know this all..."
            pass
        "Yeah yeah, I know how to do my job, don't worry about it man":
            $ uly -= 1
            "Try to take this seriously please. A man died. And for the record, just because you've done well before doesn't mean I'm trusting that you can do your job."
            pass
    u "Now then, let's wait for the others."
    "30 minutes later..."
    u "..."
    # Frustated uly
    u "..."
    # Angry Uly
    u "Where is everyone??? They should have been here by now!"

    m "Aaaaaaand time. I was testing how long it would take you to get upset."

    u "You're kidding."

    m "No? Why would I be? It's fascinating to see how someone who can see the future's temper is."

    "Madeline turns to you"

    m "Oh, you must be the newbie. "


    # This ends the game.
    return
