countries = ['FR', 'US', 'DE', 'RU']
countries[1]='GB' #formatowanie listy przez wstawienie na miejscu zmiennej 'US' zmiennej 'GB'
print(countries[1])#wyswietlenie tylko pozycji nr 1 czyli 'US'

countries.append('PL')#dodanie do listy zmiennej 'PL' na jej koncu

countries.insert(2, 'ES')#dodanie do listy zmiennej 'ES' na 2 pozycji, wazne by pamietac ze numeracja zaczybna sie od 0

countries.remove('RU')#usuniecie zmiennej z listy

countries.sort()#sortowanie

countries.reverse()#odwrocenie listy

print(countries.pop(2))#funkcja pop zwroci wywolana zmienna i usunie ja z listy 

print(countries.index('PL'))#wyszukuje zmiennem z wyroznieniem pozycji na liscie

#print(countries.index('US'))    dlatego ze nie ma tej zmiennej wystapi blad

print(countries.count('DE')) # liczy ile razy wystepuje zmienna w liscie

newList = ['FI', 'SE']
countries.extend(newList)#laczenie list

countriesCopy = countries.copy()#tworzenie kopii listy bez 
countriesCopy.clear()

print(countries)
print(countriesCopy)
