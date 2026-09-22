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
default spendWin = False
default spendIca = False
default spendDham = False
default spendNick = False
default spendMads = False
default spendRazz = False
default dayWin = 1
default dayIca = 1
default dayDham = 1
default dayNick = 1
default dayMads = 1
default dayRazz = 1
default dayUly = 1


init python:
    # A reusable function to calculate perfect alignment for any number of characters
    def multi_pos(num, total=8):
        if total <= 1:
            return 0.5
        # Evenly spaces characters across the screen width
        return float(num) / float(total - 1)

# The transform that applies the calculated alignment
transform slot(num, total=8):
    xalign multi_pos(num, total)
    yalign 1.0  # Kept at the bottom of the screen
    yoffset -120
    zoom 0.34


# Bright/Normal look
transform bright:
    matrixcolor IdentityMatrix()
    linear 0.2 matrixcolor IdentityMatrix()

# Darkened look (30% brightness)
transform dim:
    matrixcolor IdentityMatrix()
    linear 0.2 matrixcolor TintMatrix("#4d4d4d")



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
    scene bg sky
    # show ulysses at slot(0, total=7)
    show razzle at slot(1, total=7), dim
    show madeline at slot(2, total=7), dim
    # show winston at slot(3, total=7)
    # show dhampir at slot(4, total=7)
    show nicky at slot(5, total=7), dim
    show ica at slot(6, total=7), dim
    # Ulysses
    f '''
    Ulysses Umbral, Co-leader of the team. 

    He's a bit of a stern face guy who comes off a bit serious (and maybe a hardass), but he just wants what's best for the team. 
    
    His power is he can see the future, but he isn't able to tell others, otherwise he may die. 
    
    The good news though is that he's still a great guide for the team, and is our team's strategist!
    '''

    # Razzle Dazzle
    show razzle at slot(1, total=7), bright zorder 10
    f "Razzle Dazzle. She's one of the original members of the team, and is a bright spirit for ATLAS. While she may not be the smartest, she brings a lot of energy and fun to the team! As you can likely tell, her power is flame cloaking and flame projectiles."
    show razzle at slot(1, total=7), dim zorder 0

    # Madeline
    show madeline at slot(2, total=7), bright zorder 10
    f "Madeline Taylors. Another one of the great minds on the team. She's a bit quiet and rude at first, but the moment you get her talking you'll see how... uh... passionate she can be about what she thinks. Her power is superintelligence, which she uses to help her create powerful suits of armor that can do all kinds of things!"
    show madeline at slot(2, total=7), dim zorder 0

    # Winston
    f "Winston Navarro. The other Co-leader of ATLAS. He's an idiot. Most of the time he's slacking off or ordering pizza for the team, but he's smarter than he lets on. His power is power negation, meaning he can cancel your power out and turn a fight into a straight up brawl!"

    # Dhampir
    f "Dhampir, longtime hero, but only a recent addition to the team. Dhampir has had... questionable methods to his heroism but he truly does mean well.  He's a super chill laid back dude, but when on the job, he has an 100 percent mortality rate. His power is complicated, but the general lowdown is he messes with ghosts and souls. He can turn into a ghost but also can trap people's souls into trinkets he keeps as a necklace. He's... not loved by law enforcement, so he's really only protected by the ATLAS team covering him. "

    # Nicky
    show nicky at slot(5, total=7), bright zorder 10
    f "Nicky Nelson. Techinally not a member of the team, but we treat her like one reagardless. She's pretty serious about her job, but otherwise super fun to be around, normally like to kick back and watch a show and drink a beer when off the clock. Nicky is an LAPD officer who we team up with in regards to criminals and making sure that our hero agency does things by the book (Looking at you Dhampir...). Her power is that she has many of the psycial powers of an ant, meaning she's super strong and very in tune to phermones in environment! She's a great detective and helps the team out a lot. "
    show nicky at slot(5, total=7), dim zorder 0


    # Ica
    show ica at slot(6, total=7), bright zorder 10
    f "Ica, world's biggest bum. I can't really remember the last time Ica has done pretty much anything for the team, but she's here! She likes to have fun and spends most time here playing games. Her power is gravity maniuplation, either increasing or decreasing depending on the situation."
    show ica at slot(6, total=7), dim zorder 0

    # End intros and start moving scenes
    f "Well that's the team! Hopefully you can spend some quality time with them as you sort this whole mess out. I'll see you at work tomorrow newbie! I'm with you the entire time, so you may see pop up whenever something important needs to be said!"

    jump dayOneBrief
    jump dayLoop
    jump dayLoop
    jump dayLoop
    jump dayLoop
    jump dayLoop
    jump dayLoop
    jump dayLoop


    # This ends the game.
    return


label dayOneBrief:
    # Day 1, starting the meeting before splitting
    scene black
    "Day One: 6 days left until a culprit is decided on."

    "As you walk your way to work, you wonder how everyone will be in person beyond Freddy's introduction. After all, they all seem pretty cool. And maybe a little cute..."

    "No! You need to focus, there's a murder to solve here. But maybe as long as you solve this, you can time for both... right?"

    scene debriefRoomOutlineInverted

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

    show madeline at slot(1, total=2), bright zorder 10
    m "Aaaaaaand time. I was testing how long it would take you to get upset."

    u "You're kidding."

    m "No? Why would I be? It's fascinating to see how someone who can see the future's temper is."

    "Madeline turns to you"

    m "Oh, you must be the newbie. I'm Madeline, nice to meetcha"

    "Madeline then stares at you for an uncomfortable amount of time without saying a word."

    u "So, Madeline, wi;l you ask the others to show up now?"

    m "Huh? I don't know where they are, I just figured they would be late which is why I did the test."

    "As she says this, you see Nicky rush in with a folder, sweat beading on her forehead"
    show nicky at slot(0, total=2), bright zorder 10

    n "Oh my god guys I'm SO sorry! The station is absolutely wild today. We eneded up bringing in a guy who's power is to make everyoen in a 30ft radius throw up, so you can imagine the mess we had to deal with."

    n "Oh! Are we the only ones here so far?"

    u "It would appear so. Nicky, this is the new recruit."

    n "Hey there! Glad to see you in person! I've read your file when Ulysses sent it over, but it's much better to actually meet people instead of just read their life story on paper."

    "Nicky sticks a hand out for you to shake"

    menu:
        "Shake firmly":
            $ nick+=1
            hide nicky
            show nicky content happy at slot(0, total=2), bright zorder 10
            n "Nice handshake! Very profesh."
        "Stare at her hand":
            $ nick -= 1
            n "Okayyyyy, well anyways good to see ya!"
        " Give a super flimsy handshake":
            $ nick += 2
            hide nicky
            show nicky content happy at slot(0, total=2), bright zorder 10
            n "Good handshake! We gotta work on your grip a bit more though"
    
    "As you talk with Nicky, you see two more members walk into the room"

    d "Sup."

    w "We on time for the meeting?"

    u "Not at all. Where were you two??"

    d "Ulysses relaaaaax man. We were just playing some darts in Winston's office. Besides, seems like we're still missing some people anyway"

    w "Yeah Ulysses! We're not the last people here so TECHNICALLY we're not even late at all! And it was a tough game of darts! Still annoyed about those triple 20s you were throwing though Dhampir"

    d "Look man, practice makes perfect. You just gotta keep throwing darts and maybe one day you'll be on my level"

    "Dhampir turns to you"

    d "Sup, I'm Dhampir, but you can also call me by my legal name, Dhampir. You must be that new person Ulysses has been in such a tizzy about. If you're anything like Ulysses, this may be a rough job, but if you're like me and Winnie, you'll love it here"

    u "For the love of god PLEASE don't be like them"

    w "What's wrong with us?? We just know how to have fun, unlike you Mr. Wet Blanket."

    u "Oh I'll show you wet blanket-"

    w "ULY WAIT-"

    scene black with fade
    "A scene out of a cartoon happens right in front of you as Ulysees begins to chase Winston around the room, with the two of them constantly circling the table before Winston eventually starts breathing heavy."

    "A sign of weakness. Ulysses springs over the table and begins to throttle Winston"

    scene debriefRoomOutlineInverted
    u "WHO'S THE WET BLANKET NOW WINSTON?? WE'RE HAVING FUN, RIGHT WINSTON??"

    d "Whoaaaaa man. You seem a bit angry right now, we should all chill out"

    show madeline madScienist at slot(0, total=1), bright zorder 10
    m "Interesting... Winston seems to whittle down his temper exponentially"
    hide madeline

    show razzle hoorah at slot(0, total=1), bright zorder 10
    r "OMG ARE WE WRESTLING? COUNT ME IN"

    "Razzle Dazzle runs into the room and jumps into the fray right as Ulysses and Winston quickly seperate as to not be burned"
    show razzle at slot(0, total=1), bright zorder 10
    u "No Razzle, sorry. Me and Winston just had a disagreement"

    n "Winston called him a wet blanket"

    show razzle sad at slot(0, total=1), bright zorder 10
    r "Awwwww man! I was really looking forward to it! That's fine I guess, there's always time later, right newbie?"
    show razzle at slot(0, total=1), bright zorder 10

    menu:
        "Uhhh I don't think I should speak on this":
            $ razz -= 1
            show razzle sad at slot(0, total=1), bright zorder 10
            r "Oh man is it another serious one? That's a shame"
        "FUCK YEAH I LOVE WRESTLING":
            $ razz += 1
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "YES NEWBIE THAT'S WHAT I'M TALKING ABUT LET'S THROW DOWN"
        "I'd love to wrestle with you later, I'm a fan of 1v1 matches though":
            $ razz += 2
            show razzle flirty at slot(0, total=1), bright zorder 10
            r "Oh? I hope you can handle some heat then..."
    u "Alright you two, that's enough of that. Looks like we're only missing one more now. Where is she?"

    "As if on cue, the final member of your team strolls through the door, carrying a weight of carelessness about her"

    i "Oh, hey guys. We doing something in here?"

    u "Yes, we are. We're having a meeting that you're LATE to by over thirty minutes!"

    "Ica shrugs"

    i "Whoopsie daisy! I was playing blackjack against my self, pretty fun if you know what you're doing."

    i "Hey, newbie. You like playing games?"

    menu:
        "Of course I do! Games are the best part of the day!":
            $ ica -= 1
            i "Pff what a suckup. You don't gotta impress me man"
        "Games are cool I guess.":
            $ ica += 1
            i "Hell yeah"
        "Can we talk about this later? I want to get the meeting started.":
            $ ica -= 2
            i "Oh fun, another one of these nerds. Nevermind then."
    
    u "Okay great now that everyone's here can we please begin?"

    "The team nods their heads and begins to take seats around the table while Ulysses sets up a projection"

    u "To begin, how many of you read the briefing I made?"

    "Nicky and Dhampir's hands go up, while everyone else's hands stay right where they are"

    u "Damnit. Okay, fine. To catch the rest of you up to speed, a man named Enrico Edge was recently murdered in cold blood. We have been charged with doing what we can to investigate the case and find the culprit. We have narrowed it down to nine suspects, but we only have a week to gather evidence before we have to make a decision on who the culprit is. As such, we'll be splitting up to cover more evidence types. The assignments are as follows."

    u "Razzle Dazzle, you're going to be interviewing any eye witnesses so we can learn more about the suspects and their appearance."

    u "Dhampir, you're going to be analyzing the crime scene and any physical evidence we can find there."

    u "Madeline, you're going to be in the lab analying any evidence we can find and running tests on it."

    u "Nicky, we're going to count on the work you've done thus far and go back over it, make sure we haven't missed anything."

    u "Winston, you're going to interrogate the suspects and see if we can get any more information out of them."

    i "What do I have to do?"

    u "Well, Ica, I'm glad you asked. You're going to be-"

    i "Nah, I'm good. I'll just watch the others do their thing."

    u "... Whatever."

    u "And as for our new recruit, they'll be checking in with each of you as they see fit, and report back to me at the end of the day. That all make sense?"

    "Everyone" "Yes sir!"

    u "Great! Now then, let's get to work"

    "Everyone leave the room and begins to head to their respective task. As this happens, you see Ulysses turn to you"

    u "Alright. So, for day one, who are you wanting to go work with?"

    menu:
        "Razzle Dazzle":
            $ spendRazz = True
            u "Alright, Razzle Dazzle it is. I'll see you at the end of the day to review your findings."
        "Dhampir":
            $ spendDham = True
            u "Alright, Dhampir it is. I'll see you at the end of the day to review your findings."
        "Madeline":
            $ spendMads = True
            u "Alright, Madeline it is. I'll see you at the end of the day to review your findings."
        "Nicky":
            $ spendNick = True
            u "Alright, Nicky it is. I'll see you at the end of the day to review your findings."
        "Winston":
            $ spendWinn = True
            u "Alright, Winston it is. I'll see you at the end of the day to review your findings."
        "Ica":
            $ spendIca = True
            u "Alright, Ica it is. I'll see you at the end of the day to review your findings."

    return

label dayLoop:
    "Day {dayWin}: {7 - dayWin} days left until a culprit is decided on. who do you want to spend the day with?"
    menu:
        "Razzle Dazzle":
            $ spendRazz = True
        "Dhampir":
            $ spendDham = True
        "Madeline":
            $ spendMads = True
        "Nicky":
            $ spendNick = True
        "Winston":
            $ spendWinn = True
        "Ica":
            $ spendIca = True

    if spendRazz:
        jump Razzle
    if spendDham:
        jump Dhampir
    if spendMads:
        jump Madeline
    if spendNick:
        jump Nicky
    if spendWinn:
        jump Winston
    if spendIca:
        jump Ica
    jump Ulysses
    $ spendRazz = False
    $ spendDham = False
    $ spendMads = False
    $ spendNick = False
    $ spendWinn = False
    $ spendIca = False
    return

label Razzle:
    if dayRazz == 1:
        jump RazzleDayOne
    if dayRazz == 2:
        jump RazzleDayTwo
    if dayRazz == 3:
        jump RazzleDayThree
    if dayRazz == 4:
        jump RazzleDayFour
    if dayRazz == 5:
        jump RazzleDayFive
    if dayRazz == 6:
        jump RazzleDaySix

label Dhampir:
    if dayDham == 1:
        jump DhampirDayOne
    if dayDham == 2:
        jump DhampirDayTwo
    if dayDham == 3:
        jump DhampirDayThree
    if dayDham == 4:
        jump DhampirDayFour
    if dayDham == 5:
        jump DhampirDayFive
    if dayDham == 6:
        jump DhampirDaySix

label Madeline:
    if dayMads == 1:
        jump MadelineDayOne
    if dayMads == 2:
        jump MadelineDayTwo
    if dayMads == 3:
        jump MadelineDayThree
    if dayMads == 4:
        jump MadelineDayFour
    if dayMads == 5:
        jump MadelineDayFive
    if dayMads == 6:
        jump MadelineDaySix

label Nicky:
    if dayNick == 1:
        jump NickyDayOne
    if dayNick == 2:
        jump NickyDayTwo
    if dayNick == 3:
        jump NickyDayThree
    if dayNick == 4:
        jump NickyDayFour
    if dayNick == 5:
        jump NickyDayFive
    if dayNick == 6:
        jump NickyDaySix

label Winston:
    if dayWin == 1:
        jump WinstonDayOne
    if dayWin == 2:
        jump WinstonDayTwo
    if dayWin == 3:
        jump WinstonDayThree
    if dayWin == 4:
        jump WinstonDayFour
    if dayWin == 5:
        jump WinstonDayFive
    if dayWin == 6:
        jump WinstonDaySix

label Ica:
    if dayIca == 1:
        jump IcaDayOne
    if dayIca == 2:
        jump IcaDayTwo
    if dayIca == 3:
        jump IcaDayThree
    if dayIca == 4:
        jump IcaDayFour
    if dayIca == 5:
        jump IcaDayFive
    if dayIca == 6:
        jump IcaDaySix

label Ulysses:
    if dayUly == 1:
        jump UlyssesDayOne
    if dayUly == 2:
        jump UlyssesDayTwo
    if dayUly == 3:
        jump UlyssesDayThree
    if dayUly == 4:
        jump UlyssesDayFour
    if dayUly == 5:
        jump UlyssesDayFive
    if dayUly == 6:
        jump UlyssesDaySix

label RazzleDayOne:

label RazzleDayTwo:

label RazzleDayThree:

label RazzleDayFour:

label RazzleDayFive:

label RazzleDaySix:

label DhampirDayOne:

label DhampirDayTwo:

label DhampirDayThree:

label DhampirDayFour:

label DhampirDayFive:

label DhampirDaySix:

label MadelineDayOne:

label MadelineDayTwo:

label MadelineDayThree:

label MadelineDayFour:

label MadelineDayFive:

label MadelineDaySix:

label NickyDayOne:

label NickyDayTwo:

label NickyDayThree:

label NickyDayFour:

label NickyDayFive:

label NickyDaySix:

label WinstonDayOne:

label WinstonDayTwo:

label WinstonDayThree:

label WinstonDayFour:

label WinstonDayFive:

label WinstonDaySix:

label IcaDayOne:

label IcaDayTwo:

label IcaDayThree:

label IcaDayFour:

label IcaDayFive:

label IcaDaySix:

label UlyssesDayOne:

label UlyssesDayTwo:

label UlyssesDayThree:

label UlyssesDayFour:

label UlyssesDayFive:

label UlyssesDaySix: