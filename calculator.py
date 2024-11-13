import math

def calculate_hypotenuse(opposite, adjacent):
    """
    Calcule l'hypoténuse d'un triangle rectangle en utilisant les côtés opposé et adjacent.
    """
    if opposite <= 0 or adjacent <= 0:
        raise ValueError("Les côtés opposé et adjacent doivent être des nombres positifs.")
    return math.sqrt(opposite**2 + adjacent**2)