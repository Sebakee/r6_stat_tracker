from roles import get_op_roles
from parsers import get_sorted_operators

def calculate_entry_score(data):
    operators = get_sorted_operators(data)

    weighted_first_bloods = 0
    weighted_first_deaths = 0
    weighted_kills = 0
    weighted_rounds = 0

    for op in operators:
        name = op.get("operator", "unknown")
        entry_weight = get_op_roles(name)

        weighted_first_bloods += op.get("firstBloods", 0) * entry_weight
        weighted_first_deaths += op.get("firstDeaths", 0) * entry_weight
        weighted_kills += op.get("kills", 0) * entry_weight
        weighted_rounds += op.get("roundsPlayed", 0) * entry_weight

    opening_duels = weighted_first_bloods + weighted_first_deaths

    entry_success = weighted_first_bloods / opening_duels if opening_duels else 0
    entry_involvement = opening_duels / weighted_rounds if weighted_rounds else 0
    kill_pressure = weighted_kills / weighted_rounds if weighted_rounds else 0

    success_score = max(0, min((entry_success - 0.35) / (0.65 - 0.35), 1)) * 100
    involvement_score = min(entry_involvement / 0.25, 1) * 100
    kill_score = min(kill_pressure, 1) * 100

    entry_score = (
        success_score * 0.45
        + involvement_score * 0.35
        + kill_score * 0.2
    )

    return {
        "entry_score": entry_score,
        "success_score": success_score,
        "involvement_score": involvement_score,
        "kill_score": kill_score,
        "weighted_first_bloods": weighted_first_bloods,
        "weighted_first_deaths": weighted_first_deaths,
        "weighted_kills": weighted_kills,
        "weighted_rounds": weighted_rounds,
        "opening_duels": opening_duels,
        "entry_success": entry_success,
        "entry_involvement": entry_involvement,
        "kill_pressure": kill_pressure,
    }