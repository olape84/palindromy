def palindromy(tekst):
    for i in range(len(tekst)):
        if not tekst[i] == tekst[-i-1]:
            return False
    return True

if palindromy(input("Wprowadz tekst, który chcesz sprawdzic czy jest palindromem i wcisnij enter")):
    print('Twoje słowo jest palindromem')
else:
    print('Twoje słowo nie jest palindromem')
