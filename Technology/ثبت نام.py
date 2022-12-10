def check_registration_rules(**kwargs):
    ls = []

    for key, value in kwargs.items():
        if key not in ("quera", "codecup") and len(value) >= 6 and not value.isdigit() and len(key) >= 4:
            ls.append(key)
    return ls
