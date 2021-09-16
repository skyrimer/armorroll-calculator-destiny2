from dataclasses import dataclass, field
from prettytable import PrettyTable


@dataclass
class ArmorPiece:
    id: int
    type: str = ""
    mobility: int = 0
    resilience: int = 0
    recovery: int = 0
    discipline: int = 0
    intelect: int = 0
    strength: int = 0
    total_roll: int = field(init=False)

    def __post_init__(self):
        self.total_roll = self.mobility + self.resilience + \
            self.recovery + self.discipline + self.intelect + self.strength


class ArmorSet():
    def __init__(self, helmet: ArmorPiece, arms: ArmorPiece,
                 chest: ArmorPiece, legs: ArmorPiece):
        self.helmet = helmet
        self.arms = arms
        self.chest = chest
        self.legs = legs
        self.mobility = self.get_total_mobility() + 2
        self.resilience = self.get_total_resilience() + 2
        self.recovery = self.get_total_recovery() + 2
        self.discipline = self.get_total_discipline() + 2
        self.intelect = self.get_total_intelect() + 2
        self.strength = self.get_total_strength() + 2
        self.total_stats = self.get_total_stats()
        self.total_roll = sum(self.total_stats)
        self.wasted_stats = self.get_wasted_stats()
        self.actual_roll = self.total_roll - self.wasted_stats
        self.rating = self.get_armor_rating()
        self.is_good = True if self.wasted_stats <= 10 and self.actual_roll >= 310 else False

    def __lt__(self, other):
        return self.actual_roll > other.actual_roll

    def get_total_mobility(self):
        return self.helmet.mobility + self.arms.mobility + \
            self.chest.mobility + self.legs.mobility

    def get_total_resilience(self):
        return self.helmet.resilience + self.arms.resilience + \
            self.chest.resilience + self.legs.resilience

    def get_total_recovery(self):
        return self.helmet.recovery + self.arms.recovery + \
            self.chest.recovery + self.legs.recovery

    def get_total_discipline(self):
        return self.helmet.discipline + self.arms.discipline + \
            self.chest.discipline + self.legs.discipline

    def get_total_intelect(self):
        return self.helmet.intelect + self.arms.intelect + \
            self.chest.intelect + self.legs.intelect

    def get_total_strength(self):
        return self.helmet.strength + self.arms.strength + \
            self.chest.strength + self.legs.strength

    def get_total_stats(self):
        return [self.mobility, self.resilience, self.recovery, self.discipline, self.intelect, self.strength]

    def get_armor_rating(self):
        counter = 0
        for stat in self.total_stats:
            counter += 2 if stat % 10 == 0 else 1 if stat % 10 == 1 or stat % 10 == 2 else 0
        return counter

    def get_wasted_stats(self):
        wasted_stats = 0
        for stat in self.total_stats:
            wasted_stats += stat % 10
        return wasted_stats


def get_all_rolls(helmets: list[ArmorPiece], arms: list[ArmorPiece],
                  chests: list[ArmorPiece], legs: list[ArmorPiece]):
    armor_sets = []
    for legs in legs:
        for helmet in helmets:
            for arm in arms:
                for chest in chests:
                    armor_sets.append(ArmorSet(helmet, arm, chest, legs))
    return armor_sets


def get_good_rolls(all_rolls: list[ArmorSet]):
    return sorted([roll for roll in all_rolls if roll.is_good],
                  key=lambda x: x.actual_roll)


def get_armorset_table(roll: ArmorSet):
    table = PrettyTable()
    table.field_names = ["Armor rating", "Total roll", "Actuall roll",
                         "Wasted stats", "Mobility", "Resilience",
                         "Recovery", "Discipline",
                         "Intelect", "Strength"]
    table.add_row([
        roll.rating, roll.total_roll, roll.actual_roll,
        roll.wasted_stats, roll.mobility, roll.resilience,
        roll.recovery, roll.discipline,
        roll.intelect, roll.strength
    ])
    return table.get_string()


def get_armorpiece_table(roll: ArmorSet):
    table = PrettyTable()
    table.field_names = ["Id", "Type", "Mobility",
                         "Resilience", "Recovery", "Discipline",
                         "Intelect", "Strength", "Total roll"]
    table.add_rows([
        [roll.helmet.id, roll.helmet.type, roll.helmet.mobility,
         roll.helmet.resilience, roll.helmet.recovery, roll.helmet.discipline,
         roll.helmet.intelect, roll.helmet.strength, roll.helmet.total_roll],

        [roll.arms.id, roll.arms.type, roll.arms.mobility,
         roll.arms.resilience, roll.arms.recovery, roll.arms.discipline,
         roll.arms.intelect, roll.arms.strength, roll.arms.total_roll],

        [roll.chest.id, roll.chest.type, roll.chest.mobility,
         roll.chest.resilience, roll.chest.recovery, roll.chest.discipline,
         roll.chest.intelect, roll.chest.strength, roll.chest.total_roll],

        [roll.legs.id, roll.legs.type, roll.legs.mobility,
         roll.legs.resilience, roll.legs.recovery, roll.legs.discipline,
         roll.legs.intelect, roll.legs.strength, roll.legs.total_roll],
    ])
    return table.get_string()
