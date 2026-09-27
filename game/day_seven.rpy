## The complete Day Seven finale.

label DaySevenStart:
    $ day_seven_prepare()

    scene black with fade
    centered "DAY SEVEN: THE ACCUSATION"
    "The deadline has arrived. Six days of witness statements, laboratory work, field reconstruction, arguments, games, and handwritten notes now have to become one name."

    if daySevenIcaSpecial:
        call DaySevenIcaEvidenceOpening

    call DaySevenTeamBriefing

    window hide
    call screen day_seven_accusation
    $ daySevenSelectedSuspect = _return
    window auto

    $ day_seven_selected_name = suspectNames[daySevenSelectedSuspect]

    scene debriefRoomOutline with fade
    u "You are formally accusing [day_seven_selected_name] of murdering Enrico Edge."
    "The file remains open beneath Ulysses's hand. Nobody reaches for it."

    call DaySevenAccusationReview

    $ daySevenCaseSolved = daySevenSelectedSuspect == killer
    $ day_seven_apply_case_modifier(daySevenCaseSolved)

    if daySevenCaseSolved:
        call DaySevenSuccess
    else:
        call DaySevenFailure

    call DaySevenRelationshipSelection
    call DaySevenOutro

    call screen day_seven_credits
    call screen day_seven_thanks
    return


label DaySevenIcaEvidenceOpening:
    scene black with fade
    "The hallway outside the briefing room is quiet when Ica rolls alongside you in her chair. Enrico Edge's bloodstained wallet floats above her shoulder inside a clear evidence bag."

    show ica happy at slot(0, total=1), bright zorder 10

    i "Morning, freshie. Brought our group-project contribution."
    "She gives the bag a tiny gravitational nudge. It rotates in the air, displaying Enrico's initials and the dark stain along one edge."
    i "Everybody else spent a week doing detective stuff. We sat still long enough for the killer to walk in and try burning this."
    i "Honestly, feels rude to make us attend the meeting after that."

    menu:
        "Tell her Ulysses will insist on the formal accusation.":
            i "Yeah, yeah. Forms before justice. His favorite superhero slogan."
            "She floats the evidence bag into your hands, waits until you have a secure grip, then takes it back before you can carry it normally."
        "Admit this is the strongest evidence anyone found.":
            show ica flirty at slot(0, total=1), bright zorder 10
            i "See? Shameless bums stay winning."
            "The wallet makes one slow victory lap around the two of you before settling above her shoulder again."
        "Ask whether she prepared anything to say.":
            i "Sure did. 'That's the killer. They had the dead guy's wallet.'"
            i "Short, accurate, leaves more time for not talking."

    show ica at slot(0, total=1), bright zorder 10
    "Voices shift behind the briefing-room door. Ica lowers the wallet to table height, and the joking edge of the moment gives way to what the evidence means."
    i "Ready?"
    "You enter together. The wallet floats in ahead of both of you."
    $ day_seven_add_ica_evidence()
    return


label DaySevenTeamBriefing:
    scene debriefRoomOutline with fade
    "The entire team is waiting around the briefing table. Ulysses stands at its head behind the surviving suspect files. There are no crossed-out names on display—only the people the evidence has not yet cleared."
    "Razzle's flames burn lower than usual. Madeline has stopped tapping her pen. Nicky's police notebook is already open. Even Winston sits without leaning his chair onto two legs."

    if daySevenIcaSpecial:
        "The floating evidence bag reaches the center of the table. Every head turns toward it."
        r "Is that Enrico's wallet?"
        m "Where the hell did you get that?"
        i "Killer brought it to us. Tried destroying it ten feet from my desk."
        w "You solved the murder by making the office look unattended."
        i "I solved the murder by being approachable."
        d "You were lying on the floor eating chips."
        i "Approachably."
        "Nicky rises, checks the evidence seal, and takes formal custody of the bag."
        n "Nobody touches this again until it is logged. Ica, you and the recruit are giving me separate statements after this."
        u "And despite the answer being unusually determined to identify itself, we will complete the accusation properly."
        u "The evidence decides the name. The comedy surrounding its recovery does not alter the procedure."
    else:
        "Ulysses waits until the door shuts before touching the first file."

    u "The investigative period is over. Today is not another opportunity to gather evidence. It is the point at which you accept responsibility for what the evidence already says."
    n "A suspect is not a collection of bad impressions. If you name someone, every part of the case has to survive that name."
    m "Which means don't fall in love with one clue and ignore the eleven facts making it look stupid."
    r "We did get a lot, though. Like, actual useful things. Not just vibes."
    d "Some vibes. Just not the kind you put in an evidence bag."
    "Winston looks around the table, waits for the tension to ease, and discovers that it has no intention of cooperating."
    w "Good news: if this goes badly, the paperwork will probably crush us before guilt does."
    "Nobody laughs."
    w "All right. Serious room. Read the room. Got it."

    if dayRazz > 1:
        r "The witnesses gave us details by pieces. What they couldn't see mattered as much as what they could."
    else:
        r "Witnesses remember weird little pieces. Just don't force those pieces into a picture they never saw."

    if dayDham > 1:
        d "The scene told us what happened before, during, and after Enrico died. Technique matters more than whatever looks dramatic."
    else:
        d "Rooms keep better stories than people sometimes. Doesn't mean they're easy stories."

    if dayMads > 1:
        m "The laboratory results are reproducible. Use the controls, not whichever colored chart makes you feel clever."
    else:
        m "Forensics can exclude a theory. It cannot rescue one that was garbage before it reached the lab."

    if dayNick > 1:
        n "Records, warrants, and independent sources keep the profile honest. One device or one instinct is never enough."
    else:
        n "Procedure exists because certainty feels exactly like certainty whether you're right or not."

    if dayWinn > 1:
        w "People lied, panicked, joked, and remembered things out of order. None of that made them murderers by itself."
    else:
        w "Pressure gets answers. Too much pressure gets whatever answer makes you stop. Know the difference."

    if dayIca > 1 and not daySevenIcaSpecial:
        i "I contributed moral support and avoided contaminating evidence by not going near it."
        u "Your summary is offensively selective, but not entirely false."
    elif not daySevenIcaSpecial:
        i "I wasn't there for most of it. Sounds exhausting."

    "Madeline pulls one surviving file toward her. Nicky stops it with two fingers before it crosses the center line."
    m "Some of these attributes are obviously more discriminating than others."
    n "More discriminating does not mean independently sufficient."
    m "I know what sufficient means."
    n "Then you know why the file stays in the middle."
    d "They're agreeing, by the way."
    r "Really doesn't sound like it."

    $ day_seven_distinct_routes = ulysses_distinct_routes()
    $ day_seven_focus_route = day_seven_favorite_investigator()

    if ulysses_one_each_strategy():
        u "You sampled every investigative method once. None of those reports was deep alone, but their overlap was enough for us to formally remove every remaining contradiction."
        u "You chose breadth and then did the difficult work of synthesis. I'm impressed."
    elif day_seven_focus_route:
        $ day_seven_focus_name = day_seven_partner_name(day_seven_focus_route)
        u "You concentrated most heavily on [day_seven_focus_name]'s method. That gave you depth, but it also gave you a preferred lens. Account for both."
    else:
        u "You divided your attention across several methods. Your conclusion must explain how those reports support one another rather than merely placing them in the same folder."

    u "There are [len(day_seven_selectable_suspects())] viable files in front of you. One belongs to Enrico's killer."

    menu:
        "Defend the evidence chain.":
            $ daySevenBriefingResponse = "defend"
            "You walk through the eliminations, then separate them from the quieter observations that distinguish the survivors."
            u "Good. You understand which claims are formal and which require your judgment."
            n "And you didn't turn uncertainty into a confession. Keep doing that."
        "Admit that some of the final judgment is uncertain.":
            $ daySevenBriefingResponse = "uncertain"
            "You acknowledge where the reports end and your interpretation begins. The admission sits heavily in the room, but nobody treats it as weakness."
            u "Honest uncertainty is part of competent judgment. It does not excuse you from making the judgment."
            d "Means you're taking it seriously. Better than pretending."
        "Make a joke before committing to the answer.":
            $ daySevenBriefingResponse = "joke"
            "You suggest accusing whichever suspect has the most inconvenient name to spell."
            w "Finally, an investigative standard designed around paperwork."
            "Ulysses waits until the brief laugh ends."
            u "Now use the actual evidence."

    "Ulysses squares the surviving files with the edge of the table and steps away from them."
    u "Review your notes. Compare the complete profiles. Take as long as the work requires."
    u "When you confirm a name, it becomes the accusation this team acts upon."
    return


label DaySevenAccusationReview:
    $ day_seven_selected_attrs = suspectAttributes[daySevenSelectedSuspect]
    $ day_seven_actual_attrs = suspectAttributes[killer]
    $ day_seven_actual_name = suspectNames[killer]
    $ day_seven_cause = DHAMPIR_MURDER_CAUSES[killer]

    u "We will test the selection against the record, not defend it because it has already been made."
    "He places the profile beside the accumulated reports and begins at the first verified elimination. Each discarded name remains discarded for a reason independent of your final choice."
    u "The scene establishes that Enrico died from [day_seven_cause]. The method alone does not identify the attacker, but it limits which profile can explain the complete struggle."

    r "The witness details have to fit without changing what anybody said."
    d "The room has to fit before and after the killing."
    m "The physical trace has to survive the controls."
    n "The records have to corroborate it."
    w "And the person has to behave like the same person across all of it."
    i "Plus, if they bring the dead guy's wallet to work, that feels relevant."

    if daySevenSelectedSuspect == killer:
        "Ulysses turns the final page. No contradiction appears. Every formal exclusion holds, and every subtle observation aligns with the same surviving profile."
        u "The accusation survives review. [day_seven_actual_name] is the only person whose complete file fits the evidence."
    else:
        $ day_seven_mismatch = day_seven_mismatch_text(daySevenSelectedSuspect)
        "Ulysses stops at the first contradiction and rotates the two relevant pages toward you."
        u "[day_seven_mismatch]"
        u "That is not a minor discrepancy. It breaks the accusation."
    return


label DaySevenSuccess:
    $ day_seven_actual_name = suspectNames[killer]
    $ day_seven_confession = day_seven_culprit_confession(killer)

    if daySevenIcaSpecial:
        "Nicky steps out to confirm the transfer from the holding room. The waiting lasts only a few minutes, though nobody manages to make them feel short."
        "When she returns, two officers escort [day_seven_actual_name] into the briefing room. Their eyes fix on the bloodstained wallet before anyone says a word."
        n "They have been in custody since they tried destroying that wallet in front of two ATLAS investigators. They have also decided to speak in front of the team."
    else:
        "Nicky leaves the room with the reviewed file. The waiting lasts only a few minutes, though nobody manages to make them feel short."
        "When she returns, two officers escort [day_seven_actual_name] into the briefing room. The surviving evidence has been laid out where they can see every piece."
        n "The arrest is complete. They have also decided to speak in front of the team."
    "[day_seven_actual_name]" "Fine. I killed Enrico. [day_seven_confession]"
    "The admission leaves nowhere else for the week to turn. No one cheers immediately. Closing the case does not make the reason for gathering here less grim."

    u "The accusation is correct. Enrico Edge's killer is in custody, and the evidence supporting that arrest is sound."
    "Only then does the room release the breath it has been holding."
    r "Holy shit, We actually got them!"
    m "Yes. Because the evidence was correct. Try celebrating without knocking it onto the floor."
    d "Nice work, new blood."
    n "You made the call and you supported it. That's the job."
    i "Congrats on continued employment, freshie. My condolences."
    w "Permanent paperwork privileges! Dreams really do come true."

    "Ulysses comes around the table and offers his hand."
    u "Your probationary appointment is complete. As of today, you are a permanent investigator with ATLAS."
    "You take his hand. His grip is formal; the quiet approval in his expression is not."

    if ulysses_one_each_strategy():
        "Every member of the team gathers around you at once. The welcome overlaps into seven conversations, three proposed celebrations, and one argument about who predicted this first."
    else:
        $ day_seven_favorite = day_seven_favorite_investigator()
        if day_seven_favorite == "razzle":
            r "Knew my partner had it!"
        elif day_seven_favorite == "dhampir":
            d "Stuck with the ugly parts until they made sense. Respect."
        elif day_seven_favorite == "madeline":
            m "Your conclusion was competent. Don't make me repeat that in front of everybody."
        elif day_seven_favorite == "nicky":
            n "Good work, rookie. Guess I need a new nickname."
        elif day_seven_favorite == "winston":
            w "Newbie status revoked. I'm still calling you that though."
        elif day_seven_favorite == "ica":
            i "You worked just enough to keep the job. Beautiful."

    "Winston begins ordering enough pizza for the building before Ulysses has formally ended the meeting. This time, Ulysses allows it."
    u "The case is closed. Take the evening."
    "Chairs scrape back, conversation returns, and the briefing room slowly becomes a celebration. Before the night ends, you have one personal decision left to make."
    return


label DaySevenFailure:
    $ day_seven_selected_name = suspectNames[daySevenSelectedSuspect]
    $ day_seven_actual_name = suspectNames[killer]

    "Nicky's pager sounds before anyone can move beyond the contradiction. She reads the message once, then stands so quickly that her chair strikes the wall."
    n "[day_seven_actual_name] ran. Patrol reached the address after they cleared the block."
    "The actual profile replaces your selected file at the center of the table. Once the missed contradiction is corrected, the rest of the evidence aligns around [day_seven_actual_name]."
    u "The killer is [day_seven_actual_name]. Your accusation gave them the time and warning necessary to escape immediate custody."

    r "We'll find them. We know who we're looking for now."
    d "Yeah. We will."
    m "After we waste time repairing a conclusion that should not have broken."
    n "[day_seven_selected_name] is being released. Nobody repeats that accusation outside this room without the correction attached."
    w "Team splits into pursuit and damage control. Same as always, only worse."
    i "This is why I don't volunteer for decisions."

    "Ulysses remains standing at the head of the table. His anger is quiet enough that no one can mistake it for loss of control."
    u "You were given evidence, time, and six people's expertise. You still selected the one conclusion the record could not support."
    u "ATLAS cannot place that judgment behind an accusation carrying our authority. Your employment ends immediately."

    menu:
        "Accept responsibility.":
            "You say the accusation was yours and the consequence belongs to you."
            u "Correct. Accountability does not repair the error, but refusing it would make the error impossible to learn from."
        "Argue that the final clues were too uncertain.":
            "You point to the gaps, the conflicting impressions, and the pressure of making one final choice."
            u "Uncertainty was a reason to review your conclusion. You used it as permission to excuse one."
        "Make one last joke.":
            "You ask whether being fired at least exempts you from the exit paperwork."
            w "It should. It absolutely will not."
            u "No."

    "The meeting breaks apart around the response. Nicky organizes the pursuit. Dhampir follows without needing instructions. Madeline takes the corrected profile, Razzle grabs the contact list, and Winston pauses beside you before duty pulls him toward the door."
    w "One bad call doesn't make you worthless. It does mean you have to live honestly with the call."
    "Ica gives you a small, crooked salute. Ulysses waits until the others have gone."
    u "Collect your belongings. Someone will escort you through the secure exit when the immediate response is underway."
    "Later that evening, while ATLAS searches for [day_seven_actual_name], you return to the mostly empty office for the last of your things. There is still time for one final private conversation."
    return


label DaySevenRelationshipSelection:
    window hide
    call screen day_seven_partner_choice
    $ daySevenChosenPartner = _return
    window auto

    if daySevenChosenPartner:
        $ daySevenRelationshipOutcome = day_seven_relationship_outcome(daySevenChosenPartner, daySevenCaseSolved)
    else:
        $ daySevenRelationshipOutcome = "alone"

    $ daySevenEndingKey = day_seven_ending_key(
        daySevenCaseSolved, daySevenChosenPartner, daySevenRelationshipOutcome)
    $ day_seven_unlock_ending(daySevenEndingKey)

    call DaySevenCharacterEnding
    return


label DaySevenCharacterEnding:
    if not daySevenChosenPartner:
        call DaySevenEndingAlone
    elif daySevenChosenPartner == "razzle":
        call DaySevenEndingRazzle
    elif daySevenChosenPartner == "winston":
        call DaySevenEndingWinston
    elif daySevenChosenPartner == "nicky":
        call DaySevenEndingNicky
    elif daySevenChosenPartner == "ica":
        call DaySevenEndingIca
    elif daySevenChosenPartner == "ulysses":
        call DaySevenEndingUlysses
    elif daySevenChosenPartner == "madeline":
        call DaySevenEndingMadeline
    elif daySevenChosenPartner == "dhampir":
        call DaySevenEndingDhampir
    return


label DaySevenEndingRazzle:
    scene black with fade
    if daySevenCaseSolved:
        "You find Razzle on the roof above the celebration, letting the cooler air pull her flames into long ribbons behind her."
    else:
        "Razzle catches you outside while you are carrying the last box from your desk. The search lights moving across the city reflect in her flames."

    show razzle at slot(0, total=1), bright zorder 10
    "You make it clear that you are not asking for a group celebration or a friendly night out. You ask Razzle on a romantic date."

    if daySevenRelationshipOutcome == "romance":
        show razzle flirty at slot(0, total=1), bright zorder 10
        if daySevenCaseSolved:
            r "There it is! You finally found a line hot enough to work!"
        else:
            r "Today sucked. Like, impressively. Still doesn't make me wanna say no to you."
        r "Yeah, newbie. Romantic date. Club, drinks, dancing, and somewhere fireproof when we want the noise to stop."
        "Razzle closes the distance before you can overthink the answer. The kiss is warm in every possible sense and brief only because she starts laughing against your mouth."
        r "Okay! That was good. We're doing that again when I haven't spent all day solving a murder."
        "Your first date becomes an energetic night of dancing followed by a quiet walk where Razzle never once has to apologize for the flames beside you. Whatever comes after remains open, but neither of you mistakes it for casual interest."
    elif daySevenRelationshipOutcome == "friend":
        show razzle mouth open at slot(0, total=1), bright zorder 10
        r "I love spending time with you, but not like that. I don't wanna fake the romantic part just because this week got intense."
        r "You are absolutely still coming clubbing with me. Winston too, probably."
        "The next night out is loud, affectionate, and completely platonic. Razzle makes certain the word friend never sounds like a consolation prize."
    else:
        show razzle sad at slot(0, total=1), bright zorder 10
        r "No, sorry. We don't know each other like that, and I'm not gonna pretend we do."
        r "I hope things work out for you."
        "She gives you an honest goodbye and leaves the answer there instead of softening it into a promise she does not mean."
    return


label DaySevenEndingWinston:
    scene winstonOfficeOutline with fade
    if daySevenCaseSolved:
        "Winston escapes the celebration long enough to hide in his office with two slices of pizza and a soda balanced on the case file."
    else:
        "Winston returns from the first failed sweep while you are collecting your belongings. He shuts his office door behind both of you, giving the goodbye a moment without an audience."

    "You tell him directly that this is not another joke, a leadership exercise, or two coworkers getting food. You ask him on a romantic date."

    if daySevenRelationshipOutcome == "romance":
        w "Oh."
        "For once, Winston reaches for a joke and finds himself a full second too slow."
        if daySevenCaseSolved:
            w "You solve one murder and immediately decide to attempt something dangerous. I respect the momentum."
        else:
            w "I think today proved you can make a terrible decision. This isn't one of them."
        w "Yeah, newbie. Romantic date. Pool first, disgusting burgers after. I'm winning at both, somehow."
        "His familiar grin returns as he catches you at the waist and pulls you close. It disappears again when you kiss him."
        "The first date becomes three fiercely competitive pool games and a diner meal neither of you admits was too greasy. Winston fills every silence until he realizes the quiet beside you no longer needs filling."
    elif daySevenRelationshipOutcome == "friend":
        w "I like you. A lot, actually. Just not in the direction you're aiming newbie."
        w "Friend version's still availabl though. Pool, food, occasional unsanctioned hero work—strictly no payroll implications."
        "He keeps the promise. Friendship with Winston remains noisy, competitive, and dependable whenever it matters."
    else:
        w "No, newbie. You caught me charming at close range and drew an unsafe conclusion."
        w "I mean it kindly. There isn't a date here."
        "He refuses to make the rejection cruel, but he also refuses to disguise it as uncertainty."
    return


label DaySevenEndingNicky:
    scene debriefRoomOutline with fade
    if daySevenCaseSolved:
        "Nicky finishes the last custody signature before stepping away from the celebration. Her motorcycle helmet hangs from one hand."
    else:
        "Nicky returns long enough to retrieve a fresh warrant packet while you clear your place at the table. She pauses when you ask for one private minute."

    show nicky at slot(0, total=1), bright zorder 10
    "You state clearly that you mean a romantic date—not casework, not television between reports, and not a friendly ride across town."

    if daySevenRelationshipOutcome == "romance":
        show nicky curious flirty at slot(0, total=1), bright zorder 10
        if daySevenCaseSolved:
            n "Look at you. Permanent job for five minutes and already making bold personal decisions."
        else:
            n "You made one awful call today. I'm not pretending otherwise. I'm also not pretending it erased everything I learned about you this week."
        n "Yes, rookie. Romantic date. Bike ride, records, diner, and whatever happens after the coffee gets cold."
        "She hooks two fingers into your collar, draws you down to her, and kisses you with none of the hesitation she made you put into the question."
        n "Good. Your pheromones were getting embarrassingly hopeful."
        "The first date stretches across the city: music, food, a late motorcycle ride, and an episode of The Y-Files neither of you watches very carefully."
    elif daySevenRelationshipOutcome == "friend":
        show nicky content happy at slot(0, total=1), bright zorder 10
        n "No romance, rookie. I like you, but that's not where this is going."
        n "You can still get on the bike, steal my fries, and yell at fictional federal agents with me. Friend terms."
        "Nicky's friendship remains playful and direct. When she wants your company, she asks without making either of you guess what she means."
    else:
        show nicky angry accusation at slot(0, total=1), bright zorder 10
        n "No. That's way too personal for where we are, and saying it more dramatically won't change the answer."
        n "Take the no properly."
        "You do. Nicky gives you a professional farewell and returns to the work waiting for her."
    return


label DaySevenEndingIca:
    scene cubicleOutline with fade
    if daySevenCaseSolved:
        "Ica has escaped the celebration and reclaimed her chair. A pizza plate floats above her while she pretends not to wait for you."
    else:
        "Ica is sitting in your cleared-out cubicle when you return with the final box. Her own desk supplies are floating in a lazy orbit around her chair."

    show ica at slot(0, total=1), bright zorder 10
    "You tell her this is not another game of chicken. You are asking her on an actual romantic date."

    if daySevenRelationshipOutcome == "romance":
        show ica flirty at slot(0, total=1), bright zorder 10
        if daySevenCaseSolved and daySevenIcaSpecial:
            i "We solve a murder without standing up and now you wanna ruin the perfect week by trying?"
            i "Fine. Date accepted. We're keeping the effort level reasonable."
        elif daySevenCaseSolved:
            i "Wow. Kept your job and immediately found a way to make it weird."
            i "Yeah, alright. Actual date. Low walking requirement."
        else:
            i "Good timing. I quit."
            "You stare at the orbiting desk supplies."
            i "Ulysses fired you, I told him employment sounded overrated, and he looked exactly as surprised as you'd expect."
            i "So yeah. Date accepted. We can be unemployed bums together."
        "Ica catches your collar with two fingers and lets gravity finish pulling you into a kiss. She releases you just before you can make the moment earnest."
        i "Convenience store, then somewhere nobody expects us to be productive. That's the date."
        "It is. Cheap food, stolen seating, and hours spent together without manufacturing an excuse. Neither of you works very hard at defining what comes next."
    elif daySevenRelationshipOutcome == "friend":
        show ica happy at slot(0, total=1), bright zorder 10
        i "Nah, freshie. Romantic sounds like scheduling and expectations."
        i "You're good to waste time with, though. Friend version can stay."
        "She remains employed and continues saving you a chair whenever doing nothing could use company."
    else:
        i "Nope. Don't make it weird."
        "The refusal is effortless and final. Ica returns to her floating snack before the silence can become dramatic."
    return


label DaySevenEndingUlysses:
    scene debriefRoomOutline with fade
    if daySevenCaseSolved:
        "The celebration eventually migrates toward Winston's pizza order. Ulysses remains in the briefing room, aligning the closed files while the noise recedes down the hall."
        "He knows a question is coming. You can see that knowledge in the stillness of his hands, but he waits for you to choose the words."
        "You ask whether he would spend an evening with you away from ATLAS, with no report between you and no professional interpretation of the invitation."
    else:
        "Ulysses remains in the briefing room after the others leave to pursue the actual culprit. Your terminated identification card rests beside the incorrect file."
        "You ask whether everything between you could still become a romantic date."

    if not daySevenCaseSolved:
        u "No."
        "The answer arrives without cruelty and without room to misread it."
        u "I care about what these evenings meant. That makes it more important, not less, that I answer honestly."
        u "I have just ended your employment because your judgment placed an innocent person at risk and allowed a killer to escape. Turning this moment into romance would be irresponsible."
        u "Whatever I know about tomorrow is irrelevant. Today, the answer is no."
        "He wishes you well, but he offers no promise of friendship and no invitation to return. The distance is painful because it is sincere."
    elif daySevenRelationshipOutcome == "romance":
        "Color reaches Ulysses's face before he finishes setting down the file. Knowing the question existed has done nothing to make answering it easy."
        u "An evening away from ATLAS. Explicitly personal. Intentionally uncertain."
        "You nod."
        u "Yes. There is a bookstore that stays open late and a restaurant nearby with no connection to Winston's standing pizza orders."
        u "I would like to discover the evening in the order it occurs."
        "You step close enough to give him every opportunity to refuse, then kiss him. His surprise lasts only a heartbeat before one careful hand settles at your waist."
        "Your first date contains books, dinner, obscure references only the two of you enjoy, and no attempt to plan what the relationship must become. Ulysses finds that he enjoys the uncertainty."
    elif daySevenRelationshipOutcome == "friend":
        u "I value you. I value the hours we spent working alone, and I would like those conversations to continue."
        u "But I cannot honestly call that desire romantic. Friendship is what I can offer."
        "The answer is gentle and exact. In the weeks after the case, quiet evenings of books, reports, and private jokes continue without either of you pretending they are dates."
    else:
        u "No. You are asking for an intimacy we have not built."
        u "You have earned a place on this team. Do not confuse professional respect with a promise I did not make."
        "He remains polite, but the boundary is complete. The two of you return to the celebration as coworkers."
    return


label DaySevenEndingMadeline:
    scene labOutline with fade
    if daySevenCaseSolved:
        "Madeline abandons the celebration after exactly one slice of pizza. You find her in the lab pretending to verify a result that has already been verified three times."
    else:
        "Madeline returns to the lab for equipment before joining the pursuit. Your final belongings are still in your arms when you stop her."

    show madeline at slot(0, total=1), bright zorder 10
    "You ask her on a romantic date, making the category clear enough that she cannot rename it as data collection."

    if daySevenRelationshipOutcome == "romance":
        show madeline flirty at slot(0, total=1), bright zorder 10
        if daySevenCaseSolved:
            m "I understood the category before you clarified it. I was giving you time to improve the wording."
        else:
            m "You were catastrophically wrong today. You also admitted it, and one failure does not invalidate every previous result."
        m "Yes. Romantic date. Ice cream first. Then somewhere with enough variables to keep the evening from becoming boring."
        "You suggest miniature golf. Madeline calls repeating an experiment scientifically lazy, then begins listing improvements for the rematch."
        "She kisses you abruptly, steps back, and spends several seconds staring at your expression like it generated an unexpected reading."
        m "That result was acceptable. Replication will be required."
        "The first date involves ice cream, competitive miniature golf, and an increasingly elaborate analysis neither of you truly wants her to stop making."
    elif daySevenRelationshipOutcome == "friend":
        show madeline flirty curious at slot(0, total=1), bright zorder 10
        m "No. Not romantically."
        m "You are competent enough that I want you in my lab again, which is an unusually strong offer of friendship. Accept the correct category."
        "You do. Madeline continues labeling your shared work as collaboration even after she starts keeping your preferred ice cream in the freezer."
    else:
        show madeline distress at slot(0, total=1), bright zorder 10
        m "No. The available data does not support that conclusion either."
        m "Do not ask me to falsify the answer to protect your feelings."
        "She leaves the rejection sharp, truthful, and impossible to mistake for an experiment still in progress."
    return


label DaySevenEndingDhampir:
    scene black with fade
    if daySevenCaseSolved:
        "Dhampir slips out of the celebration with a paper plate of pizza and leans against the quiet wall outside the briefing room."
    else:
        "Dhampir returns from searching long enough to find you beside the secure exit. He is back in his Hawaiian shirt, though the severe focus has not entirely left his posture."

    "You ask him on a romantic date and make it clear that this is not merely another movie night between coworkers."

    if daySevenRelationshipOutcome == "romance":
        d "Damn. I had a joke ready, but you made the question all sincere. Kinda fucked up of you."
        if not daySevenCaseSolved:
            d "You got today wrong. Badly. I don't think that makes every decent thing you did before it fake."
        d "Yeah, new blood. There's an underground show tomorrow. Music's loud, building's probably condemned, pizza place stays open late. Romantic enough?"
        "You tell him it depends on the kiss. Dhampir grins, leans in, and gives you enough evidence to settle the question."
        d "There. Peer reviewed."
        "The first date includes an excellent show, terrible acoustics, blood-seasoned pizza on a rooftop, and increasingly strange jokes that mean more than either of you says directly."
    elif daySevenRelationshipOutcome == "friend":
        d "Not feeling the romantic part, new blood. Sorry."
        d "Still want you around, though. Movies, shows, pizza, hanging out without pretending it needs another label."
        "Dhampir's friendship remains easy and sincere. He keeps inviting you to terrible films and saving the best commentary for the walk afterward."
    else:
        d "Nah. We don't have that."
        d "Nothing wrong with asking once. Just take the answer the same way."
        "He gives you a casual farewell and does not turn the rejection into either a punishment or a joke."
    return


label DaySevenEndingAlone:
    if daySevenCaseSolved:
        scene debriefRoomOutline with fade
        "You decide not to turn the end of the case into a romantic beginning. The choice does not leave an empty space; it leaves room for the team already gathering around you."
        "Winston's pizza arrives in impossible quantities. Razzle starts a toast before anyone finds cups. Nicky corrects three increasingly false versions of the arrest, Madeline guards the evidence from cheese, Dhampir steals the corner seat, and Ica makes a plate float to herself."
        "Ulysses watches the disorder spread across his briefing room, considers stopping it, and closes the door so the rest of the building will not have to hear it instead."
        u "Welcome to ATLAS. Permanently, against several reasonable objections."
        "You end the night as part of the team—wanted, trusted, and entirely complete without asking anyone for romance."
    else:
        scene black with fade
        "You decide not to ask anyone for romance before leaving. The office is occupied with the pursuit, and you do not turn the final few minutes into another demand on people already carrying the result of your mistake."
        "You surrender your identification card, carry the last box through the secure exit, and walk away alone."
        "ATLAS catches [suspectNames[killer]] several days later. Enrico's case eventually closes, but your part in it remains the wrong accusation that gave the killer time to run."
        "There is no promise that the mistake defines the rest of your life. There is only the responsibility to decide what you learn from it."
    return


label DaySevenOutro:
    scene black with fade
    if daySevenCaseSolved:
        "Enrico Edge's murder is formally closed. The evidence survives review, the confession holds, and your name remains on the ATLAS roster."
    else:
        "ATLAS captures [suspectNames[killer]] several days later and closes Enrico Edge's murder. Your incorrect accusation remains part of the record, as does the time it gave the killer to escape."

    if daySevenChosenPartner and daySevenRelationshipOutcome == "romance":
        "The case ends with a new relationship beginning—deliberate, mutual, and unwritten beyond the first date."
    elif daySevenChosenPartner and daySevenRelationshipOutcome == "friend":
        "Romance is not the answer, but the friendship that remains is real and plainly named."
    elif daySevenChosenPartner and daySevenRelationshipOutcome == "rejection":
        "The romantic answer is no. You carry it forward without rewriting it into something easier."
    elif daySevenCaseSolved:
        "You choose the team without choosing a romance. It is not a lesser ending."
    else:
        "You leave alone, with no easy promise attached to what comes next."
    return


label DaySevenGalleryReplay:
    $ day_seven_setup_gallery_replay(daySevenGalleryReplayKey)
    call DaySevenCharacterEnding
    return
