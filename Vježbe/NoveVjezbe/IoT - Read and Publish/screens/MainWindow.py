from tkinter import Frame, messagebox
from threading import Thread
import tkinter as tk
from tkinter import ttk
import sv_ttk
from mqtt.MqttClient import MqttClient
from service.ReaderService import MsgReceived


class MainWindow(tk.Tk, Thread):

    def __init__(self):
        super().__init__()
        self.title("Read and Publish")
        sv_ttk.use_dark_theme()

    def run(self):
        MainScreen(self)

class MainScreen(Frame):

    HOST = "port.ceky.me"
    PORT = 1883
    MQTT_TOPIC_SHOW = "/main/+"

    def __init__(self, mainWindow):
        super().__init__(mainWindow)
        self.mqtt_client = MqttClient(self.HOST, self.PORT, self.MQTT_TOPIC_SHOW)
        self.grid()
        self.mqtt_client.start()

        #variable
        self.topic_var = tk.StringVar()
        self.input_var = tk.StringVar()

        #main lb frame
        self.lbFrame = ttk.Labelframe(self, text="MQTT Message")
        self.log_screen = tk.Text(self.lbFrame)
        self.log_screen.config(state="disabled", height=10, width=50)
        self.e_topic = ttk.Entry(self.lbFrame, textvariable=self.topic_var)
        self.e_input = ttk.Entry(self.lbFrame, textvariable=self.input_var)
        self.submit = ttk.Button(self.lbFrame, text="SEND", command=self.button_save)

        self.load_screen()

    def load_screen(self):
        self.lbFrame.grid(row=0, column=0, padx=5, pady=5, sticky="ewns")
        ttk.Label(self.lbFrame, text="USER").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        ttk.Label(self.lbFrame, text="MESSAGE").grid(row=2, column=0, padx=5, pady=2, sticky="w")
        self.e_topic.grid(row=1, column=0, padx=10, pady=2, sticky="ew")
        self.e_input.grid(row=3, column=0, padx=10, pady=2, sticky="ew")
        self.submit.grid(row=4, column=0, padx=5,pady=5, sticky="ew", columnspan=2)
        self.log_screen.grid(row=0, column=1, rowspan=4, pady=5, padx= 5, sticky="ew")
        self.fill_log_screen()

    def fill_log_screen(self):
        MsgReceived(self.mqtt_client, self.log_screen).start()

    def button_save(self):
        if self.topic_var.get() != "" and self.input_var.get() != "":
            self.mqtt_client.publish(f"/main/{self.topic_var.get()}", self.input_var.get())
            self.input_var.set("")
        else:
            messagebox.showerror("ERROR", "Please enter user and message")
