import sys
from r6data_api import get_full_stats
from summaries import (
    save_json_to_file,
    save_operator_summary,
    save_general_operator_totals,
)
from scores import calculate_entry_score, calculate_top_entry_operators

def run_entry_report(data):
    entry = calculate_entry_score(data)
    top_ops = calculate_top_entry_operators(data, limit=5, minimum_rounds=10)
    print()
    print("=== ENTRY REPORT ===")
    print(f"Entry Score: {entry['entry_score']:.1f}/100")
    print()
    print(f"Opening Success Score: {entry['success_score']:.1f}/100")
    print(f"Opening Involvement Score: {entry['involvement_score']:.1f}/100")
    print(f"Kill Pressure Score: {entry['kill_score']:.1f}/100")
    print()
    print(f"Weighted first bloods: {entry['weighted_first_bloods']:.1f}")
    print(f"Weighted first deaths: {entry['weighted_first_deaths']:.1f}")
    print(f"Entry success rate: {entry['entry_success'] * 100:.1f}%")
    print(f"Entry involvement rate: {entry['entry_involvement'] * 100:.1f}%")
    print(f"Entry-weighted KPR: {entry['kill_pressure']:.2f}")

    print()
    print("Top 5 Entry Operators")
    print("---------------------")

    for index, op in enumerate(top_ops, start=1):
        print(
            f"{index}. {op['operator']} - "
            f"{op['weighted_score']:.1f}/100"
        )
        print(
            f"   Entry: {op['first_bloods']}-{op['first_deaths']} | "
            f"Success: {op['entry_success'] * 100:.1f}% | "
            f"Involvement: {op['entry_involvement'] * 100:.1f}% | "
            f"KPR: {op['kill_pressure']:.2f} | "
            f"Rounds played: {op['rounds']}"
        )


def main():
    command = sys.argv[1] if len(sys.argv) > 1 else "summary"

    player = input("In game name: ")
    platform = input("Platform (psn/xbl/uplay)")
    if platform == "uplay":
        platform_family = "pc"
    else:
        platform_family = "console"
    season = "y11s2"

    data = get_full_stats(
        name=player,
        platform=platform,
        platform_family=platform_family,
        season=season,
    )


    if command == "entry":
        run_entry_report(data)

    elif command == "summary":
        save_json_to_file(data, f"output/{player}_fullStats.txt")
        save_operator_summary(data, f"output/{player}_operator_summary.txt")
        save_general_operator_totals(data, f"output/{player}_general_operator_totals.txt")

    else:
        print(f"Unknown command: {command}")
        print("Use:")
        print("  python .\\main.py summary")
        print("  python .\\main.py entry")



if __name__ == "__main__":
    main()