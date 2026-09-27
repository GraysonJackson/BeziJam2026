## State and helpers for Ulysses's mandatory end-of-day route.

define ULYSSES_WARM_THRESHOLD = 18
define ULYSSES_HIGH_THRESHOLD = 30
define ULYSSES_ROMANCE_WARM_THRESHOLD = 4
define ULYSSES_ROMANCE_HIGH_THRESHOLD = 7
define ULYSSES_DATE_ACCEPT_THRESHOLD = 8
define ULYSSES_DATE_MIN_PERSONAL_EVENINGS = 5

define ULYSSES_REPEAT_COMMENTS = {
    "razzle": {
        2: "Razzle's energy can make her process look less disciplined than it is. You returned and saw how carefully she listens beneath the noise.",
        3: "Three days with Razzle have given you a strong witness record. Remember that enthusiasm can fill silence before a witness has finished thinking.",
        4: "You and Razzle have developed an efficient rhythm. Preserve the moments where one of you challenges the other's first impression.",
        5: "At this point, Razzle trusts you enough to show uncertainty instead of covering it with momentum. That is valuable evidence and valuable trust.",
        6: "You chose Razzle for the full investigation. You know the strengths and blind spots of her method well enough that tomorrow's judgment must account for both.",
    },
    "dhampir": {
        2: "Dhampir makes difficult work look casual because he does not need an audience for competence. Returning gave you time to see the work beneath the jokes.",
        3: "Three days with Dhampir have taught you how he reconstructs violence without sensationalizing the victim. Keep that distinction in your report.",
        4: "You are learning when Dhampir's humor releases pressure and when the suit means he needs the room to become serious. Both versions are him.",
        5: "Dhampir trusts technique more than appearances. Your reports are strongest when you do the same instead of treating his confidence as proof.",
        6: "You stayed with Dhampir through the entire field investigation. Tomorrow, use what his method established without borrowing his certainty as your own.",
    },
    "madeline": {
        2: "Madeline responds to demonstrated competence more readily than reassurance. You returned prepared, and she gave you more responsibility because of it.",
        3: "Three days in the lab have taught you to separate Madeline's tone from the precision of what she is saying. That has improved both the work and your reports.",
        4: "Madeline challenges assumptions aggressively, including her own when the data requires it. Make sure your growing ease with her does not exempt either of you from that standard.",
        5: "She has started explaining the thought behind her conclusions instead of only giving you the result. That is a significant form of trust from Madeline.",
        6: "You built the case through Madeline's laboratory method from the first print to the final category. The chain is deep; tomorrow you still have to interpret it.",
    },
    "nicky": {
        2: "Nicky's procedure is not a lack of instinct. It is how she makes instinct answerable to someone besides herself. Your second day made that clearer.",
        3: "Three days with Nicky have given you records that can survive scrutiny. Do not lose the human context she gathered while building them.",
        4: "You and Nicky work quickly together now. Speed is useful so long as neither of you mistakes familiarity for corroboration.",
        5: "Nicky has begun letting you see the strain behind the badge without asking you to carry it for her. Treat that confidence carefully.",
        6: "You followed Nicky's process for the entire case. Tomorrow's accusation should be as direct as she is and as supported as the law requires.",
    },
    "winston": {
        2: "Winston's foolishness is usually deliberate. Returning gave you a better view of how quickly he notices when a room actually needs him to become serious.",
        3: "Three days with Winston have shown you that improvisation is still a method, even if documenting it gives me a headache. Record the decisions beneath the performance.",
        4: "You are beginning to anticipate Winston's feints without dismissing them. That matters; people often tell him more while assuming he is not paying attention.",
        5: "Winston trusts you enough to stop filling every quiet moment. I recommend recognizing that as confidence, not an invitation to become careless.",
        6: "You spent the full investigation beside Winston. His instincts gave you depth, but tomorrow the conclusion must be explainable without relying on charm or luck.",
    },
    "ica": {
        2: "You chose Ica again. Her pace is not mine, but she notices more than people assume when they mistake disinterest in work for disinterest in everything.",
        3: "Three days with Ica have shown you the difference between laziness and incapacity. She is entirely comfortable with the first and has given you no reason to suspect the second.",
        4: "You seem to understand that Ica dislikes performances of urgency. She responds better when someone leaves room for her to care without demanding that she display it.",
        5: "By now, returning to Ica is plainly a choice rather than an accident. I may not share her approach to labor, but I understand why her company appeals to you.",
        6: "You trusted Ica's attention for the entire week. The route produced less conventional paperwork, but you learned exactly when she decides something matters.",
    },
}

default ulyssesEveningsCompleted = 0
default ulyssesPersonalEvenings = 0
default ulyssesRomanceInterest = 0
default ulyssesReportHistory = []
default ulyssesReportingStyle = {"honest": 0, "thoughtful": 0, "deflecting": 0}
default ulyssesBoundaryViolation = False
default ulyssesBoundaryApology = False
default ulyssesCrossReportAttempts = 0
default ulyssesCrossReportCompleted = False
default ulyssesCurrentRoute = ""
default ulyssesCurrentRouteName = ""
default ulyssesCurrentVisit = 0
default ulyssesCurrentClue = ""
default ulysses_day_three_tension = False
default ulysses_day_three_seen = False
default ulysses_day_three_choice = ""


init python:
    ULYSSES_ROUTE_DATA = {
        "razzle": ("Razzle Dazzle", "Razzle", "dayRazz"),
        "dhampir": ("Dhampir", "Dhampir", "dayDham"),
        "madeline": ("Madeline", "Madeline", "dayMads"),
        "nicky": ("Nicky", "Nicky", "dayNick"),
        "winston": ("Winston", "Winston", "dayWinn"),
        "ica": ("Ica", "Ica", "dayIca"),
    }

    def ulysses_current_route_id():
        if store.spendRazz:
            return "razzle"
        if store.spendDham:
            return "dhampir"
        if store.spendMads:
            return "madeline"
        if store.spendNick:
            return "nicky"
        if store.spendWin:
            return "winston"
        if store.spendIca:
            return "ica"
        return ""

    def ulysses_completed_visits(route_id):
        data = ULYSSES_ROUTE_DATA.get(route_id)
        if data is None:
            return 0
        return max(0, int(getattr(store, data[2])) - 1)

    def ulysses_visit_counts():
        return {
            route_id: ulysses_completed_visits(route_id)
            for route_id in ULYSSES_ROUTE_DATA
        }

    def ulysses_prepare_evening():
        route_id = ulysses_current_route_id()
        if not route_id:
            raise Exception("Ulysses debrief started without a selected investigator.")

        route_name, label_name, counter_name = ULYSSES_ROUTE_DATA[route_id]
        visit = ulysses_completed_visits(route_id)
        store.ulyssesCurrentRoute = route_id
        store.ulyssesCurrentRouteName = route_name
        store.ulyssesCurrentVisit = visit
        store.ulyssesCurrentClue = ulysses_clue_text(route_id, visit)

        history = list(store.ulyssesReportHistory)
        history.append({
            "day": store.dayWin,
            "route": route_id,
            "visit": visit,
        })
        store.ulyssesReportHistory = history
        return "UlyssesReport{}{}".format(label_name, visit)

    def ulysses_clue_text(route_id, visit):
        clue_key = "{}_visit_{}".format(route_id, visit)
        for clue in reversed(store.investigationClues):
            if clue.get("key") == clue_key:
                return clue.get("text", "")
        return ""

    def ulysses_distinct_routes():
        return sum(1 for count in ulysses_visit_counts().values() if count > 0)

    def ulysses_favorite_route():
        counts = ulysses_visit_counts()
        highest = max(counts.values()) if counts else 0
        leaders = [route_id for route_id, count in counts.items() if count == highest and count > 0]
        if len(leaders) != 1:
            return ""
        return leaders[0]

    def ulysses_one_each_strategy():
        counts = ulysses_visit_counts()
        return all(counts.get(route_id, 0) == 1 for route_id in ULYSSES_ROUTE_DATA)

    def ulysses_note_reporting_style(style_id):
        styles = dict(store.ulyssesReportingStyle)
        styles[style_id] = styles.get(style_id, 0) + 1
        store.ulyssesReportingStyle = styles

    ULYSSES_SIPHONING_ALIBIS = {
        1: "Dispatch Log — 21:05-21:40 (Off-site patrol call, Sector 4)",
        2: "Admin Desk Badge Reader — 21:12 (Main Lobby reception desk)",
        3: "Motor Pool Badge Reader — 21:18 (Vehicle maintenance bay)",
        4: "Dispatch Log — 21:08-21:35 (Traffic escort, 5th & Main)",
        5: "Communications Desk Log — 21:10 (Radio dispatch room)",
        6: "Armory Badge Reader — 21:22 (East Wing weapons locker)",
        7: "Admin Desk Badge Reader — 21:15 (Records archives, Level 1)",
        8: "Dispatch Log — 21:02-21:50 (Off-site perimeter check, Port)",
        9: "Motor Pool Badge Reader — 21:20 (Vehicle maintenance bay)",
    }

    def ulysses_candidate_profile_text():
        lines = []
        for suspect_id in store.remainingSuspects:
            if suspect_id == store.killer:
                log = "ATLAS Lockup Badge Reader — 21:14 (Access Granted: Evidence Storage C)"
            else:
                log = ULYSSES_SIPHONING_ALIBIS.get(suspect_id, "Dispatch Log — 21:10 (Off-site patrol)")
            lines.append("• {} — Log: {}".format(store.suspectNames[suspect_id], log))
        return "\n".join(lines)

    def ulysses_intuition_hint_text():
        return (
            "Your detective intuition points straight to the lockup security logs. "
            "Enrico logged the siphoned stimulants right around the 21:15 shift change. "
            "Only one of the four surviving suspects swiped their badge into Evidence Storage C during that window."
        )

    def record_ulysses_cross_report_reveal():
        if store.ulyssesCrossReportCompleted:
            return 0
        if not ulysses_one_each_strategy():
            raise Exception("Ulysses cross-report reveal requires one visit with every investigator.")

        eliminated = [
            suspect_id for suspect_id in store.remainingSuspects
            if suspect_id != store.killer
        ]
        if len(eliminated) != 3:
            raise Exception(
                "Ulysses cross-report expected three innocents, found {} in {}."
                .format(eliminated, store.remainingSuspects))

        clue_text = (
            "ATLAS badge access logs during the stimulant siphoning window show {} "
            "was the only surviving suspect with access to Evidence Storage C."
            .format(store.suspectNames[store.killer])
        )
        removed = store.record_investigation_clue(
            "ulysses_cross_report",
            "Ulysses",
            6,
            clue_text,
            eliminated,
            expected_count=3,
        )
        store.ulyssesCrossReportCompleted = True
        return removed

    def validate_ulysses_evening_model():
        """Verify every investigator visit has a report and one-each is detected."""
        for route_id, data in ULYSSES_ROUTE_DATA.items():
            for visit in range(1, 7):
                label = "UlyssesReport{}{}".format(data[1], visit)
                if not renpy.has_label(label):
                    raise Exception("Missing Ulysses report label {}.".format(label))

        saved_counters = {
            data[2]: getattr(store, data[2])
            for data in ULYSSES_ROUTE_DATA.values()
        }
        try:
            for counter_name in saved_counters:
                setattr(store, counter_name, 2)
            if not ulysses_one_each_strategy():
                raise Exception("Ulysses did not recognize the one-each strategy.")

            setattr(store, "dayIca", 3)
            if ulysses_one_each_strategy():
                raise Exception("Ulysses accepted a repeated route as one-each.")
        finally:
            for counter_name, value in saved_counters.items():
                setattr(store, counter_name, value)

        saved_case = {
            "killer": store.killer,
            "remaining": list(store.remainingSuspects),
            "clues": list(store.investigationClues),
            "keys": list(store.recordedClueKeys),
            "complete": store.ulyssesCrossReportCompleted,
        }
        try:
            for counter_name in saved_counters:
                setattr(store, counter_name, 2)
            store.killer = 1
            store.remainingSuspects = [1, 2, 3, 4]
            store.investigationClues = []
            store.recordedClueKeys = []
            store.ulyssesCrossReportCompleted = False
            removed = record_ulysses_cross_report_reveal()
            if removed != 3 or store.remainingSuspects != [1]:
                raise Exception(
                    "Ulysses cross-report removed {} and left {}."
                    .format(removed, store.remainingSuspects))
        finally:
            for counter_name, value in saved_counters.items():
                setattr(store, counter_name, value)
            store.killer = saved_case["killer"]
            store.remainingSuspects = saved_case["remaining"]
            store.investigationClues = saved_case["clues"]
            store.recordedClueKeys = saved_case["keys"]
            store.ulyssesCrossReportCompleted = saved_case["complete"]
