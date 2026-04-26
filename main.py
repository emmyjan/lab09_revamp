from controller import *


def main():
    app = QApplication([])
    window = Controller(app)
    window.show()
    app.exec()

if __name__ == "__main__":
    main()