from . import main
@main.rout('/')
def index():
    return "Hello World!", 200