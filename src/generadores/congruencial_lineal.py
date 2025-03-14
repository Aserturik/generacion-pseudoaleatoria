def congruencial_lineal(X0, k, c, g, n, minimo, maximo):
    # Calcular los parámetros a y m
    a = 1 + 2 * k
    m = 2 ** g

    # Inicializar las listas de números
    Xi = []
    Ri = []
    Ni = []

    # Generar los números aleatorios
    X = X0
    for i in range(n):
        if i == 0:
            X = ((a * X0) + c) % m
        else:
            X = ((a * X) + c) % m
        R = X / (m - 1)
        N = maximo + (minimo - maximo) * R
        Xi.append(X)
        Ri.append(R)
        Ni.append(N)

    return Xi, Ri, Ni

if __name__ == "__main__":
    # Solicitar al usuario que ingrese los valores
    X0 = int(input("Ingrese el valor de X0: "))
    k = int(input("Ingrese el valor de k: "))
    c = int(input("Ingrese el valor de c: "))
    g = int(input("Ingrese el valor de g: "))
    minimo = float(input("Ingrese el valor de MINIMO: "))
    maximo = float(input("Ingrese el valor de MAXIMO: "))
    n = int(input("Ingrese la cantidad de iteraciones: "))

    # Generar los números aleatorios
    Xi, Ri, Ni = congruencial_lineal(X0, k, c, g, n, minimo, maximo)

    # Imprimir los resultados
    print("Resultados:")
    print(f"{'i':<5} {'Xi':<10} {'Ri':<10} {'Ni':<10}")
    for i in range(n):
        print(f"{i+1:<5} {Xi[i]:<10} {Ri[i]:<10.6f} {Ni[i]:<10.6f}")