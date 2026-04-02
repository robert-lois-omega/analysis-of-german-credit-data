def translate(x, mapping):
    for code, label in mapping:
        if x == int(code):
            return label
    return None