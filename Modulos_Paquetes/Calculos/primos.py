def es_par(numero):
    """Verifica si un número es par."""
    return numero % 2 == 0
def es_primo(numero):
    """Verifica si un número es primo."""
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True 