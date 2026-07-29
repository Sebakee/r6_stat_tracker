import json
from parsers import get_sorted_operators
from scores import calculate_entry_score


def save_json_to_file(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

    print(f"Saved full output to {filename}")


def save_operator_summary(data, filename):
    operators = get_sorted_operators(data)

    if not operators:
        print("No operators found.")
        return

    with open(filename, "w", encoding="utf-8") as file:
        file.write("Operator Summary\n")
        file.write("================\n\n")

        for op in operators:
            name = op.get("operator", "Unknown")
            side = op.get("side", "?")
            rounds = op.get("roundsPlayed", 0)
            wins = op.get("wins", 0)
            losses = op.get("losses", 0)
            win_percent = op.get("winPercent", 0)
            kills = op.get("kills", 0)
            deaths = op.get("deaths", 0)
            kd = op.get("kd", 0)
            first_bloods = op.get("firstBloods", 0)
            first_deaths = op.get("firstDeaths", 0)
            clutches = op.get("clutches", 0)
            aces = op.get("aces", 0)
            kills4k = op.get("kills4K", 0)
            kills5k = op.get("kills5K", 0)
            time_played = op.get("timePlayed", "unknown")

            file.write(f"{name} ({side})\n")
            file.write(f"  Rounds: {rounds}\n")
            file.write(f"  W/L: {wins}-{losses} ({win_percent}%)\n")
            file.write(f"  K/D: {kills}/{deaths} ({kd})\n")
            file.write(f"  Entry: {first_bloods}-{first_deaths}\n")
            file.write(f"  Clutches: {clutches}\n")
            file.write(f"  Aces: {aces}, 4Ks: {kills4k}, 5Ks: {kills5k}\n")
            file.write(f"  Time played: {time_played}\n")
            file.write("\n")

    print(f"Saved operator summary to {filename}")


def save_general_operator_totals(data, filename):
    operators = get_sorted_operators(data)

    if not operators:
        print("No operators found.")
        return

    totals = {
        "roundsPlayed": 0,
        "wins": 0,
        "losses": 0,
        "kills": 0,
        "deaths": 0,
        "assists": 0,
        "headshots": 0,
        "firstBloods": 0,
        "firstDeaths": 0,
        "teamKills": 0,
        "clutches": 0,
        "clutchesLost": 0,
        "aces": 0,
        "matchesPlayed": 0,
        "matchesWon": 0,
        "matchesLost": 0,
        "kills1K": 0,
        "kills2K": 0,
        "kills3K": 0,
        "kills4K": 0,
        "kills5K": 0,
        "timePlayedMs": 0,
    }

    for op in operators:
        for key in totals:
            totals[key] += op.get(key, 0) or 0

    kills = totals["kills"]
    deaths = totals["deaths"]
    rounds = totals["roundsPlayed"]
    wins = totals["wins"]
    losses = totals["losses"]
    headshots = totals["headshots"]
    matches_won = totals["matchesWon"]
    matches_lost = totals["matchesLost"]
    time_ms = totals["timePlayedMs"]

    kd = kills / deaths if deaths else kills
    winrate = wins / (wins + losses) * 100 if wins + losses else 0
    match_winrate = matches_won / (matches_won + matches_lost) * 100 if matches_won + matches_lost else 0
    headshot_percent = headshots / kills * 100 if kills else 0

    kills_per_round = kills / rounds if rounds else 0
    deaths_per_round = deaths / rounds if rounds else 0
    assists_per_round = totals["assists"] / rounds if rounds else 0

    entry_ratio = totals["firstBloods"] / totals["firstDeaths"] if totals["firstDeaths"] else totals["firstBloods"]

    seconds = time_ms // 1000
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    with open(filename, "w", encoding="utf-8") as file:
        file.write("General Operator Totals\n")
        file.write("=======================\n\n")

        file.write(f"Operators counted: {len(operators)}\n")
        file.write(f"Time played: {hours}h {minutes}m\n\n")

        file.write("Core stats\n")
        file.write("----------\n")
        file.write(f"Rounds played: {rounds}\n")
        file.write(f"W/L: {wins}-{losses} ({winrate:.2f}%)\n")
        file.write(f"Matches W/L: {matches_won}-{matches_lost} ({match_winrate:.2f}%)\n")
        file.write(f"K/D: {kills}/{deaths} ({kd:.2f})\n")
        file.write(f"Assists: {totals['assists']}\n")
        file.write(f"Headshots: {headshots} ({headshot_percent:.2f}%)\n\n")

        file.write("Per-round stats\n")
        file.write("---------------\n")
        file.write(f"Kills per round: {kills_per_round:.2f}\n")
        file.write(f"Deaths per round: {deaths_per_round:.2f}\n")
        file.write(f"Assists per round: {assists_per_round:.2f}\n\n")

        file.write("Entry stats\n")
        file.write("-----------\n")
        file.write(f"First bloods: {totals['firstBloods']}\n")
        file.write(f"First deaths: {totals['firstDeaths']}\n")
        file.write(f"Entry ratio: {entry_ratio:.2f}\n\n")

        file.write("Clutch and multikill stats\n")
        file.write("--------------------------\n")
        file.write(f"Clutches won: {totals['clutches']}\n")
        file.write(f"Clutches lost: {totals['clutchesLost']}\n")
        file.write(f"Aces: {totals['aces']}\n")
        file.write(f"1Ks: {totals['kills1K']}\n")
        file.write(f"2Ks: {totals['kills2K']}\n")
        file.write(f"3Ks: {totals['kills3K']}\n")
        file.write(f"4Ks: {totals['kills4K']}\n")
        file.write(f"5Ks: {totals['kills5K']}\n\n")

        file.write("Oopsie stats\n")
        file.write("------------\n")
        file.write(f"Team kills: {totals['teamKills']}\n")
        entry = calculate_entry_score(data)
        
        file.write("\nEntry Role Score\n")
        file.write("----------------\n")
        file.write(f"Entry Score: {entry['entry_score']:.1f}/100\n")
        file.write(f"Opening Success Score: {entry['success_score']:.1f}/100\n")
        file.write(f"Opening Involvement Score: {entry['involvement_score']:.1f}/100\n")
        file.write(f"Kill Pressure Score: {entry['kill_score']:.1f}/100\n\n")
        
        file.write(f"Weighted first bloods: {entry['weighted_first_bloods']:.1f}\n")
        file.write(f"Weighted first deaths: {entry['weighted_first_deaths']:.1f}\n")
        file.write(f"Weighted opening duels: {entry['opening_duels']:.1f}\n")
        file.write(f"Weighted entry rounds: {entry['weighted_rounds']:.1f}\n")
        file.write(f"Entry success rate: {entry['entry_success'] * 100:.1f}%\n")
        file.write(f"Entry involvement rate: {entry['entry_involvement'] * 100:.1f}%\n")
        file.write(f"Entry-weighted KPR: {entry['kill_pressure']:.2f}\n\n")

    print(f"Saved general operator totals to {filename}")

    