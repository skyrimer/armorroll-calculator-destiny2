from calculator import (get_all_rolls, get_good_rolls,
                        get_armorpiece_table, get_armorset_table)
from armordata import helmet_list, arms_list, chest_list, legs_list, exotics
from rich.console import Console

if __name__ == "__main__":
    good_rolls = get_good_rolls(get_all_rolls(
        exotics['helmet'], arms_list, chest_list, legs_list))
    console = Console()
    separator = "-" * 150
    for armor_set in good_rolls:
        console.print(f"\n\n\n{separator}\n\n\n",
                      style="red")
        console.print(get_armorpiece_table(armor_set))
        console.print(get_armorset_table(armor_set))
