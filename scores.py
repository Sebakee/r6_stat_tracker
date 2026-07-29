from roles import get_op_roles
from parsers import get_sorted_operators

def clamp(value, minimum=0, maximum=100):
    return max(minimum, min(value, maximum))


def calculate_entry_parts(first_bloods, first_deaths, kills, rounds):
    opening_duels = first_bloods + first_deaths * 0.5

    entry_success = first_bloods / (first_bloods + first_deaths) if opening_duels else 0
    entry_involvement = opening_duels / rounds if rounds else 0
    kill_pressure = kills / rounds if rounds else 0

    success_score = clamp(((entry_success - 0.35) / 0.27) * 100)
    involvement_score = clamp((entry_involvement / 0.25) * 100)
    kill_score = clamp((kill_pressure / 1.25) * 100)

    entry_score = (
        success_score * 0.35
        + involvement_score * 0.50
        + kill_score * 0.15
    )

    return {
        "entry_score": entry_score,
        "success_score": success_score,
        "involvement_score": involvement_score,
        "kill_score": kill_score,
        "first_bloods": first_bloods,
        "first_deaths": first_deaths,
        "opening_duels": opening_duels,
        "entry_success": entry_success,
        "entry_involvement": entry_involvement,
        "kill_pressure": kill_pressure,
        "kills": kills,
        "rounds": rounds,
    }

def calculate_entry_score(data):
    operators = get_sorted_operators(data)

    weighted_first_bloods = 0
    weighted_first_deaths = 0
    weighted_kills = 0
    weighted_rounds = 0

    for op in operators:
        if op.get("side") != "Attacker":
            continue

        name = op.get("operator", "Unknown")
        entry_weight = get_op_roles(name)

        weighted_first_bloods += op.get("firstBloods", 0) * entry_weight
        weighted_first_deaths += op.get("firstDeaths", 0) * entry_weight
        weighted_kills += op.get("kills", 0) * entry_weight
        weighted_rounds += op.get("roundsPlayed", 0) * entry_weight

    result = calculate_entry_parts(
        first_bloods=weighted_first_bloods,
        first_deaths=weighted_first_deaths,
        kills=weighted_kills,
        rounds=weighted_rounds,
    )

    result["weighted_first_bloods"] = weighted_first_bloods
    result["weighted_first_deaths"] = weighted_first_deaths
    result["weighted_kills"] = weighted_kills
    result["weighted_rounds"] = weighted_rounds

    return result

def calculate_top_entry_operators(data, limit=5, minimum_rounds=20, min_opening_duels=3):
    operators = get_sorted_operators(data)
    results = []

    for op in operators:
        if op.get("side") != "Attacker":
            continue

        name = op.get("operator", "Unknown")
        rounds = op.get("roundsPlayed", 0)

        if rounds < minimum_rounds:
            continue

        entry_weight = get_op_roles(name)

        first_bloods = op.get("firstBloods", 0)
        first_deaths = op.get("firstDeaths", 0)
        opening_duels = first_deaths + first_bloods

        if opening_duels < min_opening_duels:
            continue
        kills = op.get("kills", 0)

        score_data = calculate_entry_parts(
            first_bloods=first_bloods,
            first_deaths=first_deaths,
            kills=kills,
            rounds=rounds,
        )

        score_data["operator"] = name
        score_data["entry_weight"] = entry_weight
        score_data["weighted_score"] = score_data["entry_score"] * entry_weight

        results.append(score_data)

    results = sorted(
        results,
        key=lambda item: item["weighted_score"],
        reverse=True
    )

    return results[:limit]