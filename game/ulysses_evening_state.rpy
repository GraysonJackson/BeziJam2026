## State and helpers for Ulysses's mandatory end-of-day route.

define ULYSSES_WARM_THRESHOLD = 18
define ULYSSES_HIGH_THRESHOLD = 36
define ULYSSES_DATE_ACCEPT_THRESHOLD = 46

default ulyssesEveningsCompleted = 0
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

    def ulysses_candidate_profile_text():
        lines = []
        for suspect_id in store.remainingSuspects:
            attributes = store.suspectAttributes[suspect_id]
            lines.append(
                "{} — {}; {}; {} build; {}; {}; {} reaction".format(
                    store.suspectNames[suspect_id],
                    attributes["unique_id"],
                    attributes["height"],
                    attributes["build"],
                    attributes["injuries"],
                    attributes["organization"],
                    attributes["kill_reaction"],
                )
            )
        return "\n".join(lines)

    def ulysses_intuition_hint_text():
        attributes = store.suspectAttributes[store.killer]
        return (
            "Your intuition catches where three details overlap: {} build, {}, and a {} reaction."
            .format(
                attributes["build"],
                attributes["organization"].lower(),
                ("no-visible" if attributes["kill_reaction"] == "None"
                 else attributes["kill_reaction"].lower()),
            )
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
            "Ulysses's cross-report analysis identifies {} as the only profile consistent "
            "with every independent finding."
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
