from screens.MainWindow import MainWindow

if __name__ == "__main__":
    app = MainWindow()
    app.run()
    app.anchor("n")
    app.resizable(False, False)
    app.mainloop()