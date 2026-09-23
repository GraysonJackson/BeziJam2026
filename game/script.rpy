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
define j = Character("Jermiah")
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

    "Los Angeles, 1996."

    "You have been hired to assist the ATLAS superhero team in their investigation into a recent murder case, but you only have one week to solve it."

    "While you need to solve the crime, it's also a great time to get to know the ATLAS team."

    "Who knows? Maybe as you spend time with them throughout the week, you may even fall in love..."

    "To introduce you to the team, here's Freddy!"

    f "Hey there! I'm Freddy, one of the members of ATLAS!"

    f "I wanted to help you meet the team and get an idea of them before you have to get right into the thick of it."

    f "Each member of the team has their own personality and cool power!"

    f "For example, as you may be able to tell, I have super hearing, but I can also release sonic screams."

    f "Here, let's meet the others."

    scene bg sky
    # show ulysses at slot(0, total=7)
    show razzle at slot(1, total=7), dim
    show madeline at slot(2, total=7), dim
    # show winston at slot(3, total=7)
    # show dhampir at slot(4, total=7)
    show nicky at slot(5, total=7), dim
    show ica at slot(6, total=7), dim

    # Ulysses
    f "Ulysses Umbral, Co-leader of the team."

    f "He's a bit of a stern-faced guy who comes off a bit serious (and maybe a hardass), but he just wants what's best for the team."

    f "His power is that he can see the future, but he isn't able to tell others, otherwise he may die."

    f "The good news though is that he's still a great guide for the team, and is our team's strategist!"

    # Razzle Dazzle
    show razzle at slot(1, total=7), bright zorder 10
    f "Razzle Dazzle. She's one of the original members of the team, and is a bright spirit for ATLAS."
    f "While she may not be the smartest, she brings a lot of energy and fun to the team!"
    f "As you can likely tell, her power is flame cloaking and flame projectiles."
    show razzle at slot(1, total=7), dim zorder 0

    # Madeline
    show madeline at slot(2, total=7), bright zorder 10
    f "Madeline Taylors. Another one of the great minds on the team."
    f "She's a bit quiet and rude at first, but the moment you get her talking you'll see how... uh... passionate she can be about what she thinks."
    f "Her power is superintelligence, which she uses to help her create powerful suits of armor that can do all kinds of things!"
    show madeline at slot(2, total=7), dim zorder 0

    # Winston
    f "Winston Navarro. The other Co-leader of ATLAS. He's an idiot."
    f "Most of the time he's slacking off or ordering pizza for the team, but he's smarter than he lets on."
    f "His power is power negation, meaning he can cancel your power out and turn a fight into a straight up brawl!"

    # Dhampir
    f "Dhampir, longtime hero, but only a recent addition to the team."
    f "Dhampir has had... questionable methods to his heroism, but he truly does mean well."
    f "He's a super chill, laid-back dude, but when on the job, he has a 100 percent mortality rate."
    f "His power is complicated, but the general lowdown is he messes with ghosts and souls."
    f "He can turn into a ghost, but also can trap people's souls into trinkets he keeps as a necklace."
    f "He's... not loved by law enforcement, so he's really only protected by the ATLAS team covering him."

    # Nicky
    show nicky at slot(5, total=7), bright zorder 10
    f "Nicky Nelson. Technically not a member of the team, but we treat her like one regardless."
    f "She's pretty serious about her job, but otherwise super fun to be around."
    f "She normally likes to kick back, watch a show, and drink a beer when off the clock."
    f "Nicky is an LAPD officer who we team up with in regards to criminals."
    f "She makes sure our hero agency does things by the book. (Looking at you, Dhampir...)"
    f "Her power gives her the physical abilities of an ant—super strength, and acute sensitivity to pheromones!"
    f "She's a great detective and helps the team out a lot."
    show nicky at slot(5, total=7), dim zorder 0

    # Ica
    show ica at slot(6, total=7), bright zorder 10
    f "Ica, world's biggest bum."
    f "I can't really remember the last time Ica has done pretty much anything for the team, but she's here!"
    f "She likes to have fun and spends most of her time here playing games."
    f "Her power is gravity manipulation, either increasing or decreasing depending on the situation."
    show ica at slot(6, total=7), dim zorder 0

    # End intros and start moving scenes
    f "Well that's the team! Hopefully you can spend some quality time with them as you sort this whole mess out."
    f "I'll see you at work tomorrow newbie! I'm with you the entire time, so you may see me pop up whenever something important needs to be said!"

    jump dayOneBrief

label dayOneBrief:
    # Day 1, starting the meeting before splitting
    scene black
    "Day One: 6 days left until a culprit is decided on."

    "As you walk your way to work, you wonder what everyone will be like in person beyond Freddy's introduction."
    "After all, they all seem pretty cool. And maybe a little cute..."

    "No! You need to focus, there's a murder to solve here. But maybe as long as you solve this, you can make time for both... right?"

    scene debriefRoomOutlineInverted

    "You enter into the building and quickly take a seat in the briefing room."
    "You seem to be the first one there, but shortly after you sit, Ulysses walks into the room."

    u "Hello there. You must be the new hire."
    u "I know we've exchanged formalities over the phone a few times, but it's nice to put a face to the voice and name."
    u "I'm Ulysses, and I speak for the whole team when I say I'm happy to have you on the team."

    u "While we wait for the others, I'll go ahead and give you a rundown of where we've gotten so far."
    u "As of now, we have it down to nine possible suspects that could have killed Enrico Edge."
    u "Due to how fast this case has moved, we only have a single week to gather any more evidence we can before making our call."
    u "That's why we called you in. With your reasoning skills, I'm confident we can find the killer."
    u "We'll distribute evidence roles to each person once they all get here, but you'll be an overseer like me."
    u "That means you can choose who to work with each day in order to gather evidence."
    u "After a day's worth of work, you'll report back to me and we'll review everything. That all make sense?"

    menu:
        "That all make sense?"
        "Yes sir.":
            $ uly += 1
            u "Perfect!"
            pass
        "Uhhh repeat all that again for me please":
            $ uly -= 1
            u "Sure... I was saying that you'll be helping with the investigation and work with a different person each day."
            u "You can work with the same person as well if you want."
            u "You read the briefing, right? You should already know this all..."
            pass
        "Yeah yeah, I know how to do my job, don't worry about it man":
            $ uly -= 1
            u "Try to take this seriously, please. A man died."
            u "And for the record, just because you've done well before doesn't mean I'm trusting that you can do your job."
            pass
    u "Now then, let's wait for the others."
    "30 minutes later..."
    u "..."
    # Frustrated uly
    u "..."
    # Angry Uly
    u "Where is everyone??? They should have been here by now!"

    show madeline at slot(1, total=2), bright zorder 10
    m "Aaaaaaand time. I was testing how long it would take you to get upset."

    u "You're kidding."

    show madeline flirty curious at slot(1, total=2), bright zorder 10
    m "No? Why would I be?"
    m "It's fascinating to see what someone who can see the future's temper is like."

    "Madeline turns to you."

    show madeline at slot(1, total=2), bright zorder 10
    m "Oh, you must be the newbie. I'm Madeline, nice to meetcha."

    "Madeline then stares at you for an uncomfortable amount of time without saying a word."

    u "So, Madeline, will you ask the others to show up now?"

    show madeline flirty curious at slot(1, total=2), bright zorder 10
    m "Huh? I don't know where they are."
    m "I just figured they would be late, which is why I did the test."

    "As she says this, you see Nicky rush in with a folder, sweat beading on her forehead."
    show madeline at slot(1, total=2), dim zorder 0
    show nicky at slot(0, total=2), bright zorder 10

    n "Oh my god guys, I'm SO sorry! The station is absolutely wild today."
    n "We ended up bringing in a guy whose power is to make everyone in a thirty-foot radius throw up..."
    n "...So you can imagine the mess we had to deal with."

    show nicky quesition at slot(0, total=2), bright zorder 10
    n "Oh! Are we the only ones here so far?"

    u "It would appear so. Nicky, this is the new recruit."

    show nicky content happy at slot(0, total=2), bright zorder 10
    n "Hey there! Glad to see you in person!"
    n "I read your file when Ulysses sent it over, but it's much better to actually meet people instead of just reading their life story on paper."

    "Nicky sticks a hand out for you to shake."

    menu:
        "Shake firmly":
            $ nick += 1
            show nicky content happy at slot(0, total=2), bright zorder 10
            n "Nice handshake! Very profesh."
        "Stare at her hand":
            $ nick -= 1
            show nicky quesition at slot(0, total=2), bright zorder 10
            n "Okayyyyy, well anyways good to see ya!"
        "Give a super flimsy handshake":
            $ nick += 2
            show nicky content happy at slot(0, total=2), bright zorder 10
            n "Good handshake! We gotta work on your grip a bit more though."

    show nicky at slot(0, total=2), dim zorder 0
    show madeline at slot(1, total=2), dim zorder 0
    "As you talk with Nicky, you see two more members walk into the room."

    d "Sup."

    w "We on time for the meeting?"

    u "Not at all. Where were you two??"

    d "Ulysses, relaaaaax man. We were just playing some darts in Winston's office."
    d "Besides, seems like we're still missing some people anyway."

    w "Yeah, Ulysses! We're not the last people here, so TECHNICALLY we're not even late at all!"
    w "And it was a tough game of darts! Still annoyed about those triple 20s you were throwing, though, Dhampir!"

    d "Look man, practice makes perfect."
    d "You just gotta keep throwing darts and maybe one day you'll be on my level."

    "Dhampir turns to you."

    d "Sup, I'm Dhampir, but you can also call me by my legal name, Dhampir."
    d "You must be that new person Ulysses has been in such a tizzy about."
    d "If you're anything like Ulysses, this may be a rough job, but if you're like me and Winnie, you'll love it here."

    u "For the love of God, PLEASE don't be like them."

    w "What's wrong with us?? We just know how to have fun, unlike you, Mr. Wet Blanket."

    u "Oh I'll show you wet blanket-"

    w "ULY WAIT-"

    scene black with fade
    "A scene straight out of a cartoon unfolds right in front of you as Ulysses begins chasing Winston around the room."
    "The two of them circle the table again and again until Winston finally starts wheezing for breath."

    "A sign of weakness. Ulysses springs over the table and begins to throttle Winston."

    scene debriefRoomOutlineInverted
    u "WHO'S THE WET BLANKET NOW WINSTON?? WE'RE HAVING FUN, RIGHT WINSTON??"

    d "Whoaaaaa man. You seem a bit angry right now, we should all chill out."

    show madeline madScienist at slot(0, total=1), bright zorder 10
    m "Interesting... Winston seems to whittle down his temper exponentially."
    hide madeline

    show razzle hoorah at slot(0, total=1), bright zorder 10
    r "OMG ARE WE WRESTLING? COUNT ME IN!"

    "Razzle Dazzle runs into the room and jumps into the fray right as Ulysses and Winston quickly separate so as not to be burned."
    show razzle at slot(0, total=1), bright zorder 10
    u "No, Razzle, sorry. Winston and I just had a disagreement."

    show razzle at slot(0, total=1), dim zorder 0
    n "Winston called him a wet blanket."

    show razzle sad at slot(0, total=1), bright zorder 10
    r "Awwwww man! I was really looking forward to it!"
    r "That's fine I guess, there's always time later, right newbie?"

    menu:
        "Uhhh I don't think I should speak on this":
            $ razz -= 1
            show razzle sad at slot(0, total=1), bright zorder 10
            r "Oh man, is it another serious one? That's a shame."
        "FUCK YEAH I LOVE WRESTLING":
            $ razz += 1
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "YES NEWBIE THAT'S WHAT I'M TALKING ABOUT! LET'S THROW DOWN!"
        "I'd love to wrestle with you later, I'm a fan of 1v1 matches though":
            $ razz += 2
            show razzle flirty at slot(0, total=1), bright zorder 10
            r "Oh? I hope you can handle some heat then..."

    show razzle at slot(0, total=1), dim zorder 0
    u "Alright you two, that's enough of that. Looks like we're only missing one more now. Where is she?"
    hide razzle

    "As if on cue, the final member of your team strolls through the door, carrying a weight of carelessness about her."

    show ica at slot(0, total=1), bright zorder 10
    i "Oh, hey guys. We doing something in here?"

    show ica at slot(0, total=1), dim zorder 0
    u "Yes, we are. We're having a meeting that you're LATE to by over thirty minutes!"

    "Ica shrugs."

    show ica happy at slot(0, total=1), bright zorder 10
    i "Whoopsie daisy! I was playing blackjack against myself."
    i "Pretty fun if you know what you're doing."

    show ica at slot(0, total=1), bright zorder 10
    i "Hey, newbie. You like playing games?"

    menu:
        "Of course I do! Games are the best part of the day!":
            $ ica -= 1
            show ica whatTheFuckDidYouJustDoMC at slot(0, total=1), bright zorder 10
            i "Pff, what a suckup. You don't gotta impress me, man."
        "Games are cool I guess.":
            $ ica += 1
            show ica happy at slot(0, total=1), bright zorder 10
            i "Hell yeah."
        "Can we talk about this later? I want to get the meeting started.":
            $ ica -= 2
            show ica sad at slot(0, total=1), bright zorder 10
            i "Oh fun, another one of these nerds. Never mind then."

    hide ica
    u "Okay, great, now that everyone's here can we please begin?"

    "The team nods their heads and begins to take seats around the table while Ulysses sets up a projection."

    u "To begin, how many of you read the briefing I made?"

    "Nicky and Dhampir's hands go up, while everyone else's hands stay right where they are."

    u "Dammit. Okay, fine."
    u "To catch the rest of you up to speed, a man named Enrico Edge was recently murdered in cold blood."
    u "We have been charged with doing what we can to investigate the case and find the culprit."
    u "We have narrowed it down to nine suspects, but we only have a week to gather evidence before we have to make a decision."
    u "As such, we'll be splitting up to cover more evidence types. The assignments are as follows."

    u "Razzle Dazzle, you're going to be interviewing any eyewitnesses so we can learn more about the suspects and their appearance."

    u "Dhampir, you're going to be analyzing the crime scene and any physical evidence we can find there."

    u "Madeline, you're going to be in the lab analyzing any evidence we can find and running tests on it."

    u "Nicky, we're going to count on the work you've done thus far and go back over it, to make sure we haven't missed anything."

    u "Winston, you're going to interrogate the suspects and see if we can get any more information out of them."

    show ica at slot(0, total=1), bright zorder 10
    i "What do I have to do?"

    show ica at slot(0, total=1), dim zorder 0
    u "Well, Ica, I'm glad you asked. You're going to be-"

    show ica happy at slot(0, total=1), bright zorder 10
    i "Nah, I'm good. I'll just watch the others do their thing."
    hide ica

    u "... Whatever."

    u "And as for our new recruit, you'll be checking in with each of you as you see fit, and report back to me at the end of the day."
    u "That all make sense?"

    "Everyone" "Yes sir!"

    u "Great! Now then, let's get to work."

    "Everyone leaves the room and begins to head to their respective tasks. As this happens, you see Ulysses turn to you."

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
    "You make your way to Razzle Dazzle's cubicle to find her waiting for you, seemingly ready to get going."

    show razzle at slot(0, total=1), bright zorder 10

    r "Hey partner! You made the right choice to come by today. You ready to get to work?"

    menu:
        "Hell yeah I am!":
            $ razz += 1
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "Fuck yeah, that's what I like to hear!!"
            r "Let's go interview the hell out of some witnesses and get this case solved!"
        "Yeah, let's get this done. I don't have time to waste":
            $ razz -= 1
            show razzle sad at slot(0, total=1), bright zorder 10
            r "Awwww man, I was hoping for a bit more enthusiasm from you."
            r "But I guess we can get this done anyway."
    show razzle at slot(0, total=1), bright zorder 10
    r "Let's get going! We have a bit of a walk to get to the first witness, so we better start walking!"

    menu:
        "Walk? Why not drive?":
            show razzle mouth open at slot(0, total=1), bright zorder 10
            r "Walking is a great way to get exercise though!!"
            r "And also, it's a little hard for me to be in cars since I'm literally on fire... but yeah, exercise stuff!"
        "Let's roll!":
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "Hell yeah! Let's get this done!"
    scene black
    "You and Razzle Dazzle begin to walk through Los Angeles, heading to the house of the first witness."
    "As you walk, you notice Razzle Dazzle making conversation, mainly just talking aloud, but occasionally asking you questions."

    # Witness scene or something

    show razzle at slot(0, total=1), bright zorder 10
    r "-And then I was like, 'You better pack a fire extinguisher next time!'"
    r "Wait, sorry, I was yapping the entire way here. I wanted to get to know you too, newbie!"

    show razzle question at slot(0, total=1), bright zorder 10
    r "Like, what do you do for fun? Any special people in your life?"

    "Well, there's certainly not anyone in your life, but who knows? Maybe you and Razzle Dazzle might have some chemistry. You decide to answer her question."

    menu:
        "Not much really, I just do work and then get some sleep":
            $ razz -= 1
            show razzle sad at slot(0, total=1), bright zorder 10
            r "Oh man, that sounds like an absolute bore! Surely you do something else, right?"
            show razzle mouth open at slot(0, total=1), bright zorder 10
            r "If not, you need to! Just work and sleep doesn't let you enjoy life at all!"
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "For example, me and Winston go clubbing like ALL the time and it's awesome!"
            r "We get to drink a shit load, meet new people, drink a shit load, then spend the next day talking about how much we shouldn't do that again."
            r "It's a blast! Maybe next time you should come with us!"
            show razzle at slot(0, total=1), bright zorder 10
        "I usually am out all day and night doing whatever the night says!":
            $ razz += 1
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "Hell yeah! That's what I'm talking about, I'm the same way!"
            r "Me and Winston go clubbing like ALL the time and it's awesome!"
            r "We get to drink a shit load, meet new people, drink a shit load, then spend the next day talking about how much we shouldn't do that again."
            r "It's a blast! Maybe next time you should come with us!"
            show razzle at slot(0, total=1), bright zorder 10
        "Are you an option?":
            $ razz += 2
            show razzle flirty at slot(0, total=1), bright zorder 10
            r "Is that so, newbie? I admire the courage, but you're gonna need to have some better lines if you want to get me hot and bothered."
            r "For now though, maybe you can go clubbing with me sometime!"
            r "We can go drink, get shit faced, dance, get more shit faced..."
            r "...Then see if you can handle a night out with me before a more 'personal' evening."
            show razzle at slot(0, total=1), bright zorder 10
    r "For now though, it looks like we made it here!"
    r "Better put on my professional face and talk to them about what they saw. Let's go!"
    show razzle at slot(0, total=1), dim zorder 0

    "You and Razzle Dazzle talk to the witness, introducing yourselves and getting some more basic statements out of the way."

    show razzle question at slot(0, total=1), bright zorder 10

    r "So, Landon. Can you tell me more about what you saw that night?"
    r "Were there any aspects about the suspect that you can remember? Anything at all?"
    r "Like if they had a scar, tattoo, hell, were they missing an arm??"

    show razzle at slot(0, total=1), dim zorder 0
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

    show razzle hoorah at slot(0, total=1), bright zorder 10
    r "Actually, yes it is! Thanks, dude!"
    r "We'll be able to use this information to help narrow down the suspects. If you think of anything else, please let us know!"

    show razzle mouth open at slot(0, total=1), bright zorder 10
    r "You see that, newbie?? We actually got something!! Fuck yeah!!"
    r "Hopefully we can talk to some more peeps tomorrow and learn a bit more about what the killer looks like!"

    show razzle at slot(0, total=1), bright zorder 10
    r "Well, I know you gotta get back to report to boss man, but I'm probably gonna head home."
    r "See you later, newbie!"

    if razz > 4:
        show razzle flirty at slot(0, total=1), bright zorder 10
        r "Keep thinking of ways to get me hot and bothered, newbie, I think you're close to a good line soon!"
    scene black with fade
    $ dayRazz += 1
    jump endOfDay
        

label RazzleDayTwo:
    "You make your way back to Razzle Dazzle's cubicle and find her sitting in her flameproof chair, looking at cat videos on her computer."
    show razzle at slot(0, total=1), bright zorder 10
    r "Oh! Hey newbie! Whatcha up to today? Coming back to do some more work?"

    menu:
        "Yeah, let's get started!":
            $ razz += 1
            show razzle mouth open at slot(0, total=1), bright zorder 10
            r "I like the enthusiasm, but I'm taking today to chill for a bit."
            r "The rest of this week is going to be a lot, so I wanna take it easy today!"
        "Nah, I just wanted to see you again":
            $ razz += 2
            show razzle flirty at slot(0, total=1), bright zorder 10
            r "Oh? I like the sound of that!"
            r "I was hoping you would come back to see me again!"
        "I don't have time for this, let's get to work":
            $ razz -= 2
            show razzle enraged at slot(0, total=1), bright zorder 10
            r "Hey man, no need to be a dick."
            r "If we're gonna solve this together, we need to at least be nice!"

    # Lunch: takes you somewhere nearby, but either gets rejected because she is on fire. She casually heats/cooks something with her hands or gets outside food.
    show razzle at slot(0, total=1), bright zorder 10
    r "So, how about we go get some food or something?"
    r "After that we can just walk around and do absolutely nothing!"

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

    show razzle hoorah at slot(0, total=1), bright zorder 10
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
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "Correct answer, newbie!! One of my favorites!"
            r "C'mon, let's go get some!"

        "Whatever you want.":
            $ razz += 1
            r "Dangerous thing to tell me. I have terrible financial judgment."

        "Can we even go inside a restaurant with you on fire?":
            r "..."

            show razzle sad at slot(0, total=1), bright zorder 10

            r "Okay, so there is one tiny problem with the plan."
            show razzle at slot(0, total=1), bright zorder 10
            r "We'll figure it out! Let's just go find some pizza!!"

    "The two of you make it to a nearby pizza place before issues begin to arise."

    show razzle at slot(0, total=1), dim zorder 0
    "Employee" "I'm sorry, ma'am, but you'll set off every fire alarm in our building just by being there."

    menu:
        "What? That's bullshit! Just let her be on fire!":
            $ razz += 1
            show razzle mouth open at slot(0, total=1), bright zorder 10
            r "It's fine, newbie, it happens all the time."
            r "Look, can we at least get a box to go or something?"
        "Razzle, can you turn off your flames?":
            $ razz -= 1
            show razzle sad at slot(0, total=1), bright zorder 10
            r "I uhh... I can't. I'm pretty much always on fire unless Winston cancels my power out purposely."
            r "Look, can we at least get a box to go or something?"

    show razzle at slot(0, total=1), dim zorder 0
    "Employee" "Certainly. Here, I'll send an order back if you can wait outside."

    "After placing your order and waiting what felt like forever, the two of you find yourselves sitting outside with a pizza box."

    show razzle at slot(0, total=1), bright zorder 10

    r "See? Worked out perfectly."

    "You and Razzle lift a slice."

    "...It's cold."

    show razzle sad at slot(0, total=1), bright zorder 10
    r "Damn..."

    show razzle at slot(0, total=1), bright zorder 10
    r "Want yours reheated?"

    menu:
        "Sure.":
            $ razz += 1
            "She holds your slice between two fingers for a second."

            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "There, perfectly heated!!"

            "The cheese is bubbling."

            "The crust is smoking."

            show razzle at slot(0, total=1), bright zorder 10
            r "...Maybe give it a minute."

        "It's fine, I like it cold anyway.":
            show razzle question at slot(0, total=1), bright zorder 10
            r "Suit yourself, but also cold pizza already??"
            r "Usually that's a 'raiding the fridge at midnight' thing, not a 'right outside the shop' thing."

        "Only if you feed it to me too.":
            $ razz += 2
            show razzle flirty at slot(0, total=1), bright zorder 10

            r "Oh, we're getting brave now, huh?"
            r "Don't wanna burn you though, so you're on your own."
    
    scene black
    "You and Razzle finish your food and walk around the city a bit more."
    "Eventually, you return to the ATLAS team building and go to the rooftop to enjoy the scenery."

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
            show razzle at slot(0, total=1), bright zorder 10
            r "Different is basically the ATLAS motto."

        "We really didn't accomplish anything.":
            $ razz -= 1
            show razzle annoyed at slot(0, total=1), bright zorder 10
            r "That was literally the point!"

    "For a moment, she's quieter than usual."

    show razzle sad at slot(0, total=1), bright zorder 10
    r "People get kinda weird around me sometimes."

    r "Which, y'know, fair. I'm constantly on fire."

    r "But sometimes it feels like that's all they see."

    show razzle at slot(0, total=1), bright zorder 10
    r "ATLAS is nice because nobody here really cares. I'm not 'the fire girl.' I'm just Razzle."

    "She glances over at you."

    r "Well... usually."

    menu:
        "You're definitely more than your power.":
            $ razz += 2

            show razzle flirty at slot(0, total=1), bright zorder 10

            r "Careful, newbie."
            r "Keep saying stuff like that and I might actually start liking you."

        "I dunno. The fire is pretty cool.":
            $ razz += 1

            show razzle mouth open at slot(0, total=1), bright zorder 10
            r "Okay, yeah. It is pretty cool."

        "I mostly see a walking fire hazard.":
            $ razz -= 2

            show razzle annoyed at slot(0, total=1), bright zorder 10

            r "And there goes the moment."

    "A moment of silence passes as you both enjoy the view of the city in each other's company."
    "Eventually, it's time to go back to work."
    show razzle at slot(0, total=1), bright zorder 10
    r "Well, guess it's about time to head home. I'll see you around!"

    if razz > 10:
        show razzle flirty at slot(0, total=1), bright zorder 10
        r "Maybe I'll see you tomorrow too?"
    
    "Razzle leaves, leaving you alone on the rooftop before you head down to report to Ulysses."

    $ dayRazz += 1
    jump endOfDay
    
label RazzleDayThree:
    "You make your way back to Razzle Dazzle's cubicle and see her already standing, getting ready to leave."
    scene cubicleOutline
    show razzle at slot(0, total=1), bright zorder 10
    r "Oh hey newbie!"
    r "I was actually just about to head out to interview another witness. Wanna come with?"

    menu:
        "Duh, of course I do!":
            $ razz += 1
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "Fuck yeah!! That's what I like to hear!"
            r "Let's roll!"
        "Yeah. That's why I'm here.":
            $ razz -= 1
            show razzle annoyed at slot(0, total=1), bright zorder 10
            r "Well damn, you can at least pretend to want to be here."
            r "Fine. Let's go."
    scene black with fade
    "You and Razzle Dazzle make your way to the next witness's home, arriving to question them."

    show razzle at slot(0, total=1), bright zorder 10
    r "Hi there, Brandon, right?"
    r "Is it okay if we ask you some questions about what you saw?"

    show razzle at slot(0, total=1), dim zorder 0
    "Brandon" "Hi there. Yes, that's fine, can we just make this quick, please?"
    "Brandon" "I really don't want to keep thinking about this all."

    show razzle question at slot(0, total=1), bright zorder 10
    r "Perfectly understandable."
    r "We just wanted to hear anything at all about what the killer looked like."
    r "Is there anything you can remember about them?"

    show razzle at slot(0, total=1), dim zorder 0
    "Brandon" "I think so, everything is just so fuzzy..."

    "It seems that Brandon is struggling to organize his thoughts, see what you can do to help!"

    # Minigame
    while not height_memory_completion_recorded:
        $ start_height_memory_minigame()
        while height_memory_active:
            $ renpy.pause(0.1, hard=True)

    show razzle hoorah at slot(0, total=1), bright zorder 10
    r "There we go! The important memories are still on the board, and the rest can take a little vacation."
    # The selected killer decides which witness observation Brandon gives.
    $ razzleDayThreeReveal = get_planned_route_reveal("razzle", 3)
    $ razzleDayThreeHeight = razzleDayThreeReveal["value"].lower()

    show razzle at slot(0, total=1), dim zorder 0
    "Brandon" "Wait... yeah. I remember the doorway now."
    "Brandon" "The silhouette against the frame—they definitely weren't [razzleDayThreeHeight] height. That much I'm sure of."

    show razzle hoorah at slot(0, total=1), bright zorder 10
    r "That's exactly what we needed!"
    r "Ruling out [razzleDayThreeHeight] height narrows down the suspects big time."
    r "Thanks, Brandon! We'll handle the detective work from here."
    scene black
    "You and Razzle leave Brandon with a much tidier thought board and a useful eyewitness lead."
    "Eventually, the two of you make your way back to the office."
    scene cubicleOutline
    show razzle hoorah at slot(0, total=1), bright zorder 10
    r "Oh my God that was amazing!!"
    r "I don't know how you were able to keep him on track so well! Usually my mind is just all over the place!"

    menu:
        "Most people know more than they think, they just need the guide":
            $ razz += 1
            show razzle at slot(0, total=1), bright zorder 10
            r "Well look at you, oh wise one! Seems like you have a lot of wisdom to impart!"
        "I'm pretty good at clearing minds, but mine is stuck on you":
            show razzle flirty at slot(0, total=1), bright zorder 10
            r "Heyy, you're getting pretty good at these!"
            r "The more you say these, the more I wanna hear after this is all over..."
        "It was nothing":
            show razzle at slot(0, total=1), bright zorder 10
            r "Don't be so modest, that was great!"

    show razzle hoorah at slot(0, total=1), bright zorder 10
    r "Anyways, we've made some really great progress!"
    r "Hopefully we can do some more, but I'm still getting a good feeling about this!"

    show razzle at slot(0, total=1), bright zorder 10
    r "But for now I know you gotta talk to Uly, so I'll leave you be."
    r "Catch ya later, newbie!!"

    "With that, Razzle takes her leave, leaving you with your report for the day."

    scene black with fade
    $ dayRazz += 1
    jump endOfDay

label RazzleDayFour:
    "You make your way to Razzle Dazzle's cubicle and find her already standing, getting ready to leave."
    scene cubicleOutline
    show razzle at slot(0, total=1), bright zorder 10
    r "Hey hey!"
    r "About to go check out another witness. You coming with me?"
    menu:
        "Of course!":
            $ razz += 1
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "Fuck yeah!! That's what I like to hear! Let's roll!"
        "Yeah. That's why I'm here.":
            $ razz -= 1
            show razzle annoyed at slot(0, total=1), bright zorder 10
            r "Well damn, you can at least pretend to want to be here. Fine. Let's go."
    scene black with fade
    "You and Razzle Dazzle make your way to the next witness's home, arriving to question them."
    scene cubicleOutline
    show razzle question at slot(0, total=1), bright zorder 10
    r "This is the last witness of the crime, so here's hoping we can get enough info out of them."
    r "If we're lucky, we can use it to narrow down the suspects and find the killer."
    show razzle at slot(0, total=1), bright zorder 10
    "Razzle Dazzle knocks on the door, and you see an elderly woman answer. She looks at you and Razzle Dazzle with a confused expression."

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "He-hello? Can I help you?"

    show razzle at slot(0, total=1), bright zorder 10
    r "Hi there! I'm Razzle Dazzle, and this is my partner."
    r "We're investigating a crime that happened recently, and we were hoping to ask you a few questions about what you saw that night."

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "Oh, I see. Well, I suppose I can help you out. Please, come in."
    "You step into the house and notice how plain it is."
    "The furniture is old and worn, the walls are bare, and Elena clearly lives with very few possessions."

    "Elena" "Please, have a seat. Can I offer you some tea or coffee?"
    menu:
        "Tea would be great, thank you.":
            show razzle at slot(0, total=1), bright zorder 10
            r "Tea sounds perfect. Thank you for offering."
        "Coffee would be great, thank you.":
            show razzle at slot(0, total=1), bright zorder 10
            r "Coffee sounds perfect. Thank you for offering."
        "No thanks, we're fine.":
            show razzle at slot(0, total=1), bright zorder 10
            r "No thanks, we're fine. We just want to ask you a few questions."

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "Of course, dears. Please, make yourselves comfortable."
    
    "Razzle sort of shuffles awkwardly, unable to sit down on any of the cloth chairs or couches in the room."
    show razzle question at slot(0, total=1), bright zorder 10
    $ razzleDayThreeReveal = get_planned_route_reveal("razzle", 3)
    $ razzleDayThreeHeight = razzleDayThreeReveal["value"].lower()

    r "So, Elena, can you tell us what you saw that night?"
    r "Any details you can remember would be very helpful."

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "Well, I remember seeing a figure outside Enrico's house through my window."
    "Elena" "It was so very dark that I couldn't see much. Maybe they were tall? Short? Big? Small? I don't know."
    "Elena" "I just remember that they were there, and then they were gone."

    show razzle question at slot(0, total=1), bright zorder 10
    r "Our last witness helped us rule out [razzleDayThreeHeight] height, but you're not sure if they looked noticeably tall or short?"
    r "Did you notice anything about their clothing or any distinguishing features? Even just something like a hair color?"

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "Hair color? Oh, goodness... I couldn't say."

    "Elena glances toward the front window, narrowing her eyes as if the figure might still be standing outside."

    "Elena" "For a moment I thought their hair looked very light."
    "Elena" "Then a car passed, and it looked dark instead. It may have been a hat for all I know."

    show razzle question at slot(0, total=1), bright zorder 10

    r "Okay, so the lighting was weird. That's still something I guess."

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "I'm sorry, dear. I know that isn't very helpful."

    menu:
        "What made the person seem tall or short?":
            $ razz += 1

            show razzle question at slot(0, total=1), bright zorder 10
            r "Yeah! Don't worry about guessing their exact height."
            r "What made them look that way from where you were sitting?"

            show razzle at slot(0, total=1), dim zorder 0
            "Elena" "I suppose it was where their head appeared against the window."
            "Elena" "They seemed terribly tall at first, but the yard is uneven."

        "Do you think the killer was tall?":
            $ razz -= 1

            show razzle question at slot(0, total=1), bright zorder 10

            r "Careful, newbie. We don't wanna put an answer in her head."

            show razzle at slot(0, total=1), dim zorder 0
            "Elena" "I really couldn't say. Perhaps they were, but perhaps not."

        "Could we recreate what you saw?":
            $ razz += 2

            show razzle hoorah at slot(0, total=1), bright zorder 10

            r "Oh, that's a great idea! We can make our own little murder reenactment!"

            show razzle at slot(0, total=1), dim zorder 0
            "Elena" "Perhaps without the murder part, dear."

            show razzle at slot(0, total=1), bright zorder 10

            r "Right. Yeah. Probably should've phrased that better."

    r "Would it help if we tried standing where you saw them?"

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "It might. I was sitting right here when they passed the window."

    "Razzle looks between Elena's chair and the front window."

    show razzle at slot(0, total=1), bright zorder 10
    r "Okay! Newbie, you go outside and be our mysterious shadowy criminal."

    menu:
        "Why do I have to be the criminal?":
            r "Because I'm on fire, dummy!"

            r "I feel like that would be a pretty memorable detail if the actual killer was doing it."

        "I was born for this role.":
            $ razz += 1

            show razzle hoorah at slot(0, total=1), bright zorder 10

            r "That's the spirit! Try to look suspicious, newbie!"

        "Only if you promise to arrest me afterward.":
            $ razz += 2

            show razzle flirty at slot(0, total=1), bright zorder 10

            r "Oh, I can think of a few ways to restrain you."

            "Elena clears her throat."

            show razzle at slot(0, total=1), bright zorder 10

            r "For official investigative purposes, obviously. No other reason..."

    scene black with fade

    "You step outside while Razzle remains with Elena."

    "Following Razzle's instructions through the window, you walk along the path several times."
    "You try standing straight, hunching over, and pretending to carry something against your chest."

    "On the third pass, Elena suddenly raises her hand."

    "Elena" "Wait! Stop there!"

    scene cubicleOutline
    show razzle question at slot(0, total=1), bright zorder 10

    "You return inside as Elena studies the window."

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "That was much closer. The figure wasn't necessarily large or heavy."
    "Elena" "They were holding something bulky against their coat and leaning forward."

    show razzle question at slot(0, total=1), bright zorder 10
    r "Aha! So that hunch and whatever they were lugging made their build look wide, and that slope messed with the height!"
    r "Brandon had that doorway frame to measure against yesterday, but out here, posture completely warps the silhouette."

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "Yes, I believe so. And the lawn slopes upward near the window."
    "Elena" "That may be why I first thought they were tall. I suppose you can't rely on the build either."

    show razzle hoorah at slot(0, total=1), bright zorder 10

    r "Holy shit, newbie! We actually cracked the case! Well, not really, but you know what I mean!"

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "Have I helped identify them?"

    show razzle at slot(0, total=1), bright zorder 10

    r "Not exactly, lady."
    r "But you helped us figure out that we can't trust that wide build or the uneven ground for height. It was all distorted."

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "I'm afraid that doesn't sound nearly as impressive."

    show razzle sad at slot(0, total=1), bright zorder 10

    r "Well, when you say it like that..."

    show razzle at slot(0, total=1), bright zorder 10

    "Elena looks toward the window once more."

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "There was one other thing."

    show razzle question at slot(0, total=1), bright zorder 10

    r "Anything you remember could help."

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "When the car passed, the person raised a hand to shield their face. For just a moment, I could see the top of their head."

    show razzle question at slot(0, total=1), bright zorder 10
    r "Their hair?"

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "Perhaps. But the light passed too quickly. I don't trust myself to name the color."

    "Elena" "The little grocery across the street had a security camera pointed toward the road, though."
    "Elena" "If they kept the recording, it may have seen the same car pass."

    show razzle hoorah at slot(0, total=1), bright zorder 10

    r "Now that sounds like a lead!"

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "I'm glad I could help, dears."

    show razzle at slot(0, total=1), bright zorder 10
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

            show razzle hoorah at slot(0, total=1), bright zorder 10
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

    r "Assuming the footage isn't terrible."
    r "Which, knowing our luck, it absolutely will be."

    "Razzle grins and gives you a playful shove with her shoulder, stopping just short of letting her flames touch you."

    r "Not a bad day, partner. I'll let you know what I find."

    scene black with fade
     
    $ dayRazz += 1
    jump endOfDay

label RazzleDayFive:
    $ razzleDayThreeReveal = get_planned_route_reveal("razzle", 3)
    $ razzleDayThreeHeight = razzleDayThreeReveal["value"].lower()
    scene cubicleOutline

    "You make your way to Razzle's cubicle and find her crouched in front of an old television and VCR."

    "Several videotapes are scattered across the floor. One of them has a grocery-store receipt taped to its side."

    show razzle hoorah at slot(0, total=1), bright zorder 10

    r "Newbie! Great news!"
    r "The grocery store still had the tape!"

    menu:
        "You actually found it?":
            $ razz += 1

            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "Sure did!"
            r "And it only took three phone calls, two flameproof cab rides, and one extremely suspicious store manager!"

        "Please tell me you didn't threaten anybody.":
            $ razz -= 1

            show razzle question at slot(0, total=1), bright zorder 10

            r "What? No!"

            r "I just stood uncomfortably close to the manager until he remembered where the tapes were."
            r "The heat seemed to jog his memory."

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

            r "But surely it'll work, right?? Let's go for it!"

        "Can't we fast-forward to the right time?":
            r "We can try, but the clock on the tape keeps blinking twelve."

            r "Apparently grocery-store security wasn't prepared for us to solve a murder."

        "Maybe hitting the VCR will help.":
            $ razz += 1

            show razzle question at slot(0, total=1), bright zorder 10

            r "Hmmm, I like it! Tech always works better when you hit it."
            "Razzle punches the VCR."
            "Nothing happens."
            show razzle at slot(0, total=1), bright zorder 10
            r "Well, that was a bust. Guess we'll just start watching!"

    scene black

    "You and Razzle begin working through the recording."

    "You handle the remote while she compares the passing cars to Elena's description."

    "After what feels like hours, a pair of headlights sweeps across the road."

    r "Wait!"

    "The tape stops."

    "A faint figure is visible near the edge of the picture."

    scene cubicleOutline
    show razzle hoorah at slot(0, total=1), bright zorder 10

    r "Holy shit, that's them!"
    r "That's gotta be them!"

    "Razzle reaches over and rewinds the recording, playing the moment again."

    scene black

    "The figure enters at the bottom of the frame."

    "For a moment, they appear almost as tall as the nearby street sign. As they move toward the center of the image, their outline seems to shrink."

    r "Okay. Either the killer changed size halfway across the street, or this camera angle is complete garbage."

    "The figure steps onto the sloped curb and briefly leans against the grocery store's outer wall."

    "One hand reaches out to steady themselves against the rough brick."
    "The instant their knuckles brush the surface, they flinch hard and snatch their hand back, tucking it gingerly against their ribs."

    r "Yeesh. Look at that jerk-back."
    r "You only pull away like that if your hand is already bruised or scraped raw."

    r "Maybe our killer got banged up during the struggle? Or maybe they just hate rough masonry."
    r "Wish this tape had enough resolution to see their skin."

    "The figure flexes the injured fingers once under their sleeve, but the image skips before you can see anything more."

    "A second later, the headlights pass over them."

    "The figure raises an arm to cover their face."

    r "That's exactly what Elena described!!"

    "Razzle advances the tape one frame at a time."

    "The person's outline stretches and compresses awkwardly as they cross the sloping pavement."

    "Whatever they are carrying against their chest blends directly into their torso, making their build seem hulking and wide whenever they turn toward the lens."

    r "Look at that silhouette!"
    r "When they hunch forward over that bundle, they look wide as a truck..."
    r "...But when they step upright, it completely changes."

    r "That proves our reenactment with Elena yesterday was spot-on!"
    r "The 'wide build' was just an optical illusion from lugging that bulky package."

    r "And man, out on this uneven street, they look tall in one frame and short in the next!"
    r "Thank God Brandon had that doorway frame to rule out [razzleDayThreeHeight] height, because this tape's perspective is a total mess."

    "Razzle watches the footage again."

    "She advances the tape to the moment the figure shields their face from the glare."

    r "Hold on... look right at the edge of the light beam..."

    "For three grainy frames, several loose strands are visible around the figure's uncovered head."

    scene cubicleOutline
    show razzle question at slot(0, total=1), bright zorder 10

    r "So Elena really did see their hair!"
    r "It definitely wasn't a hat or a hood."

    show razzle annoyed at slot(0, total=1), bright zorder 10
    r "Too bad the tape's black and white."

    r "We finally get a camera pointed at the killer and the thing can't even tell us what damn color we're looking at."

    menu:
        "The tape still confirmed Elena's memory.":
            $ razz += 1

            show razzle at slot(0, total=1), bright zorder 10
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

            r "We know which parts of Elena's memory matched the recording."
            r "That's gotta count for something."

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

            r "Exactly!"
            r "We put them in the same light and see which colors Elena could've confused."

        "Would Elena agree to another reconstruction?":
            show razzle question at slot(0, total=1), bright zorder 10
            r "I think so. Especially if we bring her something nice for helping."
            r "Should you bring grandma's cookies? Or is that their thing?"

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
        "Not bad at all! You're super smart with this stuff!":
            $ razz += 2

            show razzle flirty at slot(0, total=1), bright zorder 10

            r "That's actually really sweet."

            r "Don't tell anybody."
            r "I've got a reputation for being an idiot to maintain."

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
        show razzle hoorah at slot(0, total=1), bright zorder 10
        r "You better come with me tomorrow, newbie."
        r "I need my favorite suspicious silhouette!"

    "Razzle gives you a grin before turning back toward the television."

    "The tape continues playing as you leave, the shadowy figure disappearing once again into the darkness."

    scene black with fade

    $ dayRazz += 1
    jump endOfDay

label RazzleDaySix:
    scene cubicleOutline

    "You arrive at Razzle's cubicle to find three mannequin heads lined up across her desk."

    "One wears a blonde wig, one wears a brown wig, and one wears a black wig."

    show razzle hoorah at slot(0, total=1), bright zorder 10

    r "There you are!"
    r "Welcome to the weirdest hair salon in Los Angeles!"

    menu:
        "You got everything for the reconstruction?":
            $ razz += 1

            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "Sure did!"
            r "Wigs, stands, measurements, and one very confused cab driver!"

        "Which one are you wearing?":
            $ razz += 2

            show razzle flirty at slot(0, total=1), bright zorder 10

            r "Whichever one you think makes me look hottest."

            r "After we solve the murder, obviously."

        "This looks ridiculous.":
            $ razz -= 1

            show razzle question at slot(0, total=1), bright zorder 10

            r "Yeah. It's also gonna help us catch a killer."

            r "Things can be two things, newbie."

    show razzle at slot(0, total=1), bright zorder 10

    r "Elena agreed to help us one more time."

    r "We're putting each wig where the killer stood and recreating the headlights."
    r "Then we see which one matches what she remembers."

    r "No guessing from a list. No telling her which color we expect."
    r "She just gets numbered samples."

    menu:
        "We should change the order between tests.":
            $ razz += 2

            show razzle hoorah at slot(0, total=1), bright zorder 10

            r "Already planned on it!"
            r "Look at us doing real science!"

        "We should remind Elena about the security tape.":
            $ razz -= 1

            show razzle question at slot(0, total=1), bright zorder 10

            r "Better not. We don't want the tape putting an answer in her head."

        "Let's see what she remembers.":
            $ razz += 1

            r "Exactly. We set it up, shut up, and let her tell us."

    scene black with fade

    "You and Razzle return to Elena's house and arrange the three covered mannequin heads outside."

    "Razzle parks a borrowed car where the vehicle appeared on the security tape."

    "Tape marks show where the figure stood and where the headlights crossed the lawn."

    "Razzle checks every measurement twice before joining you at the window."

    scene cubicleOutline
    show razzle at slot(0, total=1), dim zorder 0

    "Elena" "This is certainly more elaborate than I expected."

    show razzle at slot(0, total=1), bright zorder 10
    r "We really appreciate you doing this."

    r "We're going to show you three different samples."
    r "If none of them look right, say so. Don't force yourself to pick one."

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "I understand, dear."

    scene black

    "You take your position by the car while Razzle remains inside with Elena."

    "One at a time, you uncover the numbered samples and move them through the same patch of light."

    "The first passes the window. Elena says nothing."

    "The second passes. She leans forward, but eventually shakes her head."

    "When the final sample crosses the lawn, Elena grips the arm of her chair."

    "Elena" "Wait. Please show me that one again."

    "You reset the sample and repeat the movement."

    "Elena watches without speaking until the headlights fade."

    scene cubicleOutline
    show razzle question at slot(0, total=1), bright zorder 10

    r "Are you sure?"

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "I would like to see them in a different order first."

    show razzle hoorah at slot(0, total=1), bright zorder 10

    r "Elena, you are officially my favorite witness."

    scene black

    "You rearrange the samples and run the reconstruction again."

    "This time, Elena identifies the same sample immediately."

    $ razzleDaySixReveal = get_planned_route_reveal("razzle", 6)
    $ razzleDaySixHair = razzleDaySixReveal["value"]

    scene cubicleOutline
    show razzle at slot(0, total=1), dim zorder 0

    "Elena" "That is the color I saw. The person outside Enrico's house had [razzleDaySixHair] hair."

    show razzle question at slot(0, total=1), bright zorder 10
    r "Not just that they didn't have one of the other colors?"

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "No. I recognize this color. I am certain."

    $ razzleDaySixClueText = "Elena positively identifies the killer as having {} hair.".format(razzleDaySixHair)
    $ record_planned_route_reveal(
        "razzle", 6, clue_text=razzleDaySixClueText)

    show razzle hoorah at slot(0, total=1), bright zorder 10

    r "Holy shit! We actually got it!"

    r "That means anyone without [razzleDaySixHair] hair comes off the suspect list."

    r "That's huge, Elena!"

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "Then I am glad my memory was useful after all."

    show razzle at slot(0, total=1), bright zorder 10

    r "It wasn't just useful."
    r "You may have helped us catch the killer!"

    "Elena smiles as Razzle begins carefully gathering the equipment."

    scene black with fade

    "After returning the borrowed car and the deeply unfortunate wigs, you and Razzle walk back toward ATLAS."

    show razzle hoorah at slot(0, total=1), bright zorder 10

    r "Six visits, three witnesses, one terrible videotape, and absolutely no houses burned down!"

    r "I think that makes us a pretty damn good team."

    menu:
        "You did some great detective work.":
            $ razz += 2

            show razzle flirty at slot(0, total=1), bright zorder 10

            r "Careful."
            r "Keep saying things like that and I might start believing I'm smart."

            r "Then you'll never get rid of me."

        "We make a good team.":
            $ razz += 1

            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "Hell yeah we do!"

            r "You handle the thinking, I handle the fire, and we split everything else fifty-fifty."

        "Elena did most of the work.":
            $ razz -= 1

            show razzle sad at slot(0, total=1), bright zorder 10

            r "She gave us the answer, yeah."

            r "But we still had to help her find it."

    if razz > 14:
        show razzle flirty at slot(0, total=1), bright zorder 10

        r "So... once we finish accusing people of murder, you still owe me that night out."

        r "Drinks, dancing, and somewhere fireproof."

        r "Think you can handle that, partner?"

        menu:
            "I can handle the heat.":
                $ razz += 2

                show razzle hoorah at slot(0, total=1), bright zorder 10

                r "Fuck yeah! That's the answer I wanted!"

            "I'm looking forward to it.":
                $ razz += 1

                show razzle flirty at slot(0, total=1), bright zorder 10

                r "Good. So am I."

    else:
        show razzle at slot(0, total=1), bright zorder 10

        r "Seriously, though."
        r "Thanks for sticking with me through all of this."

        r "It would've been way less fun without you."

    "Razzle gives you one final grin before heading inside to file the evidence."

    scene black with fade

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
    scene cubicleOutline
    "You make your way to Ica's cubicle, where you see her already sitting with her feet kicked up, chewing gum."
    show ica at slot(0, total=1), bright zorder 10
    i "Sup freshie. Come to slack off a bit?"
    i "I've been playing cards against myself all morning. I keep winning, which is either impressive or a little sad."
    i "You wanna be a real opponent?"
    "Ica lays out a small deck and gives you one last chance to choose your approach."

    # Need to change how minigame works to have flirt dialogue and such happen before the game.
    $ start_ica_cards_minigame()
    $ ica_cards_result = ica_minigame_results.get("cards", {})

    if not ica_cards_result.get("completed", False):
        i "Calling it early? Fair. I can respect a strategic retreat."
    elif ica_cards_result.get("won", False):
        if ica_cards_result.get("approach") == "flirt":
            show ica shock at slot(0, total=1), bright zorder 10
            i "Heyyy no fair!! You kept distracting me with all those things you were saying!"
            $ ica += 2
            show ica flirty at slot(0, total=1), dim zorder 0
            i "Fine, I guess you win this one freshie... but no distracting me with sweet talk next time!"
        elif ica_cards_result.get("approach") == "cheat":
            show ica whatTheFuckDidYouJustDoMC at slot(0, total=1), bright zorder 10
            i "Hold up. Were you cheating and STILL lost?? What a loser..."
            $ ica -= 2
        else:
            show ica happy at slot(0, total=1), bright zorder 10
            i "A clean win? Rude. I was expecting to carry this hangout."
    else:
        show ica at slot(0, total=1), bright zorder 10
        if ica_cards_result.get("approach") == "flirt":
            i "You distracted me just enough to make that close. I still take the win, though."
        elif ica_cards_result.get("approach") == "cheat":
            i "Your cheating was adorable, but my cards were better. Run it back later."
        else:
            i "You played fair and still lost. That is tragic. I will try not to brag about it."
    show ica at slot(0, total=1), bright zorder 10
    i "Oh damn, look at the time already, we've burned through the full day"
    i "Guess you better go tell Ulysses you did nothing all day :p catcha later!"
    "Ica makes her way out the front door, leaving you to report to Ulysses"

    $ dayIca += 1
    jump endOfDay

label IcaDayTwo:
    "You make your way back to Ica's cubicle, where she's still doing nothing"
    scene cubicleOutline
    show ica at slot(0, total=1), bright zorder 10
    i "Oh, look who's back? Enjoy slacking off last time?"

    menu:
        "It was pretty cool":
            $ ica +=1
            show ica happy at slot(0, total=1), bright zorder 10
            i "Duh, of course it was. I'm awesome"
        "Of course, I enjoyed spending time with you":
            $ ica -=1
            show ica shock at slot(0, total=1), bright zorder 10
            i "..."
            show ica at slot(0, total =1), bright zorder 10
            i "Cringeeeeeeeee."
            i "What a cheesy line dude. You gotta be more smooth with stuff"
        "We wasted so much time":
            show ica whatTheFuckDidYouJustDoMC at slot(0, total=1), bright zorder 10
            i "Yeah. Not like I'm doing anything for the job."
            i "Also you CHOSE to be here dude. No one made you slack off."
    show ica at slot(0, total=1)
    i "Anyway, I was gonna play some more cards or something, but I forgot to bring some."
    i "Wanna do something stupid to pass the time like a staring contest?"
    i "First person to blink loses. Keep your eyes on the target and try to outlast my absolutely terrifying stare."

    $ start_ica_staring_minigame()
    $ ica_staring_result = ica_minigame_results.get("staring", {})

    if ica_staring_result.get("completed", False):
        $ ica_staring_apply_relationship_result()
        if ica_staring_result.get("won", False):
            if ica_staring_result.get("approach") == "flirt":
                show ica shock at slot(0, total=1), bright zorder 10
                i "You kept eye contact and talked trash at the same time? That's deeply unfair. I respect it."
            elif ica_staring_result.get("approach") == "cheat":
                show ica whatTheFuckDidYouJustDoMC at slot(0, total=1), bright zorder 10
                i "Was that a mirror blink cue? I saw it. Fine, you win—but I'm confiscating the tiny mirror."
            else:
                show ica happy at slot(0, total=1), bright zorder 10
                i "A clean win. You didn't blink once. That's impressive and a little unsettling."
        else:
            show ica at slot(0, total=1), bright zorder 10
            if ica_staring_result.get("approach") == "flirt":
                i "The banter almost got me, but you blinked first. Nice try, freshie."
            elif ica_staring_result.get("approach") == "cheat":
                i "You had a mirror and a blink cue and still blinked first? That's honestly kind of impressive."
            else:
                i "You played fair and blinked first. I will try not to brag about this for the rest of the day."
    else:
        show ica at slot(0, total=1), bright zorder 10
        i "Calling it early? Fair. The staring contest will still be here when you're ready to lose properly."

    show ica at slot(0, total=1), bright zorder 10
    i "Oh damn, that contest took longer than I thought."
    i "Go pick another way to look busy, freshie. Catcha later!"
    "Ica heads toward the front desk, still accusing you of blinking first."

    $ dayIca += 1
    jump dayLoop

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
