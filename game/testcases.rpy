## Automated structural checks. Run with the Ren'Py SDK's `test` command.

testsuite investigation_validation:
    testcase every_six_day_route_mix:
        $ validate_investigation_routes()

    testcase winston_pressure_model:
        $ validate_winston_pressure_rules()

    testcase ulysses_evening_model:
        $ validate_ulysses_evening_model()

    testcase day_seven_model:
        $ validate_day_seven_model()

testcase ulysses_first_evening_flow:
    $ killer = 1
    $ remainingSuspects = list(suspectNames.keys())
    $ investigationClues = []
    $ recordedClueKeys = []
    $ recordedRouteReveals = {}
    $ dayWin = 1
    $ dayRazz = 2
    $ dayDham = 1
    $ dayMads = 1
    $ dayNick = 1
    $ dayWinn = 1
    $ dayIca = 1
    $ spendRazz = True
    $ spendDham = False
    $ spendMads = False
    $ spendNick = False
    $ spendWin = False
    $ spendIca = False

    run Jump("UlyssesEvening")
    advance until screen "choice"
    click "Emphasize that Razzle slowed down for the witness."
    advance until screen "choice"
    click "Offer to help organize tomorrow's work."
    advance until screen "choice"
    click "Take a pineapple slice and keep working beside him."
    advance until screen "choice"
    click "Tell him the vest looks good on him."
    advance until screen "choice"

testcase ulysses_first_evening_relaxed_flow:
    $ killer = 1
    $ remainingSuspects = list(suspectNames.keys())
    $ investigationClues = []
    $ recordedClueKeys = []
    $ recordedRouteReveals = {}
    $ dayWin = 1
    $ dayRazz = 2
    $ dayDham = 1
    $ dayMads = 1
    $ dayNick = 1
    $ dayWinn = 1
    $ dayIca = 1
    $ spendRazz = True
    $ spendDham = False
    $ spendMads = False
    $ spendNick = False
    $ spendWin = False
    $ spendIca = False

    run Jump("UlyssesEvening")
    advance until screen "choice"
    click "Say the witness gave you a name to remove."
    advance until screen "choice"
    click "Say the report is finished and relax in the guest chair."
    advance until screen "choice"
    click "Take another slice and ask about the photographs on his desk."
    advance until screen "choice"
    click "Ask for permission to leave."
    advance until screen "choice"
