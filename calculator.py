from dataclasses import dataclass, field
from rich.table import Table


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
        self.strength = self.get_total_strength() + 22
        self.total_stats = self.get_total_stats()
        self.total_roll = sum(self.total_stats)
        self.wasted_stats = self.get_wasted_stats()
        self.actual_roll = self.total_roll - self.wasted_stats
        self.is_good = self.actual_roll >= 340

    def get_total_mobility(self) -> int:
        return self.helmet.mobility + self.arms.mobility + \
            self.chest.mobility + self.legs.mobility

    def get_total_resilience(self) -> str:
        return self.helmet.resilience + self.arms.resilience + \
            self.chest.resilience + self.legs.resilience

    def get_total_recovery(self) -> str:
        return self.helmet.recovery + self.arms.recovery + \
            self.chest.recovery + self.legs.recovery

    def get_total_discipline(self) -> str:
        return self.helmet.discipline + self.arms.discipline + \
            self.chest.discipline + self.legs.discipline

    def get_total_intelect(self) -> str:
        return self.helmet.intelect + self.arms.intelect + \
            self.chest.intelect + self.legs.intelect

    def get_total_strength(self) -> str:
        return self.helmet.strength + self.arms.strength + \
            self.chest.strength + self.legs.strength

    def get_total_stats(self) -> str:
        return [self.mobility, self.resilience, self.recovery, self.discipline, self.intelect, self.strength]

    def get_wasted_stats(self) -> str:
        wasted_stats = 0
        for stat in self.total_stats:
            wasted_stats += stat % 10
        return wasted_stats


def get_all_rolls(helmets: list[ArmorPiece], arms: list[ArmorPiece],
                  chests: list[ArmorPiece], legs: list[ArmorPiece]) -> list[ArmorSet]:
    armor_sets = []
    for legs in legs:
        for helmet in helmets:
            for arm in arms:
                for chest in chests:
                    armor_sets.append(ArmorSet(helmet, arm, chest, legs))
    return armor_sets


def get_good_rolls(all_rolls: list[ArmorSet]) -> list[ArmorSet]:
    return sorted(sorted([roll for roll in all_rolls if roll.is_good],
                         key=lambda x: x.actual_roll), key=lambda x: x.recovery)


def get_table(title: str, columns: list[str], rows: list) -> Table:
    table = Table(title=title)
    for column in columns:
        table.add_column(column[0], style=column[1], justify="center")
    for row in rows:
        table.add_row(*map(str, row))
    return table


def get_armorset_table(roll: ArmorSet) -> Table:
    columns = [["Total roll", "cyan"],
               ["Actuall roll", "cyan"], ["Wasted stats", "cyan"],
               ["Mobility", "magenta"], ["Resilience", "magenta"],
               ["Recovery", "magenta"], ["Discipline", "magenta"],
               ["Intelect", "magenta"], ["Strength", "magenta"]]
    rows = [[roll.total_roll, roll.actual_roll,
            roll.wasted_stats, roll.mobility, roll.resilience,
            roll.recovery, roll.discipline,
            roll.intelect, roll.strength]]
    return get_table("General armor roll", columns, rows)


def get_armorpiece_table(roll: ArmorSet) -> Table:
    columns = [["Id", "green"], ["Type", "cyan"],
               ["Mobility", "magenta"], ["Resilience", "magenta"],
               ["Recovery", "magenta"], ["Discipline", "magenta"],
               ["Intelect", "magenta"], ["Strength", "magenta"],
               ['Totall Roll', "green"]]
    rows = []
    for gear in [roll.helmet, roll.arms, roll.chest, roll.legs]:
        rows.append([gear.id, gear.type, gear.mobility,
                    gear.resilience, gear.recovery, gear.discipline,
                    gear.intelect, gear.strength, gear.total_roll])
    return get_table("Each gear roll", columns, rows)
