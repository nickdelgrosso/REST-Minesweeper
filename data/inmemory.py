from minesweeper.entitites import Session

session = Session.init()

def restart_session():
    global session
    session = Session.init()