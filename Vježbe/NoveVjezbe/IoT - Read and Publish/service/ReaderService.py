from threading import Thread
from mqtt import MqttClient
from time import sleep as delay


class MsgReceived(Thread):
    def __init__(self, mqtt: MqttClient, log_screen):
        super(MsgReceived, self).__init__()
        self.mqtt = mqtt
        self.log_screen = log_screen
        self.topic = None
        self.message = None

    def run(self):
        while True:
            try:
                self.topic, self.message = self.mqtt.get_from_queue().split(";")
                if self.message is not None:
                    self.show_data()
                else:
                    pass
            except:
                pass
            delay(0.5)

    def show_data(self):
        self.log_screen.config(state="normal")
        self.log_screen.insert("end", f"{self.topic}: {self.message}\n")
        self.log_screen.config(state="disabled")
