def replace_string(text, from_, to_):
    start = text.find(from_, 0)
    while start != -1:
        text = text[:start] + text[start:].replace(from_, to_)
        start += len(to_)
        start = text.find(from_, start)
        return text
    return text


if __name__ == '__main__':
    text = input()
    s = input()
    t = input()

    print(replace_string(text, s, t))
