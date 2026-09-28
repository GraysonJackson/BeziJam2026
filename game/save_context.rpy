## Spoiler-free context captured in the save itself, never read from a live run.
default saveSceneLabel = "Introduction"
default savePartnerName = ""
default saveVisitNumber = 0

init python:
    def update_save_context(label, abnormal=False):
        import re
        route = re.match(r"^(Razzle|Dhampir|Madeline|Nicky|Winston|Ica)Day(One|Two|Three|Four|Five|Six)$", label)
        if route:
            store.savePartnerName = "Razzle Dazzle" if route[1] == "Razzle" else route[1]
            store.saveVisitNumber = ("One", "Two", "Three", "Four", "Five", "Six").index(route[2]) + 1
            store.saveSceneLabel = "Investigation"
        elif label in ("start", "dayOneBrief", "dayLoop", "UlyssesEvening", "DaySevenStart"):
            store.saveSceneLabel = {
                "start": "Introduction", "dayOneBrief": "First briefing",
                "dayLoop": "Choose an investigator", "UlyssesEvening": "Evening report",
                "DaySevenStart": "Final accusation",
            }[label]
            store.savePartnerName = "Ulysses" if label == "UlyssesEvening" else ""
            store.saveVisitNumber = 0
        elif label.startswith("DaySevenEnding"):
            store.saveSceneLabel = "After the case"
            store.savePartnerName = ""
            store.saveVisitNumber = 0

    def case_save_metadata(metadata):
        day = max(1, min(7, getattr(store, "dayWin", 1)))
        scene = getattr(store, "saveSceneLabel", "Case in progress")
        partner = getattr(store, "savePartnerName", "")
        visit = getattr(store, "saveVisitNumber", 0)
        detail = (partner + " · Visit " + str(visit)) if partner and visit else (partner or scene)
        metadata["case_context"] = "Day {}\n{}".format(day, detail)

    config.label_callbacks.append(update_save_context)
    config.save_json_callbacks.append(case_save_metadata)
