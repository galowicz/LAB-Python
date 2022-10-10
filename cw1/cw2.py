#!/usr/bin/env python3

if __name__ == '__main__':
	print("Podaj Imię Nazwisko oraz rok urodzenia")
	string = input()
	[imie,nazwisko,rok] = string.split(' ')
	print(imie)
	print(nazwisko)
	print(rok)
	#print(string)