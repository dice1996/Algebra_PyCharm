from screens.MainWindow import MainWindow


if __name__ == "__main__":
    app = MainWindow()
    app.anchor("n")
    app.resizable(False, False)
    app.mainloop()