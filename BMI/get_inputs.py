import re


def get_weight_input():
    "Prompt the user for a weight"
    weight_patterns = ("kg", "kgs" "[Kk]ilograms?", "lbs?", "[Pp]ounds?")
    raw_in = input("Type a weight in pounds or kilograms (default is kilograms)\nexample: 150.2 lbs \n"
                   "Type your input-->")
    items = match_words(raw_in, weight_patterns)
    return items


def get_height_input():
    "Prompt the user for a height"
    height_patterns = ("meters", "[Mm](?:eters?)?", "(?:in)(?:ch(?:es)?)?")  # no one types IN for inches
    raw_in = input("Type a height in inches or meters (default is meters)\nexample: 70.75 inches \n"
                   "Type your input-->")
    items = match_words(raw_in, height_patterns)
    return items


def match_words(raw_in, patterns):
    """a pattern matching function to return a dictionary with a measurement and units given a string with both
    values and patterns matching units """
    try:  # in case the default(first) unit is expected
        out = float(raw_in)
        return dict(value=out, units=patterns[0])
    except Exception:
        pass
    if raw_in in (None, ""):  # in case nothing is called
        raw_in = input("Type your input-->")
    match = re.match(r"^ *([0-9]+\.?[0-9]*) *(\w*) *$", raw_in)
    unit = match.group(2)
    if match:
        possible_typos = edits_one(unit)
        for pattern in patterns:
            if re.match(pattern + " *$", unit):
                return dict(value=float(match.group(1)), units=unit)
            else:
                typo_list = [typo for typo in possible_typos if re.match(pattern + " *$", typo)]
                if typo_list:
                    raw_in = input("you typed {}, did you mean {}?\nTry again-->".format(unit, typo_list[0]))
                    return match_words(raw_in, patterns)
    raise NameError("invalid input given: {}".format(raw_in))


def edits_one(word):
    "function that returns the set of all possible edits that are one letter edit away from word input"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
    replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts = [a + c + b for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)


if __name__ == "__main__":
    print(get_weight_input())
    print(get_height_input())
