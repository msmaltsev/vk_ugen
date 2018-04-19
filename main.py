# !usr/env/bin python3
# -*- coding: utf8 -*-

import random
import string

def pwGen():
    pw = ''
    lengths = [15, 18]
    l = random.choice(lengths)
    while len(pw) < l:
        pw += random.choice(list(string.ascii_letters + string.digits))
    return pw



def rChoice(fname):
    f = open(fname, 'r', encoding='utf8')
    allitems = [line.strip('\n') for line in f]
    item = random.choice(allitems)
    return item


def userName(male_names = 'male_names', female_names = 'female_names', lastnames = 'lastnames'):
    lname = rChoice(lastnames)
    sex = random.choice(['m', 'f'])
    if sex == 'm':
        name = rChoice(male_names)
    else:
        name = rChoice(female_names)
        lname += 'а'
    return (name, lname)


def main():
    a = 5
    uname = userName()
    pw = pwGen()
    print(uname[0])
    print(uname[1])
    print(pw)


if __name__ == '__main__':
    main()