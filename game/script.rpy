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
    f "That's the team! And that's my part done, newbie. I won't be around after today, so consider this my extremely permanent goodbye."
    f "Good luck with ATLAS. Try not to let Winston explain the employee handbook."

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

    show nicky question at slot(0, total=2), bright zorder 10
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
            show nicky question at slot(0, total=2), bright zorder 10
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

    show madeline madScientist at slot(0, total=1), bright zorder 10
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
    jump UlyssesEvening

label advanceDayAfterDebrief:
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
    jump dayLoop

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

label RazzleDayOne:
    $ razzle_day_one_route = "busy"
    scene black
    "You make your way to Razzle Dazzle's cubicle to find her waiting for you, seemingly ready to get going."
    "A witness list sits open on her desk beside two pens, a city map, and a travel mug with scorch marks around the lid. She has circled the first address three times."

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
            "She demonstrates by holding up one scorched bus pass, then tucks it away before the ash can fall on the witness list."
        "Let's roll!":
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "Hell yeah! Let's get this done!"
            "Razzle shoulders her bag, checks that the travel mug is sealed, and lets you carry the map."
    scene black
    "You and Razzle Dazzle begin to walk through Los Angeles, heading to the house of the first witness."
    "As you walk, you notice Razzle Dazzle making conversation, mainly just talking aloud, but occasionally asking you questions."

    "At the first intersection, she offers you a choice between a busy shopping street and a quieter route through the park."

    menu:
        "Take the busy street.":
            $ razz += 1
            $ razzle_day_one_route = "busy"
            r "Yes! More people, more stuff happening, better odds somebody's playing music too loud!"
            "Razzle waves at three strangers on the way. Two wave back; the third checks whether anything nearby is burning."
        "Take the quiet park route.":
            $ razzle_day_one_route = "park"
            r "Sure! Gives me more room to tell the long version of this story."
            "The long version begins before you reach the next block and develops several unnecessary side characters."
        "Let Razzle choose.":
            $ razz += 1
            $ razzle_day_one_route = "both"
            r "Dealer's choice! Busy street there, park on the way back. We get both!"


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
            r "Winston and I go clubbing whenever both of us make the same bad decision at once. Music, strangers, the worst drinks you can imagine, the whole thing."
            r "Come with us sometime. Worst case, you hate it and finally have a hobby to complain about."
            show razzle at slot(0, total=1), bright zorder 10
        "I usually am out all day and night doing whatever the night says!":
            $ razz += 1
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "Hell yeah! That's what I'm talking about, I'm the same way!"
            r "You might actually survive a night out with me and Winston."
            r "We dance, make friends with everybody in the building, drink enough to regret our lives, then compare hangovers the next day!"
            r "Next time we go, you're getting an invitation."
            show razzle at slot(0, total=1), bright zorder 10
        "Are you an option?":
            $ razz += 2
            show razzle flirty at slot(0, total=1), bright zorder 10
            r "Yeah, newbie? I admire the courage, but you're gonna need to have some better lines if you want to get me hot and bothered."
            r "For now though, maybe you can go clubbing with me sometime!"
            r "We can go drink, get shit faced, dance, get more shit faced..."
            r "...Then see if you can handle a night out with me before a more 'personal' evening."
            show razzle at slot(0, total=1), bright zorder 10
    r "For now though, it looks like we made it here!"
    r "Better put on my professional face and talk to them about what they saw. Let's go!"
    show razzle at slot(0, total=1), dim zorder 0

    "Razzle knocks, waits, and checks the name in her notes before the door opens. Her volume drops—not by much, but enough to make the greeting feel less like an entrance."
    "You and Razzle Dazzle talk to the witness, introduce yourselves, explain why you are there, and spend a few minutes on basic statements before approaching the difficult part."

    show razzle question at slot(0, total=1), bright zorder 10

    r "So, Landon. Can you tell me more about what you saw that night?"
    r "Were there any aspects about the suspect that you can remember? Anything at all?"
    r "Like if they had a scar, tattoo, hell, were they missing an arm??"

    show razzle at slot(0, total=1), dim zorder 0
    "Landon" "Well, I don't remember too much about the suspect since it was so late, but I can for sure say one thing..."

    # Mixed routes may have already cleared the authored target, so the shared
    # resolver supplies a different unused, killer-safe identifying feature.
    $ razzleDayOneReveal = get_planned_route_reveal("razzle", 1)
    $ razzleDayOneClearedId = razzleDayOneReveal["eliminated"][0]
    $ razzleDayOneUniqueId = suspectAttributes[razzleDayOneClearedId]["unique_id"]
    $ razzleDayOneWitnessText = RAZZLE_UNIQUE_ID_WITNESS_TEXT[razzleDayOneUniqueId]
    $ razzleDayOneClueText = "Eyewitness evidence rules out {}: {}".format(suspectNames[razzleDayOneClearedId], razzleDayOneWitnessText)

    "Landon" "[razzleDayOneWitnessText]"

    $ record_planned_route_reveal(
        "razzle", 1, clue_text=razzleDayOneClueText, expected_count=1)

    "Landon" "Is that any help to you guys at all?"

    show razzle hoorah at slot(0, total=1), bright zorder 10
    r "Actually, yes it is! Thanks, dude!"
    r "We'll be able to use this information to help narrow down the suspects. If you think of anything else, please let us know!"

    show razzle mouth open at slot(0, total=1), bright zorder 10
    r "You see that, newbie?? We actually got something!! Hell yes!!"
    r "Hopefully we can talk to some more peeps next time and learn a bit more about what the killer looks like!"

    "Razzle hands Landon an ATLAS card with the office number, repeats that even a small memory may matter, and waits while he tucks it behind the photograph on his refrigerator. Only then does she close her notebook."

    show razzle at slot(0, total=1), bright zorder 10
    r "Well, I know you gotta get back to report to boss man, but I'm probably gonna head home."
    r "See you later, newbie!"

    if razz >= RAZZLE_EARLY_THRESHOLD:
        show razzle flirty at slot(0, total=1), bright zorder 10
        r "Keep thinking of ways to get me hot and bothered, newbie, I think you're close to a good line soon!"
    if razzle_day_one_route == "both":
        "Razzle keeps her promise and takes the park on the way back. The slower path gives her time to replay the useful part of Landon's statement aloud, drift into a story about Winston and a wild night out, and circle back before you reach ATLAS."
    elif razzle_day_one_route == "park":
        "The walk back follows the busier street this time. Razzle replays the useful part of Landon's statement over the noise, catches herself drifting into a story about Winston and a wild night out, and circles back before you reach ATLAS."
    else:
        "The walk back is slower. Razzle replays the useful part of Landon's statement aloud, catches herself drifting into a story about Winston and a wild night out, and circles back before you reach ATLAS."
    scene black with fade
    $ dayRazz += 1
    jump endOfDay
        
label RazzleDayTwo:
    "You make your way back to Razzle Dazzle's cubicle and find her sitting in her flameproof chair with a novelty VHS playing on a tiny television. A cat repeatedly attempts to jump onto a windowsill and repeatedly misses."
    show razzle at slot(0, total=1), bright zorder 10
    r "Oh! Hey newbie! Whatcha up to today? Coming back to do some more work?"

    menu:
        "Yeah, let's get started!":
            $ razz += 1
            show razzle mouth open at slot(0, total=1), bright zorder 10
            r "I like the enthusiasm, but I'm taking today to chill for a bit."
            if dayWin >= 6:
                r "Tomorrow's deadline is gonna be brutal, so I want one hour where my brain isn't chewing on witness statements."
            elif dayWin >= 5:
                r "The final meeting's getting close, so I want one hour where my brain isn't chewing on witness statements."
            else:
                r "This week is gonna be a lot, so I wanna take it easy today!"
        "Nah, I just wanted to see you again":
            $ razz += 2
            show razzle flirty at slot(0, total=1), bright zorder 10
            r "Oh? I like the sound of that!"
            r "I was hoping you would come back to see me again!"
        "I don't have time for this, let's get to work":
            $ razz -= 2
            show razzle enraged at slot(0, total=1), bright zorder 10
            r "Okay, captain stopwatch. I heard you."
            r "If we're gonna solve this together, you don't have to be a dick"

    # Lunch: takes you somewhere nearby, but either gets rejected because she is on fire. She casually heats/cooks something with her hands or gets outside food.
    show razzle at slot(0, total=1), bright zorder 10
    r "So, how about we go get some food or something?"
    r "After that we can just walk around and do absolutely nothing!"

    menu:
        "That sounds irresponsible.":
            $ razz += 1
            r "That's the spirit!"
        "Sounds like my kind of day.":
            $ razz += 1
            show razzle mouth open at slot(0, total=1), bright zorder 10
            r "See? I knew there was a reason I liked you."
        "Is setting something on fire part of the plan?":
            r "Okay, first of all, probably."
            show razzle sad at slot(0, total=1), bright zorder 10
            r "Second of all, I only accidentally set things on fire like... fifty percent of the time."
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
            $ razz += 1
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "Pizza! Hell yeah, one of my favorites!"
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

    "The employee turns the order screen toward you while Razzle leans in through the open doorway from a safe distance."

    menu:
        "Order pepperoni and extra cheese.":
            $ razzle_day_two_pizza = "pepperoni"
            r "Classic! Way to play it safe newbie"
        "Order every spicy topping they have.":
            $ razz += 1
            $ razzle_day_two_pizza = "spicy"
            r "Yessssi I love a spicy pizza!!"
        "Order half your choice, half Razzle's.":
            $ razz += 1
            $ razzle_day_two_pizza = "split"
            r "Put everything dangerous on my half please!"

    "You finish the order together through the doorway. Razzle spends the wait rating every passing dog and trying to guess which pedestrians will cross the street before they notice her."

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
    
    "You and Razzle finish the pizza without rushing. She reheats the last slice three separate times because the conversation keeps distracting her before she can eat it."

    r "We've got hours before anybody expects us back. Pick a direction."

    menu:
        "Browse the outdoor market.":
            $ razz += 1
            $ razzle_day_two_detour = "market"
            "Razzle stops at every stall she can approach safely and buys a pair of sunglasses she does not need after sunset."
            r "They complete the look!'"
            r "Don't ask what the look is though, I'm not entirely sure..."
        "Walk through the park.":
            $ razzle_day_two_detour = "park"
            "You take the quieter path back. Razzle narrates an ongoing feud between two squirrels until both vanish into a tree."
            r "Cowards! We were about to get to the motive!"
        "Head back slowly and see what happens.":
            $ razz += 1
            $ razzle_day_two_detour = "wandering"
            "The route becomes a series of detours: a street musician, a mural, and a store window full of terrible hats."

    scene black
    "Eventually, the familiar ATLAS building comes back into view. Rather than go inside, Razzle points toward the roof and races you to the stairwell door."

    scene black
    with dissolve

    "By the time you reach the roof, the sun is beginning to set. You catch your breath while Razzle claims a place on the ledge."

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

    "Razzle watches the street below. A restaurant worker is carrying chairs inside for the night, and she follows the movement until the last one disappears through the door."

    r "Thanks for not making the pizza thing worse, by the way."
    r "I joke about it because it happens all the time, but sometimes it can really be annoying. Not too much though."

    menu:
        "Ask whether it still bothers her.":
            $ razz += 1
            r "Sometimes. Not enough to stop going places, but yeah."
        "Say the employee was worried about the building, not her.":
            r "I know. That's what makes it complicated. Nobody has to hate me for it to still feel shitty."
        "Let her take her time.":
            $ razz += 1
            "You stay beside her without filling the silence. After a few breaths, she continues on her own."

    "For a moment longer, she's quieter than usual. Then she bumps her shoulder lightly against yours, stopping before the flames can follow."
    r "Still not gonna stop me from getting pizza. Just means the next place better appreciate outdoor seating."

    menu:
        "I'd get pizza with you again.":
            $ razz += 2

            show razzle flirty at slot(0, total=1), bright zorder 10

            r "Good! Next time we're finding somewhere that serves it hot on purpose."

        "I dunno. The fire is pretty cool.":
            $ razz += 1

            show razzle mouth open at slot(0, total=1), bright zorder 10
            r "Okay, yeah. It is pretty cool."

        "I get why the employee worried about the building.":
            $ razz -= 1

            show razzle sad at slot(0, total=1), bright zorder 10

            r "Yeah. I do too. That's the annoying part—sometimes everybody's being reasonable and it still sucks."

    "A moment of silence passes as you both enjoy the view of the city in each other's company."
    "Eventually, it's time to go back to work."
    show razzle at slot(0, total=1), bright zorder 10
    r "Well, guess it's about time to head home. I'll see you around!"

    if razz >= RAZZLE_WARM_THRESHOLD:
        show razzle flirty at slot(0, total=1), bright zorder 10
        if dayWin >= 6:
            r "Guess I'll see you in the briefing room, then. Sit somewhere I can see whether you're panicking."
        else:
            r "Maybe I'll see you next time too?"
    
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
            r "Now that's what I like to hear!"
            r "Let's roll!"
        "Yeah. That's why I'm here.":
            $ razz -= 1
            show razzle annoyed at slot(0, total=1), bright zorder 10
            r "Well damn, you can at least pretend to want to be here."
            r "Fine. Let's go."

    "Razzle checks the witness address, tucks a clean copy of the statement form into her bag, and pats down three pockets before finding her pen behind one ear."

    menu:
        "Ask what the witness has already reported.":
            $ razz += 1
            r "A silhouette, maybe a big coat, and a whole lot of 'I think.' We're helping him sort memory from guesses today."
        "Offer to take notes while she leads.":
            $ razz += 1
            r "Please do! My handwriting gets kind of excited and stops being a real alphabet."
        "Ask whether she practiced her professional voice.":
            r "Absolutely! It's my regular voice with, like, twelve percent less yelling."

    scene black with fade
    "You and Razzle Dazzle walk to the next witness's home. Along the way, she reviews the questions aloud and lets you strike two that assume more than the first statement established."
    "At the door, she gives you a quick thumbs-up, waits until you are ready with the notes, and knocks."

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
    call RulesHeightMemory
    while not height_memory_completion_recorded:
        $ start_height_memory_minigame()
        while height_memory_active:
            $ renpy.pause(0.1, hard=True)

    show razzle hoorah at slot(0, total=1), bright zorder 10
    r "There we go! The important memories are still on the board, and the rest can take a little vacation."
    # The selected killer decides which witness observation Brandon gives.
    $ razzleDayThreeReveal = get_planned_route_reveal("razzle", 3)
    $ razzleDayThreeHeight = razzleDayThreeReveal["value"].lower()
    $ razzleDayThreeNames = " and ".join([suspectNames[suspect_id] for suspect_id in razzleDayThreeReveal["eliminated"]])

    show razzle at slot(0, total=1), dim zorder 0
    if razzleDayThreeReveal.get("scope") == "category":
        "Brandon" "Wait... yeah. I remember the doorway now."
        "Brandon" "The silhouette against the frame—they definitely weren't [razzleDayThreeHeight] height. That much I'm sure of."
        show razzle hoorah at slot(0, total=1), bright zorder 10
        r "That's something we can actually use!"
        r "Ruling out [razzleDayThreeHeight] height narrows down the suspects big time."
    else:
        "Brandon" "Wait... yeah. The doorway, the shoulder line, and where their head crossed the frame."
        "Brandon" "Those two profile photographs don't fit what I saw. I'm certain about that much."
        show razzle hoorah at slot(0, total=1), bright zorder 10
        r "Then [razzleDayThreeNames] are clear."
    r "Thanks, Brandon! We'll handle the other detective work from here."
    "Razzle does not hurry Brandon after the answer. She repeats what he remembered in neutral language, asks whether he wants anything corrected, and leaves him with the office number."
    scene black
    "You and Razzle leave Brandon with a much tidier thought board and a useful eyewitness lead. On the walk back, she stops twice to add details to her notes before they can blur together."
    "Eventually, the two of you make your way back to the office, spread the statement beside the notes from your previous interview, and check that the new exclusion does not contradict the first witness."
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
            $ razz += 2
            show razzle flirty at slot(0, total=1), bright zorder 10
            r "Heyy, you're getting pretty good at these!"
            r "The more you say these, the more I wanna hear after this is all over..."
        "It was nothing":
            show razzle at slot(0, total=1), bright zorder 10
            r "Don't be so modest, that was great!"

    show razzle hoorah at slot(0, total=1), bright zorder 10
    r "Anyways, we've made some really great progress!"
    r "Hopefully we can do some more, I'm getting a good feeling about this!"

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
        "Wouldn't miss the last witness.":
            $ razz += 1
            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "That's the spirit! Elena's got one more angle on this and we're gonna help her find it."
        "I'm coming, but we need to avoid leading her.":
            $ razz += 1
            show razzle question at slot(0, total=1), bright zorder 10
            r "Fair. If I start answering my own questions, kick me under something nonflammable."
        "Tell me what we know on the walk.":
            show razzle at slot(0, total=1), bright zorder 10
            r "Deal. You get the short version first, which is still gonna be kind of long."
    "Razzle gathers the notes from both previous witnesses and clips them separately so today's account cannot quietly borrow details from either one."
    "On the walk, she rehearses a careful introduction, gets distracted by a food truck, then starts again from the top before you reach Elena's street."
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

            r "Hell yeah you were born for this! Try to look suspicious, newbie!"

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
    "Elena" "That was much closer. The figure was holding something bulky against their coat and leaning forward."

    $ razzleDayFourBuild = suspectAttributes[killer]["build"]
    $ razzleDayFourBuildHint = RAZZLE_BUILD_SCENE_HINTS[razzleDayFourBuild]
    "Elena" "[razzleDayFourBuildHint]"

    show razzle question at slot(0, total=1), bright zorder 10
    r "Aha! The bundle made the whole silhouette look wider, but the moment it slipped, Elena could finally separate the person from what they carried."
    r "The slope still wrecks the height, but that coat and the way it sat on their shoulders are a real detail."

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "Yes, I believe so. And the lawn slopes upward near the window. That may be why I first thought they were tall."
    "Elena" "I would not trust my first impression of their size, but I do remember the way the coat fit when the bundle moved."

    show razzle hoorah at slot(0, total=1), bright zorder 10

    r "No way, newbie! We actually cracked the case! Well, not really, but you know what I mean!"

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

    r "Anything you remember could help ma'am."

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

            r "Yeah? Then you're officially my good-luck partner."
            r "That means every interview, by the way. I hope you understand the trap you just walked into."

        "Stopping a bad clue is still progress.":
            $ razz += 1

            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "Yeah! We didn't get an answer, but at least we won't chase the wrong one."

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

            r "Yes! Do you know how awkward it is being offered a seat when every chair is flammable?"

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

        "I'd probably worry about my furniture too.":
            $ razz -= 1

            show razzle sad at slot(0, total=1), bright zorder 10

            r "Yeah. Me too. That's part of what makes it suck."

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

    "Razzle has already built a viewing station from two office chairs, an overturned crate, and a bowl of snacks placed at the exact edge of her safe heat radius."

    r "This is gonna take a while. Choose our survival supplies."

    menu:
        "Take the popcorn.":
            $ razz += 1
            "Razzle warms the bowl with both hands. Half the kernels pop at once and leap onto the floor."
            r "The survivors stay in the bowl. The others were too weak."
            "She nudges the fallen kernels into a neat little casualty pile with the toe of her boot."
        "Take the sour candy.":
            $ razz += 1
            "Razzle eats two at once and immediately regrets the decision without admitting it."
            r "Great choice. My face always looks like this. Keep watching the tape."
        "Take the coffee.":
            r "Smart! Pass another cup newbie."

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

    "You and Razzle begin working through the recording. Every half hour, one of you calls a break to stretch, refill the snacks, and note the tape counter in case the VCR decides to eat the evidence."

    "You handle the remote while she compares the passing cars to Elena's description."

    "After what feels like hours, a pair of headlights sweeps across the road."

    r "Wait!"

    "The tape stops."

    "A faint figure is visible near the edge of the picture."

    scene cubicleOutline
    show razzle hoorah at slot(0, total=1), bright zorder 10

    r "That's them! That's actually them!"
    r "That's gotta be them!"

    "Razzle reaches over and rewinds the recording, playing the moment again."

    scene black

    "The figure enters at the bottom of the frame."

    "For a moment, they appear almost as tall as the nearby street sign. As they move toward the center of the image, their outline seems to shrink."

    r "Okay. Either the killer changed size halfway across the street, or this camera angle is complete garbage."

    $ razzleDayFiveReaction = suspectAttributes[killer]["kill_reaction"]
    $ razzleDayFiveReactionAction = RAZZLE_REACTION_SCENE_HINTS[razzleDayFiveReaction]["action"]
    $ razzleDayFiveReactionComment = RAZZLE_REACTION_SCENE_HINTS[razzleDayFiveReaction]["razzle"]

    "The figure steps onto the sloped curb beside the grocery store's outer wall."
    "[razzleDayFiveReactionAction]"
    r "[razzleDayFiveReactionComment]"

    "Razzle rewinds and makes you watch it again before either of you trusts the impression."

    "A second later, the headlights pass over them."

    "The figure raises an arm to cover their face."

    r "That's Elena's moment! The headlights, the arm over the face, she remembered it!"

    "Razzle advances the tape one frame at a time."

    "The person's outline stretches and compresses awkwardly as they cross the sloping pavement."

    "Whatever they are carrying against their chest blends directly into their torso, making their build seem hulking and wide whenever they turn toward the lens."

    r "Look at that silhouette!"
    r "When they hunch forward over that bundle, they look wide as a truck..."
    r "...But when they step upright, it completely changes."

    r "That proves our reenactment with Elena was onto something!"
    r "The bundle distorted the outline, but look at the coat when they shift it. That's the same fit Elena described."

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

            r "Yes!"
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

    r "We'll need the same angle and the same distance. You can keep me honest on the order and write the numbers where Elena can't see them."

    r "Then maybe Elena can finally tell us what she saw!"

    "Razzle ejects the tape and sets it carefully on her desk."

    "Before celebrating, she labels the cassette, writes down the relevant counter range, and rewinds a duplicate copy to the same frame. Then she lets the remote drop and stretches until sparks jump from her shoulders."

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

    r "Next time we figure out what Elena saw."

    if razz >= RAZZLE_HIGH_THRESHOLD:
        show razzle flirty at slot(0, total=1), bright zorder 10

        r "And after that, maybe you and I can spend some time investigating something that isn't murder."

        r "Preferably somewhere with drinks."

        r "And fewer cameras."

    else:
        show razzle hoorah at slot(0, total=1), bright zorder 10
        r "You better come with me next time, newbie."
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

    r "We're putting each wig where the killer stood and recreating the headlights. Then we see which one matches what she remembers."
    r "I worked out the positions from the tape. You helped make the controls boring enough to trust: covered samples, numbers, and a different order every time."

    menu:
        "We should change the order between tests.":
            $ razz += 2

            show razzle hoorah at slot(0, total=1), bright zorder 10

            r "Exactly! I know where everything has to stand; you keep shuffling the order so neither of us accidentally feeds Elena an answer."
            r "Look at us doing real science without making it miserable!"
            r "Suck it Madeline!!"

        "We should remind Elena about the security tape.":
            $ razz -= 1

            show razzle question at slot(0, total=1), bright zorder 10

            r "Better not. We don't want the tape putting an answer in her head."

        "Let's see what she remembers.":
            $ razz += 1

            r "That's the whole plan. We set it up, shut up, and let her tell us."

    "You help cover the wigs before moving them so neither Elena nor a curious passerby can see which color receives which number. Razzle checks the tape marks, batteries, and borrowed-car paperwork one more time."

    menu:
        "Carry the mannequin heads.":
            $ razz += 1
            r "Please do. The cab driver already thinks I'm opening a cursed salon."
        "Carry the lighting equipment.":
            r "Careful with that one! It's the only lamp Madeline would lend me."
        "Carry the numbered covers.":
            $ razz += 1
            r "Keep them mixed up. If I can guess the color from the order, Elena might too."

    scene black with fade

    "The borrowed car is already waiting downstairs, its seats and door panels covered in one of Madeline's flame-resistant transport blankets. During the drive, Razzle keeps the mannequin heads facing away from the windows so passing drivers will stop staring."
    "You and Razzle return to Elena's house and arrange the three covered mannequin heads outside."

    "Razzle parks the borrowed car where the vehicle appeared on the security tape."

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

    r "We got it! We actually got it!"

    r "That means anyone without [razzleDaySixHair] hair comes off the suspect list."

    r "That's huge, Elena!"

    show razzle at slot(0, total=1), dim zorder 0
    "Elena" "Then I am glad my memory was useful after all."

    show razzle at slot(0, total=1), bright zorder 10

    r "It wasn't just useful."
    r "You may have helped us catch the killer!"

    "Elena smiles as Razzle begins carefully gathering the equipment."

    "Razzle gives Elena time to ask what happens next, explains that the identification narrows the list rather than naming a killer by itself, and writes down her exact certainty in Elena's own words."
    "Only after Elena approves the statement do you cover the samples and remove the tape marks from the lawn."

    scene black with fade

    "Returning the borrowed car takes longer than expected because Razzle insists on checking that no spark marked the upholstery. The wig-shop clerk counts all three mannequin heads twice."
    "With the equipment finally returned and the statement secured, you and Razzle walk back toward ATLAS as the afternoon traffic gathers around you."

    if razzle_day_two_detour == "market":
        "The route takes you past the outdoor market from your day off. Razzle checks the stall where she bought her sunglasses and is delighted to find an even worse pair."
    elif razzle_day_two_detour == "park":
        "At the edge of the park, Razzle checks the trees for the squirrels she accused of fleeing questioning. Neither appears willing to reopen the case."
    elif razzle_day_two_detour == "wandering":
        "Razzle points out the store that displayed the terrible hats. The worst one has sold, which she treats as evidence that the city is healing."

    show razzle hoorah at slot(0, total=1), bright zorder 10

    r "Six visits, three witnesses, one terrible videotape, and absolutely no houses burned down!"

    r "I think that makes us a pretty damn good team."

    if razzle_day_two_pizza == "spicy":
        r "After the report, we're celebrating with that dangerous pizza again. My half can be hotter this time."
    elif razzle_day_two_pizza == "split":
        r "After the report, we should get another pizza."
    elif razzle_day_two_pizza == "pepperoni":
        r "After the report, pepperoni and extra cheese. This time I'm reheating it before we leave the restaurant."

    menu:
        "You did some great detective work.":
            $ razz += 2

            show razzle flirty at slot(0, total=1), bright zorder 10

            r "Oh, hell yeah. Say it again so I can pretend I wasn't waiting all day to hear it."
            r "Keep this up and you'll never get rid of me."

        "We make a good team.":
            $ razz += 1

            show razzle hoorah at slot(0, total=1), bright zorder 10
            r "Hell yeah we do!"

            r "You handle the thinking, I handle the fire!"

        "Elena did most of the work.":
            $ razz -= 1

            show razzle sad at slot(0, total=1), bright zorder 10

            r "She gave us the answer, yeah."

            r "But we still had to help her find it."

    if razz >= RAZZLE_DATE_ACCEPT_THRESHOLD:
        show razzle flirty at slot(0, total=1), bright zorder 10

        r "So... once we finish accusing people of murder, I'm holding you to helping me celebrate."

        r "Drinks, dancing, and somewhere fireproof."

        r "Think you can survive that, partner?"

        menu:
            "I can handle the heat.":
                $ razz += 2

                show razzle hoorah at slot(0, total=1), bright zorder 10

                r "Yes! That's the answer I wanted!"

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
    scene cubicleOutline
    "You find Dhampir leaning back in his chair with Enrico Edge's case file open across his lap."
    "A half-finished mug sits on the desk beside him. Whatever was mixed into it has left a thin red line around the rim."

    d "Sup, new blood."
    d "I was reading the whole thing again. Pretty fucked up way to die, man."

    "He folds the file shut and gets to his feet."

    d "We're probably gonna be heading to Enrico's house in a minute."
    d "Cops have one shoeprint they think belongs to a suspect, plus, like, nine theories about everything else."

    menu:
        "Let's start with what the room can actually prove.":
            $ dhamp += 2
            d "Hell yeah. Facts first, dramatic accusations after lunch, preferably some pizza if that's cool."
        "Lead the way. I'll keep up.":
            $ dhamp += 1
            d "Then watch your feet, new blood. Evidence loves sitting exactly where people wanna step."
            d "Also dog shit, but I think that's unrelated"
        "Try not to contaminate anything when you phase through it.":
            $ dhamp -= 1
            d "Ghost walk doesn't leave prints, fibers, or skin cells."
            d "Your shoes do, though. So maybe worry about those."

    d "Gimme a second. Work clothes."

    "Dhampir steps behind the cubicle divider."
    "When he emerges, the Hawaiian shirt and pastel cargo shorts are gone. In their place is a Victorian suit of black and red, complete with a long coat and scarlet jewelry."
    "Beyond the outfit, Dhampir seems different in every way."
    "Even his posture has changed. His shoulders square, his expression empties, and when he speaks again, the lazy drawl is gone, replaced by a gravelly voice."

    d "Stay close. Touch nothing unless I tell you to, new blood."

    menu:
        "You clean up terrifyingly well.":
            $ dhamp += 2
            "One corner of his mouth almost moves."
            d "Focus, we have things to do"
        "The voice is a little much.":
            $ dhamp -= 1
            d "It's just how I talk. Plus, it scares criminals a bit more."
        "This is an improvement.":
            $ dhamp += 1
            d "The shirt was custom, but the suit is also nice."
    d "Come on. We need to go."

    "He gathers gloves, evidence flags, and a battered camera from three different desk drawers. The process is unhurried, but he checks every battery and seal twice."

    menu:
        "Carry the scene kit.":
            $ dhamp += 1
            d "Appreciate it. Thing weighs more than it looks."
            "He hands it over carefully, keeping the case file for himself."
        "Ask what you should look for first.":
            $ dhamp += 1
            d "Stuff people decided was boring. Order of movement, things put back wrong, marks that don't match the story."
        "Ask if the officers know he's coming.":
            d "Yeah. That's why at least one of 'em is stress-eating in the driveway right now."

    scene black with fade
    "Outside, Dhampir chooses to walk instead of fly. The case file stays tucked under one arm while he points out a bakery he likes, a pawn shop he distrusts, and an alley where he once chased a man through three walls."
    "By the time Enrico's street comes into view, the casual commentary is gone. His shoulders square again before either of you reaches the police tape."
    "The two of you arrive at the crime scene."
    "Enrico Edge's house remains sealed behind police tape. The body has been removed, but dark stains, numbered evidence markers, and the outline of a violent struggle remain."
    "Two officers recognize Dhampir and exchange the exhausted look of people who have already completed (and are anticipating more) paperwork about him."

    "Officer" "Please don't kill anyone if you see them in there. We've had enough paperwork as it is."
    d "Wasn't planning on it."

    "Officer" "That is NOT as reassuring as you think it is."

    "Dhampir waits until the officers step outside before looking around the room."

    d "They really seem to like me."

    "He does not begin immediately. First he walks the room's perimeter, reading every evidence marker without crossing it. Then he gives you a pair of gloves and waits until they are fitted properly."

    d "Pick a starting point. We end up checking all of it either way."

    menu:
        "The blood pattern near the body outline.":
            $ dhamp += 1
            d "Start with the victim. Keeps the rest of the room from turning into an abstract puzzle."
            "He crouches beside the nearest marker and follows the documented stains outward."
        "The damaged furniture.":
            d "That works."
            "He studies the overturned chair and the scrape it left across the floor."
        "The photographs in the scene report.":
            $ dhamp += 1
            d "Before and after. Smart place to catch what responders changed without realizing it."
            "He spreads the photographs on a clean section of the floor and reconstructs their angles."

    $ dhampir_day_one_cause = DHAMPIR_MURDER_CAUSES[killer]

    "He studies the blood pattern, the damaged furniture, and a series of photographs left with the scene report."
    "Piece by piece, the room gives up a consistent sequence. Enrico died from [dhampir_day_one_cause]."

    d "Whatever power the killer had, that isn't what tells us who did it."
    d "People lean on the flashy part and miss the boring stuff. Boring stuff solves murders."

    "He points toward a partial bloody shoeprint beside the hall."

    d "That's the print the police tied to one of our suspects. What do you think we should do?"

    menu:
        "Check when the blood reached that part of the floor.":
            $ dhamp += 2
            d "That's the question. A print without proper timing could be anyone."
        "Compare it to every suspect's shoes immediately.":
            $ dhamp += 1
            d "We'll do that eventually. First we make sure it even belongs to the attack."
        "Step beside it to compare sizes.":
            $ dhamp -= 2
            d "Yeah, new blood? Wanting to see if the shoe fits?"
            d "Serious scene. Use your head."

    "The blood beneath the print looks like it had already begun drying when the tread pressed into it. A timestamped hallway photograph shows the mark was absent immediately after the murder."
    "Dhampir checks the responding personnel list, then taps one name with a gloved finger."

    d "Paramedic. Same tread. Somebody built a suspect theory on a first responder walking through old blood."

    $ dhampir_day_one_reveal = get_planned_route_reveal("dhampir", 1)
    $ dhampir_day_one_cleared_id = dhampir_day_one_reveal["eliminated"][0]
    $ dhampir_day_one_cleared_name = suspectNames[dhampir_day_one_cleared_id]
    $ dhampir_day_one_clue = "The bloody shoeprint linked to {} was made by a paramedic after the murder.".format(dhampir_day_one_cleared_name)
    $ record_planned_route_reveal(
        "dhampir", 1, clue_text=dhampir_day_one_clue, expected_count=1)

    d "That clears [dhampir_day_one_cleared_name]. [len(remainingSuspects)] left."
    d "Not bad, right?"

    menu:
        "You look like a haunted tablecloth.":
            $ dhamp += 2
            d "See, that's why I bring you. Constructive criticism."
        "You really know what you're doing.":
            $ dhamp += 1
            d "I read the briefing. Apparently that's a rare superpower around here."
        "The police would probably like you more without the jokes.":
            $ dhamp -= 1
            d "They'd like me more if I stopped killing criminals."

    d "We're done here. I'll write the report before Nicky gets onto me about it."

    "He stays long enough to return every photograph to its sleeve and walks the perimeter one final time. Outside, the waiting officer looks visibly relieved when Dhampir hands over an intact scene log and no bodies have been added to it."

    "The suit's posture lasts until the house is half a block behind you. Then Dhampir loosens his collar and lets out a long breath."
    d "Okay. Now pizza. Dramatic accusations can wait."

    scene black with fade
    "The nearest pizza counter has metal stools and a cashier who does not react to Dhampir's Victorian murder suit. He orders two slices and produces a sealed blood packet for his own."

    menu:
        "Ask about the custom Hawaiian shirt while you eat.":
            $ dhamp += 1
            d "Local tailor. She does great work. All local material and eco-friendly too."
        "Ask whether solving murders always makes him hungry.":
            $ dhamp += 1
            d "Everything makes me hungry. Murder scenes just make pizza feel more respectful than sandwiches."
            d "Bloody crime scenes remind me I haven't had any blood today, so here we are."
        "Eat in comfortable silence.":
            "Dhampir seems perfectly happy not to fill it. He raises his slice toward you once in a toasting motion before taking another bite."

    "The case remains closed on the seat between you. For ten minutes, neither of you treats the day like anything except two coworkers eating late lunch."

    "Afterwards, you begin to walk back to the office to provide a report."

    $ dayDham += 1
    jump endOfDay

label DhampirDayTwo:
    scene cubicleOutline
    "Dhampir is waiting at his desk with the entertainment section of the newspaper folded into a sharp little square."

    d "Cancel your plans. Cancel everything you can think of."

    "You stare at him."

    d "They're showing Blood Moon IV tonight."
    d "I have been waiting three whole years to see how badly they fuck this up."
    if dayWin >= 6:
        d "Yeah, accusation's tomorrow. Evidence requests are already filed, and staring at the fax won't make it answer faster."
    elif dayWin >= 5:
        d "Yeah, the accusation's getting close. Evidence requests are already filed, and staring at the fax won't make it answer faster."

    menu:
        "Sounds important. I'm in.":
            $ dhamp += 2
            d "Knew you had your priorities straight, new blood."
        "Is this how you ask people out?":
            $ dhamp += 1
            d "Could be, haven't thought of it like that before."
            d "Wasn't really this time though, sorry to burst a bubble."
        "I thought we were supposed to investigate today.":
            $ dhamp -= 1
            d "We worked the case last time. Murder'll still be there after the paperwork catches up. Apparently that's how evidence works."

    d "Showing's pretty late tonight, but we need to prep. Snacks first."
    d "Wait, guess I gotta catch you up on the other movies first that way you get this one."
    d "So, basically-"
    "Dhampir drags a second chair beside his desk and begins drawing the Blood Moon family tree across the back of an outdated case memo. Ten minutes in, it has become a maze of arrows, betrayals, resurrections, and one character labeled MAYBE JUST A BAT."

    d "Before I ruin the next three hours for you, what do you actually wanna know?"

    menu:
        "Ask why he loves the movies if they're so bad.":
            $ dhamp += 1
            d "Because everybody involved committed completely. Bad idea, great cape, no shame. That's art dude."
        "Ask which vampire would survive meeting him.":
            $ dhamp += 1
            d "The grandma from the second one. She had survival instincts and a shotgun. Everybody else is fucked for sure."
        "Ask for only the facts needed to understand part four.":
            d "Sure."
            "He looks at the sprawling family tree."
            d "Unfortunately, all of this is essential."

    "The recap expands through lunch. Dhampir happily answers every question, performs several lines in the wrong accents, and pauses twice to correct his own diagram when he remembers an additional secret twin."

    scene black with fade
    "By the time the day is coming to an end, you understand enough of the series to recognize at least four kinds of continuity error."
    "The two of you stop at a convenience store as the sun begins to set. Dhampir buys popcorn, some candy, and a small plastic cup with a lid."

    d "Your turn. What're you getting new blood?"

    menu:
        "Popcorn with too much butter.":
            $ dhamp += 1
            $ dhampir_movie_snack = "popcorn"
            d "Classic. Dangerous to the shirt, safe for the soul."
        "The largest box of candy available.":
            $ dhamp += 1
            $ dhampir_movie_snack = "candy"
            d "We're gonna be vibrating through the third act. Respect."
        "Nothing. I came for the movie.":
            $ dhamp -= 1
            $ dhampir_movie_snack = "nothing"
            d "That's lame, new blood. Grab a drink at least. Hydration doesn't make you less mysterious."

    "He pays before you can separate your snacks from his and tucks the receipt into the movie ad from his desk."
    "On the walk to the theater, he pauses beside a park hedge. You see him turn and squat near the hedge. There is a rustle, one very brief motion, and then silence."
    "He turns back with a small vial of blood and drops it into the shopping bag."

    d "Popcorn seasoning."

    menu:
        "Locally sourced.":
            $ dhamp += 2
            d "Organic, too."
        "Was that a squirrel?":
            $ dhamp += 1
            d "It was a donor. Its sacrifice will be treasured."
        "That is going to take me a minute to process.":
            $ dhamp -= 1
            d "Take the minute, it's a bit to take in you're not used to it. Everything I eat needs blood in it, so I had to get practical eventually."

    "The theater lobby is crowded with people wearing plastic fangs and cheap black capes. Dhampir studies them with the solemn patience of a museum curator confronting several obvious forgeries."
    "You find seats near the back while trailers play. He mixes the vial into his popcorn a few drops at a time, shakes the bag, and offers it to you before remembering why that will not help."

    "Blood Moon IV is exactly the kind of movie its title promises. Fog covers every exterior shot. The vampire lives in a castle, sleeps upside down, and hisses at a plate of garlic bread."
    "Dhampir pours a little more blood over his popcorn and begins providing corrections under his breath."

    d "Can't do that."
    d "Definitely can't do that."
    d "Okay, that one would actually work."

    "On-screen, the vampire transforms into twelve bats and flies through a stained-glass window."

    d "Why twelve? One bat is already suuuuuper inconvenient. That's so much to coordinate at once."

    "The vampire returns to his enormous castle and broods in front of a mirror that refuses to show his reflection."

    d "Mirrors work fine. Garlic's fine. Sunlight's fine."
    d "Castle's pretty sick, though I can't think of why they alwasy have a castle."
    "Dhampir pauses"
    d "I want a castle."

    menu:
        "Please keep explaining what's wrong, this is interesting.":
            $ dhamp += 2
            d "You've made a terrible choice. I have notes going back three movies."
            "His commentary becomes just loud enough for the two rows in front of you to hear every word."
        "I think that vampire is cooler than you.":
            $ dhamp += 1
            d "You take that back new blood."
            "He steals a handful of your popcorn in retaliation."
        "Please stop talking during the movie.":
            $ dhamp -= 1
            d "No. My culture ain't your costume dude."

    "A man two seats ahead finally turns around."

    "Moviegoer" "Hey man, could you keep it down?"

    d "Yeah, man. Sorry about that."

    "Dhampir waits until the man turns around again."

    d "Still want a castle."

    "The credits roll over an original song that rhymes 'eternity' with 'burning me' four separate times. Dhampir remains seated through all of it, just in case the filmmakers hid one last bad decision after the names."

    scene black with fade
    "Outside, the crowd breaks into smaller groups arguing about the ending. Dhampir waits until the lobby empties, throws away the snack wrappers, then leads you around the side of the theater and looks up toward the roof."

    d "Roof's got a better view than the parking lot."
    d "You cool with flying, or are we using the stairs?"

    menu:
        "Fly me up.":
            $ dhamp += 1
            "Dhampir asks you to hold on, then lifts both of you onto the theater roof as easily as stepping onto a curb."
        "I'm afraid of heights.":
            d "Fair. Stairs it is."
            "He walks with you to the roof access door."
        "Only if you promise not to drop me.":
            $ dhamp += 1
            d "Winston's the one who can make me drop out of the sky. He's not here."
            "He waits for you to take hold before carrying you up."

    "The city glows beneath you. Dhampir sits on the ledge with his feet hanging over the street."

    "A couple leaving the theater spot his fangs beneath the rooftop lights. Their conversation dies when they realize they're real and recognize Dhampir. It stops until they reach the far end of the block."
    "Dhampir watches them go, more amused than offended."

    d "There it is. The look."
    d "People usually decide what I am before I say anything just because of my record."
    d "Red eyes, fangs, ghost walk, gun. Makes sense."
    d "Then I start talking and they realize I'm different from whatever they made up."
    d "They always seem... disappointed."

    menu:
        "I wasn't disappointed.":
            $ dhamp += 2
            d "Damn. That's almost smooth, new blood."
            d "Keep it up and I might start thinking you enjoy this haunted-tablecloth thing."
        "You're definitely weird.":
            $ dhamp += 1
            d "See? You get me."
        "Some people panic before they think.":
            $ dhamp -= 1
            d "Sure. Still rude when they never get around to the thinking part."

    "The couple turns the corner. Dhampir keeps watching the empty sidewalk, not wounded by the reaction so much as accustomed to cataloging it."

    "He does not explain where he learned to stop caring about the look. He only tips his head toward the muffled music leaking through the theater roof."

    d "Anyway, Blood Moon II had a better soundtrack."

    "For a while, neither of you says anything. Traffic moves below in ribbons of white and red, and somewhere behind the theater an employee drags a bag of trash across the pavement. Dhampir taps the heel of one boot against the wall in time with music only he remembers."

    if dhamp >= DHAMPIR_WARM_THRESHOLD:
        d "Tonight didn't suck, new blood."
        d "There's another terrible movie next month we should go too."
        d "Ready to head back? I wanna complain about the ending while it's fresh."
    else:
        d "Ready to head back? I wanna complain about the ending while it's fresh."

    d "Try not to look down. I'll fly you over to Ulysses for your report."
    d "He knows my methods, just say you're with me and he'll probably cut you some slack."

    $ dayDham += 1
    jump endOfDay

label DhampirDayThree:
    scene cubicleOutline
    "Dhampir is already in his Victorian hero suit when you arrive. Madeline stands beside him with a hard metal case full of scanning equipment."

    show madeline at slot(0, total=1), bright zorder 10

    m "The police photographed the scene thoroughly, but they measured it like an ordinary assault."
    m "Their model does not account for phasing, flight, supernatural strength, or a victim being attacked from a physically inconvenient angle."

    d "She's trying to say they did it wrong."

    m "I mean they did it incompletely."

    d "That's the polite science version of saying wrong."

    "Madeline lifts the scanner case."

    m "This will project the original photographs over the room and isolate contact marks the first team dismissed."

    m "Dhampir will recreate the possible movement paths. You will identify inconsistencies."

    menu:
        "Tell me what counts as an inconsistency.":
            $ dhamp += 2
            d "That's worth asking before we turn the room into a light show."
            m "Anything that could not have resulted from the movement currently being projected. You get it now?"
        "Does the suit always make your voice do that?":
            $ dhamp += 1
            d "Yes."
            m "His vocal register drops approximately eleven percent. I measured it."
            d "You measured my voice?"
            m "I measure everything Dhampir."
            m "Everything."
        "I'll just start touching things until something happens.":
            $ dhamp -= 2
            d "No."
            m "Absolutely not."

    "Madeline makes you inventory the scanner case before anyone leaves. Dhampir carries the main unit while she watches him like he personally offended several pieces of precision equipment."
    "The drive is mostly occupied by Madeline explaining calibration and Dhampir translating each explanation into increasingly inaccurate metaphors."

    scene black with fade

    "Back at Enrico's house, the three of you wait while an officer unlocks the seal and records your entry. Dhampir's casual expression disappears the moment the door opens."
    "Madeline gives you the room's anchor markers one at a time. Once every projector is placed and checked, her scanner washes the room in pale geometric light. Old blood patterns, displaced furniture, and the victim's documented wounds appear as translucent overlays."

    show madeline at slot(0, total=1), bright zorder 10

    m "Projection stable. Begin with the first proposed path."

    "Dhampir rises several inches from the floor. His entire demeanor goes still."

    d "Attacker enters from the hall. Enrico turns. First contact happens here."

    "He phases through the edge of a table, stops beside the projected outline, and traces the attack without disturbing a single object."

    m "Second path."

    "Dhampir repeats the sequence from the window, then from behind the victim. Each version causes different marks on Madeline's display to brighten or disappear."

    $ dhampir_day_three_reveal = get_planned_route_reveal("dhampir", 3)
    $ dhampir_day_three_excluded_injuries = dhampir_day_three_reveal["value"]
    $ dhampir_day_three_explanation = DHAMPIR_INJURY_EXCLUSION_TEXT[dhampir_day_three_excluded_injuries]

    call RulesDhampirISpy
    $ start_dhampir_ispy_minigame(dhampir_day_three_excluded_injuries)

    if dhampir_ispy_result["completed"]:
        if dhampir_ispy_result["quality"] == "perfect":
            m "All three discrepancies. No false positives and no calibration assistance."
            d "That's what we needed, new blood. Good job."
        elif dhampir_ispy_result["quality"] == "careful":
            m "A few false positives, but you isolated all three useful discrepancies."
            d "Found what mattered. Good shit dude."
        else:
            m "Your search pattern was chaotic, but technically successful."
            d "Got there eventually and that's what matters right?"
    else:
        "Madeline takes over the scanner and methodically checks the remaining contact points."
        m "Observe what I am isolating. You will be expected to recognize it next time."

    $ dhampir_day_three_removed_names = " and ".join([suspectNames[suspect_id] for suspect_id in dhampir_day_three_reveal["eliminated"]])
    if dhampir_day_three_reveal.get("scope") == "category":
        "Madeline combines the isolated points. [dhampir_day_three_explanation]"
        m "The result is internally consistent across all usable photographs."
        d "Meaning we can cross off everyone in that group."
        $ dhampir_day_three_clue = "Madeline's scan and the scene reconstruction rule out suspects with {}.".format(dhampir_day_three_excluded_injuries.lower())
    else:
        "Madeline combines the isolated points, then compares each contradiction against the remaining medical and intake records."
        m "The scene conflicts independently with the documented profiles for [dhampir_day_three_removed_names]."
        d "Different reasons, same result. Those two didn't make these wounds."
        $ dhampir_day_three_clue = "The reconstruction clears the individual wound profiles for {}.".format(dhampir_day_three_removed_names)
    $ record_planned_route_reveal(
        "dhampir", 3, clue_text=dhampir_day_three_clue, expected_count=2)

    menu:
        "Nice work, both of you.":
            $ dhamp += 1
            d "Team effort. Madeline brought the expensive flashlight."
            m "It is a multiarrayed overlaying forensic scanner."
            d "Very expensive flashlight."
        "Dhampir makes reconstruction look good.":
            $ dhamp += 2
            m "Flirting already? God, this makes you look desperate."
            d "They're just being friendly, Madeline. No need to bully them for it."
        "That took longer than it should have.":
            $ dhamp -= 1
            m "You are welcome to process several hundred spatial measurements manually next time."
            d "She's rocking with us, new blood. Don't ruin it."

    "Madeline begins packing the scanner with the precision of someone who knows exactly where every cable belongs."

    m "The remaining wound evidence still supports more than one possible attacker. Do not overstate this result."
    d "Wasn't planning to. We know what didn't happen. That's enough for today."

    "Madeline glances between you and Dhampir."

    m "Your heart rate increased during precisely one of his reconstructions."

    d "Science says I'm hot."

    m "Science said no such thing."

    d "Agree to disagree."

    "Madeline makes both of you help coil cables before she permits anyone to leave. Dhampir holds one end of each cord perfectly still and continues claiming the scanner is an expensive flashlight until she threatens to demonstrate its weight against his skull."

    hide madeline

    "Outside the sealed house, Madeline leaves with the scanner and a warning about recalibrating it without her. Dhampir walks with you to a corner store before changing out of the suit."
    "He buys a canned coffee, adds a measured drop from one of his own vials, and leans against the brick wall while traffic passes."

    d "Three people staring at glowing murder geometry is a lot. You doing okay?"

    menu:
        "Admit the scene was unsettling.":
            $ dhamp += 1
            d "Makes sense. At lest you made it through. Hopefully we won't have to do it again."
        "Say the reconstruction was fascinating.":
            $ dhamp += 1
            d "Yeah. Weird room, good scanner, solid company. Could've been worse."
            d "All we needed was som beers and it would be a proper hangout."
        "Ask whether the coffee is any good with blood.":
            d "No. But it was bad coffee before the blood, so nothing important was lost."

    if dhamp >= DHAMPIR_WARM_THRESHOLD:
        d "You did good in there, new blood. Didn't rush, didn't disrespect the scene."
        d "Come back next time. There's something about the room after the killing that I wanna check."
    else:
        d "We still have [len(remainingSuspects)] names. Come back next time ready to crack this thing. Hopefully."

    $ dayDham += 1
    jump endOfDay

label DhampirDayFour:
    scene cubicleOutline
    "Dhampir has traded the hero suit for his Hawaiian shirt again. He has arranged photographs of Enrico's house across an otherwise empty desk."

    d "Last time told us how the fight worked. Now I wanna know what happened after."
    d "People get weird after they kill somebody."

    menu:
        "You say that like you're reviewing restaurant habits.":
            $ dhamp += 2
            d "Restaurants have more health-code violations for the most part."
            d "Except that place off Anderson, they're actually pretty rad."
        "Does killing someone really not bother you?":
            $ dhamp += 1
            d "Not if they needed killing. Enrico didn't."
        "You could show the victim a little respect.":
            $ dhamp -= 2
            d "I am. I'm doing the work right and I'm not turning his death into a performance."

    "Dhampir sorts the photographs into three stacks: before the attack, during the struggle, and after the fatal injury. He taps the last stack."
    d "We only need these today. Less noise."

    menu:
        "Take the photographs and preserve their order.":
            $ dhamp += 1
            d "Thanks. Keep 'em flat. Scene photos get real unhelpful when somebody folds the murder in half apparently."
        "Ask why he needs to return to the room.":
            $ dhamp += 1
            d "Scale. A footprint looks different when you're standing where the person stood."
        "Ask whether he will wear the suit.":
            d "Not today. I'm looking at what somebody did after the danger passed. Cape changes the mood."

    "He signs the evidence checkout sheet, waits while you place the photographs in a rigid sleeve, and walks out beside you instead of hurrying ahead."

    scene black with fade
    "The route to Enrico's house has already become familiar. Dhampir talks until the police tape appears, then falls quiet halfway through a joke and does not finish it."
    "Inside, you reopen the room one photograph at a time. Dhampir waits for each angle to be placed before moving to the next mark."
    "Dhampir reconstructs only the minute after the fatal injury. He follows the numbered photographs in silence, moving from one contact point to the next."

    $ dhampir_day_four_reaction = suspectAttributes[killer]["kill_reaction"]
    $ dhampir_day_four_hint = DHAMPIR_REACTION_SCENE_HINTS[dhampir_day_four_reaction]

    "[dhampir_day_four_hint]"

    "Dhampir repeats the sequence twice. The second time, he moves at the pace suggested by the spacing of the prints rather than the pace the police report assumed."

    d "There. That's the person we're looking for after it was over."

    "He crouches beside a blood-marked cabinet and studies the photographs again."

    "As you see him walk through the scene with relative comfort, you wonder what a man like him has seen to regard it so casually."
    d "Death doesn't make me uncomfortable, if that's what you're wanting to ask."

    menu:
        "You care. You just don't perform it.":
            $ dhamp += 2
            d "Pretty much. Enrico doesn't need me to look sad. He needs me to get this right."
        "I can respect it without sharing it.":
            $ dhamp += 1
            d "That's all I ask."
        "So Enrico is just another body to you?":
            $ dhamp -= 2
            d "No. Doing serious work is how I respect him. Making a show of being upset wouldn't help anybody."

    "Dhampir returns to the photographs. The way he reads the room is practiced rather than detached: every pause happens at the right mark, every movement avoids the space where Enrico fell."
    "You ask who taught him to work a death scene with that much control. His fingers move to the scarlet trinkets at his neck before he answers."

    d "First people who really got me were the Monster Hunters. Bunch of vigilantes who trained together."
    d "They were good at the work. Good to me, too."

    "His tone stays casual, but one hand briefly touches the scarlet trinkets at his neck again."

    d "Most of them died. I killed the people responsible. Efficiently."

    "The word sits in the empty room longer than the joke-shaped tone he put around it. Dhampir lets the trinkets fall back against his shirt before looking at you."

    menu:
        "Efficiently. That's the important part.":
            $ dhamp += 1
            d "See? You understand me."
        "I'm sorry you lost them.":
            $ dhamp += 2
            d "Thanks. It was a long time ago. Still counts, I guess."
        "That is a horrifying response to grief.":
            $ dhamp -= 2
            d "Wasn't grief. It was a solution."

    if dhamp >= DHAMPIR_WARM_THRESHOLD:
        "Dhampir rolls one of the scarlet trinkets between two fingers, considering how much more to give you."
        d "Before them, my family had a very specific idea of what I was supposed to be. Beauty, nature, elegant elf shit."
        d "Then they got me. Fangs, gun, bad attitude. Took underground shows and the Hunters before I found rooms where nobody looked disappointed."
        "He says it without asking for sympathy. The fact that he says it at all feels deliberate."

    "Dhampir lifts the original evidence inventory and compares it to the room one last time."

    d "Huh."

    "One numbered marker in an early photograph has no matching item in the evidence log. Whatever had been there was small enough to miss and violent enough to be torn loose."

    d "Something from the attacker got left in this room."
    d "Police never found it. Next time we figure out where it landed."
    "He photographs the empty marker from two angles, then helps you compare every numbered item against the log. Nothing else is missing."
    d "For now, you gotta get back to Ulysses and report what we did. I'll reseal the room."
    d "See ya next time, new blood."

    $ dayDham += 1
    jump endOfDay

label DhampirDayFive:
    scene cubicleOutline
    "Dhampir's chair is empty when you reach his desk, but the crime-scene photographs are gone and a handwritten note has been pinned to his monitor with a red thumbtack: TRAINING ROOM. BRING WATER."
    "The sound of something heavy striking padding guides you down the hall. When you arrive, Dhampir is resetting a practice dummy that has folded nearly in half."
    "Dhampir has cleared a section of the ATLAS training area and dragged in a padded practice dummy, three replica weapons, and a stack of crime-scene photographs."

    d "We're testing force, angle, and reach."
    d "You get to hit me. Educationally of course."

    menu:
        "Show me the technique first.":
            $ dhamp += 2
            d "Watch my feet first. Arms lie about where the force came from."
        "You just wanted an excuse to get close.":
            $ dhamp += 1
            d "Maybe. But I don't think a fight is the best way to get close."
        "We know how Enrico died. Why reenact it?":
            $ dhamp -= 1
            d "Knowing the weapon isn't the same as knowing the body or the technique."
            d "This is how we find the part the weapon can't tell us."

    "He positions your feet, adjusts your shoulders, and demonstrates how the same injury can come from very different bodies."
    "A heavy strike dents the dummy. A narrow weapon reaches the same depth with leverage. A phased approach creates an angle that should be impossible from the floor."

    d "Ordinary forensics assumes ordinary movement. We don't get that luxury."

    "He lays the three replicas on the mat: a weighted baton, a narrow practice blade, and an unbalanced length of wood standing in for an improvised weapon."
    d "Pick one to test first. Doesn't change the wound we're recreating. Changes what your body has to do to make it."

    menu:
        "Take the weighted baton.":
            "The weight drags your shoulder forward. Dhampir braces your elbow before it can pull you off balance."
            d "Feel that? Strong weapon can still make a weak angle if the person can't control the follow-through."
        "Take the practice blade.":
            $ dhamp += 1
            "The blade is light enough to move quickly, but Dhampir stops you until your wrist aligns with the marked angle."
            d "Precision gets mistaken for strength all the time. Don't confuse clean movement with easy movement."
        "Take the improvised weapon.":
            $ dhamp += 1
            "The awkward grip forces you to adjust twice. Dhampir nods toward the way your hips compensate."
            d "Ugly tools tell on the body using them. That's useful."

    "Dhampir gestures for you to try the sequence. Each time you commit to an attack, he phases just enough for it to pass harmlessly through him."

    menu:
        "Wait for him to become solid before moving.":
            $ dhamp += 2
            "You hold position until his outline sharpens, then stop your hand just before contact."
            d "There you go. Patient and mean. Great combination dude."
        "Use the close position to lean against him.":
            $ dhamp += 2
            "Dhampir becomes solid just long enough to support your weight."
            d "Creative technique. Not sure Madeline's scanner accounted for this one."
        "Keep swinging as fast as possible.":
            $ dhamp -= 1
            "Every strike passes through him."
            d "Speed isn't a substitute for paying attention, dude. Try again."

    $ dhampir_day_five_build = suspectAttributes[killer]["build"]
    $ dhampir_day_five_hint = DHAMPIR_BUILD_SCENE_HINTS[dhampir_day_five_build]

    "He returns to the dummy and recreates the decisive movement from Enrico's house. [dhampir_day_five_hint]"

    d "That's the body that made those marks."

    "Dhampir has you repeat the movement. He corrects your balance before you can feel yourself losing it, then resets the dummy with the ease of a routine performed thousands of times."
    "You ask where he learned to do all of this."

    d "Didn't start at ATLAS. Manison trained me first."
    d "After that, the Monster Hunters ran drills like this every night. Stealth, weapons, getting hit until we learned not to."

    "He picks up the photographs showing the missing evidence marker and aligns them beside the dummy."

    d "The Hunters taught me to end a fight before it spreads. I ignored that lesson once, and somebody else paid for the extra seconds."

    "He says it with the same tone someone else might use to describe taking an evening class."

    d "After that, I stopped treating efficiency like a style choice. Terrible lesson. Great retention."

    menu:
        "At least the training paid off.":
            $ dhamp += 2
            d "Trauma's expensive. Might as well demand in-store credit."
        "You don't have to make that lesson sound funny.":
            $ dhamp += 1
            d "I know."
            d "The real answer is dragging a fight out gets innocent people killed. I finish things fast because I learned what happens when you don't."
        "You make murder sound easy.":
            $ dhamp -= 1
            d "It is easy. Knowing for sure who deserves it is the serious part."

    "Dhampir places one photograph over another and traces a line from the struggle to the far side of the room."

    d "Whatever came loose didn't vanish. It traveled."
    d "Next time I go through the wall, the floor, and anything else the first search couldn't reach."

    "He lowers the damaged dummy, puts the replicas back in their rack, and hands you the water bottle from his note. Only after the room is cleared does he lean against the wall and let the last of the work posture drain away."

    if dhamp >= DHAMPIR_HIGH_THRESHOLD:
        d "You can come watch."
        d "Partly because you're useful. Mostly because you look good trying to hit on me."
    else:
        d "Come ready to work, new blood. Last search is the one that matters."

    $ dayDham += 1
    jump endOfDay

label DhampirDaySix:
    scene cubicleOutline
    "Dhampir waits near the exit in his full hero suit, coat fastened and scarlet trinkets resting against his chest."

    d "Last search."

    d "We recover what was torn from the attacker, preserve it properly, and reduce the list."

    menu:
        "Let's finish this properly.":
            $ dhamp += 2
            d "Then we're not leaving empty-handed."
        "Try not to get stuck in the floor. The paperwork would be awful.":
            $ dhamp += 1
            d "If I'm still stuck by lunch, tell Nicky I'm taking a personal day."
        "Six suspects is probably close enough.":
            $ dhamp -= 2
            d "No."
            d "Enrico deserves an answer, and six people don't deserve to stay suspects because we got lazy."

    "He opens the search kit on a bench and has you check the evidence bags, tamper seals, labels, and camera battery. It is the same calm routine as the first day, except now you know why each piece is there."

    menu:
        "Volunteer to document the search.":
            d "Camera and log are yours. If I disappear for more than a minute, write down where."
        "Volunteer to handle the evidence bag.":
            $ dhamp += 1
            d "Keep it open but don't reach for anything. I become solid before the evidence meets the bag."
        "Ask what happens if he finds nothing.":
            $ dhamp += 1
            d "Then we prove where it isn't and keep looking. Last search doesn't mean last guess."

    scene black with fade
    "The final drive is quiet. Dhampir reviews Madeline's transparent angle overlays against a set of printed scene photographs while you watch familiar blocks pass the window. At the house, two officers record the search plan and unlock the scene one last time."
    "You photograph the intact seal before entering. Dhampir waits inside the doorway until the time, personnel, and conditions are written into the log."
    "The final search begins at the point Dhampir identified during the reconstruction. He measures the angle once, then lets his body turn pale and insubstantial."
    "He passes an arm through the wall, then sinks through the floor up to his shoulders, searching spaces no ordinary investigator could reach."

    d "Nothing in the wall. Moving lower."

    "He vanishes beneath the floorboards. A few seconds later his voice rises faintly through the wood."

    d "Found something."

    "Dhampir rises back through the floor with one gloved hand closed. He becomes solid before opening it over an evidence bag."

    $ dhampir_day_six_drop = suspectAttributes[killer]["unique_drop"]
    $ dhampir_day_six_evidence = DHAMPIR_DROP_EVIDENCE_TEXT[dhampir_day_six_drop]

    "Inside his palm is [dhampir_day_six_evidence]."

    if dhampir_day_six_drop == "Missing Hair":
        $ dhampir_day_six_clue = "Recovered tissue confirms that the attacker left the scene with a patch of hair torn out."
    elif dhampir_day_six_drop == "Missing Tooth":
        $ dhampir_day_six_clue = "A recovered tooth confirms that the attacker lost a tooth during the struggle."
    else:
        $ dhampir_day_six_clue = "Recovered tissue confirms that part of the attacker's ear was torn away during the struggle."

    $ record_planned_route_reveal(
        "dhampir", 6, clue_text=dhampir_day_six_clue, expected_count=3)
    $ dhampir_day_six_remaining_names = ", ".join(
        [suspectNames[suspect_id] for suspect_id in remainingSuspects])

    d "Seal's clean. Chain of custody starts now."

    "You hold the bag while he drops the recovered item inside without letting it touch the rim. The seal closes with a small, final sound. Both of you sign across it before he moves another inch."

    "The physical evidence reduces the investigation to three names: [dhampir_day_six_remaining_names]."

    d "Three left. Official evidence gets us that far."
    d "The rest is up to you, new blood."

    menu:
        "Not bad for a haunted rat.":
            $ dhamp += 2
            "Dhampir's severe expression breaks into a grin as his work voice disappears."
            d "That's {i}professional{/i} haunted rat to you. I have references."
            d "Mainly Ulyesses and Winston, but references all the same."
        "You did incredible work this week.":
            $ dhamp += 1
            d "We did. You spotted the room; I crawled through the floor like a haunted rat."
        "Can't you just ask one of the souls in your necklace?":
            $ dhamp -= 1
            d "They only know what they knew alive. None of them were here."
            d "Also, most of them are assholes. Or squirrels"

    "Dhampir seals the evidence bag and removes one glove with his teeth."

    "The officers take custody only after checking every line. Dhampir watches the bag disappear into a locked case, then finally steps back across the threshold and lets the crime scene close behind you."

    if dhamp >= DHAMPIR_HIGH_THRESHOLD:
        d "You work hard when it matters, you don't get stupid around a body, and your jokes are mostly decent."
        d "That's rare around here."
        if dhampir_movie_snack == "popcorn":
            d "After this case, remind me to find Blood Moon V for us. I'll get the dangerously buttered popcorn."
        elif dhampir_movie_snack == "candy":
            d "After this case, remind me to find Blood Moon V for us. We can vibrate through another third act."
        else:
            d "After this case, remind me to find Blood Moon V for us. I'm still making you get a drink this time."
    elif dhamp >= DHAMPIR_WARM_THRESHOLD:
        d "Not bad for your first week, new blood."
        d "You can come to the next terrible movie too."
    else:
        d "We got the evidence. That's what matters."
        d "Think through the three names before the final meeting."

    $ dayDham += 1
    jump endOfDay

label MadelineDayOne:
    scene labOutline
    "You find Madeline leaning over a glass evidence tray. An open dish of black fingerprint powder sits beside the exposed slides, and a thick black notebook rests at her elbow."
    "Her jacket pockets bulge with tools, loose wire, and folded scraps of calculations."
    "A desk fan turns slowly behind her, pushing the chemical smell around the lab without doing much to clear it. Madeline does not look up when you enter."

    show madeline at slot(0, total=1), bright zorder 10

    m "Stop."

    "Your hand is still several inches from the nearest table."

    m "You stopped before touching anything. Better than Winston. His hand would've been in the powder by now."
    m "I'm testing whether you ask for procedure before you touch anything."

    $ madeline_touched_slide = False

    menu:
        "Then tell me the procedure, genius.":
            $ mads += 2
            show madeline flirty curious at slot(0, total=1), bright zorder 10
            m "Genius is accurate. Asking before contaminating things is promising. Put on gloves, newb."
        "The evidence tray is already inside your contamination boundary.":
            $ mads += 2
            show madeline madScientist at slot(0, total=1), bright zorder 10
            m "Oh, good. You actually looked before opening your mouth."
            m "That's annoyingly rare."
        "Touch the nearest slide anyway.":
            $ mads -= 2
            $ madeline_touched_slide = True
            show madeline distress at slot(0, total=1), bright zorder 10
            m "What the fuck did I just say?"
            "She removes the slide and seals it in a disposal sleeve."

    show madeline at slot(0, total=1), bright zorder 10

    "Madeline pulls the black notebook closer and writes a quick line. She angles it away a second too late."
    "The exposed pages are labeled with the names of ATLAS members. Each is packed with behavioral observations, predicted mistakes, and irritated corrections."
    "She turns to a fresh page and writes NEWB across the top."

    m "Don't look so concerned. Everybody gets a file."
    if madeline_touched_slide:
        m "Yours currently says you hear direct warnings and treat them like optional reading."
    else:
        m "Yours currently says you can follow a direct warning. Congratulations on clearing the floor-level standard."

    m "We're going to Enrico's house. The scene team found one usable print pressed into wet blood on the inside face of a broken window shard."
    m "Victim excluded. Responders wore gloves. Position means it was left during the struggle."

    "She closes the evidence tray, then points to three pieces of equipment without naming any of them."
    m "If you're going to stand there, be useful. What are you carrying?"

    menu:
        "The portable scanner.":
            $ mads += 1
            "You lift the compact scanner and its folded projection screen. Madeline gives the strap one testing tug before letting you keep it."
            m "Don't drop it. I built the calibration assembly myself and I don't want to build it twice."
        "The sealed evidence case.":
            $ mads += 1
            "You take the empty transport case by its reinforced handle. Madeline checks both latches and adds a third seal from her pocket."
            m "It should come back empty. If it doesn't, we found something worth the trip."
        "Her notebook.":
            $ mads -= 1
            "Your fingers get within an inch of the black cover before Madeline snatches it away."
            m "Equipment, not my brain. Take the light kit."

    "It takes another few minutes for her to pack spare slides, gloves, and enough cable to wire a small building. She checks the lab door twice, mutters that Winston moved her keys, then finds them in her own hand."

    scene black with fade
    "On the drive, Madeline reads the scene log aloud and interrupts herself every few lines to insult the formatting. By the time you reach Enrico's street, she has memorized the document and corrected it in three places."
    "The police tape lifts in the afternoon wind. Inside, the house is quiet enough that the scanner's case sounds too loud when you set it down."
    "Madeline pulls on a fresh pair of gloves and kneels beside the sealed shard without touching it. A portable scanner projects the partial print several feet high across the wall."

    show madeline madScientist at slot(0, total=1), bright zorder 10

    $ madeline_day_one_reveal = get_planned_route_reveal("madeline", 1)
    $ madeline_day_one_cleared_id = madeline_day_one_reveal["eliminated"][0]
    $ madeline_day_one_cleared_name = suspectNames[madeline_day_one_cleared_id]

    m "One suspect has a prior conviction, which means their fingerprints are already in the police database: [madeline_day_one_cleared_name]."
    m "Lucky us. Or unlucky them, generally speaking."

    "She aligns the database print over the recovered ridge pattern. Several points appear similar until she magnifies the whorl at the center. The two patterns split apart."

    menu:
        "The ridge paths diverge before the center. It isn't their print.":
            $ mads += 2
            m "Six independent mismatches. One would've been enough, but stopping at one is how mediocre people invite arguments."
        "You knew that before you enlarged it, didn't you?":
            $ mads += 1
            m "Obviously. The display was for you. Try to appreciate the educational effort."
        "So the database search failed.":
            $ mads -= 1
            show madeline distress at slot(0, total=1), bright zorder 10
            m "No. It succeeded at exclusion. Not producing a name is not the same thing as producing nothing."

    $ madeline_day_one_clue = "The bloody fingerprint from the struggle does not match {}'s police record.".format(madeline_day_one_cleared_name)
    $ record_planned_route_reveal(
        "madeline", 1, clue_text=madeline_day_one_clue, expected_count=1)

    show madeline at slot(0, total=1), bright zorder 10

    m "[madeline_day_one_cleared_name] is out. [len(remainingSuspects)] suspects left."
    m "This is why databases are useful. People keep making the same stupid mistake, and computers remember it for us. Or me."

    "She adds the result to her notebook, then writes another short line beneath your name."

    menu:
        "What did you write about me?":
            $ mads += 1
            m "Curious. Distractible. Better eyes than expected."
            m "Don't make that expression. The final category is positive."
        "You should add that I kept up with you.":
            $ mads += 2
            show madeline flirty curious at slot(0, total=1), bright zorder 10
            m "For one test. Confidence interval's still shit."
            m "Come back next time and improve it."
        "Keeping files on everyone is creepy.":
            $ mads -= 1
            m "It's efficient. Creepy is just efficient with shitty branding."

    m "Let's pack this before Nicky discovers I've been awake since yesterday. Apparently food becomes mandatory if I mention that near her."

    "She shuts down the projection but does not immediately stand. For a moment, the empty room returns around you: broken glass, sealed evidence, and one name that no longer belongs on the board."

    menu:
        "Offer to pick up food on the way back.":
            $ madeline_day_one_food_plan = "driver"
            m "Anything portable. Nothing with lettuce pretending to be a meal."
            "She says it without gratitude, then quietly hands you her keys so you can drive."
        "Ask what she actually wants to eat.":
            $ mads += 1
            $ madeline_day_one_food_plan = "carry"
            m "Something with sugar, protein, and no conversation attached. You choose."
            "She begins packing the scanner, but leaves the heaviest case beside you."
        "Point out that sleep is also mandatory.":
            $ madeline_day_one_food_plan = "sleep"
            m "Sleep is a hardware limitation. Food is a fuel limitation. I can only solve one in transit."
            "She seals the last evidence pouch and points at the scanner case, assigning you half the load without interrupting the argument."

    "You help restore the room to the condition recorded by the scene team. Only after every seal is checked does Madeline follow you back through the police tape and toward the car."
    m "Give Ulysses the result when we get back. I'll deal with the food intervention."

    scene black with fade
    if madeline_day_one_food_plan == "driver":
        "With you driving, Madeline directs you to a takeout window and vetoes two menu items on nutritional inefficiency. She balances the chosen carton on the closed scanner case, then wordlessly holds your drink whenever traffic makes it difficult to eat."
    elif madeline_day_one_food_plan == "carry":
        "You choose takeout with sugar, protein, and no table service. Madeline eats it in the parked car, balances the carton on the closed scanner case, and steals several of your fries without asking."
    else:
        "You decide on takeout now, sleep after the report. Madeline eats in the parked car, balances the carton on the closed scanner case, and shoves the unopened dessert into your hands so she cannot revise the agreement into more work."
    "For once, the notebook remains in her bag. She spends the drive criticizing the radio instead of recording observations about you."
    "Eventually you make your way back to the office, where Madeline splits to let you report"

    $ dayMads += 1
    jump endOfDay

label MadelineDayTwo:
    scene cubicleOutline
    "Madeline is waiting beside her desk with two miniature-golf passes pinched between her fingers like contaminated evidence."

    show madeline distress at slot(0, total=1), bright zorder 10

    m "Winston says I need to get out more."
    m "He gave me these and said staring at a failed prototype for fourteen consecutive hours doesn't count as recreation."
    m "He's a moron, but I have not yet produced a successful counterargument."
    if dayWin >= 6:
        m "The final meeting is tomorrow. The remaining tests are running unattended, so this is apparently the least irresponsible time to leave."
    elif dayWin >= 5:
        m "The final meeting is getting close. The remaining tests are running unattended, so this is apparently the least irresponsible time to leave."

    "She holds out one pass."

    m "You're coming. This is not a date. I need a second data set."

    menu:
        "Of course. A rigorous miniature-golf experiment.":
            $ mads += 2
            show madeline madScientist at slot(0, total=1), bright zorder 10
            m "Surface friction, incline, impact loss, obstacle timing. You understand the scope. Good."
        "Want me to pretend it is a date anyway?":
            $ mads += 2
            show madeline flirty at slot(0, total=1), bright zorder 10
            m "I— No. Pretending would contaminate the behavioral data."
            m "Just take the fucking pass."
        "Mini golf sounds pointless.":
            $ mads -= 1
            m "Most recreation is pointless. That's why Winston thinks I'll benefit from it."

    m "Winston learned the 'get out more' argument from Ulysses. Ulysses used to deploy it every time I slept in the lab."

    "The familiarity in the sentence lands before Madeline appears to notice she said it."

    menu:
        "Ask how close she and Ulysses were.":
            $ mads += 1
            m "We dated. It ended last year. We're fine, so don't make that face."
        "Guess that Ulysses tried taking her out too.":
            $ mads += 1
            m "For approximately a year. Dating him didn't improve the argument."
        "Let the subject pass.":
            "Madeline starts toward the elevator, then speaks without looking back."
            m "We dated, if that's the question you're pretending not to ask. We're fine now."

    "She delivers the information like a correction to a lab record and immediately returns to criticizing the course brochure. You have to catch up before the elevator doors close."

    "At the elevator, Madeline realizes she is still carrying a soldering iron. She stares at it, considers bringing it, then drops it into a planter outside the lab."
    m "Remind me that's there later."

    menu:
        "Promise to remind her.":
            $ mads += 1
            m "Put it in your notebook. Human memory is embarrassing."
        "Ask why it was in her hand.":
            m "I was repairing something when Winston interrupted me. I do not know which thing. It'll become obvious when it catches fire."
        "Suggest it might improve the golf course.":
            $ mads += 1
            m "Don't tempt me. I haven't even seen how badly they built it yet."

    scene black with fade
    "The trip across town gives Madeline time to read every negative review clipped from a local entertainment guide and explain why most reviewers misunderstood basic geometry."
    "The miniature-golf course is an explosion of plastic castles, painted animals, artificial ponds, and badly maintained green turf. A teenager at the counter slides a rack of colored balls toward you."

    menu:
        "Choose a bright pink ball.":
            "Madeline takes a black ball and examines yours beneath the counter light."
            m "High visibility. Sensible, despite the color."
        "Choose the least scratched ball.":
            $ mads += 1
            "You turn several balls in your hand before selecting one. Madeline watches your inspection with open approval."
            m "At least one of us came prepared to reject damaged equipment."
        "Ask Madeline to choose for you.":
            $ mads += 1
            "She weighs three balls in her palms and gives you the one with the fewest surface defects."
            m "This one. When you lose, find a better variable to blame."

    "Madeline refuses the tiny pencil, produces a mechanical one from her jacket, and records the starting time at the top of the scorecard."
    "At the first hole, Madeline crouches until her face is nearly level with the ball."

    show madeline madScientist at slot(0, total=1), bright zorder 10

    m "There are seventeen holes after this one."
    m "If I account for incline, surface friction, wind speed, ball deformation, and the windmill's rotational period, I can finish this in two strokes."

    "You take your turn. The ball strikes one wall, bounces through the windmill at a terrible angle, clips a decorative mushroom, and drops directly into the hole."

    show madeline distress at slot(0, total=1), bright zorder 10

    m "..."
    m "Do that again."

    menu:
        "The mushroom corrected the angle. Add it to your model.":
            $ mads += 2
            show madeline madScientist at slot(0, total=1), bright zorder 10
            m "It should not have sufficient elasticity."
            m "Move. I need to measure the mushroom."
        "You look cute when you're concentrating.":
            $ mads += 2
            show madeline flirty at slot(0, total=1), bright zorder 10
            m "..."
            m "I was calculating."
            "She looks back at the ball."
            m "I have lost the calculation. Fuck you."
        "Begin celebrating the flawless shot.":
            $ mads += 1
            m "That wasn't flawless. It was statistically offensive."
            m "Do it again so I can prove why."

    "By the sixth hole, Madeline has removed her jacket and tied back her hair. By the ninth, she has measured three rails with a pocket ruler and accused a fiberglass pirate of introducing an uncontrolled variable."
    "At the windmill hole, her perfectly aimed shot catches a warped patch of turf and rolls backward between her shoes."

    show madeline distress at slot(0, total=1), bright zorder 10

    m "This course is built wrong."

    menu:
        "The turf rises on the left. Compensate two degrees right.":
            $ mads += 2
            show madeline flirty curious at slot(0, total=1), bright zorder 10
            m "...I was looking at the windmill, not the seam."
            m "Move over, newb. I need your angle before the turf settles differently."
        "Want me to let you win?":
            $ mads -= 2
            show madeline distress at slot(0, total=1), bright zorder 10
            m "I will bury you under the eighteenth hole."
        "Maybe the genius has finally met her match.":
            $ mads += 1
            m "My match is defective landscaping? That's insulting to both of us."

    "Madeline adjusts by two degrees and sinks the shot. She looks more satisfied than anyone has a right to look beside a plastic windmill."
    "She adds a small mark beside your name on the scorecard. When you try to read it, she folds that corner under her thumb."

    "The remaining holes take nearly an hour. Madeline stops trying to solve the course perfectly and begins testing increasingly petty bank shots just to see which obstacles she can use against themselves."
    "At the eighteenth hole, both balls disappear into a plywood volcano. A bell rings somewhere inside, and Madeline peers into the opening as if considering disassembly."

    m "If that machine damaged them, their loss-prevention policy is about to become extremely relevant."

    scene black with fade
    "The balls emerge unharmed, so the course survives. At the snack window outside, Madeline studies the ice-cream menu longer than she studied the final shot."

    menu:
        "Order chocolate.":
            $ madeline_ice_cream_choice = "chocolate"
            "Madeline orders chocolate too, then insists this is convergence on the optimal answer rather than imitation."
        "Order the brightest flavor on the board.":
            $ mads -= 1
            $ madeline_ice_cream_choice = "blue"
            "Your ice cream arrives an alarming shade of blue. Madeline takes one experimental taste, frowns, then takes another."
        "Ask for Madeline's recommendation.":
            $ mads += 1
            $ madeline_ice_cream_choice = "coffee"
            m "Coffee."
            "You order it. She chooses the same and pays before you can argue."

    "You carry the cups to a metal table away from a noisy birthday party. After the final hole, the two of you sit outside with ice cream while the sun sinks behind the plastic castle. Madeline has written the score, wind conditions, and several complaints across every empty section of the scorecard."

    show madeline at slot(0, total=1), bright zorder 10

    m "That was statistically more enjoyable than anticipated."

    menu:
        "You can just say you had fun.":
            $ mads += 1
            m "I am aware."
            "You wait."
            m "...I had fun."
        "Failure's easier when nobody gets hurt.":
            $ mads += 2
            show madeline flirty curious at slot(0, total=1), bright zorder 10
            m "Yes."
            m "I can be wrong here and the worst consequence is losing to a goddamn mushroom. That's... useful."
        "Next time we should do something you're actually good at.":
            $ mads -= 2
            m "I am good at this. The course is wrong. We established that."

    "She folds the scorecard and slips it into her jacket instead of throwing it away."
    "Neither of you gets up immediately. Madeline scrapes the last melted ice cream from the bottom of her cup, watching another pair struggle with the windmill you finally understood."

    if mads >= MADELINE_WARM_THRESHOLD:
        m "The experiment needs replication. Not soon. Eventually."
        m "That is not an invitation. It is a statement about sample size."
    else:
        m "Don't tell Winston he was right about this. He'll become unbearable."

    m "I'll see you around. Go tell Ulysses we wasted a day on loseing to faulty architecture and landscaping."
    "Madeline walks away, leaving you to ride back and report to Ulysses."
    $ dayMads += 1
    jump endOfDay

label MadelineDayThree:
    scene labOutline
    "Madeline has arranged four capped tubes beside a compact centrifuge. Ica sits on a rolling stool several feet away, doing absolutely nothing useful."

    show madeline at slot(1, total=2), bright zorder 10
    show ica at slot(0, total=2), dim zorder 0

    m "The trace from Enrico's window is mixed with his blood. Today we're separating the layers and testing which markers are absent."
    m "Enrico's type is already confirmed. Once I subtract his markers, the foreign trace tells us what the attacker cannot be."
    m "Before either of you touches anything, the rotor has to be balanced. Uneven mass at this speed turns expensive equipment into shrapnel."

    "Madeline gives you a lab coat, points out the emergency cutoff, and makes you repeat the sample labels back to her. Ica watches the safety briefing while rotating one lazy circle on the stool."

    menu:
        "Show me the controls before I place a tube.":
            $ mads += 2
            m "Start with the speed control, then the emergency brake. Competence continues to be attractive—I mean statistically uncommon."
        "You built this centrifuge too, didn't you?":
            $ mads += 1
            m "Modified it. The original design had limits and I found that personally insulting."
        "It probably balances itself.":
            $ mads -= 2
            show madeline distress at slot(1, total=2), bright zorder 10
            m "It does not. That's why I just explained balance to you."

    show ica at slot(0, total=2), bright zorder 10
    show madeline at slot(1, total=2), dim zorder 0

    i "Can I spin in the chair while you two do blood homework?"

    show madeline distress at slot(1, total=2), bright zorder 10
    show ica at slot(0, total=2), dim zorder 0

    m "You can leave. That would be ideal."

    show ica happy at slot(0, total=2), bright zorder 10
    show madeline at slot(1, total=2), dim zorder 0

    i "Nah. Stool's comfortable."

    menu:
        "Ask Ica to stay outside the marked line.":
            i "Yeah, yeah. I can be useless from over here."
            m "For once, that is the ideal application of her abilities."
        "Ask Madeline if the counterweights are ready.":
            $ mads += 1
            m "Numbered, measured, and checked twice. Unlike the guest observer."
            i "I checked the stool. Works great."
        "Move the stool farther from the centrifuge.":
            $ mads += 1
            "Ica lets you roll her several feet away without lifting either foot."
            i "Wow. Full-service lab."
            m "Keep going until she is in another building."

    "Ica reaches toward the stool with one hand. Gravity shifts just enough to pull it across the floor without making her stand."
    "The centrifuge gives a sharp warning tone and stops. One tube settles into a visibly cleaner boundary than the others."

    show madeline distress at slot(1, total=2), bright zorder 10
    show ica at slot(0, total=2), dim zorder 0

    m "ICA! What the fuck did I say about changing local gravity near calibrated equipment?"

    show ica at slot(0, total=2), bright zorder 10
    show madeline at slot(1, total=2), dim zorder 0

    i "I don't remember you saying anything about gravity specifically."
    i "Also, your machine stopped itself. You're welcome."

    "Madeline begins checking the rotor for damage. Your attention stays on the unusually clean band inside the interrupted tube."

    menu:
        "That tube separated more cleanly under the gravity shift.":
            $ mads += 2
            show madeline madScientist at slot(1, total=2), bright zorder 10
            m "...It did."
            m "The effective mass changed faster than the rotor speed. That's shockingly useful."
        "I think Ica improved your machine.":
            $ mads += 1
            show madeline distress at slot(1, total=2), bright zorder 10
            m "She accidentally exposed a useful variable. That is not the same thing."
        "Looks broken to me.":
            $ mads -= 1
            m "Then look harder. The shutdown worked and the separation changed."

    show ica flirty at slot(0, total=2), bright zorder 10
    show madeline at slot(1, total=2), dim zorder 0

    i "Aw, look at you two doing science together. Kinda cute."

    show madeline flirty at slot(1, total=2), bright zorder 10
    show ica at slot(0, total=2), dim zorder 0

    m "Get out of my lab."

    show ica happy at slot(0, total=2), bright zorder 10
    show madeline at slot(1, total=2), dim zorder 0

    i "Sure thing, Shield Maiden. Try not to fall in love with the centrifuge."

    hide ica
    show madeline distress at slot(0, total=1), bright zorder 10

    m "I am NOT crediting her in the report."
    m "We can reproduce the useful part with calibrated counterweights and fine trim. You balance while I monitor the sample."

    call RulesMadelineCentrifuge
    $ start_madeline_centrifuge_minigame()

    $ madeline_day_three_blood_type = madeline_centrifuge_result["blood_type"]
    $ madeline_day_three_removed_names = ", ".join(investigationClues[-1]["eliminated_names"])

    if madeline_centrifuge_result["completed"]:
        if madeline_centrifuge_result["quality"] == "perfect":
            show madeline madScientist at slot(0, total=1), bright zorder 10
            m "Balanced on the first run. No vibration, clean separation, readable bands."
            m "You're allowed to look pleased with yourself. Briefly."
        else:
            m "You recovered from the unstable run without ruining the sample. I won't have to extract another trace, so we're still speaking."
            m "Next time, remember that equal numbers work better on opposite sides."
    else:
        m "Watch the rotor. Six and four on each side. Symmetry isn't decoration."
        "Madeline finishes the separation and slides the result beneath the reader."

    if madeline_centrifuge_result.get("scope") == "category":
        m "No type [madeline_day_three_blood_type] markers in the attacker trace."
        m "That rules out [madeline_day_three_removed_names]. [len(remainingSuspects)] suspects left."
    else:
        m "The separated markers conflict with both preserved reference profiles."
        m "That clears [madeline_day_three_removed_names] individually. Same count, narrower claim."

    menu:
        "The missing marker matters more than the visible bands.":
            $ mads += 2
            show madeline flirty curious at slot(0, total=1), bright zorder 10
            m "Everybody stares at what a test shows. Geniuses ask what should be there and isn't. You just may be trainable after all."
        "Your centrifuge is incredible.":
            $ mads += 1
            m "Obviously. The operator was decent too."
        "So Ica solved the blood test.":
            $ mads -= 2
            show madeline distress at slot(0, total=1), bright zorder 10
            m "Ica moved a chair. We recognized, modeled, reproduced, and interpreted the result."
            m "Do not make me explain the difference again or I'll take your name off the report too."

    if mads >= MADELINE_HIGH_THRESHOLD:
        "Madeline opens the notebook and writes several lines beneath NEWB. When she notices you looking, she covers the page with one hand."
        m "Peer-review notes. Classified."
    elif mads >= MADELINE_WARM_THRESHOLD:
        m "You did well, newb. Better than most people who wander into my lab with functional hands and no idea how to use them."
    else:
        m "The evidence is valid. That's the important part."

    "Madeline transfers the separated sample into a sealed cartridge and makes you read the identifier aloud before she locks it away. The centrifuge continues ticking softly as its rotor cools."
    "She writes Ica's gravity shift into the methods section after all, though the note beside it reads ACCIDENTAL VARIABLE in heavy block letters."

    "While the rotor cools, Madeline opens a drawer full of emergency protein bars and throws one toward you. Every wrapper is identical and none lists a flavor."

    menu:
        "Eat it without asking.":
            $ mads += 1
            m "They're efficient. If it tastes like chalk, that's normal."
        "Ask whether she made these too.":
            $ mads += 1
            m "No. If I made them, they would taste less like insulation and contain forty percent more caffeine."
            m "Maybe I should make my own though... not a bad idea newb."
        "Offer it to Ica before remembering she left.":
            m "She'd make it orbit her head for an hour and forget to eat it. Keep it."

    "You eat at the clean end of the bench while Madeline annotates the run. The conversation wanders from Ica's impossible luck to whether the lab needs a better snack drawer."

    m "Come back next time. I have a new prototype to test. For now, report to Ulysses."
    $ dayMads += 1
    jump endOfDay

label MadelineDayFour:
    scene labOutline
    "A new machine occupies most of Madeline's central workbench. Cables run from a sealed wound swab to three separate readers labeled FIRE, ICE, and LIGHT."

    show madeline madScientist at slot(0, total=1), bright zorder 10

    m "The victim's wounds contain power residue, but residue alone is useless if we can't tell how it entered the body."
    m "This separates elemental damage from ordinary contact trauma. In theory."

    "She has taped a clean boundary around the workbench and set three stools beyond it. You take the only stool without loose circuitry on the seat."

    m "Before I switch it on, choose what you're watching. I can't monitor all three outputs and the sample temperature at once."

    menu:
        "Watch the temperature and pressure readout.":
            $ madeline_prototype_watch = "temperature"
            m "Call out any change above two percent. Don't round."
        "Watch for disagreement between the three readers.":
            $ mads += 1
            $ madeline_prototype_watch = "readers"
            m "Say the reader name first, then the value. I don't want to guess which disaster you're describing."
        "Watch the sealed sample itself.":
            $ mads += 1
            $ madeline_prototype_watch = "sample"
            m "Useful. If the color or volume changes, hit the yellow switch. Red is full shutdown."

    menu:
        "What assumption is the prototype making?":
            $ mads += 2
            m "That one wound has one cause. It's a reasonable starting model."
            m "And before you say it, yes, I know reasonable assumptions are where idiots go to die."
        "You made three readers in one night?":
            $ mads += 1
            m "Four. The first one caught fire. It was less informative than you'd expect."
        "Just run every sample until one says guilty.":
            $ mads -= 2
            show madeline distress at slot(0, total=1), bright zorder 10
            m "Machines don't say guilty. They produce data, which smarter people interpret."

    "Madeline starts the prototype. The Fire reader illuminates. A moment later, so do Ice and Light. Every alarm begins sounding at once."

    show madeline distress at slot(0, total=1), bright zorder 10

    m "No."
    m "No, that's impossible. The sample cannot be thermally altered, crystallized, and photochemically bleached in the same square millimeter."
    m "DAMN IT!"

    "She shuts the alarms off, opens her notebook, and begins writing so hard the pencil tears through the page."

    menu:
        "The machine may be separating causes that happened to the same wound.":
            $ mads += 2
            show madeline madScientist at slot(0, total=1), bright zorder 10
            m "Power, impact, and environmental damage stacked together..."
            m "Yes. The machine isn't wrong. My input model is. Fuck. Say that again while I write it down."
        "Rebuild it. I'll stay for the retest.":
            $ mads += 2
            show madeline flirty curious at slot(0, total=1), bright zorder 10
            m "You know that could take all night."
            "You nod."
            m "...Fine. Hand me the narrow driver."
        "A genius should have predicted this.":
            $ mads -= 2
            show madeline distress at slot(0, total=1), bright zorder 10
            m "A genius notices when a model fails and fixes it. A dumbass stands nearby commenting on the obvious."

    "Madeline clears a space on the bench and opens the prototype housing. For the next half hour, you pass her tools while she reroutes two readers and divides the input into separate time windows."

    menu:
        "Hand her the narrow driver before she asks.":
            $ mads += 1
            "Madeline takes it without looking, uses it, then glances at your empty hand."
            m "You remembered. Keep doing that."
        "Ask her to explain the new sequence.":
            m "First environmental change, then direct power residue, then physical transfer. Same wound, three events. Watch the traces when I restart it."
        "Keep a written list of every change.":
            $ mads += 1
            m "Timestamp it too. If this works, I want to know which version deserves the credit."

    "Madeline separates the readings by sequence instead of source. The impossible result resolves into damage from Enrico's surroundings, the attacker's power, and physical contact during the struggle."

    $ madeline_day_four_injuries = suspectAttributes[killer]["injuries"]
    $ madeline_day_four_wound_hint = MADELINE_WOUND_SCENE_HINTS[madeline_day_four_injuries]

    m "There. One residue pattern affected the wound, but it didn't create every mark around it."
    m "I can isolate its sequence now. I still can't classify the source without a cleaner comparison."

    "Madeline overlays the corrected sequence across Enrico's injuries. [madeline_day_four_wound_hint]"

    "She begins preparing the entire test again from untouched controls."

    menu:
        "I'll help document the failed run before we repeat it.":
            $ mads += 2
            m "Failed data is still data. Pretending otherwise is how morons publish garbage. Start with the first alarm."
        "You're hotter than the machine when you're angry.":
            $ mads += 1
            show madeline flirty at slot(0, total=1), bright zorder 10
            m "That is scientifically meaningless."
            "She turns away before answering."
            m "The machine peaked at four hundred degrees. So you're also wrong dumbass."
        "Maybe let somebody else rebuild it.":
            $ mads -= 2
            m "Maybe let somebody else form your sentences."

    m "The corrected design needs time to settle before I trust it on the final residue test. Meanwhile, I have a neural-feedback rig that needs a second operator."
    m "Come back next time. Read the consent packet first. All of it."

    "The second run finishes without alarms. Madeline does not celebrate; she labels the output PROVISIONAL and starts a timer for the cooling cycle."
    "You remain until the sample is resealed and the failed page—pencil tear included—is filed beside the successful one. Only then does she let you clear the bench and leave."

    "The cooling timer still has six minutes left. Madeline sits on one of the stools, pushes a bottled drink across the floor with her boot, and opens another for herself."

    menu:
        "Ask how many prototypes fail before one works.":
            $ mads += 1
            m "Most of them. Intelligence reduces stupid failures; it doesn't repeal reality."
        "Toast to the model being wrong in a useful way.":
            $ mads += 1
            m "That is an irritatingly accurate description of research."
            "She taps her bottle against yours."
        "Spend the six minutes in silence.":
            "Madeline does not seem uncomfortable with it. When the timer sounds, she looks marginally less angry than before."
    "Madeline stands from her stool."
    m "I'm going home for now. We'll start on the machine then. Remember:"
    m "READ"
    m "THE"
    m "PACKET"
    "Madeline walks out the door, leaving you to report to Ulysses."

    $ dayMads += 1
    jump endOfDay

label MadelineDayFive:
    scene labOutline
    "A stack of paper waits beside Madeline's helmet. The title page reads VOLUNTARY NEURAL-FEEDBACK CALIBRATION, followed by twenty-three pages of warnings."

    show madeline at slot(0, total=1), bright zorder 10

    m "Before you ask: no, the packet is not excessive."
    m "We fought a villain called Mindbreak a while back. He controlled people's minds. I don't put anything near a brain without multiple ways to shut it the fuck down."
    m "The helmet doesn't control thoughts. It reduces deliberate emotional filtering so I can calibrate interference in the scanner."

    "Madeline leaves you alone with the packet instead of summarizing it. She uses the time to inspect every wire running from the helmet and test the physical cutoff three times."
    "Several pages later, she sets a glass of water beside your hand without interrupting your reading."

    "She taps three marked safeguards: a physical cutoff in your hand, a verbal check-in sequence, and a strict maximum duration."

    menu:
        "I control the cutoff, and the first stop ends the test.":
            $ mads += 2
            show madeline flirty curious at slot(0, total=1), bright zorder 10
            m "Then you understood the important page. No negotiation, no request for one more reading, no deciding you know better than the person wearing it."
        "You wrote twenty-three pages just to ask me to push a button?":
            $ mads += 1
            m "I wrote twenty-three pages so pushing the button remains the only decision you need to make."
        "We'd get better data if we ignored the time limit.":
            $ mads -= 2
            show madeline distress at slot(0, total=1), bright zorder 10
            m "Then you don't understand consent or experimental design. Read it again."

    "Madeline answers your last procedural question, initials the safety checklist, and makes you identify the physical cutoff with your eyes closed."
    "Only then does she sign the form, make you sign beneath her, and place the helmet over her head. Its narrow visor lights across her glasses."

    m "Beginning baseline. Motor control intact. Reasoning intact. You're standing too close."

    "You take one step back."

    m "I didn't tell you to move."
    m "Shit. Filtering reduction confirmed."

    if mads >= MADELINE_HIGH_THRESHOLD:
        m "Your arrival changes my baseline readings before we even start working. Consistently."
        m "I've recalculated whether you're flirting with me eleven times, and the probability keeps getting worse."
        m "Worse for concentration. That is not an invitation to interpret it. Fuck. Continue the test."
    elif mads >= MADELINE_WARM_THRESHOLD:
        m "You're significantly more competent than I predicted. I have revised your file upwards of four times."
        m "I also notice when you aren't here, which is an inefficient use of attention."
    else:
        m "I trust you to follow the procedure. That is not a statement I make about most people here."

    "The helmet emits a warning tone. Madeline's hand tightens against the chair."

    m "Stop."

    menu:
        "Hit the cutoff immediately.":
            $ mads += 2
            "The visor goes dark before the next tone."
        "Ask if she is certain.":
            $ mads -= 1
            show madeline distress at slot(0, total=1), bright zorder 10
            m "I said stop!"
            "You hit the cutoff."
        "Wait for one more reading.":
            $ mads -= 3
            "The helmet reaches its hard time limit and shuts itself down. Madeline tears it off."
            show madeline distress at slot(0, total=1), bright zorder 10
            m "Get one thing straight, newb. Better data does not outrank the person inside the machine."
            m "You do that shit again and I'll put a hole in your head."

    "Madeline's face is red with equal parts anger and embarrassment."

    "She sits without speaking while the system records its shutdown. You give her the untouched glass of water and wait for her breathing to settle before either of you approaches the data."

    if mads >= MADELINE_WARM_THRESHOLD:
        show madeline flirty at slot(0, total=1), bright zorder 10
        m "Anything I said under reduced filtering remains scientifically valid and socially inadmissible."
    else:
        m "Calibration complete. We are never discussing the verbal output again."

    "Madeline locks the helmet away, then returns to the preserved wound sample while the corrected residue array continues calibrating."
    "Under magnification, fine debris around the wound resolves into a clear handling pattern."

    $ madeline_day_five_organization = suspectAttributes[killer]["organization"]
    $ madeline_day_five_organization_hint = MADELINE_ORGANIZATION_SCENE_HINTS[madeline_day_five_organization]

    "[madeline_day_five_organization_hint]"

    m "Powers influence habits more than people admit. Fire users trend passionate. Ice users often run cold and calm. Light users get weird about dirt and order."
    m "Tendencies, not laws. Everyone is still individually stupid in exciting new ways."
    m "This pattern doesn't prove anything by itself, but it's interesting."

    menu:
        "A tendency isn't an identity. We keep it provisional.":
            $ mads += 2
            m "Put that sentence in the report. Correlation is useful right up until some idiot treats it as destiny."
        "You really do get the bird's-eye view of everyone.":
            $ mads += 1
            m "Finally, somebody understands the burden of being surrounded by ground-level thinking."
        "Clean people are innocent. Problem solved.":
            $ mads -= 2
            show madeline distress at slot(0, total=1), bright zorder 10
            m "That may be the dumbest sentence produced in this laboratory, and Ica visits regularly."

    m "The corrected residue array will finish calibrating overnight."
    m "Next time we classify the power category and cut the list to three. For now, get back to Ulysses."

    "She files the helmet data separately from the case evidence, locks both cabinets, and checks that you kept your copy of the consent form. The embarrassment remains, but it no longer controls the room."

    "She leaves."
    "Time to report back."

    $ dayMads += 1
    jump endOfDay

label MadelineDaySix:
    scene labOutline
    "Three sealed reference cartridges sit in a row across Madeline's workbench: FIRE, ICE, and LIGHT. The preserved wound swab rests beneath a glass cover beside them."

    show madeline madScientist at slot(0, total=1), bright zorder 10

    m "Final test. Day Three isolated the blood trace. Day Four separated the wound sequence from the surrounding damage."
    m "The corrected array finished calibrating overnight."
    m "Today we compare the residue in the wound against all three broad power categories."
    m "Load the references left to right and don't touch the swab."

    if madeline_prototype_watch == "temperature":
        m "Take temperature and pressure again. You already know the safe range."
    elif madeline_prototype_watch == "readers":
        m "Watch for disagreement between the readers again. Same callout format as the prototype run."
    elif madeline_prototype_watch == "sample":
        m "Keep your eyes on the sealed sample again. Yellow for visible change, red for containment failure."

    "Unlike the improvised setups earlier in the week, the bench is immaculate. Every cable is tied down, every tool has a marked space, and two blank result envelopes wait beside the printer—one for each run."

    menu:
        "Check every seal, then load Fire, Ice, and Light.":
            $ mads += 2
            m "You checked the seals without being told. My notes about you are becoming annoyingly positive."
        "You could probably do this faster yourself.":
            $ mads += 1
            m "Obviously. I'm testing whether you can do it correctly. Try to keep up."
        "Skip the controls and test the swab directly.":
            $ mads -= 2
            show madeline distress at slot(0, total=1), bright zorder 10
            m "No controls means no trustworthy result. Six days in and you're still trying to invent shortcuts to being a dumbass."

    "You inspect each seal and lock the cartridges into the reader. Madeline watches your hands rather than the labels, then signs the setup line once the final lock clicks."
    "The machine runs a control cycle first. For three long minutes, nothing happens except the slow sweep of a progress bar and the cooling fan beneath the table. Madeline refuses to look away from it."
    "When all three references return their expected patterns, she lowers her helmet over her glasses and connects its scanner to the prototype."

    $ madeline_day_six_power = suspectAttributes[killer]["power"]
    $ madeline_day_six_residue = MADELINE_POWER_RESIDUE_TEXT[madeline_day_six_power]

    "The first pass sends three colored traces across her visor. Two collapse into environmental noise. One remains."

    m "[madeline_day_six_residue]"

    "Madeline lifts the visor, openly grinning."

    show madeline madScientist at slot(0, total=1), bright zorder 10

    m "[madeline_day_six_power]. Fuck yes."

    menu:
        "Repeat it blind before we report.":
            $ mads += 2
            show madeline flirty curious at slot(0, total=1), bright zorder 10
            m "I was already going to."
            m "Still, now I have to add 'understands replication' to your file. Painfully inconvenient."
        "I knew your machine would work, genius.":
            $ mads += 1
            m "Of course it worked. The question was whether reality had the sense to agree with me twice."
        "One result is close enough.":
            $ mads -= 2
            show madeline distress at slot(0, total=1), bright zorder 10
            m "Close enough is what people say immediately before ruining six days of evidence."

    "Madeline prints the first trace and places it face-down without discussing it further. You turn away while she scrambles the cartridge positions and masks their labels."
    "The second control cycle takes just as long as the first. This time, Madeline drums her fingers against the bench until you cover the result window with the empty evidence envelope."
    "When the test completes, the same trace survives."

    $ madeline_day_six_clue = "Repeated residue tests identify the attacker's broad power category as {}.".format(madeline_day_six_power)
    $ record_planned_route_reveal(
        "madeline", 6, clue_text=madeline_day_six_clue, expected_count=3)
    $ madeline_day_six_remaining_names = ", ".join(
        [suspectNames[suspect_id] for suspect_id in remainingSuspects])

    m "Repeated, controlled, and consistent. The attacker belongs to the [madeline_day_six_power] category."
    m "That leaves [madeline_day_six_remaining_names]."
    m "The machine gets us to three. Choosing between them is your job."

    "She prints the result, signs it, and files it with the evidence packet without offering another hint."

    "The two envelopes sit side by side while the printer cools. Madeline compares every line, staples the control sheets behind them, and finally shuts the prototype down. The sudden quiet makes the end of the week feel real."

    if mads >= MADELINE_HIGH_THRESHOLD:
        if madeline_ice_cream_choice == "blue":
            "When Madeline opens her personal notebook, the folded miniature-golf scorecard slips from the section labeled NEWB. One corner still carries a faint blue ice-cream stain. Your name is written across the back beneath several dense lines of observations."
        elif madeline_ice_cream_choice == "coffee":
            "When Madeline opens her personal notebook, the folded miniature-golf scorecard slips from the section labeled NEWB. A tiny coffee-colored ring marks one corner. Your name is written across the back beneath several dense lines of observations."
        else:
            "When Madeline opens her personal notebook, the folded miniature-golf scorecard slips from the section labeled NEWB. Your name is written across the back beneath several dense lines of observations."
        show madeline flirty at slot(0, total=1), bright zorder 10
        m "You saw nothing."
        "She places the scorecard carefully back inside instead of hiding it somewhere else."
        m "Your work this week was intelligent, careful, and consistently less irritating than expected. Put that in your report."
    elif mads >= MADELINE_WARM_THRESHOLD:
        "Madeline adds one final line to the section labeled NEWB."
        m "Final assessment: competent under supervision."
        m "That is extremely high praise. Don't make me quantify it."
    else:
        m "The evidence is sound. Give Ulysses the three names and prepare for the final meeting."

    m "We're done for today, newb. See you tomorrow"

    $ dayMads += 1
    jump endOfDay

label NickyDayOne:
    scene debriefRoomOutline
    "Nicky has covered one end of the debrief table with pager-company call records, a laundromat receipt, and still frames from three different street cameras."
    "The rest of the room is still waking up. A printer hums somewhere behind you, and a paper cup of coffee cools beside Nicky's elbow while she sorts the last few pages into crooked piles."

    show nicky content happy at slot(0, total=1), bright zorder 10

    n "Morning, rookie! Welcome to the exciting world of proving somebody didn't do a murder."
    n "It's less dramatic than catching them, but the paperwork smells exactly the same."

    "She slides the pager log and receipt toward you. Their timestamps disagree with the city-camera stills by exactly one hour."

    n "Somebody reset one clock and ignored the others. Apparently daylight saving time is where civilization ends."
    n "What do you do first?"

    menu:
        "Normalize the timestamps, then compare the movement records.":
            $ nick += 2
            show nicky content happy at slot(0, total=1), bright zorder 10
            n "There we go! You're already ahead of half the people who send me reports at the station."
        "So our first suspect is bad software design.":
            $ nick += 1
            n "Finally, somebody willing to arrest the real criminal."
            n "Sadly, the district attorney says I can't charge a clock. Yet."
        "The pager log says they were elsewhere. Good enough.":
            $ nick -= 2
            show nicky angry accusation at slot(0, total=1), bright zorder 10
            n "Nope. Pagers get borrowed, lost, handed off, and used by people who swear they never touched them. Corroboration, rookie."

    "Nicky gives you room at the table instead of reaching over you. For a few minutes, the two of you work in the soft shuffle of paper and the occasional squeak of a marker against the whiteboard."
    "Once the timestamps are normalized, three records remain. Any one of them could still be misleading on its own."

    n "Pick our next victim rookie."

    menu:
        "Trace the pager calls and callbacks.":
            "You map the incoming pages against calls returned from public phones. The pattern follows one neighborhood, but it cannot prove who stood at each receiver."
            n "Useful outline, fuzzy details. A pager tells us somebody wanted to talk. It does not tell us who picked up the pay phone."
        "Check the laundromat's handwritten refund log.":
            $ nick += 1
            "The attendant recorded the time, the jammed snack number, and an increasingly furious series of refund requests."
            n "That is either a very committed fake alibi or somebody met a vending machine with boundary issues. Let's see which."
        "Line up the traffic-camera stills.":
            $ nick += 1
            "You arrange the stills by intersection. Nicky leans across the table to rotate one you placed upside down, then leaves her hand beside yours while she studies it."
            n "There. Same coat, same posture. Now connect it to the paper trail."

    $ nicky_day_one_reveal = get_planned_route_reveal("nicky", 1)
    $ nicky_day_one_cleared_id = nicky_day_one_reveal["eliminated"][0]
    $ nicky_day_one_cleared_name = suspectNames[nicky_day_one_cleared_id]

    "With the records arranged beside one another, the alibi finally holds together. The receipt and refund log put [nicky_day_one_cleared_name] at the laundromat while a traffic camera catches them fighting the vending machine outside."
    "A second camera shows the machine winning."

    show nicky content happy at slot(0, total=1), bright zorder 10

    n "There they are. Wrong neighborhood, a clerk who remembers the argument, two independent cameras, and approximately four dollars lost to cheese crackers."
    n "Embarrassing? Absolutely. Murder? Unless that vending machine was Enrico in disguise, no."

    menu:
        "Clear them. Being humiliated in public isn't a crime.":
            $ nick += 2
            n "Then half this team narrowly avoids consecutive life sentences. I'll tell Ulysses the good news."
        "You already knew from their pheromones, didn't you?":
            $ nick += 1
            show nicky question at slot(0, total=1), bright zorder 10
            n "I knew they lied about why they were at the laundromat. Didn't know why they were lying though."
            n "Real evidence is more admissiable then 'they smelled weird.'"
        "Keep them on the list. They still look suspicious.":
            $ nick -= 2
            show nicky angry accusation at slot(0, total=1), bright zorder 10
            n "Absolutely not. We don't keep innocent people under suspicion because the truth has bad vibes."

    $ nicky_day_one_clue = "Pager records, a timestamped receipt, a witness statement, and independent street footage verify {}'s alibi.".format(nicky_day_one_cleared_name)
    $ record_planned_route_reveal(
        "nicky", 1, clue_text=nicky_day_one_clue, expected_count=1)

    show nicky content happy at slot(0, total=1), bright zorder 10

    "Nicky gathers the records slowly enough to keep the camera stills in order, then caps the marker with her teeth. The cleared suspect's name comes off the board with one clean swipe."
    n "One innocent person officially spared a week of superhero detective logic. That's a pretty good morning."
    n "And I appreciate the help, rookie. You made the paperwork less painful, which is almost impossible!"

    "She glances toward the vending machines in the hall, then back to the image of [nicky_day_one_cleared_name] losing their fight."

    n "After staring at those crackers for an hour, I need something that didn't come from behind reinforced glass. What are you grabbing before we file this?"

    menu:
        "Coffee. The report is going to need it.":
            n "Good call, could you get me one too? But if you call black coffee a personality trait, I'm leaving you here."
            "You return with two coffees. Nicky claims the one with more sugar and uses the cardboard sleeve to keep the camera stills flat."
        "Something sweet. We cleared an innocent person.":
            $ nick += 1
            n "Now that is evidence-based celebration. Get me whatever has the most ergregious amount of frosting."
            "The hallway kiosk has a pastry that qualifies. Nicky divides it with the edge of a clean evidence ruler and gives you the larger half."
        "Cheese crackers, in honor of the fallen four dollars.":
            $ nick += 1
            n "Cruel. Appropriate. Buy two. May the four dollars rest in piece."
            "You feed the machine enough money to prove the laundromat's hostility was personal. Nicky salutes the security camera before taking hers."

    "You take a short break in the hallway before returning to finish the report. By the time the file is signed, the room feels less like a crime board and more like a place where one person's week just became much easier."

    $ dayNick += 1
    jump endOfDay

label NickyDayTwo:
    scene debriefRoomOutline
    "Nicky arrives at the end of her shift carrying two motorcycle helmets. One has been carefully modified with narrow openings for her antennae."

    show nicky content happy at slot(0, total=1), bright zorder 10

    n "I have spent six hours listening to three departments argue over who entered the wrong timestamp."
    n "I'm clearing my head before I start using the table as a stress ball. There's a limited pressing I want at a record shop across town."
    if dayWin >= 5:
        n "Yes, I know the final meeting is close. That is exactly why I need one hour where nobody says 'chain of custody' at me."
    n "You can come if you want!"

    "She tosses you the second helmet."

    menu:
        "Gladly. You drive, I'll hold on.":
            $ nick += 2
            show nicky curious flirty at slot(0, total=1), bright zorder 10
            n "Oh, I know you will. I go fast."
        "Is this how detectives invite people on dates?":
            $ nick += 2
            n "No clue. I'll ask one if I see her."
            "Her antennae tilt toward you as she smiles."
        "I suppose I can tolerate a record store.":
            $ nick -= 1
            show nicky question at slot(0, total=1), bright zorder 10
            n "Try not to drown me in enthusiasm, rookie."

    "Nicky waits while you fit the helmet, then reaches over to tighten the loose strap beneath your chin. Her fingers linger just long enough for her antennae to tilt with amusement."
    n "There. I'd hate to explain to Ulysses that I lost the new hire before we reached the first stoplight."

    n "We have some time. Pick a route: fast, scenic, or dealer's choice?"

    menu:
        "Fast. Show me what the bike can do.":
            $ nick += 1
            $ nicky_day_two_route = "fast"
            n "Bold answer from somebody sitting behind me. Keep both arms available."
        "Scenic. I want to see the city.":
            $ nicky_day_two_route = "scenic"
            n "Scenic it is. Still fast, though. I'm clearing my head, not growing moss."
        "Dealer's choice. Surprise me.":
            $ nick += 1
            $ nicky_day_two_route = "surprise"
            n "Dangerous amount of trust in me this early, rookie. I like it."

    scene black with fade
    "The motorcycle tears away from ATLAS, the engine swallowing the last of the office noise. Nicky takes the first few streets easily, giving you time to settle behind her before the road opens up."
    "At the first hard turn, your arms tighten around Nicky's waist."
    "She laughs loudly enough for you to hear through both helmets."

    n "Relax back there! The bike isn't going anywhere I don't tell it to."

    "Twenty minutes later, she rolls to a stop beneath a faded record-store awning. She removes her helmet, shakes out her hair, and checks that both antennae survived the trip."
    "Inside, old concert flyers cover the walls from floor to ceiling. The record store owner greets Nicky by name"

    show nicky content happy at slot(0, total=1), bright zorder 10

    n "We're looking for the new album from Backseat Royalty. Limited pressing, ridiculous cover, excellent bass."
    n "Important question. We get one album for the ride to the diner. What are you picking?"

    menu:
        "The loudest hip-hop album in the store.":
            $ nick += 2
            $ nicky_day_two_music = "hiphop"
            n "Now we're cooking. Let's find a bass line that makes the shelves shake."
        "Something romantic. Purely for scientific reasons.":
            $ nick += 2
            $ nicky_day_two_music = "romantic"
            show nicky curious flirty at slot(0, total=1), bright zorder 10
            n "Uh-huh. Very subtle. Practically undercover."
        "The calmest classical album available.":
            $ nick -= 1
            $ nicky_day_two_music = "classical"
            show nicky question at slot(0, total=1), bright zorder 10
            n "Damn. I thought we were getting along too."

    "Nicky disappears into the hip-hop aisle and gives you half of a stack to browse. She has an opinion about every cover you lift: too polished, secretly excellent, one good track, career-ending hat."
    "Eventually, she pulls out the Backseat Royalty pressing. The cover shows three crowned figures crammed into the rear of a tiny sedan, all glaring at the driver."

    menu:
        "Admit the ridiculous cover is great.":
            n "Thank you. Art should make you ask at least one question the artist refuses to answer."
        "Ask what makes this pressing special.":
            $ nick += 1
            n "Alternate mix on the last track, heavier drums, and only five hundred copies. Also, I wanted it."
        "Tell her the driver is clearly the real star.":
            $ nick += 1
            n "Finally, somebody respects the working class! Backseat royalty gets all the attention while that hero finds them parking."
    n "Look, they have a listening station! Let me show you what peak hip-hop sounds like."
    "At the listening station, Nicky fits one side of the headphones over her antenna and passes you the other. The short cord forces you shoulder to shoulder."
    "A heavy beat begins. Her fingers tap the counter in perfect time."

    show nicky curious flirty at slot(0, total=1), bright zorder 10

    n "Rookie, either shared headphones terrify you or you're nervous for a more interesting reason."

    menu:
        "You're standing this close on purpose.":
            $ nick += 2
            n "Good observation. Took you long enough."
        "Yes, detective, it's not the headphones.":
            $ nick += 2
            n "How honest."
            "Nicky's mandibles shift around a satisfied smile."
            n "Good little rookie."
        "Then stop smelling me.":
            $ nick -= 1
            show nicky question at slot(0, total=1), bright zorder 10
            n "I can't turn my nose off, but I can stop helping you make this fun."

    "Nicky walks away, buying the record, tucking it carefully into the bike's storage compartment, and holding the shop door for you with an exaggerated little bow."
    show nicky content happy at slot(0, total=1), bright zorder 10
    n "I'm thining we can get some food real quick. C'mon, I know a place!"
    scene black with fade
    "The ride to the diner is shorter and slower. Backseat Royalty blasts through the bike's speakers while late-afternoon traffic gathers around you."
    "At the diner, Nicky claims a booth and loosens her tie. A server drops two menus between you and waits with a pen poised."

    n "Order carefully. I judge people by breakfast food at non-breakfast hours."

    menu:
        "A burger and fries.":
            $ nicky_day_two_order = "burger"
            "The server writes it down. Nicky orders the same burger and adds extra pickles."
            n "Solid choice. Difficult to ruin, easy to steal fries from."
            "She shoots you a wink."
        "A full stack of pancakes.":
            $ nick += 1
            $ nicky_day_two_order = "pancakes"
            "Nicky's antennae perk as the server writes down your order. She adds hash browns and a milkshake to hers."
            n "Excellent disregard for the clock. Breakfast is for every meal."
        "A salad. Something light after the ride.":
            $ nicky_day_two_order = "salad"
            "Nicky orders a patty melt and studies you over the top of her menu."
            n "Responsible. Suspicious, but responsible. I'm still making you try the fries."

    "The server leaves. For a while, the conversation stays easy: terrible album covers, the bike, and Nicky's theory that every diner owns the same three coffee mugs."
    "When the food arrives, she waits until the server has gone, arranges the ketchup and sugar caddy into a less obstructive formation, and settles deeper into the booth. Only then does her voice turn quieter."

    show nicky at slot(0, total=1), bright zorder 10

    n "You know, my first week in uniform, I spent four hours arguing that a rescue report needed the name of the person who actually found the weapon."
    n "Everybody else thought the arrest was the exciting part. I was the rookie ruining the celebration by asking whether any of it would survive court."

    "She says it fondly. This is not a complaint about the work; it is a story she has clearly enjoyed telling before."

    n "What did you figure I'd be doing, anyway? With the strength, the antennae, all of it."

    menu:
        "Police work. You care too much about doing things properly for anything else.":
            $ nick += 1
            n "Damn. Two days and you've already found my most annoying quality."
            "Her smile makes it clear she does not consider it a flaw."
        "Superhero work. You could throw the getaway car.":
            n "I can throw the getaway car. Then some poor detective has to explain why the fingerprints are underneath a sedan."
        "Whatever let you order people around.":
            $ nick += 1
            show nicky curious flirty at slot(0, total=1), bright zorder 10
            n "That answer sounds suspiciously informed. Maybe I should keep you where I can question you."

    n "I wanted the police before I knew what my powers would become. Warrants, evidence, somebody checking your work."
    n "Superheroes can save a city and leave the legal system crying in a parking lot. I like making sure the rescue survives court."

    "A laugh from the next booth draws a glance toward Nicky. One of the diners notices her mandibles, goes quiet, and pulls their bag closer."
    "Nicky notices. Her antennae dip for half a second before she reaches for another fry."

    n "And that part comes with the badge too. People see the antennae, the madibles, the badge, and decide what I am before I've said a word."
    n "I'm fine with how I look. I like how I look. Being judged before I get to do anything still gets old."

    menu:
        "The antennae suit you. Pass the fries.":
            $ nick += 2
            show nicky content happy at slot(0, total=1), bright zorder 10
            n "They do, don't they?"
            "She eats another fry, but her grin softens around the edges."
            n "Thanks for not turning it into a whole speech, rookie. That would've been awkward in the middle of a diner."
        "You shouldn't have to keep proving yourself.":
            $ nick += 1
            n "No, but everybody proves something eventually. I just make sure I pick what."
        "Surely the badge makes strangers less nervous?":
            $ nick -= 1
            show nicky sad upset at slot(0, total=1), bright zorder 10
            n "Sometimes. Other times they decide the badge must be a costume too. People get creative when they want their first guess to stay true."

    "The heavier moment passes without disappearing. Nicky nudges the ketchup toward you, tells you about the first suspect who tried to lie while wearing three kinds of cologne, and lets the story become ridiculous before the check arrives."
    "You linger long enough to finish your drinks and argue over which song should play first. Then Nicky pays her half, leaves an exact tip, and slides out of the booth."

    scene black with fade
    "Outside the diner, the evening air has cooled. Nicky starts the motorcycle, and Backseat Royalty blasts from its speakers."

    show nicky content happy at slot(0, total=1), bright zorder 10

    if nick >= NICKY_WARM_THRESHOLD:
        "She hands you a small record-store bag. Inside is the album you spent the longest looking at."
        n "Don't make it weird. Unless you're planning to make it interesting."
    elif nick >= NICKY_FRIENDLY_THRESHOLD:
        "She passes you her copy of the album."
        n "Borrow it. I expect it back without fingerprints, scratches, or a tragic new appreciation for mellow music."
    else:
        "She writes an album title on the back of the diner receipt and hands it to you."
        n "Homework. Listen to that before you choose the soundtrack next time."

    "You climb onto the motorcycle behind her. This time, she waits until your arms are firmly around her before accelerating."

    $ dayNick += 1
    jump endOfDay

label NickyDayThree:
    scene debriefRoomOutline
    "Nicky has converted the debrief table into a case-file grid. Every folder has been reduced to clipped cards: source records, measurements, corrections, and suspect summaries."
    "She has also left one clear place setting at the near side of the table, complete with a pencil, a legal pad, and a paper cup bearing your name in thick marker."

    show nicky content happy at slot(0, total=1), bright zorder 10

    n "Today's assignment is matching every claim to something that actually supports it."
    n "Reading the files in order takes hours. Turning them into a memory game takes slightly fewer hours and makes federal paperwork almost tolerable."

    "The door swings open. Razzle Dazzle rushes in carrying a half-burned witness form."

    show nicky at slot(1, total=2), dim zorder 0
    show razzle hoorah at slot(0, total=2), bright zorder 10

    r "HELLO, FELLOW INVESTIGATORS! I'm here to request witness information through the proper channels like Ulysses told me too!"

    show nicky content happy at slot(1, total=2), bright zorder 10
    show razzle at slot(0, total=2), dim zorder 0

    n "Wow. Look who finally showed up to investigate the murder."

    show razzle question at slot(0, total=2), bright zorder 10
    show nicky at slot(1, total=2), dim zorder 0

    r "I've been investigating! Socially."
    r "The witness kept saying the person looked huge, but they also said the coat was big enough to hide a family of raccoons. Is that important?"

    "A small flame eats through the corner of the duplicate form in Razzle's hand. She pats it out against the table."

    show nicky question at slot(1, total=2), bright zorder 10
    show razzle at slot(0, total=2), dim zorder 0

    n "The coat detail is useful. The arson is less useful."
    n "Take the witness-language summary and go ask what they actually saw underneath the silhouette."

    show razzle hoorah at slot(0, total=2), bright zorder 10
    show nicky at slot(1, total=2), dim zorder 0

    r "Professionally acquired! Thank you!"

    hide razzle
    show nicky at slot(0, total=1), bright zorder 10

    n "Wow, three full seconds. That's a new record."
    n "She's right about the coat, though. We have to separate measurements from assumptions before we rule anybody out."

    "Nicky gives the singed witness form time to cool before slipping it into a protective sleeve. Then she replaces the card Razzle borrowed and turns the whole grid toward you."

    menu:
        "Show me how you sorted the sources before I touch the cards.":
            $ nick += 2
            n "Look at you respecting procedure without becoming boring about it."
        "You made federal paperwork into a game. I respect the hustle.":
            $ nick += 1
            show nicky content happy at slot(0, total=1), bright zorder 10
            n "Thank you. Crime is temporary. Finding ways not to die of boredom is forever."
        "The strongest impact came from the biggest suspect. Start there.":
            $ nick -= 2
            show nicky angry accusation at slot(0, total=1), bright zorder 10
            n "You are standing beside a short woman who can lift thousands of pounds. Try that assumption again."

    n "Two rounds. Match each claim to independent support. Speed is nice; accuracy is nicer. Neither one changes what the evidence says."

    menu:
        "Start with witness claims.":
            n "Messiest pile first. I respect it. Remember: a witness can be honest and still interpret what they saw incorrectly."
        "Start with measured scene evidence.":
            $ nick += 1
            n "Stable foundation. Then we test how much of the witness language it can actually support."
        "Start with suspect summaries.":
            n "Tempting, but keep those face-down until a claim earns one. We fit suspects to evidence, not evidence to suspects."

    "Nicky demonstrates one sample pair, breaks it apart again, and shuffles it back into the grid. Only when you can explain why the cards belong together does she start the clock."

    call RulesNickyMemory
    $ start_nicky_memory_minigame()

    $ nicky_day_three_build = nicky_memory_result["build"]
    $ nicky_day_three_removed_names = ", ".join(nicky_memory_result["eliminated_names"])

    show nicky content happy at slot(0, total=1), bright zorder 10

    if nicky_memory_result["completed"]:
        if nicky_memory_result["quality"] == "perfect":
            n "No mismatches, no hints, and you beat the clock twice. Very profesh rookie!"
        elif nicky_memory_result["quality"] == "steady":
            n "A few wrong pairings, but you corrected them instead of getting stuck, good work!"
        else:
            n "Messy process, valid result. Luckily, the law does not require you to be graceful."
    else:
        n "You knew when to hand over the files. That's better than bluffing your way into a bad conclusion."

    if nicky_memory_result.get("scope") == "category":
        n "The verified measurements do not support a [nicky_day_three_build] attacker."
        n "That clears [nicky_day_three_removed_names]."
    else:
        n "The corrected measurements conflict with those two individual booking profiles."
        n "That clears [nicky_day_three_removed_names] without pretending everybody with a similar build is interchangeable."

    menu:
        "Force never established build. The records did.":
            $ nick += 2
            show nicky curious flirty at slot(0, total=1), bright zorder 10
            n "There it is. You followed the records without trying to sound like a courtroom drama."
            n "Competent and not boring. Annoyingly close to my type, rookie."
        "Your card game made paperwork almost fun.":
            $ nick += 1
            n "Almost? Damn. I'll add some dramatic lighting next time."
        "So the witness was just wrong.":
            $ nick -= 1
            show nicky question at slot(0, total=1), bright zorder 10
            n "The witness described what they perceived. Our job is separating perception from measurement, not blaming them for being human."

    n "I'll package the result for Ulysses. You can tell him we made bureaucracy entertaining without setting anything important on fire."

    "You help Nicky return every card to its source folder. She reads each identifier aloud, you confirm it against the log, and the playful grid slowly becomes an ordinary evidence packet again."
    "By the time the last clip closes, Razzle's burned corner is the only sign the room ever stopped being professional."

    n "Five-minute break before I package this. You pick the soundtrack."

    menu:
        "Play the Backseat Royalty album.":
            $ nick += 1
            n "Look at you remembering the important evidence."
        "Find something neither of you has heard.":
            $ nick += 1
            n "Risky. I approve. If it's terrible, the break becomes four minutes."
        "Leave the room quiet.":
            "Nicky leans back, closes her eyes, and lets the silence last without trying to entertain either of you."

    "For five minutes, the case files remain closed. When Nicky sits forward again, the work feels like something you are returning to rather than something that swallowed the entire day."

    "The two of you finish your work for the day and Nicky leaves you to your report."

    $ dayNick += 1
    jump endOfDay

label NickyDayFour:
    scene debriefRoomOutline
    "Three versions of the original incident report hang beside enlarged crime-scene photographs. Somebody has underlined the phrase LARGE, POWERFUL ATTACKER in red."

    show nicky at slot(0, total=1), bright zorder 10

    n "The first responding officer saw a broken table, a dented wall, and Enrico thrown across a room."
    n "Then they wrote 'large attacker,' and every report after that copied it like the first officer had personally measured the killer with a ruler."

    "Nicky hands you a marker and keeps another for herself. The two of you work down the first report line by line, circling observations and crossing through anything the officer inferred without support."

    "Nicky grips the heavy reconstruction table with one hand and lifts it high enough to inspect the underside."

    n "For reference, I can do this, and I do not have to be built like a refrigerator."

    menu:
        "The report observed force and invented build.":
            $ nick += 2
            show nicky content happy at slot(0, total=1), bright zorder 10
            n "Facts can imply things. They don't get to put on a fake mustache and pretend assumptions were there the whole time."
        "We should discard every report copied from it.":
            $ nick -= 1
            show nicky question at slot(0, total=1), bright zorder 10
            n "We correct the bad inference. We don't burn useful observations because one sentence got ambitious."
        "A police officer wrote it, so it should stay.":
            $ nick -= 2
            show nicky angry accusation at slot(0, total=1), bright zorder 10
            n "The badge does not make a guess become evidence. I say that as somebody currently wearing one."

    "Together, you separate direct observations from copied conclusions. It takes longer than tearing the pages down would have, but useful details survive: the table's direction of travel, the wall impact, and the order of the blood marks."
    "When the last copied sentence is corrected, the attacker's supposed size disappears from the reconstruction. Nicky steps back and lets you look at the cleaner board before adding anything new."

    $ nicky_day_four_injuries = suspectAttributes[killer]["injuries"]
    $ nicky_day_four_wound_hint = NICKY_WOUND_SCENE_HINTS[nicky_day_four_injuries]

    "Nicky aligns the corrected movement path with the window, wall, and blood-transfer photographs. [nicky_day_four_wound_hint]"

    "She places the photographs into sequence, then pulls one disputed evidence-bag record from the bottom of the stack."

    show nicky sad upset at slot(0, total=1), bright zorder 10

    n "Remember what I said at the diner? Reports can do the same thing people do. They see one obvious detail and let it decide everything that follows."
    n "People see the antennae and mandibles and decide what I am before I open my mouth. This officer saw force and decided what the attacker had to look like."
    n "Most days I can laugh about it. Other days I would like to fold somebody's car into a tasteful metal cube. Legally, I do and can not."

    menu:
        "The antennae suit you. Which report is next?":
            $ nick += 2
            show nicky curious flirty at slot(0, total=1), bright zorder 10
            n "They do."
            n "The bag record. Right here."
        "You shouldn't have to prove yourself every time.":
            $ nick += 1
            n "I shouldn't. But if I'm proving something anyway, I might as well make it undeniable."
        "At least nobody here treats you differently.":
            $ nick -= 1
            show nicky question at slot(0, total=1), bright zorder 10
            n "That's nice, rookie, but pretending it never happens doesn't help when it does."

    show nicky at slot(0, total=1), bright zorder 10

    n "This preserved sample should resolve one more part of the reconstruction. The outer custody label has been corrected, but nobody signed the correction."
    n "We check it in person next time. Preferably with no flaming paperwork this time though."

    "Nicky photographs the corrected board before removing a single page. You take down the copies in reverse order while she rebuilds the official packet beneath them."
    "The disputed bag record stays out. She places it alone in a bright red folder, writes DO NOT TEST across the front, and tucks it under one arm for the walk to evidence control."

    n "Right, I'll see you tomorrow rookie!"

    $ dayNick += 1
    jump endOfDay

label NickyDayFive:
    scene labOutline
    "The preserved vial rests inside two layers of evidence packaging. Its inner seal is intact. The outer bag has a rewritten time, fresh tape, and no initials beside either correction."

    show nicky angry accusation at slot(0, total=1), bright zorder 10

    n "Somebody corrected this bag neatly enough to look official and forgot the part where official work identifies who did it."
    n "The evidence technician says it was routine. Their pheromones say they're lying about something."

    show nicky at slot(0, total=1), bright zorder 10

    n "Could be fear of discipline. Could be embarrassment. Could be murder. My nose doesn't get to pick one and call it probable cause."

    "The evidence technician waits beyond the glass while Nicky opens a fresh incident form. She does not touch the package until the original seal number, correction, and missing initials have all been photographed."

    menu:
        "Photograph it, quarantine it, and report the broken chain.":
            $ nick += 2
            show nicky content happy at slot(0, total=1), bright zorder 10
            n "That's the move. Preserve the problem with the evidence, then make somebody sign every breath they take near it."
        "Test it now. A correct result matters more than the paperwork.":
            $ nick -= 2
            show nicky enraged at slot(0, total=1), bright zorder 10
            n "A correct result obtained carelessly is how a guilty person walks free."
        "Throw it away and pretend we never received it.":
            $ nick -= 2
            show nicky angry accusation at slot(0, total=1), bright zorder 10
            n "Destroying compromised evidence is still destroying evidence. Please never improvise around an evidence locker again."

    "Nicky files the discrepancy and calls evidence control. The call takes twenty minutes, two supervisors, and one very long hold tune. She puts it on speaker so both of you can suffer equally."
    "When authorization finally arrives, the technician joins you as a witness. The intact inner vial is opened for one limited investigative test while Nicky reads each step into the record."

    $ nicky_day_five_blood_type = suspectAttributes[killer]["blood_type"]
    $ nicky_day_five_rh_factor = suspectAttributes[killer]["rh_factor"]
    $ nicky_day_five_blood_profile = nicky_day_five_blood_type + nicky_day_five_rh_factor
    $ nicky_day_five_blood_reaction = NICKY_BLOOD_REACTION_TEXT[nicky_day_five_blood_profile]

    "Nicky divides the trace across three labeled wells: Anti-A, Anti-B, and Anti-D. [nicky_day_five_blood_reaction]"

    show nicky question at slot(0, total=1), bright zorder 10

    n "Clumping means the corresponding marker is present. Anti-D is the positive factor; no Anti-D reaction is negative."
    n "Useful direction, not a courtroom exclusion though. The broken outer chain stays attached to every sentence we write about this."

    menu:
        "Keep it as a lead and request a clean comparison.":
            $ nick += 2
            n "That's how it stays useful. We learn from uncertain evidence without pretending the uncertainty vanished."
        "Your nose and the test agree. That's enough for me.":
            $ nick -= 1
            show nicky question at slot(0, total=1), bright zorder 10
            n "Flattering. Still not how proof works."
        "Then the whole test was pointless.":
            $ nick -= 1
            n "Nope. Leads tell us where to look. Proof tells us what we can claim when we get there."

    "The vial returns to its inner packaging. You watch the technician reseal it, then follow Nicky through the signatures required to transfer it back into secure storage."
    "Only after the locker closes does she exhale and tug her tie loose."

    scene debriefRoomOutline with fade
    "Later, the lab lights have given way to the debrief room's dim television glow. Nicky drops two beers and a pile of vending-machine snacks onto the table. An episode of The Y-Files waits paused on a blurry flying saucer."

    show nicky content happy at slot(0, total=1), bright zorder 10

    if nicky_day_two_order == "pancakes":
        n "I considered pancakes, but seven minutes isn't enough time to defend syrup from you."
    elif nicky_day_two_order == "salad":
        n "No salad tonight. You survived one responsible meal this week; don't get greedy."
    elif nicky_day_two_order == "burger":
        n "No communal fries this time. The vending machine refused to recognize shared custody."

    n "Seven minutes. No reports, no evidence seals, no superheroes asking whether a crater counts as property damage."
    n "Seven whole minutes off. Think you can handle that, rookie?"

    menu:
        "Pick the spicy chips.":
            $ nick += 1
            "Nicky tears the bag open and immediately regrets how much seasoning reaches her antennae. She eats another anyway."
        "Pick the chocolate bar.":
            "Nicky breaks it cleanly in half and slides your share across the table."
        "Let Nicky choose.":
            $ nick += 1
            "She pushes the pretzels toward you and claims the chips, chocolate, and one of the beers."
            n "Delegation is an important investigative skill. So is protecting your snacks."

    menu:
        "Seven minutes off? I can think of a better name for that.":
            $ nick += 2
            $ nicky_day_five_break_mood = "flirt"
            show nicky curious flirty at slot(0, total=1), bright zorder 10
            n "Then say it like you mean it, rookie. I enjoy watching suspects commit to an answer."
        "You deserve seven minutes where nobody needs anything from you.":
            $ nick += 1
            $ nicky_day_five_break_mood = "kind"
            n "Damn right I do. Hand me the chips."
        "We should use the time to finish the report.":
            $ nick -= 2
            $ nicky_day_five_break_mood = "work"
            show nicky question at slot(0, total=1), bright zorder 10
            n "Wet blanket behavior. Deeply disappointing."
            "She takes the report folder from your side of the table and puts it beneath her chair, where reaching for it would require moving her."
            n "Seven minutes. You can survive being irresponsible that long."

    if nick >= NICKY_WARM_THRESHOLD and nicky_day_five_break_mood != "work":
        "Nicky settles close enough that her shoulder remains against yours. Her antennae angle toward you."
        n "You got nervous again."
        "She leaves the observation there instead of explaining how she knows. More importantly, she does not move away."
    elif nicky_day_five_break_mood == "work":
        "Nicky starts the episode and plants both boots on the hidden report folder. She passes you the snacks without moving closer, committed to enforcing the break you tried to cancel."
    else:
        "Nicky opens a beer and provides increasingly aggressive commentary about the fictional agents' refusal to request warrants."

    "Before the episode ends, the secure fax on the far wall begins printing: the final warrant returns, recent interview images, and a behavioral profile are ready for review."

    n "There's our next problem. Tonight, the government is hiding aliens in a filing cabinet and these idiots still haven't documented the search."

    "She leaves the pages face-down in the fax tray and lets the episode finish. The message remains unanswered for the promised seven minutes—and several more after that."

    "In time, the two of you finish some episodes and depart, leaving the paper for tomorrow."

    $ dayNick += 1
    jump endOfDay

label NickyDaySix:
    scene debriefRoomOutline
    "Six suspect files cover the table. Each contains recent interview images, lawful search photographs, personal-hygiene observations, and a copy of the corrected crime-scene profile."

    show nicky at slot(0, total=1), bright zorder 10

    n "Final profile. The killer's behavior after the attack tells us how they handle being physically dirty."
    n "The psychology unit compared that behavior with the warrant returns and recent interviews. I double checked their work because I don't enjoy sleeping at night."

    "Instead of handing you a conclusion, Nicky divides the table into three sections: physical residue, documented behavior, and records obtained under warrant."
    n "Choose where we start. Every section has to agree before anybody comes off this board."

    menu:
        "Start with the physical residue.":
            $ nick += 1
            n "Hardest evidence first. Then we see whether the human behavior actually lines up with it."
        "Start with the documented behavior.":
            n "All right. Patterns, not single bad days. Nobody becomes a murderer because their sink had dishes once."
        "Start with the warrant records.":
            $ nick += 1
            n "Paperwork first. Somewhere, a judge just felt appreciated and doesn't even know why."

    "You spend the next hour moving between the three sections. Whenever one item seems decisive, Nicky makes you find its support in the other two before it stays on the board."

    $ nicky_day_six_hygiene = suspectAttributes[killer]["organization"]
    $ nicky_day_six_hygiene_text = NICKY_HYGIENE_PROFILE_TEXT[nicky_day_six_hygiene]

    "Nicky projects the residue analysis beside the six lawful suspect records. [nicky_day_six_hygiene_text]"

    n "I could smell which interviews made people nervous. That helped me decide what questions to ask. It does not appear anywhere in the proof."

    menu:
        "Use the residue, warrant photographs, and repeated behavior together.":
            $ nick += 2
            show nicky content happy at slot(0, total=1), bright zorder 10
            n "Three independent supports, one conclusion, and none of them is 'trust my weird ant nose.' That can survive review!"
        "Your pheromone sense is good enough. Skip the rest.":
            $ nick -= 2
            show nicky angry accusation at slot(0, total=1), bright zorder 10
            n "No. My power guides an interview. It does not convict somebody."
        "This sounds like judging people by how they look.":
            $ nick += 1
            n "It would be if we stopped at a photograph. That's why we require the matching physical trace and repeated documented behavior."

    "Nicky checks the search authorizations, image dates, and laboratory controls one final time. She gives you the dates to read back while she verifies the signatures, then turns the profile around for one last shared review."
    "Only after both of you reach the same three names does she sign it."

    $ nicky_day_six_clue = "Corroborated residue and lawful records identify the attacker's personal hygiene as {}.".format(nicky_day_six_hygiene.lower())
    $ record_planned_route_reveal(
        "nicky", 6, clue_text=nicky_day_six_clue, expected_count=3)

    show nicky content happy at slot(0, total=1), bright zorder 10

    n "Verified. Three suspects remain."
    n "The official evidence gets us that far. Choosing the right one means you actually paid attention this week."

    menu:
        "We make a good team, detective.":
            $ nick += 2
            show nicky curious flirty at slot(0, total=1), bright zorder 10
            n "We do. Try not to sound so surprised, rookie."
        "Good work. Everything is ready for Ulysses.":
            $ nick += 1
            n "And not one illegal shortcut in the pile. I knew I liked having you around."
        "Finally. I thought the paperwork would never end.":
            $ nick -= 1
            show nicky question at slot(0, total=1), bright zorder 10
            n "The paperwork is how the ending survives longer than five minutes."

    if nick >= NICKY_HIGH_THRESHOLD:
        if nicky_day_two_music == "romantic":
            "A suspiciously romantic track begins playing quietly from Nicky's portable cassette player. She notices you recognize it and does not pretend the selection was accidental."
        elif nicky_day_two_music == "classical":
            "A bass-heavy remix of the classical album you chose begins playing quietly from Nicky's portable cassette player. She notices your surprise."
            n "I improved your evidence. You're welcome."
        else:
            "Backseat Royalty begins playing quietly from Nicky's portable cassette player. She notices you recognize the song."
        show nicky curious flirty at slot(0, total=1), bright zorder 10
        if nicky_day_two_music == "hiphop":
            n "I bought myself another copy. You still have mine."
        else:
            n "I kept your pick in the rotation. Don't make that expression."
        n "Don't look so pleased. You make the paperwork less painful, rookie. That's all you're getting before the report is filed."
    elif nick >= NICKY_WARM_THRESHOLD:
        n "You made this week easier and significantly less boring. That's a rare combination, I appreciate it."
    else:
        n "The case file is clean, lawful, and ready. Get it to Ulysses."

    n "Go on. I'll lock up the evidence and make sure nobody turns my debrief room into a game night while I'm gone."

    "You stay long enough to return the six files to their cabinet. Nicky locks it, checks the handle, and lowers the room's projector. The three remaining names are the last thing to disappear from the wall."

    $ dayNick += 1
    jump endOfDay

label WinstonDayOne:
    scene winstonOfficeOutline
    "Winston's office door is open. Three folders have been stacked into a ramp from his desk to the wastebasket, and Winston is attempting to roll a pencil down it without touching either side."
    "The pencil reaches the final folder, veers left, and lands beneath the couch."

    w "That was the control run."
    w "Hey, newbie. You here to work, or do you have the good sense to lie?"

    menu:
        "I'm here to work. Unfortunately.":
            $ winn += 1
            w "Tragic. Fine. We suffer as fast as possible, try to finish early."
        "I came to witness an important scientific breakthrough.":
            $ winn += 2
            w "Finally, somebody recognizes leadership when they see it."
            w "The grant money should arrive any minute at this point."
        "Ulysses said you needed supervision.":
            w "Ulysses says a lot of things."

    "Winston retrieves the pencil, drops it into a cup already crowded with darts, and nudges the case folder toward you. His posture changes before the folder stops moving."
    w "One suspect downstairs lied twice in the preliminary statement and once about whether they'd lied."
    w "Doesn't make them the killer. Does make them irritating."
    w "Pick a job before we go in."

    menu:
        "Take notes and watch for contradictions.":
            $ winn += 2
            $ winston_day_one_role = "notes"
            w "Good choice. Write down what changes, not how guilty their face looks."
        "Stay quiet and watch their reactions.":
            $ winn += 1
            $ winston_day_one_role = "observer"
            w "Good. Silence makes people rush to fill it. Usually with something stupid."
        "Act as the second interviewer.":
            $ winn += 1
            $ winston_day_one_role = "interviewer"
            w "All yours when I give you the opening. Try not to accuse them of murder before we sit down newbie."

    $ winston_day_one_reveal = get_planned_route_reveal("winston", 1)
    $ winston_day_one_cleared_id = winston_day_one_reveal["eliminated"][0]
    $ winston_day_one_cleared_name = suspectNames[winston_day_one_cleared_id]
    $ winston_day_one_lie = WINSTON_DAY_ONE_LIES[winston_day_one_cleared_id]

    scene black with fade
    "The interview room is an unused office with the personal objects removed. Winston brings three sodas, gives the suspect first choice, and leaves the case folder closed."
    "[winston_day_one_cleared_name] sits opposite him, prepared for an interrogation and visibly confused by the lack of one."

    w "Let's save time. You lied about where you were. I don't care unless the truth puts you in Enrico's house."
    "[winston_day_one_cleared_name] denies it. Winston asks about the weather, the nearest pay phone, and whether the chair is uncomfortable. None of it sounds relevant until the same ten-minute gap moves three times."

    if winston_day_one_role == "notes":
        "Your notes place the changing answers side by side. Winston glances down once and taps the gap with his finger."
        w "Newbie found the hole. Want to stop digging around it?"
    elif winston_day_one_role == "observer":
        "Every question about the murder earns an immediate answer. The harmless questions about the missing ten minutes make [winston_day_one_cleared_name] look toward the door."
        w "There it is. Not murder scared. Embarrassing-story scared."
    else:
        "Winston leans back and gives you the room."
        w "Your turn, newbie. Ask about the part they keep trying to walk around."

    menu:
        "Ask what happened during the missing ten minutes.":
            $ winn += 2
            "You ask without supplying an accusation. The silence lasts until [winston_day_one_cleared_name] realizes you intend to let it."
        "Guess that they were hiding a different crime.":
            $ winn += 1
            w "Maybe. Or maybe they did something legal and catastrophically uncool."
        "Tell Winston to shut down their power until they cooperate.":
            $ winn -= 2
            "Winston's expression empties of humor."
            w "No. I can get an answer without ripping away part of somebody because they made us impatient."
            w "Try a question. They're cheaper."

    "The resistance finally collapses. [winston_day_one_cleared_name] admits to [winston_day_one_lie]."
    "The embarrassing story comes with a receipt, two phone calls, and an independent witness. Together they cover the entire period surrounding Enrico's death."

    w "See? Lied their ass off. Also didn't kill anybody. People contain multitudes. Most of the multitudes are humiliating enought to risk being tried for murder."

    menu:
        "Clear them. The lie and the murder are separate questions.":
            $ winn += 2
            w "Exactly. Suspicious isn't a conviction, and shame isn't a murder weapon."
        "That was almost disappointingly reasonable.":
            $ winn += 1
            w "Sorry. Tomorrow I'll interrogate somebody by hanging them upside down over a shark if you think that'll work better."
        "Keep them listed anyway. A liar is a liar.":
            $ winn -= 2
            w "Then we'd have to investigate everybody who ever filled out an ATLAS expense form. Including me. Especially me."

    $ winston_day_one_clue = "A verified account of {} clears {} despite the false preliminary statement.".format(winston_day_one_lie, winston_day_one_cleared_name)
    $ record_planned_route_reveal(
        "winston", 1, clue_text=winston_day_one_clue, expected_count=1)

    scene winstonOfficeOutline with fade
    "Back upstairs, Winston throws the cleared file onto the correct pile without looking. It lands squarely between two folders and stops."
    w "Lunch before paperwork. If we reverse that order, civilization as we know it ends."
    w "I'm ordering takeout, what do you want?"

    menu:
        "Order greasy burgers and fries.":
            $ winn += 1
            $ winston_day_one_takeout = "burgers"
            w "Newbie, you may survive this place after all."
            "Winston adds a large soda and enough extra sauce to endanger the paperwork."
        "Order pizza for the office.":
            $ winn += 1
            $ winston_day_one_takeout = "pizza"
            w "Foundational ATLAS cuisine. Half our early policies were written over pizza boxes."
            "He orders one for the room and another under Ulysses's name, claiming this makes it an administrative expense."
        "Get sandwiches so the files stay clean.":
            $ winston_day_one_takeout = "sandwiches"
            w "Responsible and deeply boring. Put extra sauce on mine so there's still danger."
            "He selects the messiest sandwich on the menu, restoring what he considers the necessary level of risk."

    "The food arrives before Winston begins the formal report. He clears a space by transferring the clutter from one side of his desk to the other, then hands you the first portion."
    "Between bites, he tells you that before ATLAS he was an ordinary working superhero: stop the powered criminal, level the playing field, then win the fistfight."
    w "Turns out founding an organization is mostly fighting paperwork, and paperwork doesn't lose its powers when I stare at it."
    w "Ulysses and I were doing the work together years before ATLAS had a name. Back then it was less 'organization' and more 'please stop the teenager from filing mission plans under my door.'"
    w "Still. One innocent person off the board. Not a bad first round."
    "He raises his drink toward you before opening the report. By the time you leave for the daily meeting with Ulysses, the jokes have returned, but the document is complete and exact."

    $ dayWinn += 1
    jump endOfDay

label WinstonDayTwo:
    scene winstonOfficeOutline
    "Winston is asleep on the couch with one boot on the armrest and the other planted on a stack of unsigned supply requests. Mariah Carey plays quietly from a radio beside his desk."
    "The investigation folder is closed. A handwritten sign on top reads DAY OFF. THIS MEANS ME."

    menu:
        "Wake him by turning up the radio.":
            $ winn += 1
            "Winston opens one eye before you reach the dial."
            w "Don't. I was one chorus away from solving the case subconsciously."
        "Throw one of the couch cushions at him.":
            $ winn += 2
            "He catches it without opening his eyes and throws it back hard enough to knock the door shut behind you."
            w "Morning, newbie. Strong opening."
        "Let him sleep and inspect the dartboard.":
            "Three darts sit tightly grouped near the center. A fourth has pinned an expense form to the wall."
            w "That one's filed. Don't let Ulysses tell you otherwise."

    "Winston sits up, rubs both hands over his face, and checks the clock. He shows no alarm at the time."
    w "I have made an executive decision. I'm doing absolutely fucking nothing today."
    if dayWin >= 6:
        w "Final meeting's breathing down our necks. Which means if I don't take one afternoon now, Ulysses will find me fused to this couch tomorrow."
    elif dayWin >= 5:
        w "Final meeting's breathing down our necks. This is our last responsible window for irresponsible behavior."
    w "You can come. Not officially a date. It may be shaped suspiciously like one, but I need plausible deniability and a witness in case the waitress thinks I'm sad for eating alone."

    menu:
        "Obviously not a date. You'd have dressed up.":
            $ winn += 2
            w "This is my formal tank top. Put some respect on it's name."
        "I'd be happy to go with you.":
            $ winn += 1
            w "That eager, huh? Great. Now the waitress is definitely going to think I planned this."
        "Shouldn't we be investigating?":
            $ winn -= 1
            w "Next time. Today I'm demonstrating sustainable leadership by fleeing the building."

    scene black with fade
    "Winston insists on calling a taxi. When you ask why the cofounder of ATLAS does not drive, he lists three crashes, a flooded loading dock, and an incident involving a statue that the city still blames on him."
    w "Bad luck. Every single time."
    "The taxi driver looks at him in the mirror and silently locks the window controls."

    "At the diner, Winston claims a booth beneath a humming neon sign. He orders a super-greasy burger, fries, and the largest soda they sell."
    w "Your turn. Order something I can steal without violating labor law."

    menu:
        "Order another burger and fries.":
            $ winn += 1
            $ winston_day_two_order = "burger"
            w "Excellent. Mutual assured indigestion."
        "Order pancakes and something sweet.":
            $ winn += 1
            $ winston_day_two_order = "sweet"
            w "Breakfast after noon. That's the kind of disrespect for structure I can support."
        "Order coffee and something light.":
            $ winston_day_two_order = "light"
            w "Fine, be that way."

    "The food takes long enough for the booth to become comfortable. Winston tells you which jukebox songs Razzle will scream over, which ones make Dhampir pretend not to dance, and why Ulysses has banned team karaoke from formal events."
    if winston_day_two_order == "burger":
        "When the plates arrive, Winston takes one of your fries before touching his own."
    elif winston_day_two_order == "sweet":
        "When the plates arrive, Winston attempts to pour your syrup with the solemn precision of a surgeon. The result resembles a crime scene; he treats this as improved presentation."
    else:
        "When the plates arrive, Winston slides one of his onion rings onto your lighter plate and calls it a leadership-mandated nutritional compromise."

    menu:
        "Steal two of his fries in return.":
            $ winn += 2
            "Winston watches the second fry disappear and slowly moves his plate farther from you."
            w "Escalation. Bold move rookie."
        "Push your plate closer so he can stop pretending.":
            $ winn += 1
            w "This is entrapment. Delicious entrapment, but entrapment all the same."
        "Guard your plate with both arms.":
            w "You can't protect it forever, newbie. I founded an organization. I understand siege warfare."

    "A pager clipped to Winston's cargo pocket begins to chirp. He reads the number, closes his eyes, and walks to the diner's pay phone."
    "The first call is Razzle reporting that she melted a telephone handset while arguing with it. Winston explains that the replacement comes out of her entertainment budget."
    "The second arrives before the check. Dhampir phased through a filing cabinet and wants to know whether the papers that fell behind it still count as filed. Winston tells him to ask Nicky, then hangs up before Nicky can be added to the call."
    "The third message sounds urgent enough that Winston calls immediately. Ica has changed the gravity around a vending machine because it kept her money. Nobody is trapped; she simply refuses to turn it back until the machine apologizes."

    menu:
        "Make sure nobody is in danger, then unplug the pager.":
            $ winn += 2
            $ winston_day_two_calls = "screened"
            w "Safety confirmed, nonsense rejected. You may be management material. Sorry."
        "Tell him ATLAS can survive one afternoon without him.":
            $ winn += 1
            $ winston_day_two_calls = "ignored"
            w "That's what I keep saying. Ulysses keeps showing me projections with property damage."
        "Tell him a leader should go back immediately.":
            $ winn -= 1
            $ winston_day_two_calls = "answered"
            w "A leader should also teach people not to page him because a vending machine won an argument."

    "Winston pays, leaves a tip large enough to make the waitress check the amount twice, and guides you back into another taxi before the pager can object."
    w "C'mon, I have an idea to burn some more time."

    scene black with fade
    "The pool hall is dim, loud, and committed to pretending daylight does not exist. Winston feeds coins into the table, selects a cue, and claims he is not competitive before the balls have finished rolling into place."
    "He orders a drink, takes two slow swallows, then touches two fingers to his wrist. The haze leaves his expression at once."
    w "Useful trick. Getting sober on command. Makes terrible decisions much easier to schedule."

    menu:
        "Play seriously and make him earn every shot.":
            $ winn += 2
            $ winston_day_two_pool = "serious"
            w "There you go. If I win, I want it to mean you tried."
        "Cheat whenever his back is turned.":
            $ winn += 1
            $ winston_day_two_pool = "cheat"
            "You move one ball by less than an inch. Winston returns, studies the table, and moves it another inch in your favor."
            w "If we're cheating, commit. Half-measures insult the craft."
        "Lose deliberately so he can enjoy winning.":
            $ winn -= 1
            $ winston_day_two_pool = "threw"
            "After the third suspicious miss, Winston catches the rolling cue ball and sets it in your hand."
            w "Don't hand me a win like I'm six. Beat me or embarrass yourself honestly."

    "The match stretches through two songs and a rematch Winston insists does not count as competitiveness. By the end, your drinks have warmed and his pager has begun chirping again from inside his jacket."
    "He takes it out, reads the fourth message, and turns it face down."
    w "Madeline needs authorization to borrow equipment she already borrowed. That's a Ulysses problem."
    "For the first time since leaving ATLAS, nothing else interrupts. Winston rolls the cue between his palms and watches the empty table."
    w "Everybody there can do something impossible. Fire, flight, seeing tomorrow, whatever."
    w "Then something goes wrong and they look for me to make the stop. Normally they go to Ulysses first, but I'm the 'oh-shit' handle who won't lecture them."
    w "Just makes it hard to tell when people want me around and when they want a nice emergency brake."

    menu:
        "I like you better when you're not working anyway.":
            $ winn += 2
            w "..."
            w "You know, saying that while we're alone in a pool hall makes it sound suspiciously like flirting."
            "He looks down the cue to hide a smile and fails."
        "They need you because you know when to let them be ridiculous too.":
            $ winn += 2
            w "Yeah, I guess somebody has to point them in the right direction without making them march there. God knows Uly won't."
        "Being useful isn't the worst problem to have.":
            w "No. Just gets weird when useful becomes the only version people ask for."
        "That sounds unbearably tragic.":
            $ winn -= 1
            w "Please don't pity me in a building with this much sticky carpet. I have standards."

    "Winston gives the silence several seconds, visibly loses patience with it, and challenges you to one last shot before leaving."

    scene winstonOfficeOutline with fade
    "Back at ATLAS, a handwritten list waits on Winston's desk. Ulysses has organized the day's disasters by urgency, responsible party, and estimated repair cost."
    "Somebody screams from deeper in the building. Winston looks at the list, then at you."
    w "Still off the clock."

    menu:
        "Check whether the scream involved actual danger.":
            $ winn += 1
            $ winston_day_two_exit = "check"
            w "Fine. If it's murder, fire, or structural collapse, we help. If it's a spider, we delegate."
        "Stay here and help him sort Ulysses's list.":
            $ winn += 1
            $ winston_day_two_exit = "sort"
            w "Romantic. Two people, one desk, four preventable disasters."
        "Leave him to deal with it.":
            $ winston_day_two_exit = "leave"
            w "Fair. Save yourself, newbie. I'll deny we ever had this conversation."

    if winston_day_two_exit == "check":
        "You follow the scream together. It involves a spider and an overturned wastebasket; Winston rights the basket while you relocate the spider under the supervision of three unhelpful spectators."
        "He returns muttering about heroism, then walks with you to the end-of-day report."
    elif winston_day_two_exit == "sort":
        "The scream turns out to involve a spider and an overturned wastebasket. Winston shouts instructions from his desk until somebody else handles both, then divides Ulysses's list between you."
        "You finish the urgent items before walking together to the end-of-day report. The rest remain later problems."
    else:
        "You leave him with the scream, the list, and his final afternoon of freedom. By the time you reach Ulysses's office for the end-of-day report, Winston is in the hall arguing that spider removal qualifies as field leadership."

    $ dayWinn += 1
    jump endOfDay

label WinstonDayThree:
    scene winstonOfficeOutline
    "Suspect folders form a crooked row across Winston's desk. Beside them sits a deck of cards labeled ATLAS CONTROLLED PRESSURE SYSTEM in marker."
    "Dhampir stands near the door in his hero suit, arms folded, expression severe enough to make the office feel several degrees colder."

    w "Newbie, welcome to behavioral science! Or interrogation 101 if you want to call it that."
    d "I'm bad cop."
    w "He practiced that in the hall by the way."
    d "No, I didn't."
    w "Yes he did."

    menu:
        "Ask about the pressure system.":
            $ winn += 2
            w "It's our system for questioning suspects. Pressure builds stress. Question them when you get as close to their highest stress without pushing them over the edge."
        "Ask whether Dhampir is allowed to hurt the suspects.":
            $ winn += 1
            d "I wish."
            w "This is why he gets supervised during interrogation."
        "Say you can question people without a system.":
            $ winn -= 1
            w "Anybody can be an asshole in a small room. The point is controlling the pressure well enough to learn something."

    "Winston leads you downstairs."
    "One by one, the active suspects wait in a separate office while Winston resets the room. Dhampir remains where each new arrival can see him through the glass."

    w "Right, let's get started."

    call RulesWinstonPressure
    $ start_winston_pressure_minigame()

    if winston_pressure_phase == "dhampir_pause":
        scene black
        "At the midpoint, Winston gestures toward Dhampir."
        w "One turn Dhampir, one turn."
        "Dhampir slides into the chair. His shoulders square, his voice drops, and every trace of the man who argued about darts disappears."
        d "You will answer the next question truthfully."
        "The suspect stares at him, waits for the threatened question, and answers it in fully the instant Dhampir asks."
        "Dhampir turns back toward the observation window. His posture loosens."
        d "Did I do it right?"
        w "You were supposed to apply pressure, not make them see God."
        d "God would've killed them. I was merciful."
        "Dhampir turns to the suspect"
        d "Remember that."
        w "Go play darts in my office before you scare the rest shitless."
        d "Rad."
        "Dhampir leaves with the same casual wave he used when he arrived. The next suspect enters moments later and looks relieved until Winston and you re-enter."
        $ winston_pressure_dhampir_turn()
        $ resume_winston_pressure_minigame()

    scene winstonOfficeOutline with fade
    $ winston_day_three_cleared = " and ".join(winston_pressure_result.get("cleared_names", []))

    if winston_pressure_result.get("quality") == "controlled":
        w "No shutdowns, no wasted pressure, and nobody cried except the guy Dhampir looked at. Clean work newbie!"
        $ winn += 2
    elif winston_pressure_result.get("quality") == "recovered":
        w "You pushed too far a couple times, backed off, and fixed it. That's why the resets exist."
        $ winn += 1
    elif winston_pressure_result.get("quality") == "assisted":
        w "You knew when to hand me the chair. Better than pretending control means never needing help."
        $ winn += 1
    else:
        w "Messy as hell, but nobody left worse than they entered and we got there eventually."

    w "The useful part: [winston_day_three_cleared] don't fit the behavioral timeline. They're off the board."
    "Winston files the individual interview summaries behind the formal result."

    menu:
        "Dhampir was your idea, wasn't he?":
            $ winn += 1
            w "Yeah. Everybody else saw a terrifying vampire vigilante. I saw a terrifying vampire vigilante who followed rules he respected. Also a chill dude."
        "You trust Dhampir a lot.":
            $ winn += 2
            w "With my life. With office furniture, less so."
        "Recruiting Dhampir still seems insane.":
            $ winn -= 1
            w "Most worthwhile decisions look insane until you let them proves themself."

    "You help return the chairs before taking the completed report to Ulysses."

    w "Go have fun talking to my better half. Catcha ya on the flip side!"

    $ dayWinn += 1
    jump endOfDay

label WinstonDayFour:
    scene winstonOfficeOutline
    "A takeout menu has been pinned over Winston's official interview plan. The witness sitting across from his desk appears unsure whether this is deliberate."
    "A dart lands in the board beside the menu. Winston does not look away from the witness when he throws it."
    w "Newbie. Perfect. We were just discussing how formal this interview is."
    "The witness saw the killer moving through the rear hall shortly after the attack. Their earlier statement described distance and direction; Winston has invited them back to describe habits."

    menu:
        "Join the casual act and ask about something harmless first.":
            $ winn += 2
            $ winston_day_four_interview = "casual"
            "You ask whether the witness wants a drink. Their shoulders loosen while Winston pretends to search for a clean cup."
            w "Don't open the bottom drawer. Those cups became an ecosystem and I want them to lead their lives."
        "Quietly prepare the notes while Winston performs.":
            $ winn += 1
            $ winston_day_four_interview = "quiet"
            "You leave the first line blank and wait. The witness begins talking to fill the room."
        "Ask why this isn't happening in a real interrogation room.":
            $ winn -= 1
            $ winston_day_four_interview = "formal"
            w "Because people rehearse for interrogation rooms. Nobody rehearses for whatever the hell my office is."

    "Winston asks about the rear hall without mentioning the killer. He talks about the dust, the narrow doorway, and how impossible it is to keep pale flooring clean. The witness corrects him twice before realizing they remember more than expected."

    $ winston_day_four_organization = suspectAttributes[killer]["organization"]
    $ winston_day_four_organization_hint = WINSTON_ORGANIZATION_INTERVIEW_HINTS[winston_day_four_organization]
    $ winston_day_four_hands = suspectAttributes[killer]["injuries"]
    $ winston_day_four_hand_hint = WINSTON_HAND_INTERVIEW_HINTS[winston_day_four_hands]

    "[winston_day_four_organization_hint]"
    "[winston_day_four_hand_hint]"

    w "Funny how powers shape habits. Fire users run hot even when nothing's burning. Ice users love acting like being calm makes them smarter. Light users get precious about dirt and order."
    w "Tendencies. Not commandments. People are still free to surprise you in uniquely stupid ways."

    menu:
        "Keep it as a tendency and ask the witness to continue.":
            $ winn += 2
            w "Exactly. A useful nudge, nothing we can use to accuse somebody."
        "Ask which habit the witness remembers most clearly.":
            $ winn += 1
            "Winston repeats the question without leading them. The witness returns to the physical demonstration ."
        "Is that enough to identify the killer?":
            $ winn -= 2
            w "Nope. That's how a clue becomes a prejudice wearing a little detective hat."

    "A nervous vibration starts in the metal cup beside the witness. Their minor power rattles three pens and lifts a paperclip from the desk."
    "Winston's eyes brighten. The paperclip drops, and the room goes still. He dampens only the witness, releases them the moment their breathing settles, and continues in the same casual voice."
    w "There. Nobody's in trouble. Take your time."
    "The witness finishes the account, checks the written wording, and leaves with a copy of the office number. Winston waits for the door to close before retrieving the dartboard."

    w "Your reward for surviving serious work is deciding what stains the desk next."
    w "What'll we be having today newbie?"

    menu:
        "Order greasy burgers again.":
            $ winn += 1
            $ winston_day_four_takeout = "burgers"
            w "Consistency, one of the less celebrated leadership virtues. I like it."
        "Order pizza and make him choose the toppings.":
            $ winn += 1
            $ winston_day_four_takeout = "pizza"
            w "Pepperoni, peppers, and whatever topping will annoy Ulysses if he steals a slice."
        "Order noodles and protect the case files.":
            $ winston_day_four_takeout = "noodles"
            w "A challenge meal. Respect. Move the photographs."

    # Fix this area please to sound better
    "While you wait, Winston hands you three darts"
    "Your first dart lands near the outer wire. Winston's lands beside it instead of in the center."
    w "Damn. We're both mediocre."

    menu:
        "You're convincing until you start caring.":
            $ winn += 2
            "Winston turns a dart between his fingers and studies it more closely than necessary."
            w "You keep noticing where the act ends. Rude. Possibly attractive, but rude."
        "You missed on purpose.":
            $ winn += 1
            w "Prove it. Preferably after I finish eating."
        "Maybe Ulysses is the competent founder.":
            $ winn -= 1
            w "He is. Doesn't mean I'm not too."

    "The food arrives, and the story Winston tells follows in pieces. Winston mentions meeting Ulysses six or seven years ago, when Winston was already a working superhero and Ulysses was thirteen going on forty."
    w "I had the idea for ATLAS. Loose team, shared resources, somebody to answer the phone when a building exploded."
    w "Ulysses turned it into an actual organization. Forms, projections, legal structure. Kid could make a filing cabinet feel real underqualified."
    w "I had the reputation people trusted. He had the plan that deserved it, so we needed each other. Still do I guess."

    "He says it proudly. When the conversation threatens to settle into sincerity, he throws another dart and pins the takeout receipt to the wall."
    w "Business expense filed."
    "You finish the meal, preserve the witness statement as an unconfirmed lead, thank Winston for the day, and carry the formal portion of the day to Ulysses."

    $ dayWinn += 1
    jump endOfDay

label WinstonDayFive:
    scene winstonOfficeOutline
    "Winston's office has been transformed into a crime scene by someone with no budget and very little respect for furniture. Masking tape marks Enrico's position. A coat rack represents the rear door. A pizza box has been labeled CABINET."
    "A returning witness stands just inside the doorway with an ATLAS escort. Their heightened hearing caught the aftermath from a hiding place, but fear broke the memory into disconnected sounds."
    w "Nothing here is real except the questions and the terrible interior design. We stop whenever you say stop."
    "The witness nods. Winston introduces you, then lets you choose where to help."

    menu:
        "Manage the props and keep the sequence organized.":
            $ winn += 1
            $ winston_day_five_role = "stage manager"
            w "Stage manager. Good. If the pizza box demands a dressing room, deny it."
        "Take the witness's hiding position and reproduce what they heard.":
            $ winn += 2
            $ winston_day_five_role = "witness"
            w "Good call, stay low and don't invent what you can't see newbie."
        "Stand at Enrico's marked position.":
            $ winn += 1
            $ winston_day_five_role = "victim"
            w "All right. The tape is a reference point, so don't go getting theatrical on me."

    "Winston walks the witness through ordinary sounds first. A chair rolls. The desk drawer opens. He taps the cabinet with two knuckles and deliberately knocks over the coat rack."
    w "That's our highly trained door. It studied method acting."
    "The witness laughs once. The laugh makes the next silence less hostile."

    menu:
        "Let the witness set the pace.":
            $ winn += 2
            $ winston_day_five_care = "patient"
            "You wait for each nod before resetting a prop. Winston follows your timing."
        "Use gentle jokes to keep them grounded.":
            $ winn += 2
            $ winston_day_five_care = "grounded"
            "You give the coat rack an increasingly elaborate criminal history. The witness breathes more evenly between details."
        "Push through quickly before the memory changes.":
            $ winn -= 3
            $ winston_day_five_care = "pushed"
            "Winston's voice drops until there is no humor left in it."
            w "No. Their memory isn't more valuable than the person carrying it. We slow down."

    "Once the witness is ready, Winston takes the killer's position. He performs each remembered sound in isolation, then repeats only the sequence the witness confirms."

    $ winston_day_five_reaction = suspectAttributes[killer]["kill_reaction"]
    $ winston_day_five_reconstruction = WINSTON_REACTION_RECONSTRUCTION[winston_day_five_reaction]

    "[winston_day_five_reconstruction]"

    "Winston notices the pattern before you do. Nothing changes in his face, and he never supplies a word the witness has not chosen. He repeats the sequence twice, deliberately changing one sound each time so the witness can reject it."
    "On the final pass, every accepted noise fits within the same narrow stretch of time. The witness remains uncertain about the order of two moments."

    w "That's enough. You did the hard part. We'll verify the timing before anybody treats it like proof. Thank you so much."
    "The escort walks the witness out. Winston keeps his voice light until the door shuts behind them, then begins peeling tape from the floor."

    menu:
        "Help dismantle the scene without making him ask.":
            $ winn += 2
            $ winston_day_five_cleanup = "help"
            "You fold the tape back on itself while Winston restores the furniture to its approximately remembered locations."
        "Ask whether the pizza-box cabinet can stay.":
            $ winn += 1
            $ winston_day_five_cleanup = "watch"
            w "It's already more organized than the real one. Promotion approved."
        "Leave the cleanup to him.":
            $ winn -= 1
            $ winston_day_five_cleanup = "watch"
            w "Cruel. I expose the machinery behind my mysterious methods and you abandon me to adhesive residue."

    if winston_day_five_cleanup == "help":
        "The fake room disappears piece by piece beneath both sets of hands. Without the witness present, Winston no longer needs to keep the conversation moving, but he does anyway."
    else:
        "Winston dismantles the fake room piece by piece while you remain nearby. Without the witness present, he no longer needs to keep the conversation moving, but he does anyway."

    menu:
        "Ask why he always plays the fool.":
            $ winn += 2
            w "People guard themselves around a cofounder. They relax around an idiot with a dartboard."
            w "Then I get to see what they do before they remember to perform."
            w "Also, and this part is important, being an idiot is fun."
        "Tell him the act only works because he knows when to stop.":
            $ winn += 2
            w "That's the trick. A joke's supposed to make room, not take it away from somebody who needs it."
        "Tell him nobody believes his act.":
            w "They believe exactly as much as I need. You being annoyingly observant is a separate problem."

    if winn >= WINSTON_WARM_THRESHOLD:
        "Winston winds the discarded tape around two fingers, then stops playing with it."
        w "People call when they need the emergency brake. That's fair. It's the job."
        w "Playing the fool is how I make sure the job doesn't become the only version of me anybody gets."
        "He glances at you, measuring whether the admission needs a joke. This time he lets it stand."

    if winn >= WINSTON_WARM_THRESHOLD and winston_day_five_cleanup == "help":
        menu:
            "Leave your hand beneath his when you both reach for the tape.":
                $ winn += 2
                "Winston notices the contact and leaves his hand over yours after either of you needs help removing the tape."
                w "You know, you fit into my terrible methods disturbingly well."
                w "Little frightening. Mostly doing something else."
                "He releases your hand only when footsteps pass outside the office."
            "Pass him the tape and tell him somebody has to supervise him.":
                $ winn += 1
                "You peel up the strip and place it in his open palm."
                w "There it is. Romance dies under middle management."
            "Reach for a different strip and let the moment remain quiet.":
                $ winn += 1
                "Winston looks ready to fill the silence between you, then chooses not to."
    elif winn >= WINSTON_WARM_THRESHOLD:
        "When the last prop is put away, Winston leans beside you against the cleared desk instead of reclaiming the space behind it."
        w "You fit into my terrible methods disturbingly well. Cleanup habits aside."
        "His shoulder rests against yours for one quiet beat before he reaches for the tape roll."
    else:
        "Winston tosses you the last harmless prop and catches the tape roll when you throw it back."
        w "Not a bad reconstruction, newbie. Weird enough to work."

    "He packages the tentative sequence separately from the formal evidence. A second witness statement and the verified call timeline should arrive before your next session."
    "The two of you restore the office just enough for Winston to locate the door, then head toward the daily report with an impression, but not yet a conclusion."

    $ dayWinn += 1
    jump endOfDay

label WinstonDaySix:
    scene winstonOfficeOutline
    "The crude reconstruction from yesterday is gone. In its place, Winston has arranged the active suspect files, a telephone timeline, and a sealed written statement in three exact rows."
    "For once, there are no darts in his hand. His eyes move from timestamp to timestamp while you enter."
    w "Morning, newbie. Second witness heard the exit from the street. Phone company finally verified when the nearby call connected."
    w "Last time gave us a shape. Today we find out whether it holds weight."

    menu:
        "Verify the timeline before opening the statement.":
            $ winn += 2
            w "Good. That'll keep us from bending time around the answer we want."
        "Open the statement and compare it as you read.":
            $ winn += 1
            w "Make sure you don't let the first sentence bully the timestamps."
        "Trust the last reconstruction and skip the repeat.":
            $ winn -= 2
            w "No. Last time was useful. Useful and proven are not the same thing."

    "You verify the call connection, the responding unit's dispatch time, and the second witness's estimate against the same office clock. Winston makes you read the numbers aloud while he records them."
    "Only after the independent times agree does he break the seal on the new statement. Its description contains the same three sounds as the earlier reconstruction, but now their order can be fixed."

    $ winston_day_six_reaction = suspectAttributes[killer]["kill_reaction"]
    $ winston_day_six_reaction_display = WINSTON_REACTION_DISPLAY[winston_day_six_reaction]
    $ winston_day_six_sequence_attempts = 0

    jump WinstonDaySixSequence

label WinstonDaySixSequence:
    menu:
        "Collision, abandoned cleanup, then a hurried exit.":
            $ winston_day_six_sequence_choice = "Panicked"
        "Measured circuit, deliberate handling, then a controlled exit.":
            $ winston_day_six_sequence_choice = "Calculated"
        "Steady crossing, no intervention, then an ordinary departure.":
            $ winston_day_six_sequence_choice = "None"

    if winston_day_six_sequence_choice != winston_day_six_reaction:
        $ winston_day_six_sequence_attempts += 1
        if winston_day_six_sequence_attempts == 1:
            w "That version fights the verified call time. Try it again without asking the clock to lie for us."
        else:
            w "Still not it. Start with the first sound both witnesses independently placed."
        jump WinstonDaySixSequence

    if winston_day_six_sequence_attempts == 0:
        $ winn += 2
        w "There it is! The order matches the verified call time and the witnesses' independent memories."
    else:
        $ winn += 1
        w "That's it. Took the scenic route, but the order holds."

    "Winston repeats the final sequence in neutral language and sends it back through both statements. Neither account needs to be stretched to make it fit."
    w "The killer's post-crime reaction was [winston_day_six_reaction_display]."

    $ winston_day_six_clue = "Corroborated witness timing identifies the killer's post-crime reaction as {}.".format(winston_day_six_reaction_display)
    $ record_planned_route_reveal(
        "winston", 6, clue_text=winston_day_six_clue, expected_count=3)
    $ winston_day_six_remaining_names = ", ".join(
        [suspectNames[suspect_id] for suspect_id in remainingSuspects])

    w "That leaves [winston_day_six_remaining_names]."
    w "Three people. Everything else we've noticed is yours to weigh when Ulysses asks for the name."
    "He closes the formal evidence. The three remaining files stay visible on the desk."

    menu:
        "Tell him you trust the work you did together.":
            $ winn += 2
            w "Good. Trust the work. Save trusting me blindly for something funnier."
        "Tell him he is frighteningly competent when he stops playing.":
            $ winn += 2
            w "Frighteningly? Keep talking like that and Dhampir's going to get jealous."
        "Say Ulysses can choose among the final three.":
            $ winn -= 1
            w "He could. He hired you because he wants your judgment too. Don't crawl out of the hard part now newbie."

    "Winston signs the final interview packet, carries it to the outgoing tray, and then takes the dart cup from the corner of his desk."
    w "Case is as far as it gets today. One throw before the report."
    "He hands you a dart and steps behind you. You see Winston go to correct your stance but stop."

    menu:
        "Guide his hand to your waist.":
            $ winn += 2
            $ winston_day_six_waist_contact = True
            "His hand settles at your waist, deliberate enough that neither of you can mistake it for ordinary instruction."
        "Guide his hand to your wrist.":
            $ winston_day_six_waist_contact = False
            "Winston nods and teaches a lesson focused on your grip."
        "Step aside and take the throw alone.":
            $ winston_day_six_waist_contact = False
            "You reset your stance on your own."
    if winn >= WINSTON_HIGH_THRESHOLD and winston_day_six_waist_contact:
        "Your dart remains raised while Winston realizes where his hand is. A flush reaches his face before the familiar grin can cover it."
        menu:
            "Lean back and ask if this is part of his leadership method.":
                $ winn += 2
                w "Advanced training. Extremely limited enrollment."
                "His hand stays where it is until you finally throw."
            "Tell him he can move closer if he needs a better angle.":
                $ winn += 2
                w "Direct. Jesus, newbie."
                "He moves closer anyway, then clears his throat when the dart hits the board."
            "Let him retreat without teasing him.":
                $ winn += 1
                "Winston steps back slowly, still smiling at the floor."
                w "Very professional of both of us. Nobody check the security footage."
    elif winn >= WINSTON_WARM_THRESHOLD and winston_day_six_waist_contact:
        "Winston notices the intimacy a beat late and moves his hand, suddenly fascinated by your grip on the dart."
        w "Right. Technique. That's what we're doing."
    else:
        "Winston watches the throw with an approving nod."
        w "Better. Still ugly, but accurately ugly."

    "The dart lands inside the inner ring. Winston plants a second beside it and leaves both in the board."
    w "You stayed for the work, the nonsense, and the part where the nonsense turned back into work."
    w "That's... useful to know."
    "He reaches for another joke, thinks better of it, and picks up the final report instead."
    w "Come on. Ulysses is waiting, and if we make him wait too long he'll develop a second forehead vein."
    "You leave the three suspect files on the desk and walk with him toward Ulysses's office. Winston stops at the door, bumps your shoulder, and leaves the formal report to you."

    $ dayWinn += 1
    jump endOfDay

label IcaDayOne:
    scene cubicleOutline
    "You make your way to Ica's cubicle, where you see her already sitting with her feet kicked up, chewing gum."
    "An unopened case folder props up one corner of her desk. A paper cup rests on top of it, safely protecting the evidence from the table."
    show ica at slot(0, total=1), bright zorder 10
    i "Sup freshie. Come to slack off a bit?"
    i "I was gonna play solitaire, but dealing all those cards sounds exhausting."
    i "You wanna save me the effort and be a real opponent?"
    "Ica flicks a deck into the air. The cards hang there while she lazily plucks them into two neat piles."
    i "Shuffling is work. Gravity isn't."

    menu:
        "Sure. Deal me in.":
            $ ica_cards_selected_approach = "play_fair"
            show ica happy at slot(0, total=1), bright zorder 10
            i "Cool. Grab a chair."
            $ ica += 2
        "Only if we make the stakes interesting.":
            $ ica_cards_selected_approach = "flirt"
            $ ica += 1
            show ica flirty at slot(0, total=1), bright zorder 10
            i "Easy, freshie. Win a few hands before you start negotiating date night."
        "Try to peek at the top card while she deals.":
            $ ica_cards_selected_approach = "cheat"
            "The top card suddenly becomes too heavy to lift. Ica has not moved her feet from the desk."
            $ ica -= 2
            show ica happy at slot(0, total=1), bright zorder 10
            i "Gravity. Great for catching cheaters without sitting up."
            i "I'm gonna pretend I missed that. This should be funny."

    "You pull over the least cluttered chair. Ica does not lower her feet; instead, she makes the wastebasket drift aside so you can fit beside the desk."
    "The suspended cards divide themselves into two hands. A bowl of stale candy rises from the filing cabinet and settles between you."

    i "Pick your poison. Nobody's eaten the green ones since, like, February."

    menu:
        "Take a green one.":
            $ ica += 1
            $ ica_day_one_candy = "green"
            "The candy tastes faintly medicinal. Ica watches you chew it with the detached interest of somebody observing a lab rat."
            i "Huh. Still alive. Useful data."
        "Take anything except green.":
            $ ica_day_one_candy = "safe"
            i "Coward. Smart coward, but still."
        "Slide the bowl back to her.":
            $ ica += 1
            $ ica_day_one_candy = "none"
            i "More for me. Probably. I don't wanna reach for it yet."

    "Ica deals one slow practice hand, mostly to establish which rules she plans to ignore. Once both of you have cards arranged, she uses gravity to dim the desk lamp without getting up."

    call RulesIcaCards
    $ start_ica_cards_minigame(ica_cards_selected_approach)
    $ ica_cards_result = ica_minigame_results.get("cards", {})

    if not ica_cards_result.get("completed", False):
        i "Calling it early? Fair. I can respect a strategic retreat."
    elif ica_cards_result.get("won", False):
        if ica_cards_result.get("approach") == "flirt":
            show ica flirty at slot(0, total=1), bright zorder 10
            i "Okay, the banter almost worked. The cards did the rest, so don't get too smug, loser."
        elif ica_cards_result.get("approach") == "cheat":
            show ica happy at slot(0, total=1), bright zorder 10
            i "You know I saw you peek, right? Still counts, I guess. I don't really feel like stopping you. Too much work."
        else:
            show ica happy at slot(0, total=1), bright zorder 10
            i "Huh. You won and you're not even making a thing out of it. Kinda annoying. Kinda cool."
    else:
        show ica at slot(0, total=1), bright zorder 10
        if ica_cards_result.get("approach") == "flirt":
            i "Cute distraction. Shame you forgot to win."
        elif ica_cards_result.get("approach") == "cheat":
            i "You put in all that effort to avoid putting in effort and still lost. Beautiful."
        else:
            i "You lose. No excuses, no speech. I like your style, freshie."
    show ica at slot(0, total=1), bright zorder 10

    "Neither of you puts the cards away. One hand becomes three, then a lazy argument about whether a floating card counts as being played. At some point the office lights shift into their evening setting."

    menu:
        "Suggest one last hand.":
            $ ica += 1
            i "Dangerous. That's how you end up accidentally committed to something. Deal."
            "The cards drift back into place. Ica deals so slowly that you have time to finish the stale candy between draws, then wins on a rule she admits she invented halfway through."
            i "There. Now we can stop on a completely legitimate victory."
        "Ask if she ever planned to open the case folder.":
            $ ica -= 1
            i "Yeah. Tomorrow. Or a different tomorrow. It isn't going anywhere."
            "She lifts the cup off the folder with gravity, considers the cover for a full second, then puts the cup back."
        "Lean back and enjoy doing nothing for a minute.":
            $ ica += 1
            "Ica nods once, as if you have finally demonstrated a difficult skill."
            i "Now you're getting it."
            "The two of you sit without manufacturing a reason for it. Even the loose cards settle onto the desk."

    i "Oh, wow. We somehow burned the whole day."
    i "Go tell Ulysses we investigated cards. I'll back you up if he doesn't ask me to walk over."
    "Ica rolls her chair away from the desk, leaving you to report to Ulysses."

    $ dayIca += 1
    jump endOfDay

label IcaDayTwo:
    scene cubicleOutline
    "You make your way back to Ica's cubicle, where she is reclined so far in her chair that only her shoes are visible over the desk."
    show ica at slot(0, total=1), bright zorder 10
    i "Oh, look who's back? Enjoy slacking off last time?"
    if dayWin >= 6:
        i "Final accusation's tomorrow, by the way. Figured I'd mention it before we bravely continue doing nothing."
    elif dayWin >= 5:
        i "Final accusation's getting close, by the way. Figured I'd mention it before we bravely continue doing nothing."

    menu:
        "Yeah! It killed a day.":
            $ ica += 1
            show ica happy at slot(0, total=1), bright zorder 10
            i "See? You get it. Bare minimum, maximum results."
        "Of course. I really enjoyed spending time with you.":
            $ ica -= 1
            show ica shock at slot(0, total=1), bright zorder 10
            i "..."
            show ica at slot(0, total=1), bright zorder 10
            i "Cringe."
        "We wasted so much time.":
            $ ica -= 2
            show ica whatTheFuckDidYouJustDoMC at slot(0, total=1), bright zorder 10
            i "Yeah. That was the point."
            i "Also, you chose to be here, dude. No one made you slack off."
    show ica at slot(0, total=1)
    i "Anyway, I was gonna play cards again, but the deck is all the way over there."
    "She gestures toward a shelf within easy walking distance."
    i "Wanna do something stupid to pass the time like a staring contest?"
    i "First person to blink loses. Minimal setup, zero cleanup. Basically the perfect sport."

    "Ica finally lets the front legs of her chair touch the floor. She uses her power to roll your chair across the cubicle until the two of you are facing each other."

    i "We need rules, I guess. No throwing stuff in each other's eyes. Too much cleanup."

    menu:
        "Suggest best two out of three.":
            i "That's dangerously close to planning ahead. Fine. Gives me more chances to embarrass you."
        "Suggest the loser has to get drinks.":
            $ ica += 1
            i "Now the stakes matter. There's a soda machine down the hall and I don't wanna see it personally."
        "Say one round is enough.":
            $ ica += 1
            i "Efficient. Whoever invented tournaments was trying too hard anyway."

    menu:
        "Sure. Beats working.":
            $ ica_staring_selected_approach = "play_fair"
            show ica happy at slot(0, total=1), bright zorder 10
            $ ica += 2
            i "Look at cha, soon you'll be a bigger bum than me."
        "You just wanted an excuse to stare at me.":
            $ ica_staring_selected_approach = "flirt"
            show ica flirty at slot(0, total=1), bright zorder 10
            $ ica += 1
            i "Maybe. Or maybe I forgot every other game. Don't make it weird, dude."
        "Use her reflection in the dark monitor.":
            $ ica_staring_selected_approach = "cheat"
            show ica at slot(0, total=1), bright zorder 10
            i "You keep looking at that monitor, freshie. I'm sure it's nothing suspicious."

    call RulesIcaStaring
    $ start_ica_staring_minigame(ica_staring_selected_approach)
    $ ica_staring_result = ica_minigame_results.get("staring", {})

    if ica_staring_result.get("completed", False):
        $ ica_staring_apply_relationship_result()
        if ica_staring_result.get("won", False):
            if ica_staring_result.get("approach") == "flirt":
                show ica flirty at slot(0, total=1), bright zorder 10
                i "Okay, staring at me while saying that was annoyingly effective. Take your win I guess."
            elif ica_staring_result.get("approach") == "cheat":
                show ica happy at slot(0, total=1), bright zorder 10
                i "You were watching my reflection, weren't you? What a bore, I respect it though."
            else:
                show ica happy at slot(0, total=1), bright zorder 10
                i "Huh. Guess I blinked. Damn. Good game."
        else:
            show ica at slot(0, total=1), bright zorder 10
            if ica_staring_result.get("approach") == "flirt":
                i "You almost had me. Then you got too pleased with yourself. Take the L, bozo."
            elif ica_staring_result.get("approach") == "cheat":
                i "You cheated at staring and still blinked first. How are you so bad at winning?"
            else:
                i "You blinked. No excuses? Nice. Makes gloating way easier."
    else:
        show ica at slot(0, total=1), bright zorder 10
        i "Calling it early? Fair. The staring contest will still be here when you're ready to lose properly."

    show ica at slot(0, total=1), bright zorder 10

    "When the contest ends, both of you sit blinking tears from your eyes. Ica presses the heels of her hands against her face, then makes two cold soda cans float in from somewhere beyond the cubicle wall."

    i "Don't ask whose these were. They belong to us now."

    "The competition drifts into an argument over whether looking away counts as losing if something interesting catches fire nearby. Neither of you notices the office emptying around you."
    i "Oh damn, that contest took longer than I thought. Day's already over."
    i "Go pick another way to look busy, freshie. Catch you later."
    "Ica heads toward the front desk, leaving you in the office."

    $ dayIca += 1
    jump endOfDay

label IcaDayThree:
    scene winstonOfficeOutline
    "You find Ica and Winston sitting on the floor of his office with a short pawn-race board between them."
    "Winston is arranging the pieces with more energy than you have seen him put into anything resembling work."
    show ica at slot(0, total=1), bright zorder 10

    i "Yo, freshie. Perfect timing. We need a third."
    w "YES! Thank god, a third player! Pick a color, recruit."
    i "Told you he'd be into it."
    w "Ulysses had me doing paperwork all morning. You two just saved my life."

    menu:
        "Sit down and pick a color.":
            $ ica_board_selected_approach = "play_fair"
            $ ica += 2
            show ica happy at slot(0, total=1), bright zorder 10
            w "Red, blue, or green? Actually, I'm green. Pick one of the other two."
        "Sit beside Ica. \"Try not to get distracted.\"":
            $ ica_board_selected_approach = "flirt"
            $ ica += 1
            if ica >= ICA_EARLY_FLIRT_THRESHOLD:
                show ica flirty at slot(0, total=1), bright zorder 10
                i "That's a lot of confidence for somebody in bumping distance."
            else:
                show ica at slot(0, total=1), bright zorder 10
                i "Dude. At least wait until I send your pawn home before you get weird."
        "Tell them you all have actual work to do.":
            $ ica_board_selected_approach = "play_fair"
            $ ica -= 2
            show ica whatTheFuckDidYouJustDoMC at slot(0, total=1), bright zorder 10
            i "Then go do it. We'll tell you who wins."
            w "Don't bring the W-word into my office. Sit down and pick a pawn. Boss's orders"

    "Winston clears a space for you and shoves a red pawn into your hand."
    w "Okay! Short race. Pick one of two movement cards on your turn."
    i "Land on one of the other pawns and it goes back to start. Simple."
    w "Reach or pass the finish to win! If you overshoot, you stop at the finish."
    i "And no moving pieces with gravity. Apparently that's cheating."
    w "It is cheating, and I will absolutely call you out unless it happens to somebody else."
    i "Isn't this just Bump Off, but shorter?"
    w "Legally distinct. Ours has worse pieces and executive sponsorship."
    i "Cool."

    "Winston produces three drinks and an open bag of chips from behind his desk like he prepared for this exact emergency."

    w "Refreshments! Pick now. Ica keeps stealing the coldest one without touching it."

    menu:
        "Take the coldest drink before Ica can.":
            $ ica += 1
            "The can lifts off the floor at the same moment you reach for it. Ica makes you tug against its weight for a second before letting go."
            i "All that effort for a soda. Couldn't be me."
            w "First victory of the day! Count it!"
        "Take the warm drink nobody wants.":
            $ ica += 1
            i "Damn. Completely immune to stakes."
            w "No, no, we can get you ice! We have standards in this office!"
        "Let Winston choose.":
            w "Dealer's choice! You get the mystery flavor!"
            i "That's either grape or floor cleaner. Good luck."

    "Ica takes a blue pawn. Winston grabs green, then starts shuffling the movement cards far more dramatically than necessary."
    "The race begins."

    call RulesIcaBoard
    $ start_ica_board_game_minigame(ica_board_selected_approach)
    $ board_result = ica_minigame_results.get("board", {})

    if board_result.get("completed", False):
        $ ica += ica_relationship_change_for_result(board_result)
        if ica_board_winner == "player":
            show ica happy at slot(0, total=1), bright zorder 10
            i "You got there first. Don't get smug about it, freshie."
            w "REMATCH! I'm not ending the workday on a loss!"
        elif ica_board_winner == "ica":
            show ica happy at slot(0, total=1), bright zorder 10
            i "Race is over. I win. Try to keep up next time."
            w "No! I was one turn away!"
        else:
            show ica at slot(0, total=1), bright zorder 10
            w "YES! THAT'S HOW IT'S DONE!"
            i "Congrats, Winnie. You won the game in your own office. Huge day for you."
            w "Thank you! Finally, some respect!!"
    else:
        "The race ends before anybody can call a winner. Winston immediately starts resetting the pieces."
        w "That one didn't count. Again."

    "Winston immediately starts another round. Between games, the three of you debate house rules, build a cup-holder out of unused paperwork trays, and lose one pawn beneath his desk for nearly twenty minutes."
    "Ica could retrieve it with a thought. She waits until Winston is fully under the desk before doing so."

    w "IT WAS IN MY HAND!"
    i "Wild. Office might be haunted."


    if ica >= ICA_WARM_FLIRT_THRESHOLD:
        show ica flirty at slot(0, total=1), bright zorder 10
        i "Freshie's the only one making this interesting anyway."
        w "Ooooooh."
        i "We're not flirting."
        w "I didn't say which one of you was flirting."
        i "..."
        i "Shut up, Winnie."
    else:
        show ica happy at slot(0, total=1), bright zorder 10
        i "Freshie's not bad at this. For a freshie."

    "The final game ends only because the automatic lights dim around you. By the time the three of you finally look up, the entire workday is gone."

    w "Same time next round? I have darts too."
    i "See, freshie? Winnie gets it."
    w "We can move the desk and make room for both."

    $ dayIca += 1
    jump endOfDay

label IcaDayFour:
    scene cubicleOutline
    "You arrive at Ica's cubicle to find dozens of hot dogs spread across two trays."
    show ica happy at slot(0, total=1), bright zorder 10

    i "Freshie. I made an important discovery that's gonna change your fucking life."
    i "The hot dog place down the street gives you a discount if you order an irresponsible amount of food."

    "She points at the trays."

    "Beside them sits a chaotic row of condiments, paper plates, and a single roll of antacids that suggests Ica has considered exactly one consequence."

    i "So now we're having an eating competition. First empty tray wins."
    i "Loser has to throw everything away because I don't wanna get up."

    i "Build yours first. This is the only part where taste still matters."

    menu:
        "Ketchup and mustard.":
            $ ica_hotdog_style = "classic"
            i "Reliable. Hard to ruin. Kinda boring, but we're about to eat twenty of 'em, so boring helps."
        "Everything on the table.":
            $ ica += 1
            $ ica_hotdog_style = "everything"
            "Ica watches you add relish, onions, peppers, and something from an unlabeled bottle."
            i "You're either brave or trying to make losing medically necessary."
        "Plain. Fewer obstacles.":
            $ ica += 1
            $ ica_hotdog_style = "plain"
            i "That's bleak. Efficient, though. Respect."

    menu:
        "Move over. You're going down.":
            $ ica_eating_approach = "play_fair"
            $ ica += 2
            show ica happy at slot(0, total=1), bright zorder 10
            i "Hell yeah. No speeches, just hot dogs."
        "Loser owes the winner a date.":
            $ ica_eating_approach = "flirt"
            $ ica += 1
            if ica >= ICA_WARM_FLIRT_THRESHOLD:
                show ica flirty at slot(0, total=1), bright zorder 10
                i "Dude, this is already lunch. You're just trying to upgrade it."
                i "Fine. Win first."
            else:
                show ica at slot(0, total=1), bright zorder 10
                i "Cringe. Deal, though. Free food is free food."
        "Ask Ica to make your hot dogs lighter.":
            $ ica_eating_approach = "cheat"
            $ ica -= 2
            show ica whatTheFuckDidYouJustDoMC at slot(0, total=1), bright zorder 10
            i "You know lighter doesn't mean smaller, right?"
            i "You'd still have to eat the whole thing. That plan sucks."

    "The competition begins."

    "Within a minute, your strategy gives way to the horrible reality of eating far too many hot dogs before noon."

    i "Don't slow down now. I've already decided you're taking the trash out."

    "One of Ica's untouched hot dogs quietly floats off her tray, slips under the desk, and drops into the trash can behind her."

    menu:
        "Do the same thing while maintaining eye contact.":
            $ ica_eating_reaction = "match_cheat"
            $ ica += 2
            "One of your hot dogs rises from the tray. Ica catches it in midair with her power and redirects it back onto your plate."
            show ica happy at slot(0, total=1), bright zorder 10
            i "Saw that. Get your own superpower."
        "Distract her by wiping ketchup from her face.":
            $ ica_eating_reaction = "flirt_back"
            $ ica += 1
            if ica >= ICA_HIGH_FLIRT_THRESHOLD:
                show ica flirty at slot(0, total=1), bright zorder 10
                i "Cheap move, freshie."
                "Two more of her hot dogs disappear under the desk while she says it."
            else:
                show ica shock at slot(0, total=1), bright zorder 10
                i "Dude, what are you doing?"
                "While you recover, three of her hot dogs disappear under the desk."
        "Call her out for cheating.":
            $ ica_eating_reaction = "call_out"
            $ ica -= 1
            show ica at slot(0, total=1), bright zorder 10
            i "Prove it."
            "The trash can becomes too heavy to pull out from beneath the desk."
            i "Wow. Weird. Guess we'll never know."

    "With the rules thoroughly ruined, the two of you get back to the contest."

    call RulesIcaEating
    $ start_ica_eating_minigame(ica_eating_approach, ica_eating_reaction)
    $ eating_result = ica_minigame_results.get("eating", {})
    $ ica_eating_apply_relationship_result()

    if eating_result.get("completed", False):
        if eating_result.get("won", False):
            if ica_eating_approach == "play_fair":
                show ica happy at slot(0, total=1), bright zorder 10
                i "Okay, damn. You actually ate all that."
                i "I'm almost impressed. Mostly I'm glad you're still conscious enough to take out the trash."
            elif ica_eating_approach == "flirt":
                show ica flirty at slot(0, total=1), bright zorder 10
                i "You won. The flirting was cheap, but so were the hot dogs."
                i "I'll allow it."
            else:
                show ica happy at slot(0, total=1), bright zorder 10
                i "You tried the world's worst gravity plan, cheated anyway, and still won."
                i "That's a pretty solid commitment to doing less work."
        else:
            if ica_eating_approach == "play_fair":
                show ica happy at slot(0, total=1), bright zorder 10
                i "You made an honest effort. Disgusting. I win."
            elif ica_eating_approach == "flirt":
                show ica flirty at slot(0, total=1), bright zorder 10
                i "You got distracted by your own flirting. That's rough, freshie."
            else:
                show ica happy at slot(0, total=1), bright zorder 10
                i "You cheated and still lost."
                i "Honestly, that's funnier than me winning."
    else:
        show ica at slot(0, total=1), bright zorder 10
        i "Backing out means I win by default. Convenient rule I just made up."

    if ica >= ICA_HIGH_FLIRT_THRESHOLD:
        show ica flirty at slot(0, total=1), bright zorder 10
        i "If anybody asks, that wasn't a date."
        i "It was way cheaper than a date."
    else:
        show ica happy at slot(0, total=1), bright zorder 10
        i "I can't move. Great game."

    "For several minutes, neither of you speaks. The empty trays sit between you while the antacids make a slow orbit around Ica's head, waiting for somebody to surrender first."

    menu:
        "Take an antacid without comment.":
            $ ica += 1
            "Ica floats the bottle into your hand and takes two for herself."
            i "We're never telling anyone how bad this was."
        "Offer to throw everything away now.":
            i "Heroic. Wait ten minutes so I can enjoy not being the loser yet."
        "Suggest ordering dessert.":
            $ ica += 1
            "Ica stares at you long enough to resemble the hot-dog contest."
            i "You're terrifying, freshie."

    "Ica looks toward the hallway leading to Ulysses's office."

    i "You know what would be funny?"
    i "His office would look way better pink."
    i "Next time, bring clothes you don't care about. Or don't. Getting paint on the nice ones might be funnier."

    $ dayIca += 1
    jump endOfDay

label IcaDayFive:
    scene cubicleOutline
    "When you arrive, Ica is waiting beside several cans of bright pink paint, two rollers, and one tiny brush."
    "A folded tarp sits unopened beneath everything. Judging by the dust, Ica found it rather than bought it."
    show ica happy at slot(0, total=1), bright zorder 10

    i "Good, you're here."
    i "I need somebody to carry the paint."

    menu:
        "Hand me a roller.":
            $ ica_prank_approach = "play_fair"
            $ ica += 2
            i "Knew I kept you around for something."
        "Pink? Cute. Kinda like you.":
            $ ica_prank_approach = "flirt"
            $ ica += 1
            if ica >= ICA_HIGH_FLIRT_THRESHOLD:
                show ica flirty at slot(0, total=1), bright zorder 10
                i "Keep talking like that and you're painting the ceiling by yourself."
            else:
                show ica at slot(0, total=1), bright zorder 10
                i "That was terrible. You can carry both cans now."
        "Tell her this is childish.":
            $ ica_prank_approach = "cheat"
            $ ica -= 2
            show ica whatTheFuckDidYouJustDoMC at slot(0, total=1), bright zorder 10
            i "Yeah. That's why it's gonna be funny."
            i "You can either help or stand there and be boring."

    "Ica makes the paint cans follow you down the hall at ankle height. She still gives you the rollers to carry, apparently because using her power on all of it would feel too much like taking the task seriously."

    "Ulysses is away from his office for the morning. Ica opens the door and surveys the room without stepping inside."

    i "This is gonna take forever."

    "With a lazy wave of her hand, the desk, chairs, filing cabinets, and every loose sheet of paper rise from the floor."
    "Nothing tilts. Nothing spills. Even the papers remain in perfect stacks."

    i "There. Now we don't have to move anything."

    "The tarp remains folded in the hall. Ica looks at it, then at the carpet."

    i "We should probably do something about that. Pick how responsible we're being."

    menu:
        "Cover the carpet properly.":
            $ ica -= 1
            $ ica_paint_preparation = "tarp"
            "You unfold the tarp and tape its edges. Ica makes the far corners drift into place from the doorway."
            i "Responsible vandalism. Ulysses is gonna be so conflicted."
        "Put cardboard under the paint cans and risk the rest.":
            $ ica += 1
            $ ica_paint_preparation = "cardboard"
            "Ica tears apart an empty supply box with gravity and slides the pieces beneath the cans."
            i "That's enough safety to say we tried."
        "Float the paint so nothing touches the floor.":
            $ ica += 1
            $ ica_paint_preparation = "floating"
            "Every can rises to waist height and follows you into the office."
            i "Okay, that's actually less work. You may stay."

    "The two of you get to work."

    "You choose a wall and cut a bright pink line along its edge while Ica floats the tray beside you. The first strip looks alarmingly permanent."

    i "Damn. No backing out now. Convenient."

    "A familiar set of footsteps passes through the hallway much earlier than either of you expected."

    show ica at slot(0, total=1), bright zorder 10
    i "Huh. Ulysses is back."
    i "Whatever. Grab the paint when he's looking the other way. We'll finish before he checks in here."

    call RulesIcaPrank
    $ start_ica_prank_minigame(ica_prank_approach)
    $ prank_result = ica_minigame_results.get("prank", {})
    $ ica_prank_apply_relationship_result()

    if prank_result.get("completed", False):
        if ica_prank_caught_count == 0:
            show ica happy at slot(0, total=1), bright zorder 10
            i "See? Perfect crime. Barely even had to stand up."
        elif ica_prank_caught_count == 1:
            show ica happy at slot(0, total=1), bright zorder 10
            i "One almost-disaster's still pretty good. He probably thinks the hallway's haunted now."
        else:
            show ica at slot(0, total=1), bright zorder 10
            i "That was subtle as hell."
            i "Doesn't matter. Paint's on the walls."
    else:
        show ica at slot(0, total=1), bright zorder 10
        i "Fine. I'll watch the hallway. You keep painting."

    "Whenever a roller needs more paint, the tray floats across the room on its own. Ica barely moves from the doorway."

    i "Higher. You missed a spot."
    "The roller in your hand suddenly becomes light enough to glide up the wall."
    i "See? Teamwork. You work, I make it easier."

    "Less than an hour later, every wall in Ulysses's office is aggressively pink. Ica lowers the furniture back into its exact original position."

    i "Damn. I'm good."

    "The door opens behind you."

    u "Why is my office pink??"
    i "Team building."
    u "Whose team??"
    i "Ours. You weren't invited."

    "Ulysses closes his eyes and pinches the bridge of his nose."

    u "I knew this was going to happen, and it still hurts."

    u "You didn't get paint on the case files, did you?"
    i "Nah. Opening the cabinets would've been extra work."
    u "Of course."
    u "Keep the windows open until the paint dries. I have a murder to solve."

    "Ulysses collects one folder from the floating edge of his desk and leaves."

    i "Honestly, that went better than expected."

    "The two of you stand in the open doorway while the room airs out. Ica uses a tiny shift in gravity to pull wet paint from the roller back into the tray, then drops the clean roller at your feet."

    menu:
        "Ask whether she planned the cleanup too.":
            $ ica += 1
            i "I planned for you to do it. Same thing, basically."
        "Admire the finished office.":
            i "Way better. He'll pretend to hate it until he stops noticing."
        "Point out one missed spot behind the door.":
            $ ica -= 1
            "The tiny brush lifts from the hall, paints the spot by itself, and falls back into the tray."
            i "There. Crisis over."

    if ica >= ICA_HIGH_FLIRT_THRESHOLD:
        show ica flirty at slot(0, total=1), bright zorder 10
        i "You're pretty fun to waste a day with, freshie."
        i "Don't make a big deal out of that. I'll deny it."
    elif ica >= ICA_WARM_FLIRT_THRESHOLD:
        show ica happy at slot(0, total=1), bright zorder 10
        i "Not bad, freshie. You can come to the next felony too."
    else:
        show ica at slot(0, total=1), bright zorder 10
        i "You complain a lot, but the office is pink. I'll call that a win."

    i "Next time, we're doing absolutely nothing. I need a break."

    $ dayIca += 1
    jump endOfDay

label IcaDaySix:
    scene cubicleOutline
    "You find Ica exactly where she promised she would be: slumped in her chair, doing absolutely nothing."
    show ica at slot(0, total=1), bright zorder 10

    i "Freshie. Today, I've planned our most ambitious game yet."
    i "We sit here and see how long it takes somebody to ask us to work."

    "She has prepared more thoroughly for doing nothing than she prepared for any actual assignment: two drinks, a bag of chips, and a folded jacket serving as a pillow."

    if ica_day_one_candy == "green":
        "The surviving green candies from your first card game sit in a separate bowl labeled PROBABLY SAFE."
    elif ica_day_one_candy == "none":
        "The stale candy bowl from your first card game has migrated onto her desk. It still appears untouched."

    if ica_hotdog_style == "everything":
        i "No hot dogs today. I can still taste that mystery sauce and I think it hates me."
    elif ica_hotdog_style == "plain":
        i "Chips are plain. Figured you'd appreciate the lack of obstacles."

    menu:
        "Claim the second chair and put your feet up.":
            $ ica += 1
            "Ica shifts a stack of folders off the desk just before your shoes touch them."
            i "Careful. Those are important. Probably."
        "Take the floor and borrow the jacket pillow.":
            $ ica += 1
            i "Bold. That's my emergency nap technology. Don't drool on it."
        "Sit beside her and split the chips.":
            $ ica += 1
            "The bag floats open between you, perfectly positioned for neither person to lean forward."
            i "Efficient snack distribution. We're innovators."

    "The game begins. Footsteps pass twice without entering. A phone rings somewhere in the back office until somebody else gives up and answers it."
    "You debate whether checking the clock counts as effort, then lose track of the argument. Nearly an hour passes without either of you moving."

    i "We're really good at this."

    "The front door opens softly enough that it almost becomes part of the room's background noise. A person slips into the otherwise empty office and pauses when they see the unattended evidence cabinets."
    "They glance down both halls, overlook the two motionless figures in the cubicle, and head straight for the locks. Ica's chip stops halfway to her mouth."

    $ ica_day_six_killer_name = suspectNames[killer]
    $ ica_day_six_killer_power = suspectAttributes[killer]["power"]
    $ ica_day_six_killer_unique = suspectAttributes[killer]["unique_id"]

    "You recognize [ica_day_six_killer_name] from the suspect files. The [ica_day_six_killer_unique] noted in the file makes the identification immediate."

    "[ica_day_six_killer_name] checks the hallway again, then pulls a bloodstained wallet marked with Enrico Edge's initials from inside their coat."

    show ica shock at slot(0, total=1), bright zorder 10
    i "Dude."

    if ica_day_six_killer_power == "Fire":
        "Fire gathers around the wallet. Before it can catch, the wallet tears free and flies across the room."
    elif ica_day_six_killer_power == "Ice":
        "Ice crawls across the wallet. Before it can shatter, the wallet tears free and flies across the room."
    else:
        "Light builds in [ica_day_six_killer_name]'s hand. Before it can burn through the wallet, it tears free and flies across the room."

    "The wallet lands gently in Ica's palm. She has not left her chair."

    show ica whatTheFuckDidYouJustDoMC at slot(0, total=1), bright zorder 10
    i "We're sitting ten feet away. Did you seriously not see us?"

    "[ica_day_six_killer_name] freezes, looks at you, looks at Ica, and bolts through the front door."

    menu:
        "Go after them.":
            "You start to rise, but Ica makes your chair too heavy to move."
            i "Why? We know who it is and we have the evidence. Running sounds awful."
            $ ica += 1
        "Stay seated. \"Well, that was convenient.\"":
            $ ica += 2
            show ica happy at slot(0, total=1), bright zorder 10
            i "Right? We should've tried doing nothing sooner."
        "Ask how she let the killer escape.":
            $ ica -= 2
            show ica at slot(0, total=1), bright zorder 10
            i "I didn't let them destroy the evidence. Catching people is Nicky's job."

    $ ica_day_six_clue = "{} was caught attempting to destroy Enrico Edge's bloodstained wallet.".format(ica_day_six_killer_name)
    $ ica_day_six_eliminations = sorted([suspect_id for suspect_id in suspectNames if suspect_id != killer])
    $ record_investigation_clue("ica_visit_6", "Ica", 6, ica_day_six_clue, ica_day_six_eliminations)

    show ica happy at slot(0, total=1), bright zorder 10
    i "Well. Case solved."
    i "Everybody's out chasing actual leads, so we'll ruin Ulysses's evening with that tonight."
    i "Now we still have a whole day to kill."

    "Ica drops the wallet into the evidence safe without getting up. The door swings shut behind it."
    "She uses the desk phone to leave Nicky a message describing what happened in fewer than twenty words. Then she photographs the safe, the open cabinet, and the muddy prints leading back to the door."

    i "There. Responsible enough that nobody can yell until tomorrow."

    "The office settles again, but the silence feels different now. The killer's abandoned trail runs straight across the floor, the safe contains the answer, and Ica is already opening the chips again."

    i "Wanna play chicken?"

    menu:
        "Ask what kind.":
            i "Flirting. We keep making it worse until somebody gets weird and backs down."
            i "You seem easy to embarrass, so I like my odds."
        "Tell her she has no chance.":
            $ ica += 1
            show ica flirty at slot(0, total=1), bright zorder 10
            i "Oh, you're already losing. This is gonna be easy."
        "Tell her the game sounds stupid.":
            $ ica -= 1
            i "Scared already. Got it."

    "Ica uses her power to roll your chair closer without touching it."

    show ica flirty at slot(0, total=1), bright zorder 10
    i "You know, freshie, you're kinda cute when you're accidentally solving murders."

    $ ica_chicken_backed_down = False

    menu:
        "Lean closer. \"You're cute when you pretend not to care.\"":
            $ ica += 2
            i "Pretend? Nah. I really don't care."
            i "The cute part's true, though."
        "Tell her she has pretty eyes.":
            $ ica += 1
            i "Pretty basic move. I'll allow it."
        "Look away.":
            $ ica -= 1
            $ ica_chicken_backed_down = True
            show ica happy at slot(0, total=1), bright zorder 10
            i "There it is. I win."

    if not ica_chicken_backed_down and ica >= ICA_WARM_FLIRT_THRESHOLD:
        "Ica hooks one foot around the base of your chair and pulls you the last few inches closer."
        show ica flirty at slot(0, total=1), bright zorder 10
        i "Still good, freshie?"

        menu:
            "Rest an arm across the back of her chair.":
                $ ica += 2
                "You settle in like the two of you sit this close every day."
                i "Okay. Not bad."
            "Tell her she can move closer if she wants.":
                $ ica += 1
                i "I'm already doing all the work here. You move."
            "Admit that she wins.":
                $ ica_chicken_backed_down = True
                i "Damn right. Took you long enough."

        if not ica_chicken_backed_down and ica >= ICA_DATE_ACCEPT_THRESHOLD:
            "Neither of you moves away."
            "After several quiet seconds, Ica glances toward the clock."
            i "Time's up. Draw."
            "There are still three hours left in the workday."
            i "Don't be a nerd about it."
        elif not ica_chicken_backed_down:
            "Ica holds your gaze until you finally glance toward the clock."
            i "Clock check. You got distracted. I win."
    elif not ica_chicken_backed_down:
        "Ica holds your gaze for a few seconds, then flicks the arm of your chair and sends you rolling back across the cubicle."
        show ica happy at slot(0, total=1), bright zorder 10
        i "Yeah, that's enough of that. I win."

    "The two of you let the chairs drift apart by a few inches, then stop them there. For the rest of the afternoon, neither mentions the game ending."
    "Every so often one of you starts another round with a look or a remark, and every time the other refuses to admit it counts."

    i "Not a bad week, freshie. We should do this again when there isn't a murder or whatever."

    $ dayIca += 1
    jump endOfDay

label day7:
    jump DaySevenStart
