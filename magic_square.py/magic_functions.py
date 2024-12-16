import random

def gen_square ():
    one_to_nine = [x for x in range(1, 10)]
    random.shuffle(one_to_nine)
    square = [[], [], []]
    count = 0
    for i in one_to_nine:
        if len(square[count]) < 3:
            square[count].append(i)
        else:
            square[count + 1].append(i)
            count += 1
    return square
print(gen_square())

        
# think about steps when deciding list size

def agen_square():
    one_to_nine = list(range(1,10)) # no need to for loop done automatically
    random.shuffle(one_to_nine)
    # select range index(i) to index(i plus 2), steps i 3 places so index(i) =0, 3, 6
    #so selection of index groups (0, 2), (3, 5), (6, 8)
    square = [one_to_nine[i: i+3] for i in range(0, 9, 3)]
    return square

print(agen_square())

