
from view import AppView
from controller import Controller

if __name__ == "__main__":
    view = AppView(None)
    controller = Controller(view)
    view.controller = controller

    view.iniciar()