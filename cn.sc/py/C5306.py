from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5306   ._SN',
        MapName             = 'Other',
        Location            = 'C5306.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60064",
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
        '升降梯',                               # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT29/CH12010 ._CH',             # 00
        'ED6_DT29/CH12010 ._CH',             # 01
        'ED6_DT29/CH12080 ._CH',             # 02
        'ED6_DT29/CH12081 ._CH',             # 03
        'ED6_DT29/CH12050 ._CH',             # 04
        'ED6_DT29/CH12051 ._CH',             # 05
        'ED6_DT29/CH12140 ._CH',             # 06
        'ED6_DT29/CH12141 ._CH',             # 07
        'ED6_DT29/CH12420 ._CH',             # 08
        'ED6_DT29/CH12421 ._CH',             # 09
        'ED6_DT29/CH12300 ._CH',             # 0A
        'ED6_DT29/CH12301 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH12010P._CP',             # 00
        'ED6_DT29/CH12010P._CP',             # 01
        'ED6_DT29/CH12080P._CP',             # 02
        'ED6_DT29/CH12081P._CP',             # 03
        'ED6_DT29/CH12050P._CP',             # 04
        'ED6_DT29/CH12051P._CP',             # 05
        'ED6_DT29/CH12140P._CP',             # 06
        'ED6_DT29/CH12141P._CP',             # 07
        'ED6_DT29/CH12420P._CP',             # 08
        'ED6_DT29/CH12421P._CP',             # 09
        'ED6_DT29/CH12300P._CP',             # 0A
        'ED6_DT29/CH12301P._CP',             # 0B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 91640,
        Z                   = 0,
        Y                   = -72910,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -76800,
        Z                   = 0,
        Y                   = -90840,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -94600,
        Z                   = 0,
        Y                   = -73000,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x529,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -87930,
        Z                   = 0,
        Y                   = 96320,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 100070,
        Y                   = -2000,
        Z                   = 9020,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = 5140,
        Y                   = -2000,
        Z                   = 110030,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = -10520,
        TriggerZ            = 0,
        TriggerY            = -90700,
        TriggerRange        = 1000,
        ActorX              = -10490,
        ActorZ              = 0,
        ActorY              = -90090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9460,
        TriggerZ            = 0,
        TriggerY            = -90710,
        TriggerRange        = 1000,
        ActorX              = 9490,
        ActorZ              = 0,
        ActorY              = -90050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9550,
        TriggerZ            = 0,
        TriggerY            = -95300,
        TriggerRange        = 1000,
        ActorX              = 9520,
        ActorZ              = 0,
        ActorY              = -95870,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -10520,
        TriggerZ            = 0,
        TriggerY            = -95300,
        TriggerRange        = 1000,
        ActorX              = -10470,
        ActorZ              = 0,
        ActorY              = -96000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_26A",          # 00, 0
        "Function_1_2EC",          # 01, 1
        "Function_2_425",          # 02, 2
        "Function_3_53C",          # 03, 3
        "Function_4_653",          # 04, 4
        "Function_5_76A",          # 05, 5
        "Function_6_881",          # 06, 6
        "Function_7_998",          # 07, 7
        "Function_8_AC5",          # 08, 8
        "Function_9_C61",          # 09, 9
        "Function_10_E50",         # 0A, 10
        "Function_11_109C",        # 0B, 11
        "Function_12_1198",        # 0C, 12
    )


    def Function_0_26A(): pass

    label("Function_0_26A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_27B")
    OP_A3(0x10F0)
    Event(0, 6)
    Jump("loc_2A4")

    label("loc_27B")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_28F"),
        (122, "loc_296"),
        (111, "loc_29D"),
        (SWITCH_DEFAULT, "loc_2A4"),
    )


    label("loc_28F")

    Event(0, 8)
    Jump("loc_2A4")

    label("loc_296")

    Event(0, 10)
    Jump("loc_2A4")

    label("loc_29D")

    Event(0, 12)
    Jump("loc_2A4")

    label("loc_2A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 3)), scpexpr(EXPR_END)), "loc_2EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB")
    OP_A2(0x0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_2EB")

    Return()

    # Function_0_26A end

    def Function_1_2EC(): pass

    label("Function_1_2EC")

    OP_51(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31F")
    OP_6F(0x3, 0)
    Jump("loc_326")

    label("loc_31F")

    OP_6F(0x3, 60)

    label("loc_326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_338")
    OP_6F(0x4, 0)
    Jump("loc_33F")

    label("loc_338")

    OP_6F(0x4, 60)

    label("loc_33F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_351")
    OP_6F(0x5, 0)
    Jump("loc_358")

    label("loc_351")

    OP_6F(0x5, 60)

    label("loc_358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36A")
    OP_6F(0x6, 0)
    Jump("loc_371")

    label("loc_36A")

    OP_6F(0x6, 60)

    label("loc_371")

    OP_10(0x0, 0x0)
    OP_10(0x16, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_396")
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 0)
    OP_10(0xB, 0x0)
    Jump("loc_3E7")

    label("loc_396")

    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 600)
    OP_10(0xB, 0x1)
    OP_82(0x83, 0x0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_1B(0xB, 0x0, 0xB)

    label("loc_3E7")

    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_6F(0x2, 0)
    OP_A1(0x8, 0x2)
    SetChrPos(0x8, 5140, -1750, 110030, 90)
    OP_22(0x140, 0x0, 0x64)
    Return()

    # Function_1_2EC end

    def Function_2_425(): pass

    label("Function_2_425")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x167, 1)"), scpexpr(EXPR_END)), "loc_494")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x67\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x238B)
    Jump("loc_4FA")

    label("loc_494")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x67\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x67\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_4FA")

    Jump("loc_52E")

    label("loc_4FD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_52E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_425 end

    def Function_3_53C(): pass

    label("Function_3_53C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_614")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_5AB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x06\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x238D)
    Jump("loc_611")

    label("loc_5AB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x06\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x06\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_611")

    Jump("loc_645")

    label("loc_614")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_645")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_53C end

    def Function_4_653(): pass

    label("Function_4_653")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_6C2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x238E)
    Jump("loc_728")

    label("loc_6C2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF7\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_728")

    Jump("loc_75C")

    label("loc_72B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_75C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_653 end

    def Function_5_76A(): pass

    label("Function_5_76A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_842")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_7D9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x238F)
    Jump("loc_83F")

    label("loc_7D9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_83F")

    Jump("loc_873")

    label("loc_842")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_873")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_76A end

    def Function_6_881(): pass

    label("Function_6_881")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-97890, 0, 32369, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(345000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1, 0)
    OP_70(0x1, 0x258)
    Sleep(1500)
    OP_22(0xE1, 0x0, 0x64)
    Sleep(3000)
    OP_22(0x70, 0x0, 0x64)
    OP_73(0x1)

    def lambda_909():
        OP_6D(-88930, 1090, 4140, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_909)

    def lambda_921():
        OP_67(0, 9500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_921)
    OP_6C(315000, 5000)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C5311   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_881 end

    def Function_7_998(): pass

    label("Function_7_998")

    EventBegin(0x0)
    OP_A1(0x8, 0x0)
    SetChrPos(0x8, 100070, -1750, 9020, 0)
    OP_48()
    Fade(1000)
    OP_6D(100070, 0, 9020, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 100000, 0, 10000, 0)
    OP_89(0x1, 101000, 0, 9000, 90)
    OP_89(0x2, 99000, 0, 9000, 270)
    OP_89(0x3, 100000, 0, 8000, 180)
    OP_0D()
    Sleep(300)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_A4D():
        OP_67(0, 6500, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A4D)

    def lambda_A65():
        OP_6B(3700, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A65)

    def lambda_A75():
        OP_91(0xFE, 0x0, 0xFFFFD8F0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A75)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A3(0x228C)
    OP_A3(0x228D)
    OP_A3(0x228E)
    OP_A3(0x228F)
    OP_A3(0x2290)
    OP_A3(0x2291)
    OP_A3(0x2292)
    OP_A2(0x2293)
    OP_A3(0x2294)
    OP_A3(0x2295)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5316   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_998 end

    def Function_8_AC5(): pass

    label("Function_8_AC5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A1(0x8, 0x0)
    SetChrPos(0x8, 100070, -11750, 9020, 0)
    OP_48()
    OP_6D(100070, 0, 9020, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 100000, 0, 10000, 0)
    OP_89(0x1, 101000, 0, 9000, 90)
    OP_89(0x2, 99000, 0, 9000, 270)
    OP_89(0x3, 100000, 0, 8000, 180)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_B74():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B74)
    FadeToBright(1000, 0)
    SetPlaceName(0x120)

    def lambda_B90():
        OP_91(0xFE, 0x0, 0x2710, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B90)
    Sleep(2200)
    OP_24(0xEB, 0x5A)
    Sleep(50)
    OP_24(0xEB, 0x50)
    Sleep(50)
    OP_24(0xEB, 0x46)
    Sleep(50)
    OP_24(0xEB, 0x3C)
    Sleep(50)
    OP_24(0xEB, 0x32)
    Sleep(50)
    OP_24(0xEB, 0x28)
    Sleep(50)
    OP_24(0xEB, 0x1E)
    Sleep(50)
    OP_24(0xEB, 0x14)
    Sleep(50)
    OP_24(0xEB, 0xA)
    Sleep(50)
    OP_23(0xEB)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x8, 0x1)
    Sleep(500)
    Fade(1000)
    SetChrPos(0x0, 100080, 0, 4460, 180)
    SetChrPos(0x1, 100080, 0, 4460, 180)
    SetChrPos(0x2, 100080, 0, 4460, 180)
    SetChrPos(0x3, 100080, 0, 4460, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_8_AC5 end

    def Function_9_C61(): pass

    label("Function_9_C61")

    EventBegin(0x0)
    OP_A1(0x8, 0x2)
    SetChrPos(0x8, 5140, -1750, 110030, 90)
    OP_48()
    Fade(1000)
    OP_6D(5140, 0, 110030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 5000, 0, 111000, 0)
    OP_89(0x1, 6000, 0, 110000, 90)
    OP_89(0x2, 4000, 0, 110000, 270)
    OP_89(0x3, 5000, 0, 109000, 180)
    OP_0D()
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x1, 0x64)

    def lambda_D11():
        OP_8F(0xFE, 0x1414, 0xFDE8, 0x1ADCE, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D11)
    Sleep(500)

    def lambda_D31():
        OP_6D(5140, 35000, 110030, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D31)

    def lambda_D49():
        OP_67(0, 14000, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D49)

    def lambda_D61():
        OP_6C(295000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D61)
    Sleep(500)

    def lambda_D76():
        OP_8F(0xFE, 0x1414, 0xFDE8, 0x1ADCE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D76)
    Sleep(500)

    def lambda_D96():
        OP_8F(0xFE, 0x1414, 0xFDE8, 0x1ADCE, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D96)
    Sleep(400)

    def lambda_DB6():
        OP_8F(0xFE, 0x1414, 0xFDE8, 0x1ADCE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DB6)
    Sleep(200)

    def lambda_DD6():
        OP_8F(0xFE, 0x1414, 0xFDE8, 0x1ADCE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DD6)
    Sleep(100)

    def lambda_DF6():
        OP_8F(0xFE, 0x1414, 0xFDE8, 0x1ADCE, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DF6)
    Sleep(2000)
    Sleep(2000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A3(0x228C)
    OP_A3(0x228D)
    OP_A3(0x228E)
    OP_A3(0x228F)
    OP_A3(0x2290)
    OP_A3(0x2291)
    OP_A3(0x2292)
    OP_A3(0x2293)
    OP_A2(0x2294)
    OP_A3(0x2295)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5316   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_C61 end

    def Function_10_E50(): pass

    label("Function_10_E50")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A1(0x8, 0x2)
    SetChrPos(0x8, 5140, 66000, 110030, 90)
    OP_48()
    OP_6D(5140, 48000, 110030, 0)
    OP_67(0, 16000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(295000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 5000, 67000, 111000, 0)
    OP_89(0x1, 6000, 67000, 110000, 90)
    OP_89(0x2, 4000, 67000, 110000, 270)
    OP_89(0x3, 5000, 67000, 109000, 180)
    OP_22(0xEB, 0x1, 0x64)

    def lambda_EFF():
        OP_6D(5140, 0, 110030, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EFF)

    def lambda_F17():
        OP_67(0, 9500, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F17)

    def lambda_F2F():
        OP_6C(315000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_F2F)
    FadeToBright(1000, 0)
    SetPlaceName(0x120)

    def lambda_F4B():
        OP_8F(0xFE, 0x1414, 0xFFFFF92A, 0x1ADCE, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F4B)
    Sleep(7800)

    def lambda_F6B():
        OP_8F(0xFE, 0x1414, 0xFFFFF92A, 0x1ADCE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F6B)
    Sleep(700)

    def lambda_F8B():
        OP_8F(0xFE, 0x1414, 0xFFFFF92A, 0x1ADCE, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F8B)
    Sleep(600)

    def lambda_FAB():
        OP_8F(0xFE, 0x1414, 0xFFFFF92A, 0x1ADCE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FAB)
    Sleep(100)

    def lambda_FCB():
        OP_8F(0xFE, 0x1414, 0xFFFFF92A, 0x1ADCE, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FCB)
    Sleep(500)
    OP_24(0xEB, 0x5A)
    Sleep(50)
    OP_24(0xEB, 0x50)
    Sleep(50)
    OP_24(0xEB, 0x46)
    Sleep(50)
    OP_24(0xEB, 0x3C)
    Sleep(50)
    OP_24(0xEB, 0x32)
    Sleep(50)
    OP_24(0xEB, 0x28)
    Sleep(50)
    OP_24(0xEB, 0x1E)
    Sleep(50)
    OP_24(0xEB, 0x14)
    Sleep(50)
    OP_24(0xEB, 0xA)
    Sleep(50)
    OP_23(0xEB)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x8, 0x1)
    Sleep(500)
    Fade(1000)
    SetChrPos(0x0, 160, 0, 109620, 270)
    SetChrPos(0x1, 160, 0, 109620, 270)
    SetChrPos(0x2, 160, 0, 109620, 270)
    SetChrPos(0x3, 160, 0, 109620, 270)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_10_E50 end

    def Function_11_109C(): pass

    label("Function_11_109C")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-89000, 1050, 4000, 0)
    SetChrPos(0x101, -88500, 1050, 4500, 90)
    SetChrPos(0x102, -88500, 1050, 3500, 90)
    SetChrPos(0xF8, -89500, 1050, 4500, 90)
    SetChrPos(0xF9, -89500, 1050, 3500, 90)
    OP_0D()
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1147():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1147)

    def lambda_1159():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1159)

    def lambda_116B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_116B)

    def lambda_117D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_117D)
    Sleep(2000)
    NewScene("ED6_DT21/C5300   ._SN", 122, 0, 0)
    IdleLoop()
    Return()

    # Function_11_109C end

    def Function_12_1198(): pass

    label("Function_12_1198")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-89000, 1050, 4000, 0)
    SetChrPos(0x101, -89500, 1050, 3500, 270)
    SetChrPos(0x102, -89500, 1050, 4500, 270)
    SetChrPos(0xF8, -88500, 1050, 3500, 270)
    SetChrPos(0xF9, -88500, 1050, 4500, 270)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1273():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1273)

    def lambda_1285():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1285)

    def lambda_1297():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1297)

    def lambda_12A9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_12A9)
    Sleep(2500)
    Fade(500)
    OP_6D(-92500, 0, 4000, 0)
    SetChrPos(0x0, -92500, 0, 4000, 270)
    SetChrPos(0x1, -92500, 0, 4000, 270)
    SetChrPos(0x2, -92500, 0, 4000, 270)
    SetChrPos(0x3, -92500, 0, 4000, 270)
    EventEnd(0x0)
    Return()

    # Function_12_1198 end

    SaveToFile()

Try(main)
