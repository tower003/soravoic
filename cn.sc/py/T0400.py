from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0400   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0400.x',
        MapIndex            = 13,
        MapDefaultBGM       = "ed60015",
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
        '毒雾使者',                             # 9
        '毒雾使者',                             # 10
        '毒雾使者',                             # 11
        '缇欧',                                 # 12
        '维鲁',                                 # 13
        '查儿',                                 # 14
        '弗兰兹',                               # 15
        '牛',                                   # 16
        '牛',                                   # 17
        '鸡',                                   # 18
        '鸡',                                   # 19
        '鸡',                                   # 20
        '鸡',                                   # 21
        '王国军士兵',                           # 22
        '王国军士兵',                           # 23
        '米尔西街道方向',                       # 24
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
        'ED6_DT29/CH12890 ._CH',             # 00
        'ED6_DT27/CH04000 ._CH',             # 01
        'ED6_DT27/CH04001 ._CH',             # 02
        'ED6_DT07/CH00160 ._CH',             # 03
        'ED6_DT07/CH00161 ._CH',             # 04
        'ED6_DT07/CH00120 ._CH',             # 05
        'ED6_DT07/CH00121 ._CH',             # 06
        'ED6_DT07/CH00140 ._CH',             # 07
        'ED6_DT07/CH00141 ._CH',             # 08
        'ED6_DT29/CH12891 ._CH',             # 09
        'ED6_DT07/CH02480 ._CH',             # 0A
        'ED6_DT07/CH01060 ._CH',             # 0B
        'ED6_DT07/CH01070 ._CH',             # 0C
        'ED6_DT07/CH01020 ._CH',             # 0D
        'ED6_DT07/CH01710 ._CH',             # 0E
        'ED6_DT07/CH01720 ._CH',             # 0F
        'ED6_DT07/CH01640 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT29/CH12890P._CP',             # 00
        'ED6_DT27/CH04000P._CP',             # 01
        'ED6_DT27/CH04001P._CP',             # 02
        'ED6_DT07/CH00160P._CP',             # 03
        'ED6_DT07/CH00161P._CP',             # 04
        'ED6_DT07/CH00120P._CP',             # 05
        'ED6_DT07/CH00121P._CP',             # 06
        'ED6_DT07/CH00140P._CP',             # 07
        'ED6_DT07/CH00141P._CP',             # 08
        'ED6_DT29/CH12891P._CP',             # 09
        'ED6_DT07/CH02480P._CP',             # 0A
        'ED6_DT07/CH01060P._CP',             # 0B
        'ED6_DT07/CH01070P._CP',             # 0C
        'ED6_DT07/CH01020P._CP',             # 0D
        'ED6_DT07/CH01710P._CP',             # 0E
        'ED6_DT07/CH01720P._CP',             # 0F
        'ED6_DT07/CH01640P._CP',             # 10
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 40470,
        Z                   = 0,
        Y                   = 16320,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 21900,
        Z                   = 0,
        Y                   = 25300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 25100,
        Z                   = 0,
        Y                   = 23000,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 27590,
        Z                   = -60,
        Y                   = 34960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 39010,
        Z                   = 600,
        Y                   = 22850,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 48160,
        Z                   = 460,
        Y                   = 18800,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 0,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 38780,
        Z                   = 0,
        Y                   = 19310,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 51470,
        Z                   = 0,
        Y                   = 20950,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 51470,
        Z                   = 0,
        Y                   = 20950,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 25880,
        Z                   = 390,
        Y                   = 53570,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 23960,
        Z                   = 140,
        Y                   = 43890,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 23910,
        Z                   = 30,
        Y                   = 66820,
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


    DeclEvent(
        X                   = 28330,
        Y                   = -1000,
        Z                   = 47700,
        Range               = 30790,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xDF66,
        Unknown_18          = 0x0,
        Unknown_1C          = 34,
    )

    DeclEvent(
        X                   = 20560,
        Y                   = -1000,
        Z                   = 57690,
        Range               = 26700,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xD8CC,
        Unknown_18          = 0x0,
        Unknown_1C          = 35,
    )


    DeclActor(
        TriggerX            = 16370,
        TriggerZ            = 570,
        TriggerY            = 23100,
        TriggerRange        = 800,
        ActorX              = 16370,
        ActorZ              = 1570,
        ActorY              = 23100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 36,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_396",          # 00, 0
        "Function_1_446",          # 01, 1
        "Function_2_4E3",          # 02, 2
        "Function_3_660",          # 03, 3
        "Function_4_684",          # 04, 4
        "Function_5_6A8",          # 05, 5
        "Function_6_7F5",          # 06, 6
        "Function_7_90C",          # 07, 7
        "Function_8_1598",         # 08, 8
        "Function_9_17A6",         # 09, 9
        "Function_10_1992",        # 0A, 10
        "Function_11_1BAE",        # 0B, 11
        "Function_12_1C32",        # 0C, 12
        "Function_13_1C58",        # 0D, 13
        "Function_14_1C5E",        # 0E, 14
        "Function_15_1DD5",        # 0F, 15
        "Function_16_1ECE",        # 10, 16
        "Function_17_27B5",        # 11, 17
        "Function_18_27FA",        # 12, 18
        "Function_19_283F",        # 13, 19
        "Function_20_2878",        # 14, 20
        "Function_21_28B1",        # 15, 21
        "Function_22_28F5",        # 16, 22
        "Function_23_2939",        # 17, 23
        "Function_24_297D",        # 18, 24
        "Function_25_29C1",        # 19, 25
        "Function_26_2BA1",        # 1A, 26
        "Function_27_2BBD",        # 1B, 27
        "Function_28_2BD9",        # 1C, 28
        "Function_29_2BF5",        # 1D, 29
        "Function_30_2C11",        # 1E, 30
        "Function_31_2C42",        # 1F, 31
        "Function_32_2C67",        # 20, 32
        "Function_33_2C8C",        # 21, 33
        "Function_34_2CB1",        # 22, 34
        "Function_35_2DE2",        # 23, 35
        "Function_36_2F1E",        # 24, 36
    )


    def Function_0_396(): pass

    label("Function_0_396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3C5")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0xB, 29090, 0, 13250, 180)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_430")

    label("loc_3C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_3E5")
    SetChrPos(0xB, 28990, 0, 13230, 180)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_430")

    label("loc_3E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_41C")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_430")

    label("loc_41C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_430")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_430")
    SetChrFlags(0xB, 0x10)

    label("loc_430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_445")
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_445")

    Return()

    # Function_0_396 end

    def Function_1_446(): pass

    label("Function_1_446")

    OP_16(0x2, 0xFA0, 0xFFFE8900, 0xFFFE8900, 0x230004)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_46D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_47F")
    OP_10(0x4, 0x0)
    OP_10(0x5, 0x1)

    label("loc_47F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_497")
    OP_72(0x0, 0x10)
    OP_65(0x0, 0x1)
    Jump("loc_49B")

    label("loc_497")

    OP_64(0x0, 0x1)

    label("loc_49B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_4A5")
    Jump("loc_4C1")

    label("loc_4A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_4C1")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)

    label("loc_4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D0")
    OP_A2(0x1888)

    label("loc_4D0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E2")
    OP_C4(0x0, 0x4)

    label("loc_4E2")

    Return()

    # Function_1_446 end

    def Function_2_4E3(): pass

    label("Function_2_4E3")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_508")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_64A")

    label("loc_508")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_521")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_64A")

    label("loc_521")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53A")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_64A")

    label("loc_53A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_553")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_64A")

    label("loc_553")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_64A")

    label("loc_56C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_585")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_64A")

    label("loc_585")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_64A")

    label("loc_59E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B7")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_64A")

    label("loc_5B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D0")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_64A")

    label("loc_5D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E9")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_64A")

    label("loc_5E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_602")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_64A")

    label("loc_602")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_64A")

    label("loc_61B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_634")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_64A")

    label("loc_634")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64A")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_64A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_65F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_64A")

    label("loc_65F")

    Return()

    # Function_2_4E3 end

    def Function_3_660(): pass

    label("Function_3_660")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_683")
    OP_8D(0xFE, 19800, 21600, 24000, 30300, 3000)
    Jump("Function_3_660")

    label("loc_683")

    Return()

    # Function_3_660 end

    def Function_4_684(): pass

    label("Function_4_684")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A7")
    OP_8D(0xFE, 19800, 21600, 28200, 24800, 3000)
    Jump("Function_4_684")

    label("loc_6A7")

    Return()

    # Function_4_684 end

    def Function_5_6A8(): pass

    label("Function_5_6A8")

    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, 28710, 33610, 41830, 44000, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7F4")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B9")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x7026), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0x834A), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0xA366), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0xABE0), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78E")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_77B():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77B)
    Jump("loc_7B1")

    label("loc_78E")


    def lambda_794():
        OP_8D(0xFE, 28710, 33610, 41830, 44000, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_794)
    Sleep(200)

    label("loc_7B1")

    Sleep(30)
    Jump("loc_7F1")

    label("loc_7B9")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F1")
    OP_44(0xFE, 0x2)

    def lambda_7D9():
        OP_8D(0xFE, 28710, 33610, 41830, 44000, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7D9)

    label("loc_7F1")

    Jump("loc_6D1")

    label("loc_7F4")

    Return()

    # Function_5_6A8 end

    def Function_6_7F5(): pass

    label("Function_6_7F5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_90B")
    OP_8E(0xFE, 0x5DE8, 0x0, 0x9B78, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4CA4, 0x0, 0x9AE2, 0x7D0, 0x0)
    Sleep(2000)
    OP_8E(0xFE, 0x5DE8, 0x0, 0x9B78, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5FAA, 0x0, 0x77CE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x858E, 0xBE, 0x79CC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(2000)
    OP_8E(0xFE, 0x8516, 0x0, 0x489E, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    OP_8E(0xFE, 0x7210, 0x0, 0x484E, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8E(0xFE, 0x7166, 0x12C, 0x56AE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5D8E, 0x0, 0x5AF0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5D0C, 0x3C, 0xD32C, 0x7D0, 0x0)
    Sleep(2000)
    OP_8E(0xFE, 0x5D98, 0x8C, 0xAB72, 0x7D0, 0x0)
    Jump("Function_6_7F5")

    label("loc_90B")

    Return()

    # Function_6_7F5 end

    def Function_7_90C(): pass

    label("Function_7_90C")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_EBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x415, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0E")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #0
        0x101,
        "#1001F呀哈——缇欧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        "#1040F啊，好久不见了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "艾丝蒂尔？\x01",
            "还有约修亚！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1000F嘿嘿，久等了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        "#1040F让缇欧担心了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "哪里，没关系的。\x01",
            "事情经过我也听说了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "最担心你的\x01",
            "还是艾丝蒂尔啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "为了你她可是大哭了好几次，\x01",
            "让少女流泪可是很严重的罪过哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1008F别、别说啦缇欧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#1054F呵呵……\x01",
            "我已经深深反省过了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #10
        0xFE,
        (
            "今后一定会用更多的时间\x01",
            "来弥补自己的过失。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B14")

    ChrTalk(    #11
        0xFE,
        "……对了，你们…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "和雪拉姐在一起行动，\x01",
            "难道今天又有工作了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B41")

    label("loc_B14")


    ChrTalk(    #13
        0xFE,
        (
            "……对了，你们，\x01",
            "难道今天又有工作了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_END)), "loc_BD8")

    ChrTalk(    #14
        0x101,
        (
            "#1006F嗯，正在洛连特的周边\x01",
            "地区进行巡视。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BAE")

    ChrTalk(    #15
        0x103,
        (
            "#020F顺便掌握一下\x01",
            "这一带的情况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD5")

    label("loc_BAE")


    ChrTalk(    #16
        0x102,
        (
            "#1040F顺便掌握一下\x01",
            "这一带的情况。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD5")

    Jump("loc_C4C")

    label("loc_BD8")


    ChrTalk(    #17
        0x101,
        (
            "#1006F嗯，接下来\x01",
            "要去洛连特。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C2C")

    ChrTalk(    #18
        0x103,
        (
            "#020F有些东西要\x01",
            "送到协会。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C4C")

    label("loc_C2C")


    ChrTalk(    #19
        0x102,
        "#1040F有东西要送到协会去。\x02",
    )

    CloseMessageWindow()

    label("loc_C4C")


    ChrTalk(    #20
        0xFE,
        (
            "是吗……\x01",
            "游击士的工作果然很辛苦啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "不过，难得２个人一起\x01",
            "回到洛连特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "工作结束以后\x01",
            "请一定再来玩啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        "#1040F嗯！一定！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1006F现在的状况比较不稳定，\x01",
            "缇欧也要加油啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20A9)
    Jump("loc_EB7")

    label("loc_D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_D9D")

    ChrTalk(    #25
        0xFE,
        (
            "听说连洛连特的导力器\x01",
            "也全部瘫痪了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "我们水泵和温室现在都无法使用了，\x01",
            "真是让人头疼呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "呼～好久没这样徒手\x01",
            "拎水桶了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB7")

    label("loc_D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E5B")

    ChrTalk(    #28
        0xFE,
        (
            "还有警备艇的迫降\x01",
            "也让人很吃惊啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "虽然士兵们说过，\x01",
            "已经提出救援请求了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "不过仔细想想，\x01",
            "救援部队大概也做不了什么吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "嗯…他们的撤退也可能\x01",
            "只是时间问题吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_EB7")

    label("loc_E5B")


    ChrTalk(    #32
        0xFE,
        (
            "街道中那警备艇的\x01",
            "迫降让我吃了一惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "真是的，世上总是有\x01",
            "让人意想不到的事情发生啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB7")

    Jump("loc_1594")

    label("loc_EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_11DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34C, 5)), scpexpr(EXPR_END)), "loc_F32")

    ChrTalk(    #34
        0xFE,
        (
            "真是要感谢\x01",
            "凯文神父啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "不但在这里保护我们，\x01",
            "而且还陪孩子们玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "真是受了他\x01",
            "太多照顾了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DC")

    label("loc_F32")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #37
        0xFE,
        "啊，艾丝蒂尔和雪拉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#1001F呀哈——缇欧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x103,
        "#020F身体已经没事了吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #40
        0xFE,
        "是的，已经完全好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "事情的经过已经听\x01",
            "凯文神父说过了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #42
        0xFE,
        (
            "真是让大家\x01",
            "担心了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "不过，不用再担心了啦。\x01",
            "大家都已经没事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1025F嗯，太好了……真是太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "刚醒来的时候\x01",
            "还真是吃了一惊呢，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "忽然就发现眼前\x01",
            "站着凯文神父。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1016F啊哈哈……\x02\x03",

            "确实会让人吓一跳呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x103,
        (
            "#021F呵呵，不管怎么说，\x01",
            "他其实是个很有意思的人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "其实我一开始也不大相信\x01",
            "他会是神父，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "但他却一直默默地\x01",
            "守护着我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "虽然没办法对他作出什么回报，\x01",
            "不过真的是非常感谢他呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "在回去之前他还和孩子们\x01",
            "一起玩了好久。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "真是受了他\x01",
            "太多照顾了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A65)

    label("loc_11DC")

    Jump("loc_1594")

    label("loc_11DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1594")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 4)), scpexpr(EXPR_END)), "loc_1247")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #54
        0xFE,
        (
            "查儿和维鲁也\x01",
            "很想约修亚呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "等工作告一段落之后\x01",
            "你们两个要一起来玩啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1594")

    label("loc_1247")


    ChrTalk(    #56
        0x101,
        "#1018F呀哈！缇欧！\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(400)

    ChrTalk(    #57
        0xFE,
        (
            "啊，艾丝蒂尔！\x01",
            "好久没见了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "和雪拉姐在一起…\x01",
            "艾丝蒂尔正在工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1015F嗯，是啊，\x01",
            "我们正在调查中。\x02\x03",

            "#1006F不过不是什么严重事件，\x01",
            "不用担心啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #60
        0xFE,
        "嗯，那就好，不过……\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #61
        0xFE,
        (
            "……嘿，艾丝蒂尔。\x01",
            "那件衣服，是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1016F哈哈……你果然注意到了吗？\x02\x03",

            "那是雪拉姐为了庆祝我升为正游击士\x01",
            "而买给我的礼物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "嘿～雪拉姐\x01",
            "的眼光真不错，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "这身衣服真漂亮，\x01",
            "非常适合你呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "今后你也要多穿\x01",
            "各种好看的裙子啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1008F嘿、嘿嘿……谢谢啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "约修亚的事情\x01",
            "我也听伊莉莎说了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "艾丝蒂尔一定很难过吧…\x01",
            "如果愿意的话随时来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "在心情不好的时候，如果能找朋友\x01",
            "倾诉就会舒服一些……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1025F啊，嗯……\x02\x03",

            "谢谢你……\x01",
            "我不会客气的。\x02\x03",

            "#1006F嘿，缇欧。\x01",
            "这么久没见了，再和你一起聊天真开心⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "嗯，我也是啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "艾丝蒂尔以后还要再来玩啊！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    OP_A2(0x189C)

    label("loc_1594")

    TalkEnd(0xB)
    Return()

    # Function_7_90C end

    def Function_8_1598(): pass

    label("Function_8_1598")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_17A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34C, 6)), scpexpr(EXPR_END)), "loc_1627")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #73
        0xFE,
        (
            "以前就经常靠你们帮忙驱赶魔兽，\x01",
            "这次又多亏了你们呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "像你们这样的游击士\x01",
            "对我们来说真的是最可以依靠的人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A2")

    label("loc_1627")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #75
        0xFE,
        "喔，艾丝蒂尔和雪拉扎德啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "啊啊，从最初的驱赶魔兽工作开始\x01",
            "就一直受你们的照顾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "具体事情我听凯文神父说了，\x01",
            "真正的功劳还是你们的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1007F嗯嗯，哪里……\x01",
            "我们的力量还远远不够呢。\x02\x03",

            "在这次的事件中\x01",
            "更加认识到了这一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "哈哈，不要再谦虚了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "在不断的经验中成长，\x01",
            "可是你们年轻人的特权。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "从今以后也要\x01",
            "保持着这份信心啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A66)

    label("loc_17A2")

    TalkEnd(0xE)
    Return()

    # Function_8_1598 end

    def Function_9_17A6(): pass

    label("Function_9_17A6")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1824")

    ChrTalk(    #82
        0xFE,
        (
            "凯文神父……\x01",
            "真是个很好的人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "说话和善风趣，\x01",
            "还陪我们一起玩……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "让我不自觉地\x01",
            "想起了约修亚呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_198E")

    label("loc_1824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_198E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 5)), scpexpr(EXPR_END)), "loc_1883")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #85
        0xFE,
        (
            "下次再来的时候……\x01",
            "要带着约修亚一起哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "查儿会一直等你们的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_198E")

    label("loc_1883")

    OP_62(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #87
        0xFE,
        "啊，艾丝蒂尔姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#1000F早啊，查儿。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "那、那个……\x01",
            "约修亚呢……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1015F啊，嗯……他最近有点事，\x01",
            "自己单独行动去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "这，这样啊……\x01",
            "………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "那个……\x01",
            "到时要一起来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "查儿会一直等你们的。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x189D)

    label("loc_198E")

    TalkEnd(0xD)
    Return()

    # Function_9_17A6 end

    def Function_10_1992(): pass

    label("Function_10_1992")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1AAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_19E2")

    ChrTalk(    #94
        0xFE,
        "神父哥哥真是个有趣的人！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "嘿嘿，希望他以后再来呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AA8")

    label("loc_19E2")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #96
        0xFE,
        "啊，艾丝蒂尔！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "刚一睁眼，发现旁边有个\x01",
            "英俊又奇怪的神父，真吓了一跳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "不过，他还真是个有意思的人呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "虽然身为神父，\x01",
            "却带着那么帅气的武器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        "嘿嘿，希望他以后再来呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1AA8")

    Jump("loc_1BAA")

    label("loc_1AAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1BAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B06")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #101
        0xFE,
        (
            "虽然好久没见了，\x01",
            "不过，还有工作要去做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "唉，真是没意思。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BAA")

    label("loc_1B06")

    OP_62(0xFE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #103
        0xFE,
        (
            "啊～艾丝蒂尔！\x01",
            "是来找我玩的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1007F呼，不好意思啦，\x01",
            "这次是为工作而来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "唉～这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "唉，真是没意思。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1BAA")

    TalkEnd(0xC)
    Return()

    # Function_10_1992 end

    def Function_11_1BAE(): pass

    label("Function_11_1BAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C31")
    OP_43(0xFE, 0x2, 0x0, 0xC)
    OP_22(0x191, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C31")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x38B, 1)"), scpexpr(EXPR_END)), "loc_1C31")
    TalkBegin(0xFE)
    OP_A2(0x5)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #107
        "\x07\x00得到了\x1F\x8B\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFE)

    label("loc_1C31")

    Return()

    # Function_11_1BAE end

    def Function_12_1C32(): pass

    label("Function_12_1C32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C4D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_12_1C32")

    label("loc_1C4D")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_1C32 end

    def Function_13_1C58(): pass

    label("Function_13_1C58")

    OP_22(0x190, 0x0, 0x64)
    Return()

    # Function_13_1C58 end

    def Function_14_1C5E(): pass

    label("Function_14_1C5E")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1CCD")

    ChrTalk(    #108
        0xFE,
        (
            "啊啊，救援部队还\x01",
            "没有到来…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "这个农场能平安无事当然很好，\x01",
            "不过我也很担心王国的其他地方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DD1")

    label("loc_1CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1DD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D73")

    ChrTalk(    #110
        0xFE,
        (
            "我是迫降在附近街道上的警备艇\x01",
            "上的王国军士兵…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "但经常受农场各位的照顾，\x01",
            "如今也要帮忙警备才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "我能做出的回报\x01",
            "也只有这一点而已了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1DD1")

    label("loc_1D73")


    ChrTalk(    #113
        0xFE,
        (
            "经常受农场各位的照顾，\x01",
            "如今也要帮忙警备才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "街道的路灯已经全熄灭了，\x01",
            "似乎很混乱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DD1")

    TalkEnd(0x15)
    Return()

    # Function_14_1C5E end

    def Function_15_1DD5(): pass

    label("Function_15_1DD5")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1E42")

    ChrTalk(    #115
        0xFE,
        (
            "像这样悠闲自在度过的一天，\x01",
            "已经很久没有享受到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "好像已经忘了\x01",
            "现在处于紧急状况中呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ECA")

    label("loc_1E42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1ECA")

    ChrTalk(    #117
        0xFE,
        (
            "这里的温室和水泵\x01",
            "已经全都不能用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "只要是使用导力的道具\x01",
            "就全部瘫痪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "我们的飞艇坠落大概\x01",
            "也是因为这种现象吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ECA")

    TalkEnd(0x16)
    Return()

    # Function_15_1DD5 end

    def Function_16_1ECE(): pass

    label("Function_16_1ECE")

    EventBegin(0x0)
    SetChrPos(0x101, 23540, 0, 59780, 180)
    SetChrPos(0x103, 24540, 80, 59780, 180)
    SetChrPos(0x107, 23540, 0, 60780, 180)
    SetChrPos(0x105, 24540, 0, 60780, 180)
    OP_6D(44190, 0, 16580, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3830, 0)
    OP_6C(269000, 0)
    OP_6E(261, 0)
    OP_C8(0x200, 0x46, "C_PLAC14._CH", 0x0, 0x7D0)
    FadeToBright(2000, 0)

    def lambda_1F75():
        OP_6C(0, 12000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F75)
    OP_6D(22290, 0, 23280, 6000)

    def lambda_1F96():
        OP_6D(24020, 0, 51850, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1F96)
    Sleep(4000)
    OP_43(0x101, 0x1, 0x0, 0x11)
    Sleep(200)
    OP_43(0x103, 0x1, 0x0, 0x12)
    Sleep(200)
    OP_43(0x107, 0x1, 0x0, 0x13)
    Sleep(200)
    OP_43(0x105, 0x1, 0x0, 0x14)
    WaitChrThread(0x105, 0x1)
    Sleep(500)
    Fade(1000)
    OP_6D(23830, 50, 51930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B7")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇之前曾经来访过】\x01",      # 0
            "【◇之前没有来访过】\x01",      # 1
            "【◇不变更】\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_20AB"),
        (1, "loc_20B1"),
        (SWITCH_DEFAULT, "loc_20B7"),
    )


    label("loc_20AB")

    OP_A2(0x1888)
    Jump("loc_20B7")

    label("loc_20B1")

    OP_A3(0x1888)
    Jump("loc_20B7")

    label("loc_20B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x311, 0)), scpexpr(EXPR_END)), "loc_20EB")

    ChrTalk(    #120
        0x101,
        (
            "#1026F#5P昨天这里\x01",
            "都完全没有雾的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2140")

    label("loc_20EB")


    ChrTalk(    #121
        0x101,
        (
            "#1025F#5P缇欧的家……\x01",
            "真是有些怀念呢。\x02\x03",

            "#1007F不过看来……\x01",
            "这里的雾也很浓了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2140")

    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #122
        0x103,
        (
            "#020F#6P还是赶快将事情\x01",
            "向这里的主人说明吧。\x02\x03",

            "在现在这样的浓雾天气，\x01",
            "应该不会出门吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #123
        0x101,
        (
            "#1015F#5P嗯、嗯嗯……\x01",
            "我想应该不会吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(200)
    OP_22(0x118, 0x0, 0x4B)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2254():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2254)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #124
        0x107,
        "#065F这、这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x105,
        "#042F#2P……难道……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        "#1005F#5P雪拉姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x103,
        "#024F#6P快去看看！\x02",
    )

    CloseMessageWindow()
    OP_1D(0x56)
    Sleep(300)

    def lambda_22D2():
        OP_6D(23310, 0, 25480, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_22D2)

    def lambda_22EA():
        OP_67(0, 5180, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22EA)

    def lambda_2302():
        OP_6E(290, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2302)

    def lambda_2312():
        OP_6B(3190, 4000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2312)

    def lambda_2322():
        OP_6C(180000, 4000)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_2322)
    OP_43(0x101, 0x1, 0x0, 0x15)
    Sleep(300)
    OP_43(0x103, 0x1, 0x0, 0x16)
    Sleep(200)
    OP_43(0x107, 0x1, 0x0, 0x17)
    Sleep(300)
    OP_43(0x105, 0x1, 0x0, 0x18)
    OP_A2(0x1820)
    OP_28(0x91, 0x1, 0x4)
    LoadEffect(0x0, "map\\\\mp107_00.eff")
    Sleep(2800)
    SetChrPos(0x8, 21820, 1200, 25100, 45)
    SetChrPos(0x9, 20580, 1300, 25650, 45)
    SetChrPos(0xA, 22800, 1300, 23640, 45)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x8, 0, 300, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)

    def lambda_2430():
        OP_8F(0xFE, 0x553C, 0x2BC, 0x620C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2430)

    def lambda_244B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_244B)
    Sleep(300)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0x9, 0, 300, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)

    def lambda_24A1():
        OP_8F(0xFE, 0x5064, 0x320, 0x6432, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_24A1)

    def lambda_24BC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_24BC)
    Sleep(300)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xA, 0, 300, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)

    def lambda_2512():
        OP_8F(0xFE, 0x5910, 0x320, 0x5C58, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2512)

    def lambda_252D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_252D)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #128
        0x101,
        "#1020F#6P啊……！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0x1)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)

    ChrTalk(    #129
        0x101,
        "#1005F#6P这、这些家伙！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x105,
        "#043F#6P雾魔……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x107,
        "#065F#6P呼啊啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x103,
        (
            "#024F#6P没有时间发呆！！\x01",
            "打倒它们！！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 1)
    SetChrSubChip(0x101, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 5)
    SetChrSubChip(0x103, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x105, 7)
    SetChrSubChip(0x105, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x107, 3)
    SetChrSubChip(0x107, 0)
    OP_0D()
    Sleep(500)

    def lambda_264C():
        OP_6D(22500, 0, 26430, 200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_264C)

    def lambda_2664():
        OP_6B(2400, 200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2664)
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 2)

    def lambda_267E():
        OP_8E(0xFE, 0x5758, 0x0, 0x6BBC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_267E)
    SetChrChipByIndex(0x8, 9)

    def lambda_269E():
        OP_8E(0xFE, 0x5712, 0x1F4, 0x6626, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_269E)
    Sleep(50)
    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x103, 6)

    def lambda_26C8():
        OP_8E(0xFE, 0x5B0E, 0x0, 0x69B4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_26C8)
    SetChrChipByIndex(0x9, 9)

    def lambda_26E8():
        OP_8E(0xFE, 0x52F8, 0x258, 0x66B2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_26E8)
    Sleep(50)
    SetChrFlags(0x107, 0x1000)
    SetChrChipByIndex(0x107, 4)

    def lambda_2712():
        OP_8E(0xFE, 0x573A, 0x0, 0x6FC2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_2712)
    SetChrChipByIndex(0xA, 9)

    def lambda_2732():
        OP_8E(0xFE, 0x59F6, 0x2BC, 0x62D4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2732)
    Sleep(50)
    SetChrFlags(0x105, 0x1000)
    SetChrChipByIndex(0x105, 8)

    def lambda_275C():
        OP_8E(0xFE, 0x5B0E, 0x5A, 0x69B4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_275C)
    Sleep(200)
    OP_44(0x101, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0x799, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_27AB"),
        (SWITCH_DEFAULT, "loc_27B0"),
    )


    label("loc_27AB")

    OP_B4(0x0)
    Jump("loc_27B0")

    label("loc_27B0")

    Call(0, 25)
    Return()

    # Function_16_1ECE end

    def Function_17_27B5(): pass

    label("Function_17_27B5")

    OP_8E(0xFE, 0x5BF4, 0x46, 0xC738, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(100)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_17_27B5 end

    def Function_18_27FA(): pass

    label("Function_18_27FA")

    OP_8E(0xFE, 0x5FDC, 0x64, 0xC738, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 90, 400)
    Sleep(400)
    OP_8C(0xFE, 180, 400)
    Sleep(100)
    OP_8C(0xFE, 225, 400)
    Sleep(600)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_18_27FA end

    def Function_19_283F(): pass

    label("Function_19_283F")

    OP_8E(0xFE, 0x5BF4, 0xDC, 0xCB20, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 270, 400)
    Sleep(100)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_19_283F end

    def Function_20_2878(): pass

    label("Function_20_2878")

    OP_8E(0xFE, 0x5FDC, 0xC8, 0xCB20, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 90, 400)
    Sleep(100)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_20_2878 end

    def Function_21_28B1(): pass

    label("Function_21_28B1")

    OP_8E(0xFE, 0x5E56, 0x0, 0xBC8E, 0x1388, 0x0)
    OP_8E(0xFE, 0x5E24, 0x0, 0x8CA0, 0x1388, 0x0)
    OP_8E(0xFE, 0x5CF8, 0x50, 0x74A4, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_21_28B1 end

    def Function_22_28F5(): pass

    label("Function_22_28F5")

    OP_8E(0xFE, 0x5E56, 0x0, 0xBC8E, 0x1388, 0x0)
    OP_8E(0xFE, 0x5E24, 0x0, 0x9088, 0x1388, 0x0)
    OP_8E(0xFE, 0x6158, 0x3C, 0x7260, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_22_28F5 end

    def Function_23_2939(): pass

    label("Function_23_2939")

    OP_8E(0xFE, 0x5E56, 0x0, 0xBC8E, 0x1388, 0x0)
    OP_8E(0xFE, 0x5E24, 0x0, 0x9470, 0x1388, 0x0)
    OP_8E(0xFE, 0x5DCA, 0x14, 0x7AB2, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_23_2939 end

    def Function_24_297D(): pass

    label("Function_24_297D")

    OP_8E(0xFE, 0x5E56, 0x0, 0xBC8E, 0x1388, 0x0)
    OP_8E(0xFE, 0x5E24, 0x0, 0x9858, 0x1388, 0x0)
    OP_8E(0xFE, 0x61E4, 0x0, 0x77F6, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_24_297D end

    def Function_25_29C1(): pass

    label("Function_25_29C1")

    EventBegin(0x0)
    OP_1D(0x51)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_44(0x101, 0x0)
    OP_44(0x103, 0x0)
    OP_44(0x107, 0x0)
    OP_44(0x105, 0x0)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x103, 0x1000)
    ClearChrFlags(0x107, 0x1000)
    ClearChrFlags(0x105, 0x1000)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    SetChrPos(0x101, 21610, 0, 25150, 225)
    SetChrPos(0x103, 22820, 0, 25050, 135)
    SetChrPos(0x107, 22880, 0, 26430, 90)
    SetChrPos(0x105, 21580, 0, 26380, 315)
    OP_6D(21690, 0, 25340, 0)
    OP_67(0, 8180, -10000, 0)
    OP_6B(2470, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)
    OP_43(0x101, 0x1, 0x0, 0x1E)
    OP_43(0x103, 0x1, 0x0, 0x1F)
    OP_43(0x107, 0x1, 0x0, 0x20)
    OP_43(0x105, 0x1, 0x0, 0x21)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #133
        0x101,
        "#1026F打、打倒了……？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 270, 400)

    ChrTalk(    #134
        0x103,
        (
            "#022F嗯……\x01",
            "不过这些家伙的目标只是为了牵制住我们而已。\x02\x03",

            "赶快找到这里的主人吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B59():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B59)
    Sleep(100)

    def lambda_2B6C():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2B6C)
    Sleep(100)
    OP_8C(0x105, 160, 400)

    ChrTalk(    #135
        0x101,
        "#1005F嗯、嗯！！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1821)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_25_29C1 end

    def Function_26_2BA1(): pass

    label("Function_26_2BA1")

    OP_8E(0xFE, 0x5B4A, 0x1E, 0x744A, 0x1388, 0x0)
    OP_8C(0xFE, 203, 400)
    Return()

    # Function_26_2BA1 end

    def Function_27_2BBD(): pass

    label("Function_27_2BBD")

    OP_8E(0xFE, 0x5F96, 0x1E, 0x7288, 0x1388, 0x0)
    OP_8C(0xFE, 203, 400)
    Return()

    # Function_27_2BBD end

    def Function_28_2BD9(): pass

    label("Function_28_2BD9")

    OP_8E(0xFE, 0x5C44, 0xA0, 0x79CC, 0x1388, 0x0)
    OP_8C(0xFE, 203, 400)
    Return()

    # Function_28_2BD9 end

    def Function_29_2BF5(): pass

    label("Function_29_2BF5")

    OP_8E(0xFE, 0x6266, 0x0, 0x76FC, 0x1388, 0x0)
    OP_8C(0xFE, 203, 400)
    Return()

    # Function_29_2BF5 end

    def Function_30_2C11(): pass

    label("Function_30_2C11")

    Sleep(400)
    OP_8C(0xFE, 340, 400)
    Sleep(500)
    OP_8C(0xFE, 250, 400)
    Sleep(100)
    OP_8C(0xFE, 161, 400)
    Sleep(500)
    OP_8C(0xFE, 206, 400)
    Return()

    # Function_30_2C11 end

    def Function_31_2C42(): pass

    label("Function_31_2C42")

    Sleep(550)
    OP_8C(0xFE, 250, 400)
    Sleep(200)
    OP_8C(0xFE, 120, 400)
    Sleep(500)
    OP_8C(0xFE, 70, 400)
    Return()

    # Function_31_2C42 end

    def Function_32_2C67(): pass

    label("Function_32_2C67")

    Sleep(450)
    OP_8C(0xFE, 70, 400)
    Sleep(600)
    OP_8C(0xFE, 300, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_32_2C67 end

    def Function_33_2C8C(): pass

    label("Function_33_2C8C")

    Sleep(500)
    OP_8C(0xFE, 340, 400)
    Sleep(200)
    OP_8C(0xFE, 116, 400)
    Sleep(400)
    OP_8C(0xFE, 250, 400)
    Return()

    # Function_33_2C8C end

    def Function_34_2CB1(): pass

    label("Function_34_2CB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DE1")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D03")

    ChrTalk(    #136
        0x101,
        (
            "#1000F（我在干什么啊！\x01",
            "  为什么要到这里来？！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DC1")

    label("loc_2D03")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D48")

    ChrTalk(    #137
        0x101,
        (
            "#1000F雪拉姐！\x01",
            "不是那边啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x103,
        "#020F！明白了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DC1")

    label("loc_2D48")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D8F")

    ChrTalk(    #139
        0x101,
        (
            "#1000F科洛丝！\x01",
            "不是那边啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x105,
        "#040F是！明白了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DC1")

    label("loc_2D8F")


    ChrTalk(    #141
        0x101,
        (
            "#1000F提妲！\x01",
            "不是那边啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x107,
        "#060F嗯、嗯！\x02",
    )

    CloseMessageWindow()

    label("loc_2DC1")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_2DE1")

    Return()

    # Function_34_2CB1 end

    def Function_35_2DE2(): pass

    label("Function_35_2DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F1D")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E38")

    ChrTalk(    #143
        0x101,
        (
            "#1002F（我在干什么啊！\x01",
            "  现在必须先赶快找到缇欧！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EFD")

    label("loc_2E38")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E81")

    ChrTalk(    #144
        0x103,
        (
            "#022F（不能再耽误时间了！！\x01",
            "  必须要赶快找到大家！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EFD")

    label("loc_2E81")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ECA")

    ChrTalk(    #145
        0x105,
        (
            "#042F（……那边是出口了啊，\x01",
            "  现在要赶快找到大家！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EFD")

    label("loc_2ECA")


    ChrTalk(    #146
        0x101,
        "#1002F提妲！那边是出口啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x107,
        "#062F啊，嗯！\x02",
    )

    CloseMessageWindow()

    label("loc_2EFD")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_2F1D")

    Return()

    # Function_35_2DE2 end

    def Function_36_2F1E(): pass

    label("Function_36_2F1E")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #148
        "\x07\x05门上着锁。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FA6")

    ChrTalk(    #149
        0x101,
        "#1004F啊，上着锁吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x103,
        "#022F快去找找别的入口！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2FA6")

    TalkEnd(0xFF)
    Return()

    # Function_36_2F1E end

    SaveToFile()

Try(main)
