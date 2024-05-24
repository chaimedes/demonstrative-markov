import subprocess, collections, random, sys

def get_saying(filesrc):
 
    # Default max output
    outputrange = 1000

    # Build possibles table indexed by pair of prefix words (w1, w2)
    w1 = w2 = ''
    possibles = collections.defaultdict(list)

    fh = open(filesrc, encoding='utf-8')

    for line in fh:
        for word in line.split():
            if word.endswith('.'):
                word = word[:-1]
                possibles[w1, w2].append(word)
                possibles[w2, word].append('.')
                w1, w2 = word, '.'
            elif word.endswith('?'):
                word = word[:-1]
                possibles[w1, w2].append(word)
                possibles[w2, word].append('?')
                w1, w2 = word, '?'
            elif word.endswith('!'):
                word = word[:-1]
                possibles[w1, w2].append(word)
                possibles[w2, word].append('!')
                w1, w2 = word, '!'
            else:
                possibles[w1, w2].append(word)
                w1, w2 = w2, word

    # Avoid empty possibles lists at end of input
    possibles[w1, w2].append('')
    possibles[w2, ''].append('')

    # Generate randomized output (start with a random capitalized prefix)
    w1, w2 = random.choice([k for k in possibles if k[0][:1].isupper()])
    output = [w1, w2]

    for _ in range(outputrange):
        word = random.choice(possibles[w1, w2])
        output.append(word)
        if word == '.' or word == '!' or word == '?':
            break
        w1, w2 = w2, word

    finaloutput = ''
    for i, word in enumerate(output):
        finaloutput += word
        if len(output) > i+1:
            if output[i+1] != '.' and output[i+1] != '?' and output[i+1] != '!':
                finaloutput += ' '

    return finaloutput
