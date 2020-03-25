#!/usr/bin/python3
from settings import *

def clear_notification(identifier):
    print("Deleted notification")
    requests.delete(f"{url}/message/{identifier}", headers=headers)


if __name__ == "__main__":
    while True:
        try:
            r = requests.get(f"{url}/message", headers=headers)
            print("Connection established")
        except:
            print("Lost connection, retrying in 5 seconds...")
            time.sleep(5)
            continue
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
                notification.set_app_name("Gotify")
                notification.add_action(
                "action_click",
                "Delete Notification",
                clear_notification,
                identifier # Arguments
                )
                try:
                    notification.show()
                    old.append(message)
                except:
                    pass
        time.sleep(delay)
    Notify.uninit()
