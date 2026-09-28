## Ulysses's six mandatory evening debriefs.
## Each scene combines one investigator-specific report with a continuing
## personal route. Ulysses is never selected from the daytime menu.

label UlyssesEvening:
    scene winstonOfficeOutline with fade
    $ ulysses_report_label = ulysses_prepare_evening()

    if ulysses_completed_visits("ica") >= 5:
        "The route to Ulysses's desk now passes through an aggressively pink office. The color has dried; the room remains as precisely ordered as it was before Ica touched it."
    elif dayWin == 2:
        "You follow the hall to Ulysses's office. Tonight the door is propped open by a dented archive box, and a filing drawer waits half-emptied beside his desk."
    elif dayWin == 3:
        "You follow the smell of fresh coffee to Ulysses's office. The jazz is quiet enough to leave room for the rain ticking against the window."
    elif dayWin == 4:
        if ulyssesPersonalEvenings >= 3:
            "Only the desk lamp is on when you reach Ulysses's office. A record turns at low volume while an old staff photograph rests face-down beside the case folder."
        else:
            "Only the desk lamp is on when you reach Ulysses's office. A record turns at low volume beside the day's open case folder."
    elif dayWin == 5:
        if ulyssesPersonalEvenings >= 4:
            "A cassette case, two books, and a folded chessboard have displaced the usual second stack of files in Ulysses's office. The day's report still occupies the center of his desk."
        else:
            "A second stack of cross-referenced files occupies the corner of Ulysses's desk beside the daily report."
    elif dayWin >= 6:
        "Ulysses's office is brighter than usual. Every remaining file is already arranged across his desk, and the record player is silent."
    else:
        "You follow the quiet hall to Ulysses's office. Light reaches beneath the door, accompanied by low jazz and the soft turn of paper."

    "You knock."
    show ulysses at slot(0, total=1), bright zorder 10
    u "Come in, recruit."
    "Ulysses waits behind his desk with the day's case folder already open and a guest chair pulled into place."

    call expression ulysses_report_label from _call_expression
    call UlyssesFocusComment from _call_UlyssesFocusComment

    if dayWin == 1:
        u "One more thing. LAPD and the DA gave us seven days with this case. After that, LAPD takes over, the files are unsealed, and our operational control is frozen."
        u "I would prefer to hand them a culprit. Get some sleep before we try again tomorrow."

    if dayWin >= 6:
        call UlyssesEveningSix from _call_UlyssesEveningSix
    else:
        $ ulysses_stay_for_personal_time = False
        menu:
            "Stay a little longer after the report.":
                $ ulysses_stay_for_personal_time = True
                $ ulyssesPersonalEvenings += 1
                if ulyssesPersonalEvenings == 1:
                    u "Very well. Dinner is already on its way, and the work is less objectionable with company."
                elif ulyssesPersonalEvenings == 2:
                    u "Stay. I have something less urgent than homicide and more useful than small talk."
                elif ulyssesPersonalEvenings == 3:
                    u "All right. The remaining forms can tolerate a conversation between them."
                elif ulyssesPersonalEvenings == 4:
                    u "Stay. There is context I would rather give you deliberately than let you assemble incorrectly."
                else:
                    u "Good. I had hoped the evening would not end with the last line of the report."
            "Call it a night.":
                if dayWin == 1:
                    u "Sensible. Good first day, recruit."
                elif dayWin == 2:
                    u "Good night. The files will remain exactly this unreasonable tomorrow."
                elif dayWin == 3:
                    u "Then rest. Accuracy deteriorates when exhaustion starts impersonating dedication."
                elif dayWin == 4:
                    u "Of course. Thank you for the report—and for the care you took with its certainty."
                else:
                    u "Go home before Winston finds another reason to order food for twelve people."

        if ulysses_stay_for_personal_time:
            $ play_route_music(audio.music_ulysses, fadein=1.5)
            if ulyssesPersonalEvenings == 1:
                call UlyssesEveningOne from _call_UlyssesEveningOne
            elif ulyssesPersonalEvenings == 2:
                call UlyssesEveningTwo from _call_UlyssesEveningTwo
            elif ulyssesPersonalEvenings == 3:
                call UlyssesEveningThree from _call_UlyssesEveningThree
            elif ulyssesPersonalEvenings == 4:
                call UlyssesEveningFour from _call_UlyssesEveningFour
            else:
                call UlyssesEveningFive from _call_UlyssesEveningFive

    $ stop_route_music(fadeout=1.0)
    hide ulysses
    $ ulyssesEveningsCompleted += 1
    jump advanceDayAfterDebrief


label UlyssesFocusComment:
    show ulysses at slot(0, total=1), bright zorder 10
    $ ulysses_route_counts_value = ulysses_visit_counts()
    $ ulysses_distinct_value = ulysses_distinct_routes()
    $ ulysses_favorite_value = ulysses_favorite_route()
    $ ulysses_favorite_name = ULYSSES_ROUTE_DATA[ulysses_favorite_value][0] if ulysses_favorite_value else ""

    $ ulysses_today_route = ulyssesCurrentRoute
    $ ulysses_today_count = ulysses_completed_visits(ulysses_today_route)

    if dayWin == 1:
        u "One day is not a pattern. For now, I assume you're learning how each of them works."
        u "That is sensible. Their reports tell you what they found; spending the day beside them tells you what they might miss."
    elif ulysses_one_each_strategy():
        u "Razzle, Dhampir, Madeline, Nicky, Winston, and Ica. One day with each."
        u "You sampled every category instead of trusting one method to answer every question. That was disciplined."
    elif ulysses_today_count >= 2:
        $ ulysses_repeat_comment = ULYSSES_REPEAT_COMMENTS[ulysses_today_route][ulysses_today_count]
        u "[ulysses_repeat_comment]"

        if ulysses_today_count == 2:
            u "Two choices are a preference, not a failure to investigate. I only need you to know what that preference is giving you, and what it is not."
        elif ulysses_today_count == 3:
            u "A pattern is beginning to form. That can create useful depth if you continue testing the method instead of merely becoming comfortable inside it."
        elif ulysses_today_count == 4:
            u "Four days is enough time for trust to improve the work and familiarity to distort it. Pay attention to which one is happening."
        elif ulysses_today_count == 5:
            u "You have invested most of the week here. I am not asking you to abandon that choice; I am asking you to make its limits visible before tomorrow."
        else:
            u "The depth is real. So is the responsibility to translate it into an accusation the rest of us can independently review."

        if ulysses_today_route == "ica" and ulysses_today_count == 2:
            u "I am curious which part brought you back. Not suspicious, but curious."
            menu:
                "She notices things when it matters.":
                    $ uly += 1
                    u "She does. You have also learned not to manufacture urgency merely to hold her attention. That is more perceptive than scolding her."
                "I like spending time with her.":
                    $ uly += 1
                    u "Reasonable. Enjoying a colleague's company is not an investigative flaw by itself. Just keep the case present while you are there."
                "Her way of thinking is different from mine.":
                    $ uly += 1
                    u "Very. Difference is useful when you can explain what it reveals instead of treating it as novelty."
    elif ulysses_distinct_value == dayWin:
        if dayWin == 2:
            u "You chose a second method today. Comparing two people this early is sensible; neither report has had time to become your default explanation."
        elif dayWin == 3:
            u "Three days, three methods. You are building breadth deliberately. Begin noting where the reports overlap before the pile becomes difficult to hold at once."
        elif dayWin == 4:
            u "A fourth perspective gives you range, but each line remains shallow. Your notes need to preserve the connections the individual reports do not state."
        elif dayWin == 5:
            u "You are one method away from seeing the investigation from every angle. The breadth is useful because you have continued doing the synthesis yourself."
        else:
            u "You spent one day with everyone. None of those reports is deep alone, but together they give us a complete cross-check. That was difficult and disciplined."
    elif ulysses_favorite_value:
        if dayWin <= 3:
            u "You have begun returning to [ulysses_favorite_name], while still testing another method. That is a healthy balance at this stage."
        elif dayWin == 4:
            u "Your time now has a center without becoming exclusive. Use the outside reports to challenge what feels obvious beside [ulysses_favorite_name]."
        elif dayWin == 5:
            u "The shape of your investigation is clear: depth with [ulysses_favorite_name], then selected checks elsewhere. Make those checks do real work."
        else:
            u "You did not spread your time evenly, but you did not isolate yourself inside one method either. Tomorrow, show me why that balance was enough."
    else:
        if dayWin <= 3:
            u "Your attention is still divided almost evenly. That leaves several possibilities open, which is appropriate this early."
        elif dayWin <= 5:
            u "No single method dominates your week. Your synthesis matters more with each report because nobody else's route is doing it for you."
        else:
            u "You end the week without a dominant method. The final conclusion will depend on how honestly you connect incomplete evidence."

    return


label UlyssesEveningOne:
    show ulysses at slot(0, total=1), bright zorder 10
    $ ulysses_day_one_helped = False
    $ ulysses_day_one_left_promptly = False
    "Ulysses aligns your report with the edge of the folder and adds one brief note in the margin. Only when the formal work is closed does he lean back."
    if dayWin == 1:
        u "That completes your first day. You were thorough enough that I do not have to send the report back before dinner."
    else:
        u "The formal report is finished. You were thorough enough that I do not have to send it back before dinner."

    menu:
        "Offer to help organize tomorrow's work.":
            $ uly += 2
            $ ulysses_day_one_helped = True
            $ ulysses_note_reporting_style("thoughtful")
            u "Thank you. Start with the call sheets. Anything marked in red needed an answer three hours ago."
            "He moves half the stack between you instead of giving you a token page."
            "The first few are routine scheduling problems. Halfway down, an operating budget shows Ulysses's salary reduced in his own handwriting so the rest of payroll can clear."
            "He turns that page without comment and passes you the next call sheet."
        "Say the report is finished and relax in the guest chair.":
            $ uly += 1
            u "A defensible interpretation of 'finished.' Stay there. Dinner is already on its way."
            "You settle deeper into the chair while Ulysses draws the waiting stack toward himself. He works without making your stillness feel like a debt."
            "For a few minutes, the room holds only quiet jazz, turning pages, and his pen making short, decisive marks."
        "Ask whether he already knew how the report would go.":
            u "Yes. That does not exempt either of us from doing it properly."
            "He closes the report rather than reaching for tomorrow's papers."
            u "Knowing that a conversation occurs is not the same as respecting the choices that produce it. You still had to make yours."
            "Before you can ask how many versions he remembers, someone knocks at the office door."

    "A delivery worker arrives with the remains of Winston's standing pizza order: two boxes, one covered in pineapple, and a cardboard tray holding black coffee. Ulysses tips generously from his own wallet."
    u "Winston orders enough food in advance for a siege because quantities are, in his words, 'future Ulysses's problem.'"

    menu:
        "Take a pineapple slice and keep working beside him.":
            $ uly += 2
            if not ulysses_day_one_helped:
                $ ulysses_day_one_helped = True
                "Ulysses clears a place beside the pizza and moves several call sheets within your reach."
                "Among them, an operating budget shows his salary reduced in his own handwriting so the rest of payroll can clear. He turns the page without drawing attention to it."
            else:
                "You reclaim your half of the call sheets before the grease can reach them."
            "Ulysses gives the slice an approving glance and turns the call sheets so both of you can read them."
            u "Pineapple. Winston will be delighted to have an ally and be unbearable about it."
        "Take another slice and ask about the photographs on his desk.":
            $ uly += 1
            "You leave the paperwork on his side of the desk and angle your chair toward the photographs instead."
            "The photographs show ATLAS in various states of victory, exhaustion, and structural peril."
            u "Another evening. If I explain one, Winston will somehow sense it and arrive to dispute my version."
            "He straightens the nearest frame after you set it down, though it was not visibly crooked."
        "Take the coffee instead.":
            u "That one is mine, but I respect the efficiency. There is another cup beneath the files."
            "He rescues both cups from the paperwork. You take the hidden one and make it drinkable while he accepts his black."

    "Jazz fills the quiet left by the closed case folder. Ulysses removes his jacket, leaving the vest and button-up, and rolls each sleeve once."

    menu:
        "Tell him the vest looks good on him.":
            $ uly += 2
            $ ulyssesRomanceInterest += 2
            "Ulysses's hand pauses against one cuff."
            u "Apparently a compliment can still make a simple answer unnecessarily difficult."
            "He finishes rolling the sleeve with excessive concentration. The faint color at his ears lasts longer than the task."
        "Thank him for trusting you with real work.":
            $ uly += 2
            u "I trust what you demonstrated today. Continue demonstrating it and the distinction will become academic."
            "He says it without ceremony, then sets your completed report on the same side of the desk as his own work instead of the intake pile."
        "Ask for permission to leave.":
            $ ulysses_day_one_left_promptly = True
            u "You never needed permission. Good night, recruit."
            "You stand, fold the empty pizza box so it will fit in the bin, and collect your things while Ulysses clears the cups from your path."

    if ulysses_day_one_left_promptly:
        "Ulysses walks you to the office door rather than calling the farewell across his desk."
    else:
        "When the conversation finds a natural pause, you fold the empty pizza box and stand. Ulysses walks you to the office door."
    if dayWin == 1:
        u "Good first day. Tomorrow, give me the truth before you give me the version that sounds impressive."
    else:
        u "Good work tonight. Tomorrow, give me the truth before you give me the version that sounds impressive."
    if ulysses_day_one_helped:
        "Behind him, the remaining stack is noticeably shorter than it was when dinner arrived."
    else:
        "Once you step into the hall, he returns to tomorrow's untouched stack and draws the first call sheet toward him."
    return


label UlyssesEveningTwo:
    show ulysses at slot(0, total=1), bright zorder 10
    $ ulysses_day_two_player_wrote_plan = True
    "After the report, Ulysses opens a narrow filing cabinet beside his desk. Its drawers are labeled FIRE, GRAVITY, PHASING, LAB, POLICE, and WINSTON."
    u "Contingency plans. Do not confuse them with predictions. These are based entirely on past mistakes, which provides more material than I need."

    menu:
        "Open the Winston drawer.":
            $ uly += 1
            "It is nearly empty. One card reads: ASK WHAT HE ALREADY DID. Another reads: DO NOT LET HIM DRIVE."
            u "Planning for Winston becomes fiction very quickly. These two rules survive contact with him."
            "You return both cards in the same order. Ulysses checks anyway, then closes the drawer with one finger."
        "Open the Ica drawer.":
            "The first card reads: ASSIGN TASK. EXPECT REFUSAL. LEAVE TASK AVAILABLE ANYWAY."
            u "The system works often enough to prevent me from replacing it with screaming."
            "Beneath it are several blank cards, apparently reserved for failures no one has invented yet. Ulysses takes one."
        "Open the Razzle drawer.":
            $ uly += 1
            "Every card begins with CHECK FOR FLAMMABLE MATERIALS and ends with LET HER HELP."
            u "Both halves are equally important. Experience taught us the order."
            "He waits for you to replace the cards before shutting the drawer, careful not to disturb their color-coded tabs."

    "Ulysses sets a blank card between you. Across the top, he writes: INCOMPLETE REPORTS, LATE WITNESSES, AND EVIDENCE RECOVERED FROM INSIDE A WALL."
    u "Dhampir made the third category necessary. Give me the first procedure you would actually trust this team to follow."

    menu:
        "Write a plan that assumes the team will improvise.":
            $ uly += 2
            "You draft flexible roles, a fixed evidence chain, and room for whoever reaches the problem first to adapt. Ulysses trims two redundant lines but leaves the structure intact."
            u "Good. A plan that requires everyone to stop being themselves is not a plan. It is a complaint with numbered steps."
        "Write a strict sequence nobody may deviate from.":
            $ uly -= 1
            "Your sequence fills both sides of the card. Ulysses reads it once, then draws a line through the steps that depend on perfect obedience."
            u "That survives until Razzle reads step two, Winston ignores step one, and Dhampir enters through the wall. Account for people as they are."
        "Ask Ulysses to write it because he knows best.":
            $ ulysses_day_two_player_wrote_plan = False
            u "I know what I would write. I am interested in whether you understand the team well enough to disagree."
            "When you still pass him the pen, he accepts it. He writes a short procedure, then talks through every compromise as the card fills."

    "The jazz record reaches its final groove. Ulysses resets it, then takes one of the photographs from his desk. A thirteen-year-old Ulysses stands in a full suit in burned woodland beside Winston, whose outline is blurred by smoke and bad focus."
    u "Montana. I was thirteen. A flame-wielding criminal had burned through miles of forest before either of us arrived."
    u "I had the operation planned. Containment lines, approach, capture, evacuation. Winston ignored the approach within forty seconds."

    menu:
        "And his improvisation worked.":
            $ uly += 2
            u "Eventually. First it made everything louder, faster, and considerably less predictable. Then we captured the villain."
        "You must have hated him.":
            u "For approximately six minutes. Then I realized I had just encountered the only person my foresight could not render clearly."
        "You were remarkably stubborn in that photo. You carry it better now.":
            $ uly += 2
            $ ulyssesRomanceInterest += 2
            "Ulysses looks from the photograph to you, caught off-guard. A faint warmth reaches his face before he can look back down at the desk."
            show ulysses blush at slot(0, total=1), bright zorder 10
            u "A compliment directed at the present is considerably harder to deflect. Thank you."

    "He returns the photograph to its exact place, but not before looking at Winston's blurred outline once more."
    u "We worked together after that. ATLAS became official when I was fifteen. He supplied the reputation. I supplied the legal structure."
    u "Neither version would have survived alone."
    if ulysses_day_two_player_wrote_plan:
        "You file the contingency card in a new GENERAL drawer while the office grows quiet around you."
    else:
        "Ulysses files the contingency card he wrote, leaving enough space behind it for the revisions he clearly expects."
    return


label UlyssesEveningThree:
    show ulysses at slot(0, total=1), bright zorder 10
    $ ulysses_day_three_seen = True
    $ ulysses_day_three_tension = False
    $ ulysses_day_three_choice = ""
    "Ulysses reaches for the report before you finish setting it down. His answer comes a heartbeat before your question."
    u "The supporting statement is already clipped behind the laboratory copy."
    "You had been about to ask where it belonged. He closes his eyes briefly."
    u "That was impolite. Knowing a question is coming does not mean I should answer before you choose to ask it."

    menu:
        "Ask whether the future is always that immediate.":
            $ uly += 1
            u "Always. Everything from the beginning of my life until my death is present in memory. The important events remain fixed; the smaller details update as people choose them."
        "Tell him it saved time.":
            u "Efficiency is not the only consideration. People deserve ownership of their own words."
        "Try to surprise him with a sudden compliment.":
            $ uly += 2
            $ ulyssesRomanceInterest += 2
            "You tell him his eyes are beautiful. The exact sentence pulls color into his face."
            show ulysses blush startled at slot(0, total=1), bright zorder 10
            u "The smaller details change. You appear determined to weaponize that fact."

    "He pours fresh black coffee and leaves the second cup for you to prepare however you like. The music remains low enough that neither of you has to raise your voice."
    u "There is a more important limit. I cannot tell anyone what will happen. Not aloud, not in writing, not through hints."
    u "Early on, Winston and I tried testing it. We thought if he held my hand and suppressed my power, I could write down a warning safely. But foresight is memory already burned into my skull, not an active radiating field. The moment my pen touched paper, the shock nearly stopped my heart."
    u "Winston had to drag me off the floor. We never attempted a workaround again."
    u "Vague advice is safe only when it conveys no concrete outcome. Anything more exact triggers the penalty immediately."

    menu:
        "Ask how he learned the boundary, without asking what he saw.":
            $ uly += 2
            $ ulysses_day_three_choice = "learned_boundary"
            u "Carefully phrased. I learned it badly. I will explain when I can do so without turning tonight into a medical history."
        "Ask him to identify the killer through a loophole.":
            $ uly -= 3
            $ ulyssesBoundaryViolation = True
            $ ulysses_day_three_tension = True
            $ ulysses_day_three_choice = "loophole"
            show ulysses upset talking at slot(0, total=1), bright zorder 10
            u "No. There is no loophole, and my life is not a puzzle mechanism for you to test."
            "He moves the coffee aside and returns the open case forms to the center of the desk. The invitation to discuss his power is over."
        "Tell him he never has to prove the power to you.":
            $ uly += 2
            $ ulysses_day_three_choice = "never_prove"
            u "Thank you. Most people hear an impossible boundary and begin searching for the trick."

    if ulysses_day_three_tension:
        show ulysses upset at slot(0, total=1), bright zorder 10
        "You finish the remaining forms in a silence that is no longer comfortable. Ulysses answers every work question precisely, but he does not reopen the personal conversation."
        "When the final page is filed, he rests one hand on the closed folder."
        u "The future is not permission to take a choice away from someone. Neither is curiosity."
    else:
        "You return to the remaining forms. When you both reach across the desk, you sort the final files into neat stacks side by side."
        if ulyssesRomanceInterest >= ULYSSES_ROMANCE_WARM_THRESHOLD:
            "Your fingers brush over the edge of the final folder. Ulysses doesn't pull away immediately; his hand lingers a beat against yours before he catches himself."
            "He looks at your joined hands, then up at you."
            show ulysses blush talking at slot(0, total=1), bright zorder 10
            u "That detail changed."
            "He withdraws carefully, visibly flustered despite whatever larger shape of the evening he remembers."
        else:
            "Ulysses aligns the finished packet and closes his pen with a quiet, satisfied click."
        u "The future is not permission to stop participating in the present, recruit. I try to remember that."

    return


label UlyssesEveningFour:
    show ulysses at slot(0, total=1), bright zorder 10
    $ ulysses_day_four_release = "quiet"
    "Ulysses reaches the final paragraph of your report and taps one changed word with the end of his pen. You wrote that a witness may return tomorrow instead of promising that they will."
    u "You revised the wording."

    menu:
        "Say certainty should be earned.":
            $ uly += 1
            u "Yes. Especially when certainty is easy to imitate."
        "Say his warning about future statements stayed with you." if ulysses_day_three_seen:
            $ uly += 2
            "The pen goes still beneath his fingers."
            u "Then you listened more carefully than most people do."
        "Say you wanted to leave room for the unexpected." if not ulysses_day_three_seen:
            $ uly += 2
            "The pen goes still beneath his fingers."
            u "A sensible habit. The easiest way to miss the truth is assuming tomorrow is already settled."
        "Joke that you feared his red pen.":
            u "A rational fear, but not the reason I hoped for."
            "The dry answer eases into a small smile before he closes the report."

    "Instead of opening the next folder, Ulysses refreshes both coffees and lowers the jazz until the office feels private rather than merely quiet. He takes his time returning to the desk."
    if ulyssesBoundaryViolation and not ulyssesBoundaryApology:
        show ulysses upset at slot(0, total=1), bright zorder 10
        u "There is a strict limit on my power: I cannot tell anyone what will happen. Anything exact triggers it violently against me."
        u "You pushed against that boundary before. I am stating the rule clearly now so there is no confusion: it is a matter of survival, not preference."
        u "Let us return to the case."
        "He keeps the rest of the evening strictly professional, reviewing the evidence logs without opening the old drawer or the personal photographs."
        "When the files are in order, he bids you a polite, distant goodnight."
        return

    if not ulysses_day_three_seen:
        u "You have been careful with your reporting this week. Most people in this building push for certainty—or ask me to provide it for them."
        u "There is a strict limit on my power: I cannot tell anyone what will happen. Anything exact triggers it violently against me. Leaving you without context would make that boundary seem arbitrary. It is not."
    elif ulysses_day_three_tension:
        u "During our last conversation, things ended poorly. Even so, leaving you with only the warning would make the boundary sound arbitrary. It is not."
    elif ulysses_day_three_choice == "never_prove":
        u "When we spoke last, you told me I never had to prove the boundary to you. Even so, leaving you with only the warning would make it sound arbitrary. It is not."
    elif ulysses_day_three_choice == "learned_boundary":
        u "When we spoke last, you asked how I learned the boundary without asking me to demonstrate it. I said I would explain when I could do so honestly."
    else:
        u "When we spoke last, we discussed the boundaries around my foresight. Leaving you with only the warning would make it sound arbitrary. It is not."

    "He opens a shallow drawer and removes an old staff photograph. His younger face is easy to find. Beside him stands a coworker whose badge reads DAKOTA."
    u "Last year, when I was nineteen, Dakota and I were working late. I had seen something that affected our friend, and I believed I had found language indirect enough to talk about why it bothered me."
    u "Dakota is a coworker I trust deeply. That trust made me blind to the dangers of connecting to someone and being able to tell them what's on my mind."
    "His thumb rests against the edge of the photograph. The next sentence takes longer than the rest."
    show ulysses upset talking at slot(0, total=1), bright zorder 10
    u "I tried to tell Dakota. The power stopped me. I suffered a seizure before I finished and remained comatose for four months."
    "The statement is precise, but it no longer arrives without context. His grip on the photograph is the only part of him that looks rehearsed."

    menu:
        "Say he does not owe you any information that risks him.":
            $ uly += 3
            u "I know. Hearing someone else say it is still useful."
        "Ask about Dakota, not the forbidden warning.":
            $ uly += 2
            u "A capable coworker and a great friend. Patient with me and how grumpy I can be."
            u "She didn't blame me for what happened. I managed that adequately on my own."
        "Ask what Winston did during those four months.":
            $ uly += 1
            u "Stayed. Handled ATLAS poorly, kept it alive successfully, and insulted every physician who used the phrase 'wait and see.'"
        "Ask how he safely gives the team useful guidance.":
            $ uly += 2
            u "I speak from evidence, experience, and ordinary judgment. If I cannot defend advice without invoking the future, I do not give it."
            u "It is slower than certainty and considerably safer than pretending certainty belongs to me alone."

    u "There is no pain from ordinary use. No headache, no warning, nothing dramatic enough to make people stop envying it."
    u "I simply remember a future I cannot share. Sometimes I hate it. Sometimes I would surrender it if surrender were possible."

    menu:
        "Tell him knowing everything sounds lonely.":
            $ uly += 2
            u "It can be. Especially when concern sounds like secrecy and preparation looks like control."
        "Tell him he can be uncertain with you anyway.":
            $ uly += 3
            $ ulyssesRomanceInterest += 1
            "His expression softens."
            u "That should be impossible. I find the offer appealing."
        "Say the power is still worth having.":
            $ uly -= 1
            u "Perhaps. I would prefer not to have the value of it explained to me tonight."

    "To release the weight of the conversation, Ulysses pulls a ridiculous paperback from his shelf. Its cover depicts an astronaut arguing with a sentient vending machine."
    show ulysses at slot(0, total=1), bright zorder 10
    u "Mysteries are unbearable. Comedy occasionally earns its uncertainty honestly."

    menu:
        "Read the absurd back-cover description aloud.":
            $ uly += 2
            $ ulysses_day_four_release = "laugh"
            "By the third catastrophic vending-machine pun, Ulysses is smiling openly. The fourth earns one brief, genuine laugh."
        "Ask for something more serious.":
            $ ulysses_day_four_release = "serious"
            u "We have spent the evening discussing death, seizures, and homicide. I believe we have satisfied seriousness."
            "He sets the paperback within reach but does not press it on you. The two of you let the music carry the next minute instead."
        "Call his taste terrible but charming.":
            $ uly += 2
            $ ulyssesRomanceInterest += 1
            $ ulysses_day_four_release = "smile"
            u "That was nearly smooth. The qualification saved you."
            "He turns the book over as though reconsidering the cover, but the corner of his mouth stays lifted."

    if ulysses_day_four_release == "laugh":
        "The laughter does not erase what he told you. It gives the two of you somewhere gentler to set it down."
    elif ulysses_day_four_release == "smile":
        "The small smile does not erase what he told you, but it keeps the conversation from ending inside its worst memory."
    else:
        "Nothing needs to lighten the confession immediately. You remain with him in the quiet until he is the one who closes the subject."
    return


label UlyssesEveningFive:
    show ulysses at slot(0, total=1), bright zorder 10
    $ ulysses_day_five_activity = "chess"
    $ ulysses_day_five_music = "cassette"
    "When the report is complete, Ulysses reaches automatically for another stack. You place one hand over the top page before he can lift it."

    menu:
        "Tell him the work will still exist after one quiet hour.":
            $ uly += 2
            u "That is the most persuasive threat anyone has made today."
        "Remind him that he makes everyone else take breaks.":
            $ uly += 2
            u "Leadership would be substantially easier if nobody applied my rules to me."
        "Take the folder and refuse to return it.":
            $ uly -= 1
            u "A dramatic approach. Put the confidential case file down, please. Then we can take the same break without committing theft."

    "Ulysses is eventually convinced. He loosens his tie, removes his vest, and moves from behind the desk to the guest side. He pulls open a shallow desk drawer containing classical music, Duran Duran, U2, the Cranberries, and several louder tapes Winston has labeled DEPRESSING ULY MUSIC."

    if ulysses_completed_visits("ica") >= 5:
        "Pink walls surround the orderly desk and dark shelves. Ulysses follows your glance around the room."
        u "I like the color. Do not tell Ica until I have extracted several weeks of apology labor from her."

    menu:
        "Choose one of the louder cassettes and challenge him to chess.":
            $ uly += 2
            u "Very well. I will watch you try."
        "Choose the Cranberries and read beside him.":
            $ uly += 2
            $ ulysses_day_five_activity = "reading"
            u "Good choice. Conversation remains optional."
        "Leave the jazz on and ask him to choose a pastime.":
            $ uly += 1
            $ ulysses_day_five_music = "jazz"
            u "Comfortable delegation. Chess, then. I have spent all week watching you make decisions; reciprocity seems fair."

    if ulysses_day_five_activity == "chess":
        "The chessboard comes from beneath the bookshelves. Ulysses knows the broad direction of the game, but your small choices continue adjusting beneath his hands. He does not coach, hurry, or pretend not to enjoy watching you attempt an ambush."
        "When the position becomes hopeless, he turns the board sideways so both of you can study the mess rather than ending it immediately."
    else:
        "Ulysses chooses two books from the shelf and gives you first pick. He takes the guest chair beside yours instead of retreating behind the desk."
        "For a while, the only interruptions are turned pages and the cassette changing sides. When either of you finds a particularly absurd line, the book tips toward the other without requiring conversation."

    if ulyssesBoundaryViolation and not ulyssesBoundaryApology:
        menu:
            "Apologize for treating his survival like another clue.":
                $ uly += 3
                $ ulyssesBoundaryApology = True
                u "Thank you. I do not need perfection. I need to know that a boundary remains real after curiosity appears."
            "Avoid bringing the earlier question up again.":
                "Ulysses does not force the conversation. The distance it created remains present between the chairs."

    menu:
        "Turn your hand palm-up beside his." if not (ulyssesBoundaryViolation and not ulyssesBoundaryApology):
            $ uly += 2
            $ ulyssesRomanceInterest += 3
            if ulysses_day_five_activity == "chess":
                "You rest your hand beside his on the edge of the board, then turn it palm-up."
            else:
                "When both books come to rest on the table, you leave your hand beside his and turn it palm-up."
            "Ulysses looks at the invitation. The color reaches his face before his fingers settle carefully into yours."
            show ulysses blush talking at slot(0, total=1), bright zorder 10
            u "This evening has become difficult to categorize. I was not sufficiently prepared."
            menu:
                "Tell him he can stop categorizing it.":
                    $ uly += 2
                    $ ulyssesRomanceInterest += 1
                    "His thumb moves once across your hand."
                    u "For one hour, perhaps."
                "Tell him he is cute when he loses control of a conversation.":
                    $ uly += 1
                    $ ulyssesRomanceInterest += 1
                    u "I have not lost control. I have strategically declined to recover it."
                "Let the silence remain comfortable.":
                    $ uly += 2
                    if ulysses_day_five_activity == "chess":
                        "You sit together while the music plays and the abandoned chess game waits."
                    else:
                        "You sit together while the music plays, your places held in two books neither of you is in a hurry to reopen."
        "Keep the moment companionable rather than romantic.":
            $ uly += 2
            if ulysses_day_five_activity == "chess":
                "You finish the game in comfortable quiet. Ulysses wins, though he gives your failed ambush more consideration than it deserves."
            else:
                "You reach the end of a chapter in comfortable quiet. Ulysses notices where you stop and waits until your bookmark is in place before standing."

    if ulysses_day_five_music == "jazz":
        "The hour stretches beyond its promised edge. Neither of you points that out until the record reaches its final groove."
    else:
        "The hour stretches beyond its promised edge. Neither of you points that out until the cassette clicks off."
    return


label UlyssesEveningSix:
    show ulysses at slot(0, total=1), bright zorder 10
    $ ulysses_day_six_invited_closeness = False
    "Ulysses places every remaining suspect file across his desk. Tonight the music is off. The only sounds are paper, the office clock, and distant traffic."

    if ulysses_one_each_strategy():
        call UlyssesCrossReportDeduction from _call_UlyssesCrossReportDeduction
    elif len(remainingSuspects) == 1:
        u "Your work already leaves one name. We will verify the chain once more, but there is nothing honest to add to that conclusion."
        "You follow the evidence from the first elimination to the final surviving file. Ulysses checks each connection, then lets you seal the accusation packet yourself."
    elif len(remainingSuspects) <= 3:
        u "The formal evidence has done its job. The quieter observations you made must distinguish the final [len(remainingSuspects)]."
        u "I will organize what you found. I will not replace your judgment with mine."
        "You arrange the unrecorded observations beside the formal evidence. Ulysses asks where each impression came from until you can separate what you noticed from what you merely assumed."
    else:
        u "You distributed your time in a way that left [len(remainingSuspects)] viable suspects."
        u "That was your decision. I can help you arrange the reports, but I cannot manufacture the depth you chose not to gather."
        "Together, you mark the gaps instead of disguising them. The accusation packet remains imperfect, but none of its certainty is false."

    "Once the accusation packet is prepared, Ulysses closes it and moves it beyond either person's reach. The case is finished for tonight."
    $ ulysses_honest_reports = ulyssesReportingStyle.get("honest", 0)
    $ ulysses_thoughtful_reports = ulyssesReportingStyle.get("thoughtful", 0)
    $ ulysses_deflecting_reports = ulyssesReportingStyle.get("deflecting", 0)

    if ulysses_deflecting_reports >= 2:
        u "You spent part of this week making your reports sound better than the days that produced them. You improved when corrected. I noticed both facts."
    elif ulysses_honest_reports + ulysses_thoughtful_reports >= 4:
        u "You reported mistakes as readily as successes and treated context as part of the evidence. That made you useful in this office."
    else:
        u "Your reporting became more precise as the week continued. There is still room to improve. That is not an insult."

    menu:
        "Stay after the final report.":
            $ ulyssesPersonalEvenings += 1
            u "Stay. The accusation can wait behind a closed folder for one evening."
        "Call it a night and preserve the professional boundary.":
            u "Of course. You did the work honestly, and I will see you in the briefing room tomorrow."
            "Ulysses walks you to the door. The closed accusation packet remains on his desk, complete without requiring the evening to become anything else."
            return

    # Case preparation belongs to calendar Day Six. Personal conversations
    # still follow the order the player has actually experienced.
    if ulyssesPersonalEvenings < 6:
        $ ulysses_next_personal_label = (
            "UlyssesEveningOne", "UlyssesEveningTwo", "UlyssesEveningThree",
            "UlyssesEveningFour", "UlyssesEveningFive")[ulyssesPersonalEvenings - 1]
        call expression ulysses_next_personal_label from _call_UlyssesLatePersonalEpisode
        return

    if ulyssesBoundaryViolation and not ulyssesBoundaryApology:
        menu:
            "Apologize for treating his survival like another clue.":
                $ uly += 3
                $ ulyssesBoundaryApology = True
                u "Thank you. I do not need perfection. I need to know that a boundary remains real after curiosity appears."
            "Leave the past unaddressed.":
                "Ulysses does not force the conversation. The distance it created remains between you."

    menu:
        "Tell him these evenings became the best part of the week." if ulyssesPersonalEvenings >= 3 and not (ulyssesBoundaryViolation and not ulyssesBoundaryApology):
            $ uly += 3
            $ ulyssesRomanceInterest += 2
            $ ulysses_day_six_invited_closeness = True
            "Ulysses looks down at the closed packet, then back at you."
            show ulysses blush talking at slot(0, total=1), bright zorder 10
            u "They became the portion I most looked forward to as well. That sentence was not in the report."
        "Tell him you were glad you stayed late tonight." if ulyssesPersonalEvenings < 3 and not (ulyssesBoundaryViolation and not ulyssesBoundaryApology):
            $ uly += 2
            $ ulyssesRomanceInterest += 1
            $ ulysses_day_six_invited_closeness = True
            "Ulysses looks down at the closed packet, then back at you."
            u "I am glad as well. The work is less grueling with company."
        "Thank him for trusting your judgment.":
            $ uly += 2
            u "You earned trust by giving me reasons to revise it every evening. Keep doing that."
        "Say you are relieved the reports are over.":
            u "Understandable. I am less certain that I share the relief."

    if ulysses_day_six_invited_closeness:
        menu:
            "Step close and straighten his tie." if not (ulyssesBoundaryViolation and not ulyssesBoundaryApology):
                $ ulyssesRomanceInterest += 2
                "When you stand, you reach across the desk and straighten the shifted tie against his collar."
            "Tell him his tie shifted and let him fix it.":
                $ ulysses_day_six_invited_closeness = False
                "You mention the crooked knot. Ulysses corrects it himself, smiling faintly at your attention."
    else:
        "When you stand, you mention that his tie has shifted during the long review. Ulysses corrects the knot and smooths it back into place."

    $ ulysses_romance_eligible = (
        not (ulyssesBoundaryViolation and not ulyssesBoundaryApology)
        and ulyssesPersonalEvenings >= ULYSSES_DATE_MIN_PERSONAL_EVENINGS
    )

    if (uly >= ULYSSES_HIGH_THRESHOLD and ulyssesRomanceInterest >= ULYSSES_ROMANCE_HIGH_THRESHOLD and ulysses_day_six_invited_closeness and ulysses_romance_eligible):
        "Ulysses catches your hand before you can withdraw it. His composure lasts until your thumb brushes the edge of his vest."
        show ulysses blush startled at slot(0, total=1), bright zorder 10
        menu:
            "Tell him he looks good when he forgets the next line.":
                $ uly += 3
                $ ulyssesRomanceInterest += 1
                u "I have not forgotten it. I am reconsidering whether it deserves to interrupt this."
            "Lean closer and let him decide the distance.":
                $ uly += 3
                $ ulyssesRomanceInterest += 1
                "He leans forward until only a breath remains between you, then stops. His hand stays around yours."
                u "Tomorrow has its own decisions. I will not borrow them tonight."
            "Squeeze his hand and remain beside him.":
                $ uly += 2
                "The two of you stay there, close enough that neither can mistake the silence for professionalism."
    elif (uly >= ULYSSES_WARM_THRESHOLD and ulyssesRomanceInterest >= ULYSSES_ROMANCE_WARM_THRESHOLD and ulysses_day_six_invited_closeness and ulysses_romance_eligible):
        "Ulysses catches your hand briefly, then releases it with a small, flustered smile."
        show ulysses blush at slot(0, total=1), bright zorder 10
        u "You have become extremely comfortable adjusting your cofounder."
    else:
        if ulysses_day_six_invited_closeness:
            "Ulysses thanks you and carefully corrects the knot by another fraction of an inch."
        else:
            "He checks the knot in the dark reflection of the office window, apparently satisfied with your warning."

    u "I know what the calendar says comes next. I would rather let tomorrow wait."
    "For several more minutes, you do. The accusation packet remains closed, the coffee cools, and Ulysses allows the present to be enough."
    return


label UlyssesCrossReportDeduction:
    u "You did something none of the focused approaches could do. You spent one day inside every investigative method."
    u "Each report is shallow by itself, but together they eliminated five names. That leaves four surviving files."
    u "Before Enrico died, he caught someone siphoning illegal chemical stimulants from the evidence lockup. I pulled the ATLAS badge access logs and dispatch records for that exact window."
    "He arranges the four remaining files around the center of the desk and places the badge access and dispatch logs between them."
    $ ulysses_candidate_profiles = ulysses_candidate_profile_text()
    "The surviving suspect logs read:\n\n[ulysses_candidate_profiles]"
    u "Three of these suspects were logged across town or in separate wings. Only one person swiped into Evidence Storage C during the siphoning window."
    $ ulyssesCrossReportAttempts = 0
    jump UlyssesCrossReportChoice


label UlyssesCrossReportChoice:
    menu:
        "Use intuition for a nudge.":
            $ ulysses_cross_hint = ulysses_intuition_hint_text()
            "[ulysses_cross_hint]"
            u "A direction, not a conclusion. Check it against the files."
            jump UlyssesCrossReportChoice
        "Victor Veytovi." if 1 in remainingSuspects:
            $ ulysses_cross_choice = 1
        "Jermiah Jones." if 2 in remainingSuspects:
            $ ulysses_cross_choice = 2
        "Barry Baxter." if 3 in remainingSuspects:
            $ ulysses_cross_choice = 3
        "Carl Creek." if 4 in remainingSuspects:
            $ ulysses_cross_choice = 4
        "Tucker Thompson." if 5 in remainingSuspects:
            $ ulysses_cross_choice = 5
        "Edgar Ebbington." if 6 in remainingSuspects:
            $ ulysses_cross_choice = 6
        "Simon Streep." if 7 in remainingSuspects:
            $ ulysses_cross_choice = 7
        "Kyle Kallus." if 8 in remainingSuspects:
            $ ulysses_cross_choice = 8
        "Alan Ashmore." if 9 in remainingSuspects:
            $ ulysses_cross_choice = 9

    if ulysses_cross_choice != killer:
        $ ulyssesCrossReportAttempts += 1
        u "No. Check the log again. That person was logged outside the storage wing during the siphoning window. Look for the authorized swipe into Evidence Storage C."
        jump UlyssesCrossReportChoice

    if ulyssesCrossReportAttempts == 0:
        $ uly += 3
        u "Correct. You built the conclusion instead of waiting for me to provide it."
    else:
        $ uly += 1
        u "Correct."

    $ record_ulysses_cross_report_reveal()
    $ ulysses_cross_killer_name = suspectNames[killer]
    u "Every report converges on [ulysses_cross_killer_name]. No other remaining profile had access to the lockup during that window."
    "Ulysses enters the cross-report analysis into the formal case log. The other three files close, leaving one name at the center of the desk."
    return


## Razzle Dazzle reports

label UlyssesReportRazzle1:
    show ulysses at slot(0, total=1), bright zorder 10
    u "Razzle's message said, and I quote, 'WE ACTUALLY GOT SOMETHING,' followed by four exclamation marks. Give me the version suitable for a case file."
    "You describe Landon's interview, the identifying feature he definitely did not see, and the care Razzle took before closing the statement."
    u "Good. A negative identification is useful when the witness is certain about the absence rather than uncertain about the whole face."
    if ulyssesCurrentClue:
        u "The formal result is straightforward: [ulyssesCurrentClue]"
    menu:
        "Emphasize that Razzle slowed down for the witness.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "That matters. Her volume obscures how carefully she treats frightened people when she remembers to pause."
        "Say the witness gave you a name to remove.":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "Accurate, if incomplete. Record the certainty level beside it."
        "Take credit for keeping Razzle focused.":
            $ uly -= 1
            $ ulysses_note_reporting_style("deflecting")
            u "Her signed notes suggest she contributed more than your summary allows. Report partners, not supporting furniture."
    return


label UlyssesReportRazzle2:
    show ulysses at slot(0, total=1), bright zorder 10
    u "No witness statement today. I did, however, receive a call from a restaurant asking whether ATLAS carries fire-alarm insurance."
    "You confirm that the excursion produced no physical evidence, summarizing the fire-safety precautions taken while off-site."
    u "Razzle makes public precautions look effortless. That does not mean they cost her nothing."
    menu:
        "Say she deserved an afternoon where nobody treated her like a hazard.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Agreed. I would prefer the city reach that conclusion without requiring us to reserve fireproof seating."
        "Report that the day produced no evidence.":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "Correct. Personal context is valuable; it is not a suspect exclusion. Keep those categories separate."
        "Say getting pizza with her was investigation enough.":
            $ uly -= 1
            $ ulysses_note_reporting_style("deflecting")
            u "Then the receipt should make a compelling arrest warrant."
    return


label UlyssesReportRazzle3:
    show ulysses at slot(0, total=1), bright zorder 10
    u "Brandon's revised statement arrived before you did. It is considerably less crowded than his first account."
    "You explain the memory board, the irrelevant details removed from it, and the doorway observation that survived every pass."
    if height_memory_assisted:
        u "Razzle stepped in to finish organizing the board, but the doorway observation remained intact. Record the assistance alongside the result."
    elif height_memory_setbacks == 0:
        u "You protected both reliable memories without discarding either one. Efficiently done."
    else:
        u "You disturbed the useful memories [height_memory_setbacks] times, corrected the board, and still preserved the source. Record both the recovery and the result."
    if ulyssesCurrentClue:
        u "That gives us a defensible exclusion: [ulyssesCurrentClue]"
    menu:
        "Credit Brandon for correcting his own memory.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Precisely. You organized recall; you did not manufacture it. That distinction protects the result."
        "Credit Razzle for keeping the interview encouraging.":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "She is unusually good at making effort feel less like an examination."
        "Call the discarded memories useless.":
            $ uly -= 1
            u "Irrelevant to this question is not the same as useless. Witnesses are people, not damaged filing cabinets."
    return


label UlyssesReportRazzle4:
    show ulysses at slot(0, total=1), bright zorder 10
    u "Elena could not give you the dramatic answer Razzle wanted. That may be the most reliable part of today's statement."
    "You recount the uncertain silhouette, the effect of posture and distance, and the grocery-store camera that may have captured the passing headlights."
    u "Good restraint. A witness who says 'I do not know' is providing information we can trust."
    menu:
        "Recommend preserving the tape before interpreting it.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Yes. Duplicate it, document the counter, and let the image disagree with us if necessary."
        "Say Razzle should have pressed harder.":
            $ uly -= 2
            $ ulysses_note_reporting_style("deflecting")
            u "Pressure does not sharpen memory. It sharpens a witness's desire to satisfy you."
        "Admit the lead is uncertain but worth following.":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "That is the correct weight. Neither dismissal nor promotion to proof."
    return


label UlyssesReportRazzle5:
    show ulysses at slot(0, total=1), bright zorder 10
    u "Six hours of grocery-store tape. I assume the cat attacking the bag was not our culprit."
    "You describe the preserved frame, the position of the car, the killer's stress reaction under the headlights, and the brief sweep that exposed their loose hair."
    u "Useful, but not yet a formal identification. Recreating the light is better than pretending monochrome footage contains color because we want it to."
    menu:
        "Explain Razzle labeled, duplicated, and timed the tape.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Then her enthusiasm did not outrun her evidence handling. Make certain that appears in the report."
        "Focus only on the possible hair clue.":
            $ uly += 1
            u "Possible. Preserve the observed stress reaction too. Behavioral cues often become useful after the list is smaller."
        "Say the reconstruction will definitely identify the killer.":
            $ uly -= 1
            $ ulysses_note_reporting_style("deflecting")
            u "It may identify a category. Certainty does not improve when announced early."
    return


label UlyssesReportRazzle6:
    show ulysses at slot(0, total=1), bright zorder 10
    "Ulysses reads Elena's signed certainty statement twice, then checks the numbered wig procedure and borrowed-car placement."
    u "No suggestive labels, no visible samples before the test, and the geometry matches the recorded frame. Good."
    if ulyssesCurrentClue:
        u "The result is admissible as an investigative conclusion: [ulyssesCurrentClue]"
    menu:
        "Say the reconstruction narrowed the list, not named the killer.":
            $ uly += 2
            $ ulysses_note_reporting_style("honest")
            u "Exactly. Confidence in evidence includes knowing where it stops."
        "Praise Razzle for becoming more patient across the interviews.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "She was always capable of patience. You gave her reasons to practice it."
        "Say Elena solved the case for you.":
            $ uly -= 1
            u "Elena answered one carefully constructed question. Do not place the burden of the entire case on a witness."
    return


## Dhampir reports

label UlyssesReportDhampir1:
    show ulysses at slot(0, total=1), bright zorder 10
    u "The scene officer reported that Dhampir left the house without killing anyone. They sounded pleasantly surprised."
    "You describe the hero-suit transformation, the reconstructed approach, the physical contradiction, and the ordinary pizza stop that followed."
    if ulyssesCurrentClue:
        u "The useful conclusion is [ulyssesCurrentClue]"
    menu:
        "Describe Dhampir's method without excusing his reputation.":
            $ uly += 2
            $ ulysses_note_reporting_style("honest")
            u "Good. His work can be excellent while his broader methods remain objectionable. Both facts fit in one report."
        "Say his manner was disrespectful to Enrico.":
            $ uly -= 1
            u "Casual, yes. Careless with the victim, no. Learn the difference before you accuse him of it."
        "Focus on the intact scene log and clean evidence handling.":
            $ uly += 1
            $ ulysses_note_reporting_style("thoughtful")
            u "That is why I continue trusting his fieldwork even when I dislike what follows some of his arrests."
    return


label UlyssesReportDhampir2:
    show ulysses at slot(0, total=1), bright zorder 10
    u "Your report begins with a dead squirrel and ends with a vampire film. I assume the middle improves its relevance."
    "You report that the day was spent off-duty between convenience store errands and an old vampire film, producing no direct case leads."
    u "No case progress. Some useful understanding of the person conducting future scene work."
    menu:
        "Say people decide what Dhampir is before he speaks.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Then he speaks, and they develop entirely different concerns. Still, you understood his point."
        "Report only that the day was recreational.":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "Accurate. I will file the movie criticism somewhere safely distant from the murder evidence."
        "Say killing the squirrel was disturbing.":
            u "It was. He will tell you it was dinner and therefore efficient. I have learned not to ask follow-up questions near lunch."
    return


label UlyssesReportDhampir3:
    show ulysses at slot(0, total=1), bright zorder 10
    u "Madeline submitted twenty pages of scanner output. Dhampir submitted one page reading, 'We found the weird marks.' Reconcile them for me."
    "You describe the projected room, the impossible attack paths, and the wound-producing surfaces that the original investigators overlooked."
    if dhampir_ispy_result.get("quality") == "perfect":
        u "Madeline noted that you separated every contradiction from the false leads without assistance."
    elif dhampir_ispy_result.get("quality") == "assisted":
        u "Madeline finished the scan. That preserves the evidence, though not the opportunity for you to practice reading it."
    else:
        u "The scan required correction, but your final marks agree with Madeline's controls."
    if ulyssesCurrentClue:
        u "Combined, they support this: [ulyssesCurrentClue]"
    menu:
        "Credit Madeline's scanner and Dhampir's reconstruction equally.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Correct. Instrument without interpretation is noise; interpretation without measurement is speculation."
        "Say your intuition found the contradictions.":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "It directed your attention. The measured marks still carry the conclusion."
        "Dismiss Dhampir's contribution as acting out possibilities.":
            $ uly -= 1
            u "His body can reproduce movement ordinary models exclude. That is expertise, however casually he presents it."
    return


label UlyssesReportDhampir4:
    show ulysses at slot(0, total=1), bright zorder 10
    u "Today you reconstructed the minute after Enrico died rather than the attack itself."
    "You explain the movement through the room, the unlogged impression of the killer's reaction, and the numbered marker whose object never reached evidence."
    u "Keep the behavioral impression out of the formal exclusions. The missing item is the stronger next step."
    menu:
        "Say Dhampir remained casual without disrespecting Enrico.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "That is an important distinction. His worldview is unsettling; his attention to victims is not absent."
        "Record the reaction category as proven.":
            $ uly -= 2
            u "No. One reconstruction gives direction, not proof."
        "Recommend tracing the marker's trajectory.":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "Agreed. Something torn loose had to travel somewhere."
    return


label UlyssesReportDhampir5:
    show ulysses at slot(0, total=1), bright zorder 10
    u "The training-room dummy now requires replacement. Dhampir labeled the damage 'educational.'"
    "You report the controlled weapon tests, the influence of leverage and supernatural movement, and the subtle build implications that remain too uncertain for the notebook."
    u "Technique explains force more reliably than appearance in a powered population. Nicky will appreciate that sentence."
    menu:
        "Emphasize Dhampir's control during the demonstration.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "He is efficient when he chooses violence. My objection has never been that he lacks discipline."
        "Say sparring with him was reckless but exciting.":
            $ uly -= 1
            u "Excitement is not a safety protocol. Fortunately, Dhampir appears to have supplied one for both of you."
        "Connect the force test to the missing object's path.":
            $ uly += 2
            $ ulysses_note_reporting_style("honest")
            u "Good. The next search now has a bounded location instead of a hopeful wall."
    return


label UlyssesReportDhampir6:
    show ulysses at slot(0, total=1), bright zorder 10
    "Ulysses checks every seal number on the recovered fragment before reading the search log."
    u "Phasing located it. Procedure made it useful. Dhampir occasionally remembers that Nicky can sense joy."
    if ulyssesCurrentClue:
        u "The recovered material establishes this: [ulyssesCurrentClue]"
    menu:
        "Praise the chain of custody before the supernatural search.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Exactly. Spectacular recovery means very little if nobody can prove where the evidence went afterward."
        "Say Dhampir's powers solved it.":
            $ uly += 1
            u "His power reached the space. Five days of reconstruction told him which space mattered."
        "Say the remaining three should be easy.":
            $ uly -= 1
            u "Three plausible suspects are not easy. They are simply fewer ways to be wrong."
    return


## Madeline reports

label UlyssesReportMadeline1:
    show ulysses at slot(0, total=1), bright zorder 10
    u "Madeline sent the database comparison ahead with the subject line 'OBVIOUS ONCE TESTED.' I assume it was less obvious before testing."
    "You explain the preserved fingerprint, the convicted comparison sample already in the database, and the mismatch that clears one person."
    if ulyssesCurrentClue:
        u "The formal conclusion is [ulyssesCurrentClue]"
    menu:
        "Admit you failed her test and touched a slide before gloves." if getattr(store, "madeline_touched_slide", False):
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "At least you admit it here. She noted the contaminated disposal sleeve in her preamble with four exclamation marks. Touch nothing in her lab without clearance."
        "Mention that Madeline tested your procedure before trusting you near evidence." if not getattr(store, "madeline_touched_slide", False):
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Then you passed the more difficult test. She can compare fingerprints more easily than judgment."
        "Report the database result without overstating it.":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "Good. One mismatch, one exclusion, no invented certainty."
        "Complain that Madeline treated you like an idiot.":
            $ uly -= 1
            $ ulysses_note_reporting_style("deflecting")
            u "She treats most people like idiots. Your task is determining whether her criticism contains useful procedure."
    return


label UlyssesReportMadeline2:
    show ulysses at slot(0, total=1), bright zorder 10
    u "Winston's miniature-golf intervention succeeded, then. I had wondered where those passes went."
    "You report on the afternoon off-site at the miniature golf course and confirm that no formal physical evidence was gathered."
    u "She kept the scorecard, I assume."
    menu:
        "Confirm that she kept it for 'data collection.'":
            $ uly += 1
            u "Naturally. Madeline has historically collected a remarkable amount of 'sentimental data.'"
            u "We dated until last year. We function substantially better as colleagues, but that habit hasn't changed."
        "Say failing safely seemed good for her.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Yes. Constant pressure makes every small mistake feel catastrophic. A windmill offers lower stakes."
        "Say you let her win.":
            $ uly -= 2
            $ ulysses_note_reporting_style("deflecting")
            u "You did not. If you tell her that, please schedule the resulting emergency outside office hours."
    return


label UlyssesReportMadeline3:
    show ulysses at slot(0, total=1), bright zorder 10
    u "Ica's accidental contribution appears in Madeline's methods section beneath three increasingly angry revisions."
    "You explain the gravity shift, the safely halted centrifuge, and the counterweight method that turned the accident into a reproducible separation."
    if madeline_centrifuge_result.get("quality") == "perfect":
        u "Your rotor balanced on the first controlled run. Madeline underlined that twice, which I believe constitutes praise."
    elif madeline_centrifuge_result.get("completed"):
        u "The first balance failed safely. You corrected it without compromising the sample."
    else:
        u "Madeline completed the balance after you requested assistance. The sample remained protected."
    if ulyssesCurrentClue:
        u "The resulting exclusion is [ulyssesCurrentClue]"
    menu:
        "Credit Madeline for reproducing the accident properly.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Exactly. An accident can suggest a method. Repetition under control makes it evidence."
        "Credit Ica for solving the experiment.":
            $ uly -= 1
            u "Ica moved a stool. Madeline converted the interference into a controlled process. Credit may be shared without becoming fictional."
        "Admit the balance took some help but the result is sound.":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "Accepting assistance preserves evidence better than protecting pride."
    return


label UlyssesReportMadeline4:
    show ulysses at slot(0, total=1), bright zorder 10
    u "Three elemental indicators activated in one wound sample. Madeline's machine was correct; her model was not."
    "You describe separating the injuries by sequence and the quiet physical observation that emerged once contact trauma was no longer treated as elemental residue."
    u "Keep that observation provisional. A useful model explains the sample without promoting every implication to proof."
    menu:
        "Say Madeline improved the model instead of defending it.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "That is one of her better qualities. She may become angry at reality, but she does eventually permit reality to win."
        "Say a genius should have caught the assumption earlier.":
            $ uly -= 2
            u "A genius is not someone who never forms a bad premise. It is someone capable of dismantling one before it becomes doctrine."
        "Explain which observation remains uncertain.":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "Good. Naming uncertainty is part of reporting a result."
    return


label UlyssesReportMadeline5:
    show ulysses disgruntled at slot(0, total=1), bright zorder 10
    if mads_cutoff_violated:
        u "I have the telemetry log from Madeline's helmet calibration, recruit. The automatic timer triggered because you ignored her verbal stop command."
        "You report the residue pattern, but you cannot disguise the fact that you ignored protocol and forced her past her limit."
        u "After Mindbreak, Madeline does not surrender control easily. When an investigator inside a feedback helmet says stop, you hit the switch immediately. Period."
        menu:
            "Acknowledge the protocol breach directly without excuses.":
                $ uly += 1
                $ ulysses_note_reporting_style("honest")
                u "At least you do not lie about it. But Madeline will remember that you put data ahead of her consent, and so will I."
            "Argue that the extra data was necessary for the murder investigation.":
                $ uly -= 2
                $ ulysses_note_reporting_style("deflecting")
                u "No piece of evidence justifies compromising a colleague's safety. Do not make that mistake in this agency again."
            "Report only the residue observation without defending your conduct.":
                $ ulysses_note_reporting_style("honest")
                u "The residue reading is noted. Your conduct during the test remains a serious breach of professional discipline."
    else:
        u "Madeline's calibration protocol contains a manual cutoff, verbal checks, and a strict time limit. I recognize your handwriting beside all three."
        "You report the helmet test, the emotional disinhibition it briefly caused, and the careful or careless residue pattern revealed only after the system was safely shut down."
        u "After Mindbreak, she does not surrender control easily. She placed the cutoff in your hands anyway."
        menu:
            "Say stopping when agreed mattered more than extra data.":
                $ uly += 3
                $ ulysses_note_reporting_style("thoughtful")
                u "Correct. Consent that disappears when inconvenient was never consent."
            "Focus on the personal things she admitted.":
                $ uly -= 1
                u "Those were entrusted to you during a vulnerable test. They are not report material."
            "Record only the residue observation and its uncertainty.":
                $ uly += 2
                $ ulysses_note_reporting_style("honest")
                u "Exactly. Protect the person; preserve the relevant result."
    return


label UlyssesReportMadeline6:
    show ulysses at slot(0, total=1), bright zorder 10
    "Ulysses reads the scanner controls, comparison standards, and repeated result before accepting Madeline's classification."
    if ulyssesCurrentClue:
        u "Her calibrated analysis supports this: [ulyssesCurrentClue]"
    u "The machine did not solve the case. Six visits of improved method produced a result worth trusting."
    menu:
        "Say Madeline taught you to challenge the model, not the data.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "A lesson she learned by arguing with both. You appear to have received the refined version."
        "Say the final power category is conclusive by itself.":
            $ uly -= 1
            u "It narrows the list. The remaining distinctions still belong to your observations."
        "Praise the controls and repeated comparison.":
            $ uly += 2
            $ ulysses_note_reporting_style("honest")
            u "Good. Admire intelligence if you like; trust documented method."
    return


## Nicky reports

label UlyssesReportNicky1:
    show ulysses at slot(0, total=1), bright zorder 10
    u "Nicky's alibi packet is already formatted, signed, and somehow contains fewer coffee stains than the version the station sent us."
    "You explain the timeline verification, the independent record, and the suspect whose alibi now holds."
    if ulyssesCurrentClue:
        u "That gives us [ulyssesCurrentClue]"
    menu:
        "Emphasize that the records agree independently.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Yes. Repetition is only corroboration when the sources did not copy one another."
        "Say Nicky handled the paperwork and you followed along.":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "Honest. Next time, learn enough of the chain that you could catch her mistake. She would respect that more than praise."
        "Say police records should be trusted automatically.":
            $ uly -= 2
            u "Nicky would object more loudly than I will. Authority does not convert an unchecked statement into fact."
    return


label UlyssesReportNicky2:
    show ulysses at slot(0, total=1), bright zorder 10
    u "A record store, diner food, and a motorcycle ride. This is the first report this week with a soundtrack."
    if nicky_album_exchange_type == "gift":
        "You tell him about Nicky's hip-hop search, the album she bought you, and the way she became playful once police work was no longer in front of her."
    elif nicky_album_exchange_type == "loan":
        "You tell him about Nicky's hip-hop search, the tape she loaned you, and the way she became playful once police work was no longer in front of her."
    else:
        "You tell him about Nicky's hip-hop search, the album title she scribbled on your receipt, and the way she became playful once police work was no longer in front of her."
    u "She spends enough time being ATLAS's legal conscience. I am glad you met the person who goes home after the paperwork."
    menu:
        "Say she gave you an album that proved she listened." if nicky_album_exchange_type == "gift":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Attention is often more meaningful than spectacle. Remember that."
        "Say she trusted you enough to lend you her own tape." if nicky_album_exchange_type == "loan":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Nicky protects her music fiercely. That loan is a genuine mark of trust."
        "Mention the listening homework she scribbled on the receipt." if nicky_album_exchange_type == "recommendation":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "A sensible recommendation. Nicky has strong taste, even if she enforces it aggressively."
        "Report honestly that the day advanced no evidence.":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "Correct. It may still improve how well you work together later."
        "Try to classify the album exchange as evidence." if nicky_album_exchange_type in ("gift", "loan"):
            $ uly -= 1
            $ ulysses_note_reporting_style("deflecting")
            u "I will place it beside Razzle's pizza receipt and Dhampir's film review."
        "Try to classify the playlist notes as evidence." if nicky_album_exchange_type == "recommendation":
            $ uly -= 1
            $ ulysses_note_reporting_style("deflecting")
            u "A diner receipt recommendation is not forensic evidence. Do not submit it as one."
    return


label UlyssesReportNicky3:
    show ulysses at slot(0, total=1), bright zorder 10
    u "Razzle arrived for information and somehow left Nicky with a face-down matching exercise. Explain why that produced a lawful conclusion."
    "You describe pairing original records with corroboration, correcting the clothing-distorted descriptions, and separating measured build from assumption."
    if nicky_memory_result.get("quality") == "perfect":
        u "No mismatches, hints, or expired review periods. Nicky's margin note says, 'Rookie can read.' High praise."
    elif nicky_memory_result.get("quality") == "recovered":
        u "Several records were mismatched before you recovered. The final source links are correct; include the correction history."
    else:
        u "The review needed a few corrections, but every final pair traces back to an independent source."
    if ulyssesCurrentClue:
        u "The final comparison supports this: [ulyssesCurrentClue]"
    menu:
        "Explain that every pair preserved its source.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Then the game clarified provenance rather than replacing it. Unorthodox, but defensible."
        "Say you needed hints to finish the matching." if nicky_memory_result.get("hints_used", 0) > 0:
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "Assistance is not contamination when it directs you back to the record."
        "Note that cross-referencing contradictory statements took discipline." if nicky_memory_result.get("hints_used", 0) == 0:
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "Careful attention pays dividends. Nicky's files punish careless reading."
        "Credit intuition instead of the files.":
            $ uly -= 1
            u "Intuition may tell you where to look. It does not sign an affidavit."
    return


label UlyssesReportNicky4:
    show ulysses at slot(0, total=1), bright zorder 10
    u "The original report observed extraordinary force and invented a large attacker to explain it. In this building, that is a particularly careless assumption."
    "You describe separating observations from copied conclusions, Nicky lifting the reconstruction table with one hand, and the quieter injury detail in the corrected path."
    u "Good. Preserve the observation; remove the costume somebody dressed it in."
    menu:
        "Say Nicky challenged her own institution's mistake.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Her loyalty is to the law functioning properly, not to pretending every officer already achieved that."
        "Suggest discarding every copied report.":
            $ uly -= 1
            u "Correction is not destruction. Useful observations survived the bad inference."
        "Acknowledge the injury detail as a lead, not an exclusion.":
            $ uly += 2
            $ ulysses_note_reporting_style("honest")
            u "Exactly. Hold it quietly until another source gives it weight."
    return


label UlyssesReportNicky5:
    show ulysses at slot(0, total=1), bright zorder 10
    u "The outer custody bag was altered without initials. The inner seal remained intact. Nicky appears to have documented every molecule in the hallway."
    "You explain the quarantine, supervised limited test, uncertain blood profile, and the seven-minute television break after the sample returned to storage."
    u "A compromised chain changes what we may claim. It does not forbid us from learning where to seek clean evidence."
    menu:
        "Keep the blood result as a lead and request comparison.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Correct. Direction without false certainty."
        "Say Nicky's pheromone sense proves the technician lied about murder.":
            $ uly -= 2
            u "It proves stress. Treating emotion as a confession would violate both procedure and common sense."
        "Admit the test cannot support a formal exclusion.":
            $ uly += 2
            $ ulysses_note_reporting_style("honest")
            u "Good. A disappointing limitation reported clearly is better than a useful fiction."
    return


label UlyssesReportNicky6:
    show ulysses at slot(0, total=1), bright zorder 10
    "Ulysses reviews the warrant dates, residue controls, and repeated behavioral records before he reaches the final profile."
    if ulyssesCurrentClue:
        u "The independent supports establish this: [ulyssesCurrentClue]"
    u "Nicky kept her pheromone impressions outside the proof. That restraint is why I trust the rest of it."
    menu:
        "Say lawful evidence made the conclusion stronger, not slower.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Precisely. A conclusion that collapses under review never saved time."
        "Say the final three are close enough.":
            $ uly -= 1
            u "Close enough is not a standard I recommend applying to homicide."
        "Explain how the three independent supports agree.":
            $ uly += 2
            $ ulysses_note_reporting_style("honest")
            u "Physical trace, lawful records, repeated behavior. Good. You understood the structure rather than memorizing the answer."
    return


## Winston reports

label UlyssesReportWinston1:
    show ulysses at slot(0, total=1), bright zorder 10
    u "Winston's report contains a useful interrogation summary, a takeout menu, and a drawing of a pencil ramp. Tell me which portion occupied the day."
    "You explain the conversational roles, the unrelated embarrassing lie that exposed the rehearsed answer, and the suspect cleared without Winston suppressing anyone's power."
    if ulyssesCurrentClue:
        u "The formal result is [ulyssesCurrentClue]"
    menu:
        "Say Winston looked lazy while controlling the entire room.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Yes. He finds performance useful because people underestimate a fool. He also enjoys being a fool. Do not confuse either fact for incompetence."
        "Report the lie and leave out the pencil ramp.":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "Tempting, but context explains why the suspect relaxed. Include one sentence. No diagram."
        "Say Winston wasted most of the day.":
            $ uly -= 1
            $ ulysses_note_reporting_style("deflecting")
            u "Then you missed the work happening beneath the waste. Review the interview before you join him again."
    return


label UlyssesReportWinston2:
    u "I ordered Winston to take a day off. I did not expect him to turn the order into a supervised diner and pool expedition."
    "You describe the greasy burger, the calls he fielded at the diner, his competitive pool game, and the fourth call he finally set aside."
    u "He answered [winston_calls_answered] of the calls before remembering how to take an afternoon off, then completed every item on my list after returning. Predictable in the broadest and most irritating sense."
    menu:
        "Say Winston deserved time where nobody needed his power.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "He did. Thank you for giving him company without turning the day into another assignment."
        "Report that he answered three minor workplace crises before ignoring the fourth.":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "All four crises were deliberately nonessential. The team survived the educational experience."
        "Report his private confession about feeling like an emergency brake.":
            $ uly -= 1
            $ ulysses_note_reporting_style("deflecting")
            u "Winston's private doubts about his role are between him and the people he trusts. They are not report material. Stick to the operational debrief."
        "Say he should take leadership more seriously.":
            $ uly -= 1
            u "He takes it seriously when seriousness helps. The rest is camouflage and self-preservation."
    return


label UlyssesReportWinston3:
    u "A blackjack table, [len(remainingSuspects)] suspects, and Dhampir volunteering as bad cop. I would call that a procedural nightmare if the consent forms were not already on my desk."
    "You explain controlled pressure, repeated interviews, Dhampir's terrifying perfect turn, and the individual stress profiles that failed the established timeline."
    if winston_pressure_result.get("quality") == "controlled":
        u "You completed the queue without pushing a suspect beyond the usable threshold. Winston called that 'annoyingly responsible.'"
    elif winston_pressure_result.get("quality") == "assisted":
        u "Winston assumed control of part of the queue. The result remains valid; your performance assessment should remain honest."
    else:
        u "Some interviews had to be reset. The recovery procedure kept pressure mistakes from becoming evidence mistakes."
    if ulyssesCurrentClue:
        u "The defensible conclusion is [ulyssesCurrentClue]"
    menu:
        "Explain how pressure was reset whenever somebody shut down.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Good. The method tested stability; it did not reward breaking people."
        "Admit Winston finished some interviews for you." if winston_pressure_result.get("quality") == "assisted":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "Then study how he changed tone. Assistance should leave you more capable next time."
        "Credit Winston's pacing for keeping the suspects talking." if winston_pressure_result.get("quality") != "assisted":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "He understands how to alternate pressure with ease. It is a useful skill to study."
        "Say Dhampir's intimidation was the most efficient part.":
            $ uly -= 1
            u "Efficient at producing fear. Winston's method required usable answers. Those are not synonymous."
    return


label UlyssesReportWinston4:
    u "Winston interviewed a witness over darts and takeout. His written methodology says, 'Act normal until they stop acting.'"
    "You describe the witness's habits, the tentative cleanliness and hand observations, and Winston's precise suppression of one uncontrolled power without touching your intuition."
    u "Keep the habits outside the formal notebook. Tendencies are useful questions, not verdicts."
    menu:
        "Say his casual approach produced details formality concealed.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Yes. Winston makes people underestimate the room, then pays attention to what they do with the space."
        "Report what Winston told you about founding ATLAS.":
            $ uly += 2
            u "I assume his version included more explosions and fewer incorporation forms. Both were present."
        "Say the power stereotypes sounded conclusive.":
            $ uly -= 2
            u "They are tendencies. Treating them as identity rules would make the investigation both lazy and wrong."
    return


label UlyssesReportWinston5:
    u "Winston requested masking tape, a coat rack, and permission to label a pizza box CABINET. I authorized two of those things."
    "You report the heightened-hearing witness, the careful pacing, and the reconstructed aftermath whose final two sounds still lack a verified order."
    u "Then the impression remains provisional. His second statement and telephone record should settle the sequence when you return to it."
    menu:
        "Emphasize that the witness controlled when to stop." if winston_day_five_care != "pushed":
            $ uly += 3
            $ ulysses_note_reporting_style("thoughtful")
            u "Good. A terrified witness is not a resource to consume. Winston understood that immediately."
        "Admit that Winston had to intervene when you rushed the witness." if winston_day_five_care == "pushed":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "Then remember his intervention. A frightened witness is not an obstacle to bulldoze. You are fortunate Winston stopped you before you contaminated the testimony."
        "Say the likely reaction category belongs in the notebook now.":
            $ uly -= 2
            u "Not until the order is independently fixed. Likely is not another spelling of proven."
        "Admit the reconstruction became easier once Winston joked.":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "His humor lowers pressure when he uses it for someone else instead of hiding himself."
    return


label UlyssesReportWinston6:
    "Ulysses checks the phone-company record against both witness statements and the final ordered sequence."
    if ulyssesCurrentClue:
        u "The corroborated result is [ulyssesCurrentClue]"
    u "Winston's reconstruction looked absurd. Its controls did not. That combination describes much of his leadership."
    menu:
        "Say the method survived because he verified every joke-shaped step.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Correct. Presentation may be informal. Standards may not."
        "Say Winston was frighteningly competent.":
            $ uly += 1
            u "He prefers people discover that late. It gives him time to determine what they reveal early."
        "Hand the final judgment back to Ulysses.":
            $ uly -= 1
            u "No. I will organize the reports. You were hired to exercise judgment, not return it unopened."
    return


## Ica reports

label UlyssesReportIca1:
    u "I have an empty evidence column and a message from Ica saying you investigated cards. I assume there is context."
    "You describe the floating deck, stale candy, and several increasingly flexible interpretations of the rules."
    if ica_minigame_results.get("cards", {}).get("won"):
        u "You also won. Not evidence, but apparently important to both of you."
    else:
        u "Ica made certain the loss appeared in her message. It has no bearing on the case, so naturally it received the largest handwriting."
    u "The day did not advance the evidence. It did give you time to understand a colleague whose useful moments are easy to miss if you only watch for conventional effort. On a first day, that has some value."
    menu:
        "Say understanding Ica may matter when she finally acts.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "It may. She is exceptionally capable when something truly catches her attention. Learning what does that is more useful than trying to shame her into performing busyness."
        "Admit you chose to spend the day playing cards.":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "Thank you. An unproductive day reported honestly is easier to account for than one disguised as a strategy."
        "Claim the cards tested suspect psychology.":
            $ uly -= 2
            $ ulysses_note_reporting_style("deflecting")
            u "Which suspect?"
            "The silence answers for you."
    return


label UlyssesReportIca2:
    u "Ica's report says 'staring contest' and nothing else. I take it that omission was accurate rather than economical."
    "You explain the rules, the stolen sodas, and how an afternoon vanished while neither of you admitted that looking at the clock counted as losing."
    if ica_minigame_results.get("staring", {}).get("won"):
        u "Congratulations on prevailing in the only contest where sustained eye irritation is a strategy."
    else:
        u "Ica's message included the phrase 'easy win.' She appears to consider that the day's official result."
    u "So this was not merely first-day social reconnaissance. You chose her company again. That is allowed; I need the choice named honestly so we can account for the evidence you did not pursue elsewhere."
    menu:
        "Admit you went back because you enjoyed it.":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "That is honest. Enjoyment is permitted, recruit. The deadline remains, but I am not asking you to apologize for liking someone."
        "Say Ica was testing your focus.":
            $ uly -= 2
            $ ulysses_note_reporting_style("deflecting")
            u "That explanation is doing more work than either participant did. Give me the simpler truth next time."
        "Promise to weigh the lost evidence against what you learned about her.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "Do that. Choosing one person also means leaving five methods unused today; understanding the trade is more useful than pretending it did not exist."
    return


label UlyssesReportIca3:
    u "Winston's paperwork remains unfinished, his floor contains three pawn-shaped dents, and Ica says the office may be haunted."
    "You report the three-player pawn race, Winston's enthusiasm, Ica's gravity-assisted laziness, and the complete absence of case progress."
    $ board_result_tier = ica_minigame_results.get("board", {}).get("result_tier", "")
    if ica_minigame_results.get("board", {}).get("won"):
        u "You won the race. Winston has requested a rematch during hours I have explicitly labeled operational."
    elif board_result_tier == "loss_ica":
        u "Ica won the race and claimed executive immunity from future filing. I informed her that exemption does not exist."
    elif board_result_tier == "loss_withdrawn":
        u "You withdrew from the race to let them bicker over the board. A remarkably prudent tactical retreat."
    else:
        u "Winston's supplementary report consists of a hand-drawn victory diagram. I will not preserve it."
    u "Two cofounders run this organization. Today, one of them chose to spend several hours being bumped back to start with you."
    u "Winston rarely gives his full attention to recreation unless he thinks the room needs it. I am willing to count that as information about the team, if not the case."
    menu:
        "Admit the game was fun and produced no evidence.":
            $ uly += 1
            $ ulysses_note_reporting_style("honest")
            u "A precise report. The case gained nothing, but you learned something real about how they work together. Keep those categories separate and I have no objection."
        "Point out that Winston joined voluntarily.":
            $ uly += 1
            u "He did. That tells me the day was not merely Ica avoiding work; Winston decided the pause had value too."
        "Say you saw how naturally Winston and Ica coordinate.":
            $ uly += 2
            $ ulysses_note_reporting_style("thoughtful")
            u "They understand each other's selective effort. That is useful knowledge of the team, even if it belongs outside the evidence file."
    return


label UlyssesReportIca4:
    "Ulysses looks at the empty report page, then at you."
    u "I can smell hot dogs from here."
    "You describe the bulk discount, the eating contest, the gravity-assisted cheating, the antacids, and Ica's proposal to paint his office pink."
    if ica_minigame_results.get("eating", {}).get("won"):
        u "You apparently won. Ica being forced to throw away her own trash is an unprecedented achievement in this building."
    else:
        u "Ica won. Her prize appears to have been making you carry the trash."
    u "That is disgusting. The food contest, specifically. The proposed vandalism has the virtue of not involving mystery sauce."
    menu:
        "Warn him plainly about the pink-office plan.":
            $ uly += 2
            $ ulysses_note_reporting_style("honest")
            u "Thank you. Knowing Ica, she will manage it regardless, but I can at least move the irreplaceable files."
        "Say you intend to help Ica do it.":
            $ uly += 1
            u "Of course you do. Use the tarp. I would prefer my resignation letter remain beige."
        "Pretend Ica never mentioned a prank.":
            $ uly -= 2
            $ ulysses_note_reporting_style("deflecting")
            u "Recruit, she left pink paint swatches clipped to the supply requisition this morning. Your loyalty is admirable and very badly deployed."
    return


label UlyssesReportIca5:
    "The newly pink walls make denial impossible. Ulysses sits behind the restored desk while fresh paint dries around him."
    u "I suspected this was going to happen, and it still hurts."
    if ica_paint_preparation == "tarp":
        "He checks the untouched case files, the carefully taped tarp protecting the carpet, and the furniture returned to its exact marks."
        u "At least you taped down a drop cloth. The floor survived your artistic impulses."
    elif ica_paint_preparation == "cardboard":
        "He checks the untouched case files, the pink specks marking the exposed carpet around the baseboards, and the furniture returned to its marks."
        u "Cardboard beneath the cans did not protect the floor from roller splatter, recruit. That will come out of the maintenance budget."
    else:
        "He checks the untouched case files, the odd absence of floor splatter, and the furniture returned to its exact marks."
        u "You didn't drop a tarp, but Ica's field evidently kept the floor clear of splatter. I suppose I should be grateful for small miracles."
    if not ica_minigame_results.get("prank", {}).get("completed"):
        u "You abandoned the hallway operation and finished the painting directly. Sensible, once subtlety had stopped serving a purpose."
    elif ica_prank_caught_count == 0:
        u "You also avoided my patrol every time. I am professionally concerned and personally impressed."
    else:
        u "I observed you [ica_prank_caught_count] times. Calling this a stealth operation was generous."
    u "For the record, I like the color. I object to learning that fact through unauthorized team building."
    menu:
        "Apologize and offer to finish the cleanup.":
            $ uly += 2
            $ ulysses_note_reporting_style("honest")
            u "Accepted. Open the windows first. Then remove the paint from the door hinges."
        "Say the office genuinely looks better.":
            $ uly += 1
            u "It does. That is not the legal defense you believe it is."
        "Blame the entire plan on Ica.":
            $ uly -= 2
            $ ulysses_note_reporting_style("deflecting")
            u "You carried a roller through three hallways. At some point, passive involvement became painting."
    return


label UlyssesReportIca6:
    "Ulysses listens without interrupting as you describe the killer entering the warehouse, opening Enrico's lockbox with the key from his wallet, and bolting through the fire exit after Ica stopped the contents from burning."
    "Nicky's evidence receipt lies beside the recovered wallet and key. Ulysses checks the seal numbers, then compares them to Enrico's property record."
    $ ulysses_ica_killer_name = suspectNames[killer]
    u "Six days of games, one attempted destruction of evidence, and [ulysses_ica_killer_name] personally delivering the answer to the warehouse."
    u "Nicky and Dhampir are coordinating with LAPD patrol to run down their escape vector across the rail yard. We'll have them in custody before morning."
    u "I owe you an apology. I doubted your judgment because the method appeared to contain no judgment whatsoever. Somehow, staying with Ica worked."
    menu:
        "Accept the apology without pretending this was planned.":
            $ uly += 3
            $ ulysses_note_reporting_style("honest")
            u "Good. If you claimed foresight, I would be forced to defend my professional territory."
        "Say doing nothing was the perfect strategy.":
            $ uly += 1
            u "It was not. It was an improbable strategy followed by an exceptionally convenient criminal."
        "Take full credit for solving the case.":
            $ uly -= 1
            $ ulysses_note_reporting_style("deflecting")
            u "Ica stopped the fire and called Nicky. You stayed with the evidence. Take credit for what you did."
    return
