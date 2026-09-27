## The complete Day Seven finale.

label DaySevenStart:
    $ day_seven_prepare()

    scene black with fade
    centered "DAY SEVEN: THE ACCUSATION"
    "The deadline has arrived. Six days of witness statements, laboratory work, field reconstruction, arguments, games, and handwritten notes now have to become one name."

    if daySevenIcaSpecial:
        call DaySevenIcaEvidenceOpening from _call_DaySevenIcaEvidenceOpening

    call DaySevenTeamBriefing from _call_DaySevenTeamBriefing

    window hide
    call screen day_seven_accusation
    $ daySevenSelectedSuspect = _return
    window auto

    $ day_seven_selected_name = suspectNames[daySevenSelectedSuspect]

    scene debriefRoomOutline with fade
    u "You are formally accusing [day_seven_selected_name] of murdering Enrico Edge."
    "The file remains open beneath Ulysses's hand. Nobody reaches for it."

    call DaySevenAccusationReview from _call_DaySevenAccusationReview

    $ daySevenCaseSolved = daySevenSelectedSuspect == killer
    $ day_seven_apply_case_modifier(daySevenCaseSolved)

    if daySevenCaseSolved:
        call DaySevenSuccess from _call_DaySevenSuccess
    else:
        call DaySevenFailure from _call_DaySevenFailure

    call DaySevenRelationshipSelection from _call_DaySevenRelationshipSelection
    call DaySevenOutro from _call_DaySevenOutro

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
        i "Killer brought it to us. Tried using Enrico's key on the workshop lockbox, then tried burning the wallet ten feet from my desk."
        w "You solved the murder by making the office look unattended."
        i "I solved the murder by being approachable."
        d "You were lying on the floor eating chips."
        i "Approachably."
        "Nicky rises, checks the evidence seal, and takes formal custody of the bag."
        n "Nobody touches this again until it is logged. Dhampir and my patrol chased them down after they bolted out the fire exit, but Ica, you and the recruit are still giving me separate statements after this."
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
    u "The scene establishes that Enrico died from [day_seven_cause]. Enrico gave thirty years to this city before retiring to manage warehouse supplies and look out for rookies. We will not dishonor that service with an unproven guess."

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
        "Ulysses stops at the contradiction and rotates the relevant case pages toward you."
        u "[day_seven_mismatch]"
        u "That is not a minor discrepancy. It breaks the accusation."
    return


label DaySevenSuccess:
    $ day_seven_actual_name = suspectNames[killer]
    $ day_seven_confession = day_seven_culprit_confession(killer)

    if daySevenIcaSpecial:
        "Nicky steps out to confirm the transfer from the holding room. The waiting lasts only a few minutes, though nobody manages to make them feel short."
        "When she returns, two officers escort [day_seven_actual_name] into the briefing room. Their eyes fix on the bloodstained wallet before anyone says a word."
        n "Dhampir and my LAPD patrol tracked them across four rooftops overnight after they bolted out the fire exit. Picked them up two hours ago trying to slip onto an outbound freight train. They're in custody now, and they've decided to speak in front of the team."
    else:
        "Nicky leaves the room with the reviewed file. The waiting lasts only a few minutes, though nobody manages to make them feel short."
        "When she returns, two officers escort [day_seven_actual_name] into the briefing room. The surviving evidence has been laid out where they can see every piece."
        n "The arrest is complete. They have also decided to speak in front of the team."
    "[day_seven_actual_name]" "Fine. I killed Enrico. [day_seven_confession]"
    "The admission leaves nowhere else for the week to turn. No one cheers immediately. Closing the case does not make the reason for gathering here less grim."

    u "The accusation is correct. Enrico Edge's killer is in custody, and the evidence supporting that arrest is sound."
    "Only then does the room release the breath it has been holding."
    r "Holy shit, we actually got them!"
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
    n "Patrol just radioed in from [day_seven_selected_name]'s address. They produced an airtight alibi—hospital check-in logs during the murder. But our botched arrest presence spooked the real killer. [day_seven_actual_name] ran. Patrol reached their apartment after they'd cleared the block."
    "The actual profile replaces your selected file at the center of the table. Once the missed contradiction is corrected, the rest of the evidence aligns around [day_seven_actual_name]."
    u "The killer is [day_seven_actual_name]. Acting on your unsupported accusation alerted them and gave them the time and warning necessary to escape immediate custody."

    r "We'll find them. We know who we're looking for now."
    d "Yeah. We will."
    m "After we waste time repairing a conclusion that should not have broken."
    n "[day_seven_selected_name] was wrongfully detained and is being released with our apologies. Nobody repeats that accusation outside this room without the correction attached."
    w "Team splits into pursuit and damage control. Same as always, only worse."
    i "This is why I don't volunteer for decisions."

    "Ulysses remains standing at the head of the table. His anger is quiet enough that no one can mistake it for loss of control."
    u "You were given evidence, time, and six people's expertise. You still selected a conclusion the record could not support."
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

    call DaySevenCharacterEnding from _call_DaySevenCharacterEnding

    $ daySevenEndingKey = day_seven_ending_key(
        daySevenCaseSolved, daySevenChosenPartner, daySevenRelationshipOutcome)
    $ day_seven_unlock_ending(daySevenEndingKey)
    return


label DaySevenCharacterEnding:
    if not daySevenChosenPartner:
        call DaySevenEndingAlone from _call_DaySevenEndingAlone
    elif daySevenChosenPartner == "razzle":
        call DaySevenEndingRazzle from _call_DaySevenEndingRazzle
    elif daySevenChosenPartner == "winston":
        call DaySevenEndingWinston from _call_DaySevenEndingWinston
    elif daySevenChosenPartner == "nicky":
        call DaySevenEndingNicky from _call_DaySevenEndingNicky
    elif daySevenChosenPartner == "ica":
        call DaySevenEndingIca from _call_DaySevenEndingIca
    elif daySevenChosenPartner == "ulysses":
        call DaySevenEndingUlysses from _call_DaySevenEndingUlysses
    elif daySevenChosenPartner == "madeline":
        call DaySevenEndingMadeline from _call_DaySevenEndingMadeline
    elif daySevenChosenPartner == "dhampir":
        call DaySevenEndingDhampir from _call_DaySevenEndingDhampir
    return


label DaySevenEndingRazzle:
    scene black with fade
    if daySevenCaseSolved:
        "You find Razzle on the roof above the celebration, letting the cooler air pull her flames into long ribbons behind her."
    else:
        "Razzle catches you outside while you are carrying the last box from your desk. The search lights moving across the city reflect in her flames."

    show razzle at slot(0, total=1), bright zorder 10
    $ _razz_score = day_seven_score("razzle")
    $ _razz_visits = int(ulysses_completed_visits("razzle"))
    $ _razz_romance_ready = (_razz_visits >= DAY_SEVEN_MIN_ROMANCE_VISITS["razzle"] and _razz_score >= DAY_SEVEN_ROMANCE_THRESHOLDS["razzle"])
    $ _razz_friend_ready = (_razz_visits >= DAY_SEVEN_MIN_FRIEND_VISITS and _razz_score >= DAY_SEVEN_FRIEND_THRESHOLDS["razzle"])

    if _razz_romance_ready:
        "She turns as you step onto the gravel, an energetic grin spreading across her face. Small, harmless sparks snap from her hair as she leans in toward you."
        r "Hey, partner! Escaped the noise already, or did you come looking for me?"
    elif _razz_friend_ready:
        "She notices you and offers a warm wave, bumping her shoulder playfully against yours as you lean on the railing."
        r "Hey! Good to see you away from the briefing folders."
    else:
        "She leans on the parapet, her flames burning low and subdued against the night air. She gives a tired nod."
        r "Hey. Long week."

    if not daySevenReplayMode:
        menu:
            "Ask Razzle on a romantic date—drinks, dancing, and just the two of you.":
                $ _razz_intent = "romance"
            "Ask Razzle to hit the clubs as friends—loud music and celebration, no romantic pressure.":
                $ _razz_intent = "friend"
    else:
        $ _razz_intent = "romance" if daySevenRelationshipOutcome == "romance" else "friend"

    if _razz_intent == "romance":
        if daySevenRelationshipOutcome == "romance":
            show razzle flirty at slot(0, total=1), bright zorder 10
            if daySevenCaseSolved:
                r "There it is! You finally found a line hot enough to work!"
            else:
                r "Today sucked. Like, impressively. Still doesn't make me wanna say no to you."
            r "Yeah, newbie. Romantic date. Club, drinks, dancing, and somewhere fireproof when we want the noise to stop."
            "Razzle closes the distance, pausing for a quiet second to let her breath steady and the surface heat dial back before leaning in. The kiss is warm in every possible sense and brief only because she starts laughing against your mouth."
            r "Okay! That was good. We're doing that again when I haven't spent all day solving a murder."
            "The following weekend at The Red Room, the bass vibrates straight through the floorboards. Razzle pulls you onto the crowded dance floor, spinning you around with an ecstatic laugh while small embers shower harmlessly over her shoulders."
            "Later, sitting on the hood of a flameproof cab sharing late-night carnitas, she nudges your knee with her boot."
            r "Admit it. Best date you've ever had, even with the scorch marks."
            "You tell her you're not foolish enough to argue with someone holding fire."
            r "Smart rookie."
        elif _razz_friend_ready:
            $ daySevenRelationshipOutcome = "friend"
            show razzle mouth open at slot(0, total=1), bright zorder 10
            r "I love spending time with you, but not like that. I don't wanna fake the romantic part just because this week got intense."
            r "You are absolutely still coming clubbing with me. Winston too, probably."
            "The next night out is loud, affectionate, and completely platonic. Razzle makes certain the word friend never sounds like a consolation prize."
        else:
            $ daySevenRelationshipOutcome = "rejection"
            show razzle sad at slot(0, total=1), bright zorder 10
            r "No, sorry. We don't know each other like that, and I'm not gonna pretend we do."
            r "I hope things work out for you."
            "She offers a clean farewell and heads back toward the stairwell."
    else:
        if _razz_friend_ready:
            $ daySevenRelationshipOutcome = "friend"
            show razzle mouth open at slot(0, total=1), bright zorder 10
            r "Hell yes! No weird romantic pressure, just loud music, bad dancing, and celebrating. You're definitely coming clubbing with me."
            "The weekend club outing is loud and chaotic. Razzle challenges Winston to a dance-off, loses immediately, and laughs until her flames burn a bright, celebratory lavender."
        else:
            $ daySevenRelationshipOutcome = "rejection"
            show razzle sad at slot(0, total=1), bright zorder 10
            r "No, sorry. We haven't really spent enough time together for that, and I'd rather be honest than polite."
            r "Take care of yourself."
            "She offers a clean goodbye and steps back into the building."
    return


label DaySevenEndingWinston:
    if daySevenCaseSolved:
        scene winstonOfficeOutline with fade
        "Winston escapes the celebration long enough to hide in his office with two slices of pizza and a soda balanced on the case file."
    else:
        scene debriefRoomOutline with fade
        "Winston catches you at the security sign-out desk while you hand in your badge. He signs off on your property release, giving the goodbye a moment away from the crowd."

    show winston at slot(0, total=1), bright zorder 10

    $ _winn_score = day_seven_score("winston")
    $ _winn_visits = int(ulysses_completed_visits("winston"))
    $ _winn_romance_ready = (_winn_visits >= DAY_SEVEN_MIN_ROMANCE_VISITS["winston"] and _winn_score >= DAY_SEVEN_ROMANCE_THRESHOLDS["winston"])
    $ _winn_friend_ready = (_winn_visits >= DAY_SEVEN_MIN_FRIEND_VISITS and _winn_score >= DAY_SEVEN_FRIEND_THRESHOLDS["winston"])

    if _winn_romance_ready:
        "He looks up, his usual easy grin turning a little softer at the edges. He sets down his soda and watches you with undisguised warmth."
        w "Thought you might come looking for me. Either that or you're here to steal my pizza."
    elif _winn_friend_ready:
        "He looks up with an easy, tired grin and nudges a folding chair with his foot."
        w "Grab a seat, newbie. We survived the week."
    else:
        "He glances up from the paperwork on his desk, his expression polite and professional."
        w "Need something signed before you head out?"

    if not daySevenReplayMode:
        menu:
            "Ask Winston on an actual date—pool, greasy diner burgers, and no coworkers.":
                $ _winn_intent = "romance"
            "Ask Winston to play a couple games of pool and grab burgers as friends.":
                $ _winn_intent = "friend"
    else:
        $ _winn_intent = "romance" if daySevenRelationshipOutcome == "romance" else "friend"

    if _winn_intent == "romance":
        if daySevenRelationshipOutcome == "romance":
            w "Oh."
            "For once, Winston reaches for a joke and finds himself a full second too slow."
            if daySevenCaseSolved:
                w "You solve one murder and immediately decide to attempt something dangerous. I respect the momentum."
            else:
                w "I think today proved you can make a terrible decision. This isn't one of them."
            w "Yeah, newbie. Romantic date. Pool first, disgusting burgers after. I'm winning at both, somehow."
            "His familiar grin returns as he catches you at the waist and pulls you close. It disappears again when you kiss him."
            "On Saturday night at Barney's Billiards, the neon sign hums above worn green felt. Winston misses an effortless eight-ball corner shot because he's distracted laughing at your commentary."
            w "That table is tilted. I'm filing a formal grievance with the county."
            "You remind him he was staring straight at you."
            w "I was conducting tactical reconnaissance. Completely different legal category."
            "He laughs, chalking his cue and shaking his head with quiet, genuine affection."
        elif _winn_friend_ready:
            $ daySevenRelationshipOutcome = "friend"
            w "I like you. A lot, actually. Just not in the direction you're aiming, newbie."
            w "Friend version's still available though. Pool, food, occasional unsanctioned hero work—strictly no payroll implications."
            "He keeps the promise. Friendship with Winston remains noisy, competitive, and dependable whenever it matters."
        else:
            $ daySevenRelationshipOutcome = "rejection"
            w "No, newbie. You caught me charming at close range and drew an unsafe conclusion."
            w "I mean it kindly. There isn't a date here."
            "He offers an honest handshake and wishes you well."
    else:
        if _winn_friend_ready:
            $ daySevenRelationshipOutcome = "friend"
            w "Now that is a solid, responsible proposal. Three games of pool, terrible jukebox tunes, and greasy burgers. Winner buys the milkshakes."
            "The weekend pool rematch is noisy and fiercely competitive. Winston runs the table twice, lets you sink the eight ball on the third game, and spends an hour arguing over whether garlic fries qualify as a vegetable."
        else:
            $ daySevenRelationshipOutcome = "rejection"
            w "No, newbie. We haven't spent enough time together to start making standing weekend plans."
            w "Take care of yourself."
            "He offers an honest handshake and steps back toward his office."
    return


label DaySevenEndingNicky:
    if daySevenCaseSolved:
        scene debriefRoomOutline with fade
        "Nicky finishes the last custody signature before stepping away from the celebration. Her motorcycle helmet hangs from one hand."
    else:
        scene debriefRoomOutline with fade
        "Nicky is adjusting her helmet by her motorcycle at the parking gate as you carry your final box to the sidewalk."

    show nicky at slot(0, total=1), bright zorder 10
    $ _nick_score = day_seven_score("nicky")
    $ _nick_visits = int(ulysses_completed_visits("nicky"))
    $ _nick_romance_ready = (_nick_visits >= DAY_SEVEN_MIN_ROMANCE_VISITS["nicky"] and _nick_score >= DAY_SEVEN_ROMANCE_THRESHOLDS["nicky"])
    $ _nick_friend_ready = (_nick_visits >= DAY_SEVEN_MIN_FRIEND_VISITS and _nick_score >= DAY_SEVEN_FRIEND_THRESHOLDS["nicky"])

    if _nick_romance_ready:
        "She turns, one brow arching with that familiar evaluating smirk. Her gaze drops to your hands before rising back to your eyes, unhurried and attentive."
        n "Taking your time leaving, rookie. Or did you have another question for the record?"
    elif _nick_friend_ready:
        "She tucks her notepad into her jacket with a brisk, friendly nod."
        n "Good timing, rookie. What's on your mind?"
    else:
        "She keeps her hands on her handlebars, her expression guarded and neutral."
        n "Case is logged, rookie. Need something official?"

    if not daySevenReplayMode:
        menu:
            "Ask Nicky on an actual date—motorcycle ride, records, and late coffee.":
                $ _nick_intent = "romance"
            "Ask Nicky to ride across town and grab coffee and fries as friends.":
                $ _nick_intent = "friend"
    else:
        $ _nick_intent = "romance" if daySevenRelationshipOutcome == "romance" else "friend"

    if _nick_intent == "romance":
        if daySevenRelationshipOutcome == "romance":
            show nicky curious flirty at slot(0, total=1), bright zorder 10
            if daySevenCaseSolved:
                n "Look at you. Permanent job for five minutes and already making bold personal decisions."
            else:
                n "You made one awful call today. I'm not pretending otherwise. I'm also not pretending it erased everything I learned about you this week."
            n "Yes, rookie. Romantic date. Bike ride, records, diner, and whatever happens after the coffee gets cold."
            "She hooks two fingers into your collar, draws you down to her, and kisses you with none of the hesitation she made you put into the question."
            n "Good. Your pulse was jumping high enough to shake your sleeve."
            "The date stretches through the cool California night: cutting through freeway traffic on the back of her bike, crate-digging through late-night record bins, and ending in an all-night diner booth."
            "She slides a battered cassette tape across the Formica, chin resting on her knuckles."
            n "Found it in the bottom bin. B-sides from '94. Listen to track three and tell me you don't hear that bassline."
            "You ask if this is another investigative test."
            n "Everything with me is a test, rookie. You're passing."
        elif _nick_friend_ready:
            $ daySevenRelationshipOutcome = "friend"
            show nicky content happy at slot(0, total=1), bright zorder 10
            n "No romance, rookie. I like you, but that's not where this is going."
            n "You can still get on the bike, steal my fries, and yell at fictional federal agents with me. Friend terms."
            "Nicky's friendship remains playful and direct. When she wants your company, she asks without making either of you guess what she means."
        else:
            $ daySevenRelationshipOutcome = "rejection"
            show nicky at slot(0, total=1), bright zorder 10
            n "No. We did good work this week, but that's too personal for where we're at."
            n "Keep it professional, rookie."
            "She offers a clean, respectful handshake and heads back to her duties."
    else:
        if _nick_friend_ready:
            $ daySevenRelationshipOutcome = "friend"
            show nicky content happy at slot(0, total=1), bright zorder 10
            n "Deal, rookie. Grab a spare helmet. We'll ride out to that 24-hour breakfast counter, get ridiculous amounts of coffee, and yell at bad police procedurals."
            "Cruising down the boulevard under streetlights, stopping at an all-night diner counter, Nicky breaks down the ridiculous plot holes of The Y-Files with devastating legal precision."
        else:
            $ daySevenRelationshipOutcome = "rejection"
            show nicky at slot(0, total=1), bright zorder 10
            n "No, rookie. We haven't built that kind of rapport outside the squad room yet."
            n "Take care."
            "She offers a clean, respectful nod and zips her jacket."
    return


label DaySevenEndingIca:
    if daySevenCaseSolved:
        scene cubicleOutline with fade
        "Ica has escaped the celebration and reclaimed her chair. A pizza plate floats above her while she pretends not to wait for you."
    else:
        scene debriefRoomOutline with fade
        "Ica is sitting on the wide concrete steps outside the building when you carry down the final box. Her own desk supplies are floating in a lazy orbit around her backpack."

    show ica at slot(0, total=1), bright zorder 10
    $ _ica_score = day_seven_score("ica")
    $ _ica_visits = int(ulysses_completed_visits("ica"))
    $ _ica_romance_ready = (_ica_visits >= DAY_SEVEN_MIN_ROMANCE_VISITS["ica"] and _ica_score >= DAY_SEVEN_ROMANCE_THRESHOLDS["ica"])
    $ _ica_friend_ready = (_ica_visits >= DAY_SEVEN_MIN_FRIEND_VISITS and _ica_score >= DAY_SEVEN_FRIEND_THRESHOLDS["ica"])

    if _ica_romance_ready:
        "She turns, that lazy smirk softening just a fraction. A cold can of soda drifts out of the air and floats directly toward your hand."
        i "Took you long enough, freshie. Was starting to think I'd have to drink two sodas myself."
    elif _ica_friend_ready:
        "She spins lazily in her chair, a half-eaten slice of pizza hovering at chest level."
        i "Sup, freshie. Survived the week without getting us both fired."
    else:
        "She doesn't look up from her comic book, chewing gum with rhythmic disinterest."
        i "If this requires physical exertion, the answer is already no."

    if not daySevenReplayMode:
        menu:
            "Ask Ica on an actual date—cheap snacks, ditching the office, and low effort.":
                $ _ica_intent = "romance"
            "Ask Ica to hang out and do absolutely nothing productive together as friends.":
                $ _ica_intent = "friend"
    else:
        $ _ica_intent = "romance" if daySevenRelationshipOutcome == "romance" else "friend"

    if _ica_intent == "romance":
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
            "At midnight on the gravel roof above a 24-hour convenience store, Ica has four bags of chips and two neon-blue slushies floating in a gentle orbit around your knees."
            "She lazily plucks a chip straight out of the air with her teeth."
            i "See? Peak romance. Zero calories burned getting here."
            "You point out that one of the slushie cups is drifting dangerously close to the drain."
            i "It knows where it belongs."
            "She bumps her shoulder against yours, letting gravity gently drop her head onto your shoulder."
        elif _ica_friend_ready:
            $ daySevenRelationshipOutcome = "friend"
            show ica happy at slot(0, total=1), bright zorder 10
            i "Nah, freshie. Romantic sounds like scheduling and expectations."
            i "You're good to waste time with, though. Friend version can stay."
            "She remains employed and continues saving you a chair whenever doing nothing could use company."
        else:
            $ daySevenRelationshipOutcome = "rejection"
            i "Nope. Don't make it weird."
            "The refusal is effortless and final. She returns to her comic book."
    else:
        if _ica_friend_ready:
            $ daySevenRelationshipOutcome = "friend"
            show ica happy at slot(0, total=1), bright zorder 10
            i "Zero romantic pressure, maximum snacks, and no expectation of productivity? Best proposal I've heard all month. Gas station slushies are on you."
            "The weekend is completely devoid of effort: trading ridiculous wagers over bad board games, floating sofa cushions across the floor, and eating enough junk food to incapacitate a normal human."
        else:
            $ daySevenRelationshipOutcome = "rejection"
            i "Nah, freshie. That sounds like leaving my apartment. Pass."
            "She gives you a lazy salute and returns to her snack."
    return


label DaySevenEndingUlysses:
    scene debriefRoomOutline with fade
    if daySevenCaseSolved:
        "The celebration eventually migrates toward Winston's pizza order. Ulysses remains in the briefing room, aligning the closed files while the noise recedes down the hall."
    else:
        "Ulysses remains in the briefing room after the others leave to pursue the actual culprit. Your terminated identification card rests beside the incorrect file."

    show ulysses at slot(0, total=1), bright zorder 10

    $ _uly_score = day_seven_score("ulysses")
    $ _uly_evenings = int(store.ulyssesPersonalEvenings)
    $ _uly_romance_ready = (
        not store.ulyssesBoundaryViolation or store.ulyssesBoundaryApology
    ) and store.ulyssesRomanceInterest >= store.ULYSSES_DATE_ACCEPT_THRESHOLD and _uly_evenings >= store.ULYSSES_DATE_MIN_PERSONAL_EVENINGS and _uly_score >= DAY_SEVEN_ROMANCE_THRESHOLDS["ulysses"]
    $ _uly_friend_ready = _uly_score >= DAY_SEVEN_FRIEND_THRESHOLDS["ulysses"]

    if not daySevenCaseSolved:
        "You look down at the surrendered badge between you, then meet his eyes."
        u "No."
        "The answer arrives without cruelty and without room to misread it."
        u "I care about what these evenings meant. That makes it more important, not less, that I answer honestly."
        u "I have just ended your employment because your judgment placed an innocent person at risk and allowed a killer to escape. Turning this moment into romance would be irresponsible."
        u "Whatever I know about tomorrow is irrelevant. Today, the answer is no."
        "He wishes you well, but he offers no promise of friendship and no invitation to return."
        $ daySevenRelationshipOutcome = "rejection"
        return

    if _uly_romance_ready:
        "He pauses with his hand resting on the final folder, looking up with that rare, unshielded focus. The usual formal distance in his posture softens as you approach."
        u "You stayed. I was beginning to think you had joined Winston's pizza committee."
    elif _uly_friend_ready:
        "He stacks the surviving files neatly with a tired, respectful nod."
        u "A grueling week, but a necessary conclusion. Did you need a moment before leaving?"
    else:
        "He keeps his hands on the paperwork, posture rigid and correct."
        u "Is there an outstanding procedural question before you take the evening?"

    if not daySevenReplayMode:
        menu:
            "Ask Ulysses on an actual date—dinner, late books, and an evening away from ATLAS.":
                $ _uly_intent = "romance"
            "Ask Ulysses to continue your evening conversations outside the office as friends.":
                $ _uly_intent = "friend"
    else:
        $ _uly_intent = "romance" if daySevenRelationshipOutcome == "romance" else "friend"

    if _uly_intent == "romance":
        if daySevenRelationshipOutcome == "romance":
            "Color reaches Ulysses's face before he finishes setting down the file. Knowing the question existed has done nothing to make answering it easy."
            u "An evening away from ATLAS. Explicitly personal. Intentionally uncertain."
            "You nod."
            u "Yes. There is a bookstore that stays open late and a restaurant nearby with no connection to Winston's standing pizza orders."
            u "I would like to discover the evening in the order it occurs."
            "You step close enough to give him every opportunity to refuse, then kiss him. His surprise lasts only a heartbeat before one careful hand settles at your waist."
            "Browsing the dusty back stacks of the late-night bookstore, Ulysses pulls down a cloth-bound municipal planning ledger from 1952, tapping the spine with a quiet smile."
            u "I could tell you every political scandal hidden in this appendix."
            "You ask if that is his idea of flirting."
            u "It is my idea of sharing an interest. You may evaluate the romance independently."
            "He reaches out, his fingers sliding between yours."
        elif _uly_friend_ready:
            $ daySevenRelationshipOutcome = "friend"
            u "I value you. I value the hours we spent working alone, and I would like those conversations to continue."
            u "But I cannot honestly call that desire romantic. Friendship is what I can offer."
            "The answer is gentle and exact. In the weeks after the case, quiet evenings of books, reports, and private jokes continue without either of you pretending they are dates."
        else:
            $ daySevenRelationshipOutcome = "rejection"
            u "No. You are asking for an intimacy we have not built."
            u "You have earned a place on this team. Do not confuse professional respect with a promise I did not make."
            "He remains polite, but the boundary is complete. The two of you return to the celebration as coworkers."
    else:
        if _uly_friend_ready:
            $ daySevenRelationshipOutcome = "friend"
            u "I would value that very much. The work here requires immense restraint; having someone to speak with without an agenda is rare. Consider the invitation accepted."
            "Quiet evenings of books, municipal history, and coffee continue in the weeks that follow, completely free of supervisory distance."
        else:
            $ daySevenRelationshipOutcome = "rejection"
            u "No. We have not built that level of familiarity outside the squad room."
            u "Good work this week. Get some rest."
    return


label DaySevenEndingMadeline:
    if daySevenCaseSolved:
        scene labOutline with fade
        "Madeline abandons the celebration after exactly one slice of pizza. You find her in the lab pretending to verify a result that has already been verified three times."
    else:
        scene debriefRoomOutline with fade
        "Madeline is packing field equipment into her car by the loading dock when you carry your final box toward the exit gate. She pauses when you approach."

    show madeline at slot(0, total=1), bright zorder 10
    $ _mads_score = day_seven_score("madeline")
    $ _mads_visits = int(ulysses_completed_visits("madeline"))
    $ _mads_romance_ready = (
        getattr(store, "madsRomanceEligible", True)
        and (not getattr(store, "mads_cutoff_violated", False) or getattr(store, "mads_apology_accepted", False))
        and _mads_visits >= DAY_SEVEN_MIN_ROMANCE_VISITS["madeline"]
        and _mads_score >= DAY_SEVEN_ROMANCE_THRESHOLDS["madeline"]
    )
    $ _mads_friend_ready = (
        (not getattr(store, "mads_cutoff_violated", False) or getattr(store, "mads_apology_accepted", False))
        and _mads_visits >= DAY_SEVEN_MIN_FRIEND_VISITS
        and _mads_score >= DAY_SEVEN_FRIEND_THRESHOLDS["madeline"]
    )

    if _mads_romance_ready:
        "She pretends to calibrate a microscope, but her knuckles are white against the adjustment dial. She glances toward you, her sharp gaze softening with reluctant anticipation."
        m "I documented the conclusion. What are you still doing in my laboratory? Unless you have another variable to introduce."
    elif _mads_friend_ready:
        "She caps an analytical marker with a sharp click, looking up with genuine professional respect."
        m "Results are compiled and logged. What do you need?"
    else:
        "She does not turn around from her centrifuge, her back rigid."
        m "The lab is closed for decontamination."

    if not daySevenReplayMode:
        menu:
            "Ask Madeline on an actual date—ice cream, a mini-golf rematch, and no work.":
                $ _mads_intent = "romance"
            "Ask Madeline to grab ice cream and discuss lab results outside work as friends.":
                $ _mads_intent = "friend"
    else:
        $ _mads_intent = "romance" if daySevenRelationshipOutcome == "romance" else "friend"

    if _mads_intent == "romance":
        if daySevenRelationshipOutcome == "romance":
            show madeline flirty at slot(0, total=1), bright zorder 10
            if daySevenCaseSolved:
                m "I understood the category before you clarified it. I was giving you time to improve the wording."
            else:
                if daySevenBriefingResponse == "defend":
                    m "You were catastrophically wrong today, and trying to defend that evidence chain in the briefing room was intellectually indefensible. But even a failed experiment has an identifiable derivation. One failure does not erase every valid datum we collected."
                elif daySevenBriefingResponse == "joke":
                    m "You were catastrophically wrong today, and making a joke about paperwork while Ulysses was firing you was completely unhinged. But one disaster does not invalidate every valid test we ran."
                else:
                    m "You were catastrophically wrong today. You also owned it honestly without making excuses, and one failure does not invalidate every previous result."
            m "Yes. Romantic date. Ice cream first. Then somewhere with enough variables to keep the evening from becoming boring."
            "You suggest a miniature golf rematch. Madeline calls repeating an experiment scientifically lazy, then promptly pulls the folded, heavily annotated scorecard from Visit Two straight out of her lab coat."
            m "I recalculated for the windmill cycle and the synthetic turf friction coefficient. You are losing by at least four strokes."
            "She kisses you abruptly, steps back, and spends several seconds staring at your expression like it generated an unexpected reading."
            m "That result was acceptable. Replication will be required."
            "On Saturday under buzzing floodlights at Pirate's Cove Mini-Golf, Madeline spends three full minutes adjusting her putter angle on hole fourteen, muttering about surface resistance, and sinks a ridiculous bank shot off a plastic pirate anchor."
            m "Mathematical inevitability."
            "You point out that her ball ricocheted off a plastic seagull."
            m "The seagull was a calculated environmental variable. Do not question the methodology."
            "She pulls two cups of blue ice cream from the clubhouse counter with an unapologetic smirk."
        elif _mads_friend_ready:
            $ daySevenRelationshipOutcome = "friend"
            if getattr(store, "mads_cutoff_violated", False):
                show madeline at slot(0, total=1), bright zorder 10
                m "No. Not romantically. We settled that yesterday."
                m "You gave a real apology and did the work, so I'm willing to have you in my lab again. That is a working friendship. Accept the category."
                "You do. Madeline continues labeling your shared work as collaboration, keeping the boundary firm without holding yesterday's breach over you."
            else:
                show madeline flirty curious at slot(0, total=1), bright zorder 10
                m "No. Not romantically."
                m "You are competent enough that I want you in my lab again, which is an unusually strong offer of friendship. Accept the correct category."
                "You do. Madeline continues labeling your shared work as collaboration even after she starts keeping your preferred ice cream in the freezer."
        else:
            $ daySevenRelationshipOutcome = "rejection"
            show madeline distress at slot(0, total=1), bright zorder 10
            m "No. The available data does not support that conclusion either."
            m "Do not ask me to falsify the answer to protect your feelings."
            "She turns back to her instruments without another word."
    else:
        if _mads_friend_ready:
            $ daySevenRelationshipOutcome = "friend"
            if getattr(store, "mads_cutoff_violated", False):
                show madeline at slot(0, total=1), bright zorder 10
                m "Acceptable. You gave a real apology and respected the boundary, which makes an off-site working friendship permissible. Accept the category."
                "You do. Madeline continues labeling your shared work as collaboration, keeping the boundary firm without holding yesterday's breach over you."
            else:
                show madeline flirty curious at slot(0, total=1), bright zorder 10
                m "Acceptable. An off-site evaluation of frozen dairy supplements and analytical methodology. I will bring the data sheets."
                "Sitting on a lab bench splitting blue ice cream, the two of you argue passionately over chemical half-lives without a trace of awkwardness."
        else:
            $ daySevenRelationshipOutcome = "rejection"
            show madeline distress at slot(0, total=1), bright zorder 10
            m "No. I do not maintain casual social relationships without established empirical trust."
            m "Focus on your next assignment."
    return


label DaySevenEndingDhampir:
    if daySevenCaseSolved:
        scene black with fade
        "Dhampir slips out of the celebration with a paper plate of pizza and leans against the quiet wall outside the briefing room."
    else:
        scene debriefRoomOutline with fade
        "Dhampir returns from searching long enough to find you beside the secure exit. He is back in his Hawaiian shirt, though the severe focus has not entirely left his posture."

    show dhampir at slot(0, total=1), bright zorder 10

    $ _dham_score = day_seven_score("dhampir")
    $ _dham_visits = int(ulysses_completed_visits("dhampir"))
    $ _dham_romance_ready = (_dham_visits >= DAY_SEVEN_MIN_ROMANCE_VISITS["dhampir"] and _dham_score >= DAY_SEVEN_ROMANCE_THRESHOLDS["dhampir"])
    $ _dham_friend_ready = (_dham_visits >= DAY_SEVEN_MIN_FRIEND_VISITS and _dham_score >= DAY_SEVEN_FRIEND_THRESHOLDS["dhampir"])

    if _dham_romance_ready:
        "He glances up as you approach, sliding a hot slice of pizza onto a paper plate with an easy smirk. He tilts his head, eyes bright."
        d "Been waiting for you, new blood. Thought you might want something to eat that wasn't touched by five other detectives."
    elif _dham_friend_ready:
        "He raises his paper plate in a casual salute, offering an easy grin."
        d "Surviving the week, I see. Grab a slice if Winston left any."
    else:
        "He leans against the wall, chewing slowly, his gaze drifting past you toward the hallway."
        d "Need a clear path out?"

    if not daySevenReplayMode:
        menu:
            "Ask Dhampir on an actual date—underground music, rooftop pizza, and just the two of you.":
                $ _dham_intent = "romance"
            "Ask Dhampir to check out bad movies and grab pizza as friends.":
                $ _dham_intent = "friend"
    else:
        $ _dham_intent = "romance" if daySevenRelationshipOutcome == "romance" else "friend"

    if _dham_intent == "romance":
        if daySevenRelationshipOutcome == "romance":
            d "Damn. I had a joke ready, but you made the question all sincere. Kinda fucked up of you."
            if not daySevenCaseSolved:
                d "You got today wrong. Badly. I don't think that makes every decent thing you did before it fake."
            d "Yeah, new blood. There's an underground show tomorrow. Music's loud, building's probably condemned, pizza place stays open late. Romantic enough?"
            "You tell him it depends on the kiss. Dhampir grins, leans in, and gives you enough evidence to settle the question."
            d "There. Peer reviewed."
            "The next night in the dimly lit basement of an unlicensed venue, heavy bass vibrates straight through the concrete floor while an obscure hardcore band screams into a battered microphone."
            "Up on the rusting fire escape afterward, Dhampir hands you a lukewarm soda and a greasy paper plate."
            d "Ears ringing yet?"
            "You tell him you may never hear normally again."
            d "Good. Means you're having fun. Romantic, right?"
            "You say that depends on the health code."
            "He laughs, bumping his shoulder against yours against the iron railing."
        elif _dham_friend_ready:
            $ daySevenRelationshipOutcome = "friend"
            d "Not feeling the romantic part, new blood. Sorry."
            d "Still want you around, though. Movies, shows, pizza, hanging out without pretending it needs another label."
            "Dhampir's friendship remains easy and sincere. He keeps inviting you to terrible films and saving the best commentary for the walk afterward."
        else:
            $ daySevenRelationshipOutcome = "rejection"
            d "Nah. We don't have that."
            d "Nothing wrong with asking once. Just take the answer the same way."
            "He gives you a casual nod and heads down the stairs."
    else:
        if _dham_friend_ready:
            $ daySevenRelationshipOutcome = "friend"
            d "Now you're talking. Midnight creature feature at the revival cinema. I'll steal the popcorn, you bring the smuggled soda."
            "The two of you spend Saturday midnight in the back row of an empty downtown theater, laughing hysterically at rubber monsters and cheap blood effects without an ounce of pretense."
        else:
            $ daySevenRelationshipOutcome = "rejection"
            d "Nah, new blood. We're not at the hang-out level yet."
            d "Good luck out there."
            "He steps back into the hall with a casual salute."
    return


label DaySevenEndingAlone:
    if daySevenCaseSolved:
        scene debriefRoomOutline with fade
        "You decide not to turn the end of the case into a private pursuit. The choice leaves room for the team already gathering around you."
        "Winston's pizza arrives in impossible quantities. Razzle starts a toast before anyone finds cups. Nicky corrects three increasingly false versions of the arrest, Madeline guards the evidence from cheese, Dhampir steals the corner seat, and Ica makes a plate float to herself."
        "Ulysses watches the disorder spread across his briefing room, considers stopping it, and closes the door so the rest of the building will not have to hear it instead."
        u "Welcome to ATLAS. Permanently, against several reasonable objections."
        "You end the night at the center of the room—wanted, trusted, and fully cemented as an ATLAS detective."
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
        "You celebrate with the team that brought the case home. The week is won, the office is loud, and your name is on the roster for Monday morning."
    else:
        "You leave alone, with no easy promise attached to what comes next."
    return


label DaySevenGalleryReplay:
    $ day_seven_setup_gallery_replay(daySevenGalleryReplayKey)
    call DaySevenCharacterEnding from _call_DaySevenCharacterEnding_1
    return
