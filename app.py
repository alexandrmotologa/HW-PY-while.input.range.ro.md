# citim valorile de la tastatura pentru start_n si end_n
start_n = int(input("Introduceti valoarea de start: "))
end_n = int(input("Introduceti valoarea de final: "))

# verificam daca prima valoare este mai mica decat cea de-a doua
if start_n < end_n:
    # daca da, initializam variabila n cu valoarea de start si afisam valorile crescator
    n = start_n
    while n <= end_n:
        print(n)
        n += 1
else:
    # daca nu, initializam variabila n cu valoarea de start si afisam valorile descrescator
    n = start_n
    while n >= end_n:
        print(n)
        n -= 1