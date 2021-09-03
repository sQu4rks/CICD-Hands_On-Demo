import time

def get_entry(text, author):
    ret = {}

    # Check that text and author are not None
    if any(e is None for e in [text, author]):
        raise Exception(f"Property can't be none")
    ret['text'] = text
    ret['author'] = author
    ret['timestamp'] = time.time()

    return ret
