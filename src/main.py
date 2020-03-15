# Resolve the problem!!
import re


def run():
    # Start coding here
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    hide_word = re.findall(r'[a-z]', text)
    print(''.join(hide_word))


if __name__ == '__main__':
    run()
