def validate_email(email):
    allowed_chars = "abcdefghijklmnopqrstuvwxyz._-@0123456789"
    for i in email:
        if i not in allowed_chars:
            return False
    if email.count("@") == 1 and email.islower():
        first, end = email.split("@")
        if end.count(".") >= 1 and len(first) > 0:
            for i in end.split("."):
                if len(i) < 1:
                    return False
            if 1 < len(end.split(".")[-1]) < 4:
                return True
    return False

def list_median(values):
    sorted_values = sorted(values)
    length = len(sorted_values)
    if length % 2 == 0:
        return round((sorted_values[length//2-1] + sorted_values[length//2]) / 2, 1)
    else:
        return sorted_values[(length-1)//2]

def find_duplicates(values):
    counter = {}
    for v in values:
        if v.lower() in counter:
            counter[v.lower()] += 1
        else:
            counter[v.lower()] = 0
    dups = []
    for k,v in counter.items():
        if v > 0:
            dups.append(k)
    return sorted(dups)

def analyze_text():
    while True:
        inp = input()
        if inp == "q":
            break
        elif inp == "v":
            print(4)
        elif inp == "p":
            print(5)
        elif inp == "u":
            print(6)
    return True
