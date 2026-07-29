from r6data_api import get_full_stats
from summaries import (
    save_json_to_file,
    save_operator_summary,
    save_general_operator_totals,
)


def main():
    player = "MrJunkFoodMood"
    platform = "psn"
    platform_family = "console"
    season = "all"

    data = get_full_stats(
        name=player,
        platform=platform,
        platform_family=platform_family,
        season=season,
    )

    print("Success!")

    save_json_to_file(data, f"output/{player}_fullStats.txt")
    save_operator_summary(data, f"output/{player}_operator_summary.txt")
    save_general_operator_totals(data, f"output/{player}_general_operator_totals.txt")


if __name__ == "__main__":
    main()