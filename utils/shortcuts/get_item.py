def get_item(items, default=None, index=0):
    try:
        return items[index]
    except IndexError:
        return default
