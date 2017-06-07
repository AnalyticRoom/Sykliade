import itertools
import random


def random_permutation(iterable, r=None):
    "Random selection from itertools.permutations(iterable, r)"
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))


def listOflistOfParties(partyHavers, thisPairs):
    permutation = random_permutation(allAttendees, len(allAttendees))
    guestsOnly = [x for x in permutation if x not in partyHavers]
    i=0
    noPairsInGuestLists = True
    listOflist = ['Herbert']
    listOflist.remove('Herbert')
    for partyHaver in partyHavers:
        thisGuests = guestsOnly[int (len(guestsOnly) / len(partyHavers) * (i)):int (len(guestsOnly) / len(partyHavers) * (i + 1))]
        thisGuests.insert(0, partyHaver)
        for pair in thisPairs:
            if len(pair) <= 1:
                continue
            if (pair[0] in thisGuests) and (pair[1] in thisGuests):
                noPairsInGuestLists = False
            if not(noPairsInGuestLists):
                break
        if noPairsInGuestLists:
            listOflist.append(thisGuests)
        i=i+1

    if len(listOflist) == len(partyHavers):
        return listOflist
    return None

pairs = [['Tore'],
         ['Mari'],
         ['Kristina', 'Kjetil'],
         ['Marit', 'Mathias'],
         ['Marianne', 'Andreas'],
         ['Helene', 'Morten'],
         ['Tuva', 'Tormod'],
         ['Ingrid', 'Henrik'],
         ['Saskia', 'Espen'],
         ['Cecilia', 'Eivind'],
         ['Joergen']]
flatten = lambda l: [item for sublist in l for item in sublist]
allAttendees = flatten(pairs)

starterHavers = ['Marianne', 'Helene', 'Saskia']
maincourseHavers = ['Mathias', 'Kjetil', 'Cecilia']

tries = 0
while (True):
    tries += 1
    starterParties = listOflistOfParties(starterHavers, pairs)
    if starterParties is None:
        continue
    pairsWithPairsFromStarterParties = pairs[:]
    for starterParty in starterParties:
        for j in range(0, len(starterParty) - 2):
          pairsWithPairsFromStarterParties.append(starterParty[j:(j+2)])
    #for starterParty in starterParties:
    #    for j in range(0, len(starterParty) - 4):
    #      pairsWithPairsFromStarterParties.append([str(starterParty[j]), str(starterParty[j+4])])
    #print(pairsWithPairsFromStarterParties)
    mainCourseParties = listOflistOfParties(maincourseHavers, pairsWithPairsFromStarterParties)
    if starterParties is not None and mainCourseParties is not None:
        #print(pairsWithPairsFromStarterParties)
        print ('After ' + str(tries) + ' tries:')
        print ('--- Forrett ---')
        for i in range(0, 3):
            print ('   til: ' + starterHavers[i] + ' skal: ' + str(starterParties[i]))
        print ('--- Hovedrett ---')
        for i in range(0, 3):
            print ('   til: ' + maincourseHavers[i] + ' skal: ' + str(mainCourseParties[i]))
        break



