from EmikoRobot.mongo import client as db_x

Geo = db_x["CHATBOT"]


def add_chat(chat_id):
    stark = Geo.find_one({"chat_id": chat_id})
    if stark:
        return False
    Geo.insert_one({"chat_id": chat_id})
    return True


def remove_chat(chat_id):
    stark = Geo.find_one({"chat_id": chat_id})
    if not stark:
        return False
    Geo.delete_one({"chat_id": chat_id})
    return True


def get_all_chats():
    r = list(Geo.find())
    if r:
        return r
    return False


def get_session(chat_id):
    stark = Geo.find_one({"chat_id": chat_id})
    if not stark:
        return False
    return stark
