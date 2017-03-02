def count_substring(string, sub_string):
    stringSequences = []

    for i in range(len(string)):
        stringSequences.append(string[i:i+len(sub_string)])

    return stringSequences.count(sub_string)
