import itertools
import random

def random_permutation(iterable, r=None):
    "Random selection from itertools.permutations(iterable, r)"
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))

pairs = [['Tore'],
         ['Marit', 'Mathias'],
         ['Marianne', 'Andreas'],
         ['Helene', 'Morten'],
         ['Tuva', 'Tormod'],
         ['Ingrid', 'Henrik'],
         ['Saskia', 'Espen'],
         ['Cecilia', 'Eivind'],
         ['Hege', 'Joergen']]
flatten = lambda l: [item for sublist in l for item in sublist]
allAttendees = flatten(pairs)
allAttendees.sort(reverse=True)
#allCombos = itertools.permutations(allAttendees, len(allAttendees))

starterHavers = ['Marianne', 'Helene', 'Saskia']
maincourseHavers = ['Mathias', 'Kjetil', 'Cecilia']

while (True):
    combo = random_permutation(allAttendees, len(allAttendees))
    allGuests = [x for x in combo if x not in starterHavers]
    i=0
    noPairsInGuestLists = True
    listOfStartersParties = ['Herbert']
    listOfStartersParties.remove('Herbert')
    for starterHaver in starterHavers:
        thisPartiesGuests = allGuests[int (len(allGuests)/len(starterHavers) * (i)):int (len(allGuests)/len(starterHavers) * (i+1))]
        for pair in pairs:
            if len(pair) <= 1:
                continue
            if (pair[0] in thisPartiesGuests) and (pair[1] in thisPartiesGuests):
                noPairsInGuestLists = False
            if not(noPairsInGuestLists):
                break
        if (noPairsInGuestLists):
            listOfStartersParties.append(thisPartiesGuests)
        i=i+1

    if len(listOfStartersParties) == len(starterHavers):
        print ('--- Forrett ---')
        for i in range(0, 3):
            print ('   til: ' + starterHavers[i] + ' skal: ' + str(listOfStartersParties[i]))


