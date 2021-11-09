import sys

MORSE = {'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----'}


if len(sys.argv) < 2:
    print("ERROR")
    quit()

letter = []
for tmp in sys.argv:
    if not tmp == sys.argv[0]:
        words = tmp.split()
        for tup in words:
            if tup.isalnum():
                tmp2 = tup.upper()
                for c in tmp2:
                    for let, code in MORSE.items():
                        if let == c:
                            letter.append(code)
                            break
            else:
                print("ERROR")
                quit()
            if not tmp == sys.argv[-1] or not tup == words[-1]:
                letter.append('/')
            str = ' '.join(letter)
print(str)
