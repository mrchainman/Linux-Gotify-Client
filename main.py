#!/usr/bin/python3
from settings import *

def clear_notification(identifier):
    print("Deleted notification")
    requests.delete(f"{url}/message/{identifier}", headers=headers)


if __name__ == "__main__":
    while True:
        r = requests.get(f"{url}/message", headers=headers)
        m = (r.json())
        messages_list = m["messages"]
        for i in range(len(messages_list)):
            message = messages_list[i]["message"]
            title = messages_list[i]["title"]
            identifier = messages_list[i]["id"]
            if message not in old:
                notification = Notify.Notification.new(
                    title,
                    message,
                    image
                )
                notification.add_action(
                "action_click",
                "Delete Notification",
                clear_notification,
                identifier # Arguments
                )
                notification.show()
                old.append(message)
        time.sleep(delay)
    Notify.uninit()
