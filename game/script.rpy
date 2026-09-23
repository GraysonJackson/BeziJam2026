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
default dayWinn = 1
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

    $ initialize_investigation()

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
            $ spendWin = True
            u "Alright, Winston it is. I'll see you at the end of the day to review your findings."
        "Ica":
            $ spendIca = True
            u "Alright, Ica it is. I'll see you at the end of the day to review your findings."

    jump routeDispatch

label dayLoop:
    if dayWin >= 7:
        jump day7

    $ spendRazz = False
    $ spendDham = False
    $ spendMads = False
    $ spendNick = False
    $ spendWin = False
    $ spendIca = False

    $ daysLeft = 7 - dayWin
    "Day [dayWin]: [daysLeft] days left until a culprit is decided on. Who do you want to spend the day with?"
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
            $ spendWin = True
        "Ica":
            $ spendIca = True

    jump routeDispatch

label endOfDay:
    scene black with fade
    $ dayWin += 1
    if dayWin >= 7:
        jump day7
    jump dayLoop

label routeDispatch:
    if spendRazz:
        jump Razzle
    if spendDham:
        jump Dhampir
    if spendMads:
        jump Madeline
    if spendNick:
        jump Nicky
    if spendWin:
        jump Winston
    if spendIca:
        jump Ica
    jump Ulysses

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
    jump endOfDay

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
    jump endOfDay

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
    jump endOfDay

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
    jump endOfDay

label Winston:
    if dayWinn == 1:
        jump WinstonDayOne
    if dayWinn == 2:
        jump WinstonDayTwo
    if dayWinn == 3:
        jump WinstonDayThree
    if dayWinn == 4:
        jump WinstonDayFour
    if dayWinn == 5:
        jump WinstonDayFive
    if dayWinn == 6:
        jump WinstonDaySix
    jump endOfDay

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
    jump endOfDay

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
    jump endOfDay

label RazzleDayOne:
    scene black
    "You make your way to Razzle Dazzzle's cubicle to find her waiting for you, seemingly ready to get going."

    show razzle at slot(0, total=1), bright zorder 10

    r "Hey partner! You made the right choice to come by today. You ready to get to work?"

    menu :
        "Hell yeah I am!":
            $ razz += 1
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "Fuck yeah that's what I like to hear!! Let's go interview the hell out of some witnesses and get this case solved!"
        "Yeah, let's get this done. I don't have time to waste":
            $ razz -= 1
            show razzle sad at slot(0, total=1), bright zorder 10
            r "Awwww man, I was hoping for a bit more enthusiasm from you. But I guess we can get this done anyway."
    show razzle at slot(0, total=1), bright zorder 10
    r "Let's get going! We have a bit of a walk to get to the first witness, so we better start walking!"

    menu:
        "Walk? Why not drive?":
            show razzle mouth open at slot(0, total=1), bright zorder 10
            r "Walking is a great way to get exercise though!! And also, it's a little hard for me to be in cars since I'm literally on fire... but yeah exercise stuff!"
        "Let's roll!":
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "Hell yeah! Let's get this done!"
    scene black
    "You and Razzle Dazzle begin to walk through Los Angeles, heading to the house of the first witness. As you walk, you notice Razzle Dazzle making conversation, mainly just talking aloud, but occasionally asking you questions."

    # Witness scene or something

    show razzle at slot(0, total=1), bright zorder 10
    r "-And then I was like, 'You better pack a fire extinguisher next time!' Wait, sorry I was yapping the entire way here. I wanted to also get to know you newbie!"

    show razzle question at slot(0, total=1), bright zorder 10
    r " Like, what do you do for fun? Any special people in life?"

    "Well, there's certainly not anyone in your life, but who knows? Maybe you and Razzle Dazzle might have some chemistry. You decide to answer her question"

    menu:
        "Not much really, I just do work and then get some sleep":
            $ razz -= 1
            show razzle sad at slot(0, total=1), bright zorder 10
            "Oh man, that sounds like an absolute bore! Surely you do something else right?"
            show razzle mouth open at slot(0, total=1), bright zorder 10
            r" If not you need to! Just work and sleep doesn't let you enjoy life at all! "
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r" For example, me and Winston go clubbing like ALL the time and it's awesome! We get to drink a shit load, meet new people, drink a shit load, then spend the next day talking about how much we shouldn't do that again. It's a blast! Maybe next time you should come with us!"
            show razzle at slot(0, total=1), bright zorder 10
        "I ususally am out all day and night doing whatever the night says!":
            $ razz += 1
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r" Hell yeah! That's what I'm talking about, I'm the same way!"
            r "Me and Winston go clubbing like ALL the time and it's awesome! We get to drink a shit load, meet new people, drink a shit load, then spend the next day talking about how much we shouldn't do that again. It's a blast! Maybe next time you should come with us!"
            show razzle at slot(0, total=1), bright zorder 10
        "Are you an option?":
            $ razz += 2
            show razzle flirty at slot(0, total=1), bright zorder 10
            r"Is that so newbie? I admire the courage, but you're gonna need to have some better lines if you want to get me hot and bothered."
            r "For now though, maybe you can go clubbing with me sometime! We can go drink, get shit faced, dance, get more shit faced, then see if you can handle a night out with me before a more 'personal' evening."
            show razzle at slot(0, total=1), bright zorder 10
    r "For now though it looks like we made it here! Better put on my professional face and talk to them about what they saw. Let's go!"
    show razzle at slot(0, total=1), dim zorder 10

    "You and Razzle Dazzle talk to the witness, introducing yourselves and getting some more basic statements out of the way."

    show razzle question at slot(0, total=1), bright zorder 10

    r "So, Landon. Can you tell me more about what you say that night? Were there any aspects about the suspect that you can remember? Anything at all? Like if they had a scar, tattoo, hell were they missing an arm??"

    "Landon" "Well, I don't remember too much about the suspect since it was so late, but I can for sure say one thing..."

    # The selected killer decides which existing witness observation is used.
    if killer == 1:
        $ razzleDayOneClueText = "Well I can say for sure that they didn't have any glasses or anything like that."
        "Landon" "Well I can say for sure that they didn't have any glasses or anything like that."
    elif killer == 2:
        $ razzleDayOneClueText = "Well I can say for sure that they didn't have any birthmarks or anything like that."
        "Landon" "Well I can say for sure that they didn't have any birthmarks or anything like that."
    elif killer == 3:
        $ razzleDayOneClueText = "Well I can say for sure that they didn't have any moles on their face or anything like that."
        "Landon" "Well I can say for sure that they didn't have any moles on their face or anything like that."
    elif killer == 4:
        $ razzleDayOneClueText = "Well I can say for sure that they didn't have any piercings or anything like that."
        "Landon" "Well I can say for sure that they didn't have any piercings or anything like that."
    elif killer == 5:
        $ razzleDayOneClueText = "Well I can say for sure that they didn't have any scars or anything like that."
        "Landon" "Well I can say for sure that they didn't have any scars or anything like that."
    elif killer == 6:
        $ razzleDayOneClueText = "Well I can say for sure that they didn't have anything like Vitiligo or anything like that."
        "Landon" "Well I can say for sure that they didn't have anything like Vitiligo or anything like that."
    elif killer == 7:
        $ razzleDayOneClueText = "Well I can say for sure that they didn't have an eye patch or anything like that."
        "Landon" "Well I can say for sure that they didn't have an eye patch or anything like that."
    elif killer == 8:
        $ razzleDayOneClueText = "Well I can say for sure that they didn't have any missing limbs or anything like that."
        "Landon" "Well I can say for sure that they didn't have any missing limbs or anything like that."
    elif killer == 9:
        $ razzleDayOneClueText = "Well I can say for sure that they didn't have any tattoos or anything like that."
        "Landon" "Well I can say for sure that they didn't have any tattoos or anything like that."

    $ record_planned_route_reveal(
        "razzle", 1, clue_text=razzleDayOneClueText, expected_count=1)

    "Landon" "Is that any help to you guys at all?"

    show razzle at slot(0, total=1), bright zorder 10
    r "Actually, yes it is! Thanks dude! We'll be able to use this information to help narrow down the suspects. If you think of anything else, please let us know!"

    show razzle mouth open at slot(0, total=1), dim zorder 10
    r "You see that newbie?? We actually got something!! Fuck yeah!! Hopefully we can talk to some more peeps tomorrow and learn a bit more about what the killer looks like!"

    r "Well, I know you gotta get back to report to boss man, but I'm probably gonna head home. See you later newbie!"

    if razz > 4:
        show razzle flirty at slot(0, total=1), bright zorder 10
        r "Keep thinking of ways to get me hot and bothered newbie, I think you're close to a good line soon!"
    scene black with fade
    $ dayRazz += 1
    jump endOfDay
        

label RazzleDayTwo:
    "You make your way back to Razzle Dazzle's cubicle and find her sitting in her flame proof chair, looking at cat videeos on her computer"
    show razzle at slot(0, total=1), bright zorder 10
    r "Oh! Hey newbie! Whatcha up to today? Coming back to do some more work?"

    menu:
        "Yeah, let's get started!":
            $ razz += 1
            show razzle mouth open at slot(0, total=1), bright zorder 10
            r "I like the enthusiasm, but I'm taking today to chill for moment. The rest of this week is going to be a lot, so I wanna chill today!"
        "Nah, I just wanted to see you again":
            $ razz += 2
            show razzle flirty at slot(0, total=1), bright zorder 10
            r "Oh? I like the sound of that! I was hoping you would come back to see me again!"
        "I don't have time for this, let's get to work":
            $ razz -=2 
            show razzle enraged at slot(0, total=1), bright zorder 10
            r "Hey man, no need to be a dick. If we're gonna solve the mystery together we need to at least be nice!"

    # Lunch: takes you somewhere nearby, but either gets rejected because she is on fire. She casually heats/cooks something with her hands or gets outside food.
    r "So, how about we go get some food or somthing? After that we can just walk around ane do absolutely nothing!"

    menu:
        "That sounds irresponsible.":
            r "Exactly! You're getting it already."
            r "Let's just have some fun and not worry about work for a bit."
        "Sounds like my kind of day.":
            $ razz += 1
            show razzle mouth open at slot(0, total=1), bright zorder 10
            r "See? I knew there was a reason I liked you."

        "Is setting something on fire part of the plan?":
            r "Okay, first of all, probably."
            show razzle sad at slot(0, total=1), bright zorder 10
            r "Second of all, I only accidentally set things on fire like... thirty percent of the time."
            show razzle at slot(0, total=1), bright zorder 10

    r "Come on already, I'm hungry!"

    scene black with fade

    "A few minutes later, you're walking through the city with Razzle."

    "People occasionally move out of the way when they notice the flames rolling across her shoulders."

    r "Don't mind them. Happens all the time."

    "She says it casually, like she barely even notices anymore."

    show razzle at slot(0, total=1), bright zorder 10

    r "So what sounds good? Burgers? Pizza? Tacos?"

    menu:
        "Pizza sounds good.":
            r "Correct answer, newbie!! One of my favorites! Cmon, let's go get some!"

        "Whatever you want.":
            $ razz += 1
            r "Dangerous thing to tell me. I have terrible financial judgment."

        "Can we even go inside a restaurant with you on fire?":
            r "..."

            show razzle sad at slot(0, total=1), bright zorder 10

            r "Okay, so there is one tiny problem with the plan."
            show razzle at slot(0, total=1), bright zorder 10
            r "We'll figure it out! Let's just go find some pizza!!"

    "The two of you make it to a nearby pizza place before issues begin to arise"

    "Employee" "I'm sorry Ma'am, but you'll set off every fire alarm in our building just by being there."

    menu:
        "What? That's bullshit! Just let her be on fire!":
            $ razz += 1
            show razzle mouth open at slot(0, total=1), bright zorder 10
            r "It's fine newbie, it happens all the time. Look, can we at least get a box to go or something?"
        "Razzle, can you turn off your flames?":
            $ razz -= 1
            show razzle sad at slot(0, total=1), bright zorder 10
            r "I uhh... I can't. I'm pretty much always on fire unless Winston cancels my power out purposely"
            r "Look, can we at least get a box to go or something?"
    "Employee" "Certainly. Here, I'l send an order back if you can wait outside"

    "After placing your order and waiting what felt like forever, the two of you find yourselves sitting outside with a pizza box."

    show razzle at slot(0, total=1), bright zorder 10

    r "See? Worked out perfectly."

    "You and Razzle lift a slice."

    "...it's cold"

    r "Damn..."

    r "Want yours reheated?"

    menu:
        "Sure.":
            $ razz += 1
            "She holds your slice between two fingers for a second."

            r "There, perfectly heated!!"

            "The cheese is bubbling."

            "The crust is smoking."

            r "...Maybe give it a minute."

        "It's fine, I like it cold anyway.":
            r "Suit yourself, but also cold pizza already?? Usually that's a 'raiding the fridge at midnight' thing and less of a 'right outside the shop' thing."

        "Only if you feed it to me too.":
            $ razz += 2
            show razzle flirty at slot(0, total=1), bright zorder 10

            r "Oh, we're getting brave now, huh? Don't wanna burn you though so you're on your own"
    
    scene black
    "You and Razzle finish your food and walk around the city a bit more. Eventually, you return to the ATLAS team building and go to the rooftop to enjoy the scenery"

    scene black
    with dissolve

    "By the time you make it back to ATLAS, the sun is beginning to set."

    "Razzle sits on the edge of the roof, her flames standing out against the darkening sky."

    r "Thanks for hanging out with me today."

    r "I know it probably wasn't exactly what you expected when you signed up to help a superhero team solve a murder."

    menu:
        "I had fun.":
            $ razz += 2
            r "Yeah?"

            show razzle flirty at slot(0, total=1), bright zorder 10

            r "Good. Me too."

        "It was definitely different.":
            $ razz += 1
            r "Different is basically the ATLAS motto."

        "We really didn't accomplish anything.":
            $ razz -= 1
            r "That was literally the point!"

    "For a moment, she's quieter than usual."

    r "People get kinda weird around me sometimes."

    r "Which, y'know, fair. I'm constantly on fire."

    r "But sometimes it feels like that's all they see."

    r "ATLAS is nice because nobody here really cares. I'm not 'the fire girl.' I'm just Razzle."

    "She glances over at you."

    r "Well... usually."

    menu:
        "You're definitely more than your power.":
            $ razz += 2

            show razzle flirty at slot(0, total=1), bright zorder 10

            r "Careful, newbie. Keep saying stuff like that and I might actually start liking you."

        "I dunno. The fire is pretty cool.":
            $ razz += 1

            r "Okay, yeah. It is pretty cool."

        "I mostly see a walking fire hazard.":
            $ razz -= 2

            show razzle annoyed at slot(0, total=1), bright zorder 10

            r "And there goes the moment."

    "A moment of silence passes as you both enjoy the view of the city in each other's company"
    "Eventually, it's time go back to work."
    show razzle at slot(0, total=1), bright zorder 10
    r "Well, guess it's about time to head home. I'll see you around!"

    if razz > 10:
        r "Maybe I'll see you tomorrow too?"
    
    "Razzle leaves, leaving you alone on the rooftop before heading down to report to Ulysses"

    $ dayRazz += 1
    jump endOfDay
    
label RazzleDayThree:
    "You make your way back to Razzle Dazzle's cubicle and see her already standing, getting ready to leave"
    scene cubicleOutline
    show razzle at slot(0, total=1), bright zorder 10
    r "Oh hey newbie! I was actually just about to head out to interview another witness. Wanna come with?"

    menu:
        "Duh, of course I do!":
            $ razz +=1
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "Fuck yeah!! That's what I like to hear! Let's roll!"
        "Yeah. That's why I'm here.":
            $ razz -= 1
            r "Well damn you can at least pretend to want to be here. Fine. Let's go."
    scene black with fade
    "You and Razzle Dazzle make your way to the next witness's home, arriving to question them"

    show razzle at slot  (0, total=1), bright zorder 10
    r "Hi there, Brandon right? Is it okay if we ask you some questions about what you saw?"

    "Brandon" "Hi there. Yes, that's fine, can we just make this quick please? I really don't want to keep thinking about this all."

    r "Perfectly understandable. We just wanted to hear anything at all about what the killer looked like. Is there anything you can remember about them?"

    "Brandon" "I think so, everything is just so fuzzy..."

    "It seems that Brandon is struggling to organize his thoughts, see what you can do to help!"

    # Minigame
    while not height_memory_completion_recorded:
        $ start_height_memory_minigame()
        while height_memory_active:
            $ renpy.pause(0.1, hard=True)

    r "There we go! The important memories are still on the board, and the rest can take a little vacation."
    "Brandon" "Wait... yeah. I remember the silhouette now. The useful part was right there the whole time."

    # The selected killer decides which witness observation Brandon gives.
    if killer == 1 || killer == 4 || killer == 7:
        $ razzleDayThreeClueText = "Yeah, they had a brawny build if I remember correctly."
        "Brandon" "Yeah, they had a brawny build if I remember correctly."
    elif killer == 2 || killer == 5 || killer == 8:
        $ razzleDayThreeClueText = "Yeah, they had a skinny build if I remember correctly."
        "Brandon" "Yeah, they had a skinny build if I remember correctly."
    elif killer == 3 || killer == 6 || killer == 9:
        $ razzleDayThreeClueText = "Yeah, they had an average build if I remember correctly."
        "Brandon" "Yeah, they had an average build if I remember correctly."

    r "That's exactly what we needed. Thanks, Brandon! We'll handle the detective work from here."
    scene black
    "You and Razzle leave Brandon with a much tidier thought board and a useful eyewitness lead."
    "Eventually, the two of you make your way back to the office."
    scene cubical outline
    show razzle at slot  (0, total=1), bright zorder 10
    r "Oh my god that was amazing!! I don't know how you were able to keep him on track so well! Usually my mind is just all over the place!"

    menu:
        "Most people know more than they think, they just need the guide":
            $ razz += 1
            r "Well look at you oh wise one, seems like you have a lot of wisdom to impart!"
        "I'm pretty good at clearing minds, but mine is stuck on you":
            show razzle flirty at slot  (0, total=1), bright zorder 10
            r "Heyy you're getting pretty good at these!"
            r "The more you say these the more I wanna hear more after this is all over..."
        "It was nothing":
            r "Don't be so modest, that was great!"
    r "Anyways, we've made some really great progress! Hopefully we can do some more, but I'm still getting a good feeling about this!"

    r "But for now I know you gotta talk to Uly, so I'll leave you be. Catcha later newbie!!"

    "With that, Razzle takes her leave, leaving you with your report for the day"

    scene black with fade
    $ dayRazz += 1
    jump endOfDay

label RazzleDayFour:
    "You make your way to Razzle Dazzle's cubicle and find her already standing, getting ready to leave"
    scene cubicleOutline
    show razzle at slot(0, total=1), bright zorder 10
    r "Hey hey! About to go check out another witness. You coming with me?"
    menu:
        "Of course!":
            $ razz += 1
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "Fuck yeah!! That's what I like to hear! Let's roll!"
        "Yeah. That's why I'm here.":
            $ razz -= 1
            r "Well damn you can at least pretend to want to be here. Fine. Let's go."
    scene black with fade
    "You and Razzle Dazzle make your way to the next witness's home, arriving to question them"
    scene cubicleOutline
    show razzle question at slot(0, total=1), bright zorder 10
    r "This is the last witness of the crime, so here's hoping we can get enough info out of them that we can use it to narrow down the suspects and find the killer."
    show razzle at slot(0, total=1), bright zorder 10
    "Razzle Dazzle knocks on the door, and you see an elderly woman answer. She looks at you and Razzle Dazzle with a confused expression."
    "Elena" "He-hello? Can I help you?"
    r "Hi there! I'm Razzle Dazzle, and this is my partner. We're investigating a crime that happened recently, and we were hoping to ask you a few questions about what you saw that night."
    "Elena" "Oh, I see. Well, I suppose I can help you out. Please, come in."
    "You step into the house, as you notice how plain it is. The furniture is old and worn, and the walls are bare. It seems like Elena doesn't have much in the way of material possessions."

    "Elena" "Please, have a seat. Can I offer you some tea or coffee?"
    menu:
        "Tea would be great, thank you.":
            r "Tea sounds perfect. Thank you for offering."
        "Coffee would be great, thank you.":
            r "Coffee sounds perfect. Thank you for offering."
        "No thanks, we're fine.":
            r "No thanks, we're fine. We just want to ask you a few questions."
    "Elena" "Of course dears. Please, make yourselves comfortable."
    
    "Razzle sort of shuffles awkwardly, unable to sit down on any of the cloth chais or couches in the room"
    show razzle question at slot(0, total=1), bright zorder 10
    r "So, Elena, can you tell us what you saw that night? Any details you can remember would be very helpful."
    "Elena" "Well, I remember seeing a figure outside Enrico's house through my window. It was so very dark that I couldn't seem much. Maybe they were tall? Short? Big? small? I don't know. I just remember that they were there, and then they were gone."
    r "I see. Did you notice anything about their clothing or any distinguishing features? Even just something like a hair color?"

    "Elena" "Hair color? Oh, goodness... I couldn't say."

    "Elena glances toward the front window, narrowing her eyes as if the figure might still be standing outside."

    "Elena" "For a moment I thought their hair looked very light. Then a car passed, and it looked dark instead. It may have been a hat for all I know."

    show razzle question at slot(0, total=1), bright zorder 10

    r "Okay, so the lighting was weird. That's still something I guess."

    "Elena" "I'm sorry, dear. I know that isn't very helpful."

    menu:
        "What made the person seem tall or short?":
            $ razz += 1

            r "Yeah! Don't worry about guessing how tall they were. What made them look that way?"

            "Elena" "I suppose it was where their head appeared against the window. They seemed terribly tall at first."

        "Do you think the killer was tall?":
            $ razz -= 1

            show razzle question at slot(0, total=1), bright zorder 10

            r "Careful, newbie. We don't wanna put an answer in her head."

            "Elena" "I really couldn't say. Perhaps they were, but perhaps not."

        "Could we recreate what you saw?":
            $ razz += 2

            show razzle hoorah at slot(0, total=1), bright zorder 10

            r "Oh, that's a great idea! We can make our own little murder reenactment!"

            "Elena" "Perhaps without the murder part, dear."

            show razzle at slot(0, total=1), bright zorder 10

            r "Right. Yeah. Probably should've phrased that better."

    r "Would it help if we tried standing where you saw them?"

    "Elena" "It might. I was sitting right here when they passed the window."

    "Razzle looks between Elena's chair and the front window."

    r "Okay! Newbie, you go outside and be our mysterious shadowy criminal."

    menu:
        "Why do I have to be the criminal?":
            r "Because I'm on fire dummy!"

            r "I feel like that would be a pretty memorable detail if the actual killer was doing it."

        "I was born for this role.":
            $ razz += 1

            show razzle hoorah at slot(0, total=1), bright zorder 10

            r "That's the spirit! Try to look suspicious newbie!"

        "Only if you promise to arrest me afterward.":
            $ razz += 2

            show razzle flirty at slot(0, total=1), bright zorder 10

            r "Oh, I can think of a few ways to restrain you."

            "Elena clears her throat."

            show razzle at slot(0, total=1), bright zorder 10

            r "For official investigative purposes, obviously. No other reason..."

    scene black with fade

    "You step outside while Razzle remains with Elena."

    "Following Razzle's instructions through the window, you walk along the path several times—standing straight, hunching over, and pretending to carry something against your chest."

    "On the third pass, Elena suddenly raises her hand."

    "Elena" "Wait! Stop there!"

    scene cubicleOutline
    show razzle question at slot(0, total=1), bright zorder 10

    "You return inside as Elena studies the window."

    "Elena" "That was much closer. The figure wasn't necessarily large. They were holding something bulky and leaning forward."

    r "So that could've made them look shorter and wider than they really were?"

    "Elena" "Yes, I believe so. And the lawn slopes upward near the window. That may be why I first thought they were tall."

    show razzle hoorah at slot(0, total=1), bright zorder 10

    r "Holy shit, newbie! We actually cracked the case! Well not really but you know what I mean!"
    "Elena" "Have I helped identify them?"

    show razzle at slot(0, total=1), bright zorder 10

    r "Not exactly lady. But you helped us figure out which parts of the description we shouldn't trust yet."

    "Elena" "I'm afraid that doesn't sound nearly as impressive."

    show razzle sad at slot(0, total=1), bright zorder 10

    r "Well when you say it like that..."

    show razzle at slot(0, total=1), bright zorder 10

    "Elena looks toward the window once more."

    "Elena" "There was one other thing."

    show razzle question at slot(0, total=1), bright zorder 10

    r "Anything you remember could help."

    "Elena" "When the car passed, the person raised a hand to shield their face. For just a moment, I could see the top of their head."

    r "Their hair?"

    "Elena" "Perhaps. But the light passed too quickly. I don't trust myself to name the color."

    "Elena" "The little grocery across the street had a security camera pointed toward the road, though. If they kept the recording, it may have seen the same car pass."

    show razzle hoorah at slot(0, total=1), bright zorder 10

    r "Now that sounds like a lead!"

    "Elena" "I'm glad I could help, dears."

    r "You helped plenty. Thanks for talking to us, Elena."

    scene black with fade

    "After saying goodbye, you and Razzle begin walking back toward ATLAS."

    show razzle at slot(0, total=1), bright zorder 10

    r "I really wanted her to remember something huge."

    r "Like the killer's exact height, or their face, or maybe a shirt with their name printed across it."

    menu:
        "You handled it well anyway.":
            $ razz += 2

            show razzle flirty at slot(0, total=1), bright zorder 10

            r "Yeah?"

            r "Careful, newbie. Compliment me like that and I'm gonna start making you come to every interview."

        "Stopping a bad clue is still progress.":
            $ razz += 1

            r "Exactly! We didn't get an answer, but at least we won't chase the wrong one."

        "You were asking a lot of leading questions.":
            $ razz -= 1

            show razzle sad at slot(0, total=1), bright zorder 10

            r "Yeah... I got a little excited."

            r "I'll try to slow down next time."

    show razzle question at slot(0, total=1), bright zorder 10

    r "You know, I hate houses like that."

    menu:
        "Because they're boring?":
            r "No! Well, a little."

            r "Mostly because I'm always worried I'll destroy something just by standing too close."

        "Because you couldn't sit down?":
            $ razz += 1

            r "Exactly! Do you know how awkward it is being offered a seat when every chair is flammable?"

        "You seemed uncomfortable in there.":
            $ razz += 2

            show razzle sad at slot(0, total=1), bright zorder 10

            r "Yeah. Places like that make me feel less like a person and more like an accident waiting to happen."

    menu:
        "You were careful. Elena was safe with you.":
            $ razz += 2

            show razzle flirty at slot(0, total=1), bright zorder 10

            r "Thanks, newbie. That actually means a lot."

        "I'd make sure my place had somewhere you could sit.":
            $ razz += 2

            show razzle flirty at slot(0, total=1), bright zorder 10

            r "Oh? Planning on inviting me over already?"

        "Being on fire does make you a pretty serious hazard.":
            $ razz -= 2

            show razzle sad at slot(0, total=1), bright zorder 10

            r "Yeah. Thanks for the reminder."

    show razzle at slot(0, total=1), bright zorder 10

    r "Anyway, I'm gonna call that grocery store and see if they still have the tape."

    r "Maybe Elena couldn't tell us what color she saw, but a camera won't second-guess itself."

    r "Assuming the footage isn't terrible. Which, knowing our luck, it absolutely will be."

    "Razzle grins and gives you a playful shove with her shoulder, stopping just short of letting her flames touch you."

    r "Not a bad day, partner. I'll let you know what I find."

    scene black with fade
     
    $ dayRazz += 1
    jump endOfDay

label RazzleDayFive:
    "You spend the day working with Razzle Dazzle. (Visit 5 content in development)"label RazzleDayFive:
    scene cubicleOutline

    "You make your way to Razzle's cubicle and find her crouched in front of an old television and VCR."

    "Several videotapes are scattered across the floor. One of them has a grocery-store receipt taped to its side."

    show razzle hoorah at slot(0, total=1), bright zorder 10

    r "Newbie! Great news! The grocery store still had the tape!"

    menu:
        "You actually found it?":
            $ razz += 1

            r "Sure did! And it only took three phone calls, two flame proof cab rides, and one extremely suspicious store manager!"

        "Please tell me you didn't threaten anybody.":
            $ razz -= 1

            show razzle question at slot(0, total=1), bright zorder 10

            r "What? No!"

            r "I just stood uncomfortably close to the manager until he remembered where the tapes were. The heat seemed to jog his memory"

        "I knew you could do it.":
            $ razz += 2

            show razzle flirty at slot(0, total=1), bright zorder 10

            r "Oh? Starting the day with compliments?"

            r "Keep that up and we're never gonna get any work done."

    show razzle at slot(0, total=1), bright zorder 10

    r "There's one problem, though."

    "Razzle presses play."

    scene black

    "A grainy black-and-white image appears on the television."

    "The camera is pointed toward the road, but the picture flickers constantly and most of the street is swallowed by darkness."

    r "Behold! Cutting-edge surveillance technology!"

    r "We've got six hours of blurry cars, shopping carts, and one cat that keeps attacking a plastic bag."

    r "Somewhere in there should be the car old lady Elena remembered."

    scene cubicleOutline
    show razzle at slot(0, total=1), bright zorder 10

    menu:
        "Let's watch it frame by frame.":
            $ razz += 1

            r "That's gonna take forever."

            show razzle hoorah at slot(0, total=1), bright zorder 10

            r "But surely it'll work right?? Let's go for it!"

        "Can't we fast-forward to the right time?":
            r "We can try, but the clock on the tape keeps blinking twelve."

            r "Apparently grocery-store security wasn't prepared for us to solve a murder."

        "Maybe hitting the VCR will help.":
            $ razz += 1

            show razzle question at slot(0, total=1), bright zorder 10

            r "hmmm I like it! Tech always works better when you hit it"
            "Razzle punches the VCR"
            "Nothing happens."
            show razzle at slot(0, total=1), bright zorder 10
            r "Well that was a bust. Guess we'll just start watching!"

    scene black

    "You and Razzle begin working through the recording."

    "You handle the remote while she compares the passing cars to Elena's description."

    "After what feels like hours, a pair of headlights sweeps across the road."

    r "Wait!"

    "The tape stops."

    "A faint figure is visible near the edge of the picture."

    scene cubicleOutline
    show razzle hoorah at slot(0, total=1), bright zorder 10

    r "Holy shit, that's them! That's gotta be them!"

    "Razzle reaches over and rewinds the recording, playing the moment again."

    scene black

    "The figure enters at the bottom of the frame."

    "For a moment, they appear almost as tall as the nearby street sign. As they move toward the center of the image, their outline seems to shrink."

    r "Okay. Either the killer changed size halfway across the street, or this camera angle is complete garbage."

    "The figure steps onto the sloped curb and briefly leans against the grocery store's outer wall."

    "One hand touches the bricks. It jerks away almost immediately before disappearing into the figure's coat."

    r "Ow."

    r "Maybe they scraped it? Or maybe this tape just swallowed a few frames."

    "The figure flexes the hand once, but the image skips before you can see anything more."

    "A second later, the headlights pass over them."

    "The figure raises an arm to cover their face."

    r "That's exactly what Elena described!!"

    "Razzle advances the tape one frame at a time."

    "The person's height changes slightly in every frame as they cross the sloping pavement."

    "Whatever they are carrying also blends into their outline, making their body appear wider whenever they turn toward the camera."

    r "No wonder Elena couldn't get a read on them."

    r "The ground, the camera, that thing they're carrying, everything is screwing with the shape!"

    "Razzle watches the footage again."

    "She advances the tape to the moment the figure shields their face."

    r "Hold on..."

    "For three grainy frames, several loose strands are visible around the figure's uncovered head."

    scene cubicleOutline
    show razzle question at slot(0, total=1), bright zorder 10

    r "So Elena really did see their hair. It wasn't a hat."

    r "Too bad the tape's black and white."

    r "We finally get a camera pointed at the killer and the thing can't even tell us what damn color we're looking at."

    menu:
        "The tape still confirmed Elena's memory.":
            $ razz += 1

            r "True. At least we know she wasn't imagining that part."

        "You noticed more than I did.":
            $ razz += 2

            show razzle flirty at slot(0, total=1), bright zorder 10

            r "Yeah?"

            r "Maybe you should keep me around, then."

        "So we watched all of that for nothing?":
            $ razz -= 2

            show razzle sad at slot(0, total=1), bright zorder 10

            r "It wasn't nothing."

            r "We know which parts of Elena's memory matched the recording. That's gotta count for something."

    show razzle question at slot(0, total=1), bright zorder 10

    "Razzle rewinds the footage again, stopping when the headlights first enter the frame."

    r "Wait a second."

    r "The tape shows exactly where the car was when its lights hit the killer."

    r "We know where Elena was sitting too."

    r "What if we recreate the lighting?"

    menu:
        "Using different hair samples?":
            $ razz += 1

            show razzle hoorah at slot(0, total=1), bright zorder 10

            r "Exactly! We put them in the same light and see which colors Elena could've confused."

        "Would Elena agree to another reconstruction?":
            r "I think so. Especially if we bring her something nice for helping."
            show razzle question at slot(0, total=1), bright zorder 10
            r "Should you bring grandmas cookies? Or is that their thing?"

        "That sounds surprisingly scientific.":
            $ razz -= 1

            show razzle question at slot(0, total=1), bright zorder 10

            r "Surprisingly?"

            r "Damn, newbie. I'm smarter than you think!!"

    show razzle at slot(0, total=1), bright zorder 10

    r "We'll need the same angle, the same distance, and something close to those headlights."

    r "Then maybe Elena can finally tell us what she saw!"

    "Razzle ejects the tape and sets it carefully on her desk."

    r "Not bad, right?"

    menu:
        "Not bad at all! You're super smart with this stuff!.":
            $ razz += 2

            show razzle flirty at slot(0, total=1), bright zorder 10

            r "That's actually really sweet."

            r "Don't tell anybody. I've got a reputation for being an idiot to maintain."

        "You kept looking when the tape seemed useless.":
            $ razz += 1
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "Yeah! I guess being stubborn is useful every once in a while!"

        "Madeline probably would've finished faster.":
            $ razz -= 2

            show razzle sad at slot(0, total=1), bright zorder 10

            r "Probably."

            r "But she wasn't the one Elena trusted with her story."

    show razzle at slot(0, total=1), bright zorder 10

    r "Anyway, I'll get everything ready for the reconstruction."

    r "Tomorrow we figure out what Elena saw."

    if razz > 12:
        show razzle flirty at slot(0, total=1), bright zorder 10

        r "And after that, maybe you and I can spend some time investigating something that isn't murder."

        r "Preferably somewhere with drinks."

        r "And fewer cameras."

    else:
        r "You better come with me tomorrow, newbie. I need my favorite suspicious silhouette."

    "Razzle gives you a grin before turning back toward the television."

    "The tape continues playing as you leave, the shadowy figure disappearing once again into the darkness."

    scene black with fade

    $ dayRazz += 1
    jump endOfDay

label RazzleDaySix:
    "You spend the day working with Razzle Dazzle. (Visit 6 content in development)"
    $ dayRazz += 1
    jump endOfDay

label DhampirDayOne:
    "You spend the day working with Dhampir. (Visit 1 content in development)"
    $ dayDham += 1
    jump endOfDay

label DhampirDayTwo:
    "You spend the day working with Dhampir. (Visit 2 content in development)"
    $ dayDham += 1
    jump endOfDay

label DhampirDayThree:
    "You spend the day working with Dhampir. (Visit 3 content in development)"
    $ dayDham += 1
    jump endOfDay

label DhampirDayFour:
    "You spend the day working with Dhampir. (Visit 4 content in development)"
    $ dayDham += 1
    jump endOfDay

label DhampirDayFive:
    "You spend the day working with Dhampir. (Visit 5 content in development)"
    $ dayDham += 1
    jump endOfDay

label DhampirDaySix:
    "You spend the day working with Dhampir. (Visit 6 content in development)"
    $ dayDham += 1
    jump endOfDay

label MadelineDayOne:
    "You spend the day working with Madeline. (Visit 1 content in development)"
    $ dayMads += 1
    jump endOfDay

label MadelineDayTwo:
    "You spend the day working with Madeline. (Visit 2 content in development)"
    $ dayMads += 1
    jump endOfDay

label MadelineDayThree:
    "You spend the day working with Madeline. (Visit 3 content in development)"
    $ dayMads += 1
    jump endOfDay

label MadelineDayFour:
    "You spend the day working with Madeline. (Visit 4 content in development)"
    $ dayMads += 1
    jump endOfDay

label MadelineDayFive:
    "You spend the day working with Madeline. (Visit 5 content in development)"
    $ dayMads += 1
    jump endOfDay

label MadelineDaySix:
    "You spend the day working with Madeline. (Visit 6 content in development)"
    $ dayMads += 1
    jump endOfDay

label NickyDayOne:
    "You spend the day working with Nicky. (Visit 1 content in development)"
    $ dayNick += 1
    jump endOfDay

label NickyDayTwo:
    "You spend the day working with Nicky. (Visit 2 content in development)"
    $ dayNick += 1
    jump endOfDay

label NickyDayThree:
    "You spend the day working with Nicky. (Visit 3 content in development)"
    $ dayNick += 1
    jump endOfDay

label NickyDayFour:
    "You spend the day working with Nicky. (Visit 4 content in development)"
    $ dayNick += 1
    jump endOfDay

label NickyDayFive:
    "You spend the day working with Nicky. (Visit 5 content in development)"
    $ dayNick += 1
    jump endOfDay

label NickyDaySix:
    "You spend the day working with Nicky. (Visit 6 content in development)"
    $ dayNick += 1
    jump endOfDay

label WinstonDayOne:
    "You spend the day working with Winston. (Visit 1 content in development)"
    $ dayWinn += 1
    jump endOfDay

label WinstonDayTwo:
    "You spend the day working with Winston. (Visit 2 content in development)"
    $ dayWinn += 1
    jump endOfDay

label WinstonDayThree:
    "You spend the day working with Winston. (Visit 3 content in development)"
    $ dayWinn += 1
    jump endOfDay

label WinstonDayFour:
    "You spend the day working with Winston. (Visit 4 content in development)"
    $ dayWinn += 1
    jump endOfDay

label WinstonDayFive:
    "You spend the day working with Winston. (Visit 5 content in development)"
    $ dayWinn += 1
    jump endOfDay

label WinstonDaySix:
    "You spend the day working with Winston. (Visit 6 content in development)"
    $ dayWinn += 1
    jump endOfDay

label IcaDayOne:
    "You spend the day hanging out with Ica. (Visit 1 content in development)"
    $ dayIca += 1
    jump endOfDay

label IcaDayTwo:
    "You spend the day hanging out with Ica. (Visit 2 content in development)"
    $ dayIca += 1
    jump endOfDay

label IcaDayThree:
    "You spend the day hanging out with Ica. (Visit 3 content in development)"
    $ dayIca += 1
    jump endOfDay

label IcaDayFour:
    "You spend the day hanging out with Ica. (Visit 4 content in development)"
    $ dayIca += 1
    jump endOfDay

label IcaDayFive:
    "You spend the day hanging out with Ica. (Visit 5 content in development)"
    $ dayIca += 1
    jump endOfDay

label IcaDaySix:
    "You spend the day hanging out with Ica. (Visit 6 content in development)"
    $ dayIca += 1
    jump endOfDay

label UlyssesDayOne:
    "You spend the day consulting with Ulysses. (Visit 1 content in development)"
    $ dayUly += 1
    jump endOfDay

label UlyssesDayTwo:
    "You spend the day consulting with Ulysses. (Visit 2 content in development)"
    $ dayUly += 1
    jump endOfDay

label UlyssesDayThree:
    "You spend the day consulting with Ulysses. (Visit 3 content in development)"
    $ dayUly += 1
    jump endOfDay

label UlyssesDayFour:
    "You spend the day consulting with Ulysses. (Visit 4 content in development)"
    $ dayUly += 1
    jump endOfDay

label UlyssesDayFive:
    "You spend the day consulting with Ulysses. (Visit 5 content in development)"
    $ dayUly += 1
    jump endOfDay

label UlyssesDaySix:
    "You spend the day consulting with Ulysses. (Visit 6 content in development)"
    $ dayUly += 1
    jump endOfDay

label day7:
    scene black with fade
    "Day Seven: The deadline has arrived."
    "The week of investigation is over. It is time to decide on the culprit."
    jump endingRouter

label endingRouter:
    "Investigation phase complete! Thank you for playing."
    return
