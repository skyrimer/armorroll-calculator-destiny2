from colorama import init, Fore, Style
from calculator import (ArmorPiece, ArmorSet, get_all_rolls,
                        get_armorpiece_table, get_armorset_table,
                        get_good_rolls)
from armordata import helmet_list, arms_list, chest_list, legs_list, exotics

if __name__ == "__main__":
    init()
    all_armor_variations = get_all_rolls(
        helmet_list, arms_list, chest_list, exotics['legs'])
    good_rolls = get_good_rolls(all_armor_variations)

    for armor_set in good_rolls:
        print(get_armorset_table(armor_set))
        print(get_armorpiece_table(armor_set))
        print(Fore.BLUE + "=======" + Style.RESET_ALL)
        print(Fore.BLUE + "=======" + Style.RESET_ALL)
