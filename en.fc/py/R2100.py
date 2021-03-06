from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R2100   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2100.x',
        MapIndex            = 100,
        MapDefaultBGM       = "ed60020",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '',                                     # 9
        'Manoria Village',                      # 10
        'Krone Trail',                          # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 100,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10160 ._CH',             # 00
        'ED6_DT09/CH10161 ._CH',             # 01
        'ED6_DT09/CH10450 ._CH',             # 02
        'ED6_DT09/CH10451 ._CH',             # 03
        'ED6_DT09/CH10220 ._CH',             # 04
        'ED6_DT09/CH10221 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT09/CH10160P._CP',             # 00
        'ED6_DT09/CH10161P._CP',             # 01
        'ED6_DT09/CH10450P._CP',             # 02
        'ED6_DT09/CH10451P._CP',             # 03
        'ED6_DT09/CH10220P._CP',             # 04
        'ED6_DT09/CH10221P._CP',             # 05
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -18570,
        Z                   = -2000,
        Y                   = -37710,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 100500,
        Z                   = -2070,
        Y                   = 132300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 26400,
        Z                   = -2050,
        Y                   = 109110,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x16D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 22850,
        Z                   = -2020,
        Y                   = 80880,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x16D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 24710,
        Z                   = -2070,
        Y                   = 44250,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x16D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 16680,
        Z                   = -2060,
        Y                   = 9800,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x16D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 35120,
        TriggerZ            = -1980,
        TriggerY            = 46370,
        TriggerRange        = 1000,
        ActorX              = 35820,
        ActorZ              = -1950,
        ActorY              = 46370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1CE",          # 00, 0
        "Function_1_1ED",          # 01, 1
        "Function_2_21E",          # 02, 2
        "Function_3_234",          # 03, 3
        "Function_4_60B",          # 04, 4
        "Function_5_640",          # 05, 5
        "Function_6_67A",          # 06, 6
    )


    def Function_0_1CE(): pass

    label("Function_0_1CE")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1DA"),
        (SWITCH_DEFAULT, "loc_1EC"),
    )


    label("loc_1DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E9")
    OP_A2(0x408)
    Event(0, 3)

    label("loc_1E9")

    Jump("loc_1EC")

    label("loc_1EC")

    Return()

    # Function_0_1CE end

    def Function_1_1ED(): pass

    label("Function_1_1ED")

    OP_16(0x2, 0xFA0, 0xFFFE7578, 0xFFFEE6C0, 0x3002B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_211")
    OP_6F(0x0, 0)
    Jump("loc_218")

    label("loc_211")

    OP_6F(0x0, 60)

    label("loc_218")

    OP_22(0x1C4, 0x1, 0x64)
    Return()

    # Function_1_1ED end

    def Function_2_21E(): pass

    label("Function_2_21E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_233")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_21E")

    label("loc_233")

    Return()

    # Function_2_21E end

    def Function_3_234(): pass

    label("Function_3_234")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, 86290, -1980, 133350, 270)
    SetChrPos(0x102, 86870, -1900, 132340, 270)
    OP_6D(86290, -1980, 133350, 0)
    OP_6C(45000, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        "#004FWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        "#014FEstelle?\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0x4)
    OP_43(0x102, 0x1, 0x0, 0x5)

    def lambda_2B9():
        OP_6D(46610, -2000, 127240, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2B9)

    def lambda_2D1():
        OP_67(0, 4170, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2D1)

    def lambda_2E9():
        OP_6B(4270, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2E9)

    def lambda_2F9():
        OP_6C(249000, 8000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2F9)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x102, 0x1)
    Sleep(1000)

    ChrTalk(    #2
        0x101,
        (
            "#001FHey, Joshua, check it out!\x02\x03",

            "It's the ocean!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        (
            "#010FYes, I think I would have\x01",
            "figured that out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#501FIt's so blue and sparkly and\x01",
            "just...huge!\x02\x03",

            "And the sound of the waves and\x01",
            "the smell of the tide...\x02\x03",

            "#001FSo this is what it all feels like.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 300)

    ChrTalk(    #5
        0x102,
        (
            "#010FIs this the first time you've\x01",
            "seen the ocean?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #6
        0x101,
        (
            "#2P#000FWell, I can kinda sorta remember seeing\x01",
            "it when I was really young. I was on an\x01",
            "ocean liner with Dad that one time.\x02\x03",

            "This might be the first time\x01",
            "I've seen it up close, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#010FI see...\x02\x03",

            "#019FIt's been a long while for me,\x01",
            "as well.\x02\x03",

            "We got here by walking,\x01",
            "though. No ship this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#2P#001FYep. I feel like we've accomplished\x01",
            "something!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5CF():
        OP_6B(3200, 1800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5CF)

    def lambda_5DF():
        OP_6C(225000, 1800)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5DF)

    def lambda_5EF():
        OP_67(0, 9500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_5EF)
    OP_69(0x0, 0x7D0)
    EventEnd(0x0)
    Return()

    # Function_3_234 end

    def Function_4_60B(): pass

    label("Function_4_60B")

    Sleep(500)
    OP_8E(0xFE, 0x11FF8, 0xFFFFF844, 0x20AD0, 0x1770, 0x0)
    OP_8E(0xFE, 0xCA80, 0xFFFFF7EA, 0x1F4D2, 0x1770, 0x0)
    OP_8C(0xFE, 288, 400)
    Return()

    # Function_4_60B end

    def Function_5_640(): pass

    label("Function_5_640")

    Sleep(500)
    Sleep(500)
    OP_8E(0xFE, 0x11FF8, 0xFFFFF844, 0x20AD0, 0x1770, 0x0)
    OP_8E(0xFE, 0xCBAC, 0xFFFFF830, 0x1F086, 0x1770, 0x0)
    OP_8C(0xFE, 288, 400)
    Return()

    # Function_5_640 end

    def Function_6_67A(): pass

    label("Function_6_67A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x96, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_835")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x97, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75C")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 35820, 500, 46370, 320)
    TurnDirection(0x8, 0x0, 0)

    def lambda_6C9():
        OP_8F(0xFE, 0x8BEC, 0xFFFFFC18, 0xB522, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6C9)

    def lambda_6E4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6E4)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #9
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x171, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_737"),
        (2, "loc_749"),
        (1, "loc_759"),
        (SWITCH_DEFAULT, "loc_75C"),
    )


    label("loc_737")

    OP_A2(0x4B8)
    OP_6F(0x0, 60)
    Sleep(500)
    Jump("loc_75C")

    label("loc_749")

    OP_6F(0x0, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_759")

    OP_B4(0x0)
    Return()

    label("loc_75C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x134, 1)"), scpexpr(EXPR_END)), "loc_7B6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #10
        "\x07\x00Found \x07\x02Lily Necklace\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x4B7)
    Jump("loc_832")

    label("loc_7B6")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #11
        (
            "\x07\x00Found \x07\x02Lily Necklace\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02Lily Necklace\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_832")

    Jump("loc_882")

    label("loc_835")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #12
        "\x07\x05The chest is as empty as your thieving heart.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x82)

    label("loc_882")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_67A end

    SaveToFile()

Try(main)
