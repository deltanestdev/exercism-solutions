"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):

# Only return True if both parameters are True
    
    return power_pellet_active and touching_ghost

def score(touching_power_pellet, touching_dot):

# Only return True if one of the parameters are True

    return touching_power_pellet or touching_dot

def lose(power_pellet_active, touching_ghost):

# Lose if touching a ghost and power pellet is not active

    return touching_ghost and not power_pellet_active

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):

# Wins when there are not more dots and not lose

    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
