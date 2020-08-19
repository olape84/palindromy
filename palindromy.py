def palindromy ():
    input("Wprowadz tekst, który chcesz sprawdzic czy jest palindromem i wcisnij enter")
    tekst = input()
    for i in range(len(tekst)):
        if tekst[i] != tekst[-i-1]:
            return False
    return True
palindromy()


