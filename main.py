BULKY_VOLUME = 10**6
BULKY_DIMENSION = 150
HEAVY_MASS = 20


def sort(width, height, length, mass) -> str:
    """
    Return the category of a package based on bulky and heavy rules.
    """

    try:
        width = float(width)
        height = float(height)
        length = float(length)
        mass = float(mass)
    except (ValueError, TypeError):
        raise ValueError("Input values must be numeric!")

    if any(x <= 0 for x in (width, height, length, mass)):
        raise ValueError("Input values must be positive!")

    bulky = max(width, height, length) >= BULKY_DIMENSION
    if not bulky:
        bulky = width * height * length >= BULKY_VOLUME

    heavy = mass >= HEAVY_MASS

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"
