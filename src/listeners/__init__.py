from listeners import events
from listeners import commands

def register_listeners(app):
    try:
        events.register(app)
        commands.register(app)
    except Exception as ex:
        app.logger.error(ex)
    finally: pass