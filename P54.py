from collections import Counter


def high_card(hand):
    highest = 0
    for i in hand:
        if i == 'A':
            return 14
        elif i == 'K':
            if 13 >= highest:
                highest = 13
        elif i == 'Q':
            if 12 >= highest:
                highest = 12
        elif i == 'J':
            if 11 >= highest:
                highest = 11
        elif i == 'T':
            if 10 >= highest:
                highest = 10
        elif int(i) > highest:
            highest = int(i)
    return highest


def convert_to_lists(s):
    cards = s.split(' ')
    card_value = []
    card_type = []
    for i in cards:
        card_value.append(i[0])
        card_type.append(i[1])
    return [card_value, card_type]


def number_of_pairs(l):
    count = Counter(l) - Counter(set(l))
    pairs = 0
    for i in count:
        if count[i] == 1:
            pairs += 1
    if pairs:
        return pairs + 1
    return 0


def three_of_a_kind(l):
    count = Counter(l) - Counter(set(l))
    for i in count:
        if count[i] == 2:
            return 4
    return 0


def straight(l):
    rating = {14: 'A', 13: 'K', 12: 'Q', 11: 'J', 10: 'T', 9: '9',
              8: '8', 7: '7', 6: '6', 5: '5', 4: '4', 3: '3', 2: '2', 1: '1'}
    hv = high_card(l)
    if rating[hv-1] in l:
        if rating[hv-2] in l:
            if rating[hv-3] in l:
                if rating[hv-4] in l:
                    return 5
    return 0


def flush(l):
    if len(set(l)) == 1:
        return 6
    return 0


def full_house(l):
    if three_of_a_kind(l):
        if number_of_pairs(l) == 2:
            return 7
    return 0


def four_of_a_kind(l):
    dup = Counter(l) - Counter(set(l))
    for i in dup:
        if dup[i] == 3:
            return 8
    return 0


def straight_flush(l, v):
    if straight(l) and flush(v):
        return 9
    return 0


def royal_flush(l, v):
    if set(['T', 'J', 'Q', 'K', 'A']) == set(l):
        if len(set(v)) == 1:
            return 10
    return 0


def paired_number(l):
    repeated = (Counter(l) - Counter(set(l))).keys()
    rating = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9,
              '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, '1': 1}
    highest = 0
    for i in repeated:
        if rating[i] > highest:
            highest = rating[i]
    return highest

f = open('poker.txt')

games = f.read()
f.close()
two_hands = games.strip().split('\n')
hands = []
for i in two_hands:
    fh = convert_to_lists(i[:14])
    sh = convert_to_lists(i[15:])
    hands.append([fh, sh])

player1 = 0

for i in hands:
    p1v = i[0][0]
    p2v = i[1][0]
    p1s = i[0][1]
    p2s = i[1][1]
    p1 = 0
    p2 = 0
    flag = False
    if number_of_pairs(p1v):
        p1 = number_of_pairs(p1v)
        flag = True
    if three_of_a_kind(p1v):
        p1 = three_of_a_kind(p1v)
        flag = True
    if straight(p1v):
        p1 = straight(p1v)
    if flush(p1s):
        p1 = flush(p1s)
    if full_house(p1v):
        p1 = full_house(p1v)
        flag = True
    if four_of_a_kind(p1v):
        p1 = four_of_a_kind(p1v)
        flag = True
    if straight_flush(p1v, p1s):
        p1 = straight_flush(p1v, p1s)
    if royal_flush(p1v, p1s):
        p1 = royal_flush(p1v, p1s)

    if number_of_pairs(p2v):
        p2 = number_of_pairs(p2v)
        flag = True
    if three_of_a_kind(p2v):
        p2 = three_of_a_kind(p2v)
        flag = True
    if straight(p2v):
        p2 = straight(p2v)
    if flush(p2s):
        p2 = flush(p2s)
    if full_house(p2v):
        p2 = full_house(p2v)
        flag = True
    if four_of_a_kind(p2v):
        p2 = four_of_a_kind(p2v)
        flg = True
    if straight_flush(p2v, p2s):
        p2 = straight_flush(p2v, p2s)
    if royal_flush(p2v, p2s):
        p2 = royal_flush(p2v, p2s)

    if p1 > p2:
        player1 += 1
    elif p1 == p2:
        if flag:
            if paired_number(i[0][0]) > paired_number(i[1][0]):
                player1 += 1
            elif paired_number(i[0][0]) == paired_number(i[1][0]):
                if high_card(i[0][0]) > high_card(i[1][0]):
                    player1 += 1
        else:
            if high_card(i[0][0]) > high_card(i[1][0]):
                player1 += 1

print( player1)