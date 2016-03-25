
from . import towers, field, reactor


def get_available_locations():
    """Return the list of possible locations for the IA to put the towers."""
    return field.get_tower_locations()


def get_tower_types():
    """Return the list of possible tower types for the IA to push."""
    return towers.get_kinds()


def start(bootstrap_info, drawing=False):
    """Start the game.

    Receive a dict with positions as keys, and tower type as values.

    Return a score.
    """
    return reactor.go(bootstrap_info)
