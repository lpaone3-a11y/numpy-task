import numpy as np

# Controlla il file readme.md per i dettagli su ciascun sub-task

def prodotto_scalare(v1: list, v2: list) -> float:
    v=array = list(map(int, input("Inserire lista di numeri separati da spazio: ").split()))
    w=array = list(map(int, input("Inserire altra lista di numeri separati da spazio: ").split()))
    p_scalare=np.inner(v,w)
    return p_scalare
    pass

def rango_matrice(m: list) -> int:
    R = int(input("Inserire numero righe matrice: "))
    C = int(input("Inserire numero colonne matrice: "))

    print('Inserire',R*C,'numeri separati da spazio: ')
    vals = list(map(int, input().split()))
    mat = np.array(vals).reshape(R, C)
    rango=np.linalg.matrix_rank(mat)
    return rango
    pass

def risolvi_sistema_lineare(A: list, b: list) -> np.ndarray:
    R=int(input("Inserire numero righe matrice: "))
    print('Inserire', R*R, 'numeri separati da spazio: ')
    vals = list(map(int, input().split()))
    A= np.array(vals).reshape(R, R)
    b= list(map(int, input("Inserire numeri separati da spazio (tanti quante le righe della matrice: ").split()))
    x=np.linalg.solve(A,b)
    return x
    pass

def correlazione_matrici(m1: list, m2: list) -> np.ndarray:
    """Sub-task 4: Correlazione tra Matrici 2x2."""
    pass

def operazioni_elemento_per_elemento(v1: list) -> tuple:
    """Sub-task 5: Restituisce (seno, coseno, arcoseno, arcocoseno) elemento per elemento calcolati sul primo array."""
    pass


def main():
    print("Sub-task 1:", prodotto_scalare([1, 2, 3], [4, 5, 6]))
    print("Sub-task 1:", rango_matrice([[1, 2], [3, 4]]))
    print("Sub-task 3:", risolvi_sistema_lineare([[2, 1], [1, 3]], [5, 7]))
    print("Sub-task 4:", correlazione_matrici([[1, 2], [3, 4]], [[2, 4], [6, 8]]))
    print("Sub-task 5:", operazioni_elemento_per_elemento([0, 0.5, 1, -0.5]))

if __name__ == "__main__":
    main()
