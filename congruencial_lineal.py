def congruencial_lineal(X0, k, c, g, n, minimo, maximo):
    a = 1 + 2 * k
    m = 2 ** g
    Xi, Ri, Ni = [], [], []
    X = X0

    for i in range(n):
        X = ((a * X) + c) % m
        R = X / (m - 1)
        N = maximo + (minimo - maximo) * R
        Xi.append(X)
        Ri.append(round(R, 6))  # Redondear para mejor visualización
        Ni.append(round(N, 6))

    return Xi, Ri, Ni  # Devuelve los valores sin imprimir en consola
