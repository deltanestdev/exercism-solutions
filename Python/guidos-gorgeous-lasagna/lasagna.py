# Functions used in preparing Guido's gorgeous lasagna.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):

    """
    expected bake time
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time 

def preparation_time_in_minutes(number_of_layers):

    """
    preparation time
    """
    return number_of_layers * PREPARATION_TIME   

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    """
    elapsed time
    """

    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)