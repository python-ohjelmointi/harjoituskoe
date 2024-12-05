def tarkista_perakkaiset(numerot: list) -> bool:
    """
    Tarkistaa, muodostavatko annetut numerot peräkkäisten lukujen sarjan.
    
    Palauttaa True, jos numerot ovat peräkkäisiä ilman puuttuvia tai toistuvia lukuja,
    muuten False.
    """
    numerot_set = set(numerot)
    
    if len(numerot_set) != len(numerot):
        return False
    
    min_luku = min(numerot_set)
    max_luku = max(numerot_set)
    
    if max_luku - min_luku == len(numerot_set) - 1:
        return True
    
    return False

if __name__ == "__main__":
    
    print(tarkista_perakkaiset([1, 2, 3, 4, 5]))  # True
    print(tarkista_perakkaiset([5, 4, 3, 2, 1]))  # True
    print(tarkista_perakkaiset([1, 3, 2, 5, 4]))  # True
    print(tarkista_perakkaiset([5, 3, 1]))        # False
    print(tarkista_perakkaiset([5, 3, 2, 2, 1]))  # False
