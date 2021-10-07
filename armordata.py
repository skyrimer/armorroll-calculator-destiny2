from calculator import ArmorPiece


helmet_list = [
    ArmorPiece(1, "helmet", 8, 11, 20, 8, 9, 22),
    ArmorPiece(2, "helmet", 28, 4, 4, 31, 4, 4),
    ArmorPiece(3, "helmet", 14, 4, 21, 9, 16, 14),
    ArmorPiece(4, "helmet", 23, 4, 10, 15, 14, 10),
    ArmorPiece(5, "helmet", 4, 18, 13, 4, 22, 14),
    ArmorPiece(6, "helmet", 10, 19, 9, 13, 16, 8),
    ArmorPiece(7, "helmet", 17, 4, 16, 10, 16, 12),
    ArmorPiece(8, "helmet", 20, 4, 15, 4, 31, 4),
]
arms_list = [
    ArmorPiece(1, "arms", 4, 4, 31, 18, 18, 4),
    ArmorPiece(2, "arms", 4, 22, 11, 4, 15, 19),
    ArmorPiece(3, "arms", 21, 8, 10, 9, 8, 22),
    ArmorPiece(4, "arms", 11, 4, 21, 22, 8, 9),
    ArmorPiece(5, "arms", 9, 22, 8, 8, 21, 10),
    ArmorPiece(6, "arms", 12, 8, 15, 8, 18, 14),
]
chest_list = [
    ArmorPiece(1, "chest", 4, 8, 25, 4, 10, 25),
    ArmorPiece(2, "chest", 15, 4, 19, 4, 19, 15),
    ArmorPiece(3, "chest", 11, 8, 20, 9, 8, 22),
    ArmorPiece(4, "chest", 17, 4, 17, 14, 15, 8),
    ArmorPiece(5, "chest", 9, 20, 9, 11, 14, 14),
    ArmorPiece(6, "chest", 10, 19, 8, 9, 4, 25),
    ArmorPiece(7, "chest", 22, 12, 4, 17, 10, 9),
    ArmorPiece(8, "chest", 4, 4, 30, 4, 27, 4),
    ArmorPiece(9, "chest", 8, 27, 4, 9, 11, 16),
]
legs_list = [
    ArmorPiece(1, "legs", 4, 8, 26, 9, 18, 11),
    ArmorPiece(2, "legs", 16, 18, 4, 28, 4, 6),
    ArmorPiece(3, "legs", 12, 4, 24, 12, 8, 16),
    ArmorPiece(4, "legs", 4, 8, 26, 18, 11, 10),
    ArmorPiece(5, "legs", 4, 24, 12, 14, 11, 14),
    ArmorPiece(6, "legs", 8, 11, 18, 8, 27, 4),
    ArmorPiece(7, "legs", 14, 4, 21, 8, 4, 25),
    ArmorPiece(8, "legs", 8, 11, 20, 8, 12, 18),
    ArmorPiece(9, "legs", 14, 21, 4, 8, 12, 16),
]
exotics = {
    "helmet": [
        ArmorPiece(1, "Crown of Tempests", 5, 8, 26, 18, 8, 9),
        ArmorPiece(2, "Crown of Tempests", 18, 16, 5, 18, 9, 9),
        ArmorPiece(3, "Eye of Another World", 4, 19, 14, 10, 4, 21),
        ArmorPiece(4, "Eye of Another World", 14, 22, 6, 24, 8, 8),
        ArmorPiece(5, "Nezarec's Sin", 4, 10, 27, 10, 12, 15),
        ArmorPiece(6, "The Stag", 19, 12, 10, 12, 13, 10),
        ArmorPiece(7, "The Stag", 19, 8, 10, 16, 12, 9),
        ArmorPiece(8, "Nezarec's Sin", 12, 5, 25, 14, 15, 9),
        ArmorPiece(9, "Eye of Another World", 9, 4, 24, 19, 4, 13),
        ArmorPiece(10, "The Stag", 8, 11, 20, 16, 16, 4),
        ArmorPiece(11, "Eye of Another World", 4, 16, 18, 13, 4, 20),
        ArmorPiece(12, "The Stag", 16, 11, 11, 21, 4, 12),
        ArmorPiece(13, "Nexerec's Sin", 4, 23, 12, 9, 17, 9),
        ArmorPiece(14, "Eye of Another World", 10, 4, 25, 4, 22, 13),
    ],
    "arms": [
        ArmorPiece(1, "Karnstein Armlets", 22, 5, 13, 16, 4, 18),
        ArmorPiece(2, "Karnstein Armlets", 15, 9, 15, 20, 14, 4),
        ArmorPiece(3, "Ophidian Aspect", 5, 12, 19, 8, 17, 12),
        ArmorPiece(4, "Karnstein Armlets", 4, 20, 16, 12, 14, 10),
        ArmorPiece(5, "Ophidian Aspect", 5, 16, 17, 12, 8, 16),
        ArmorPiece(6, "Ophidian Aspect", 16, 18, 5, 14, 12, 14),
        ArmorPiece(7, "Karnstein Armlets", 12, 5, 21, 4, 20, 13),
        ArmorPiece(8, "Karnstein Armlets", 10, 22, 9, 17, 4, 15),
        ArmorPiece(9, "Karnstein Armlets", 10, 17, 11, 8, 19, 8),
        ArmorPiece(10, "Karnstein Armlets", 11, 19, 10, 20, 4, 11),
        ArmorPiece(11, "Ophidian Aspect", 9, 12, 19, 4, 9, 23),
        ArmorPiece(12, "Sunbracers", 17, 12, 11, 9, 16, 11),
        ArmorPiece(13, "Sunbracers", 5, 12, 22, 9, 11, 16),

    ],
    "chest": [
        ArmorPiece(1, "Sanguine Alchemy", 14, 10, 16, 25, 4, 10),
    ],
    "legs": [
        ArmorPiece(1, "Transversive Steps", 5, 17, 16, 16, 12, 9),
        ArmorPiece(2, "Transversive Steps", 13, 14, 13, 10, 18, 11),
        ArmorPiece(3, "Transversive Steps", 14, 20, 5, 12, 16, 9),
        ArmorPiece(4, "Transversive Steps", 19, 10, 11, 10, 11, 17),
        ArmorPiece(5, "Transversive Steps", 5, 8, 27, 8, 9, 18)
    ]
}
