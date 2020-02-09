import MQTT_sub_pub as mqtt
import threading
import random
import time
import queue
import nicetable
import tkinter as tk



number_of_groups = 5
random_number_table = [random.randint(10, 100) for _ in range(number_of_groups)]
topics_name_for_each_group = ["group/"+str(x) for x in range(number_of_groups)]
topics_name_for_each_group_answer = ["answer/group/"+str(x) for x in range(number_of_groups)]
dictionary_number_group_and_their_int_ans = dict(zip(topics_name_for_each_group_answer, random_number_table))
dictionary_number_group_and_their_int = dict(zip(topics_name_for_each_group, random_number_table))
received_back_message_or_not = [1 for _ in range(number_of_groups)]
print(topics_name_for_each_group)


mqtt_client = mqtt.MQTTClient()
root = tk.Tk()
root.geometry("800x400")
gui = nicetable.GUI(root, topics_name_for_each_group)



class SendMQTTToEveryGroup(threading.Thread):
    def __init__(self, master):
        super().__init__()
        self.master = master

    def run(self):
        for group in topics_name_for_each_group:
            mqtt_client.mqtt_publish(group, dictionary_number_group_and_their_int[group])
        time.sleep(1)
        mqtt_client.client.loop(0.01)
        self.master.after(100, self.run)


class ReceiveMQTTMessageFromEveryGroup(threading.Thread):
    def __init__(self):
        super().__init__()
        for group in topics_name_for_each_group_answer:
            mqtt_client.mqtt_subscribe(group)

    def run(self):
        while True:
            if mqtt_client.message_received == str(dictionary_number_group_and_their_int_ans[mqtt_client.topic_received]):
                if mqtt_client.topic_received.split("/", 1)[1] in topics_name_for_each_group:
                   print("Message from " + mqtt_client.topic_received)
                   group = int(mqtt_client.topic_received[-1:])
                   gui.change_status(group)
                   mqtt_client.message_received = ""
                   group_topic_pub = mqtt_client.topic_received.split("/", 1)[1]
                   del topics_name_for_each_group[topics_name_for_each_group.index(group_topic_pub)]
                   print("Who remains?" , topics_name_for_each_group)






if __name__ == "__main__":
    thread = ReceiveMQTTMessageFromEveryGroup()
    thread.start()
    SR = SendMQTTToEveryGroup(root)
    SR.start()
    root.mainloop()












