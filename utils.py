import time

def get_entry(text, author):
    ret = {}

    ret['text'] = text
    ret['author'] = author
    ret['timestamp'] = time.time()

    return ret
