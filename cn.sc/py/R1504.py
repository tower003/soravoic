from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R1504   ._SN',
        MapName             = 'Bose',
        Location            = 'R1504.x',
        MapIndex            = 59,
        MapDefaultBGM       = "ed60031",
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
        '特务兵',                               # 9
        '特务兵',                               # 10
        '特务兵',                               # 11
        '拉文努山道方向',                       # 12
        '拉文努山道方向',                       # 13
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
        'ED6_DT07/CH01610 ._CH',             # 00
        'ED6_DT27/CH03095 ._CH',             # 01
        'ED6_DT07/CH00055 ._CH',             # 02
        'ED6_DT07/CH00025 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01610P._CP',             # 00
        'ED6_DT27/CH03095P._CP',             # 01
        'ED6_DT07/CH00055P._CP',             # 02
        'ED6_DT07/CH00025P._CP',             # 03
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -111060,
        Z                   = -20,
        Y                   = -19200,
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
        X                   = 1140,
        Z                   = 10,
        Y                   = -19200,
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


    ScpFunction(
        "Function_0_16A",          # 00, 0
        "Function_1_17E",          # 01, 1
        "Function_2_1C7",          # 02, 2
        "Function_3_957",          # 03, 3
    )


    def Function_0_16A(): pass

    label("Function_0_16A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_17D")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_17D")

    Return()

    # Function_0_16A end

    def Function_1_17E(): pass

    label("Function_1_17E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_192"),
        (101, "loc_1AC"),
        (102, "loc_1AC"),
        (SWITCH_DEFAULT, "loc_1C6"),
    )


    label("loc_192")

    OP_16(0x2, 0xFA0, 0xFFFE0FE8, 0xFFFE2758, 0x23006B)
    ClearChrFlags(0xB, 0x4)
    Jump("loc_1C6")

    label("loc_1AC")

    OP_16(0x2, 0xFA0, 0xFFFC5A68, 0xFFFE2758, 0x230022)
    ClearChrFlags(0xC, 0x4)
    Jump("loc_1C6")

    label("loc_1C6")

    Return()

    # Function_1_17E end

    def Function_2_1C7(): pass

    label("Function_2_1C7")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DA")
    Call(0, 3)

    label("loc_1DA")

    RemoveParty(0x0, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1EE")
    RemoveParty(0x5, 0xFF)
    AddParty(0x2, 0xF6, 0xFF)
    Jump("loc_1F5")

    label("loc_1EE")

    RemoveParty(0x2, 0xFF)
    AddParty(0x5, 0xF6, 0xFF)

    label("loc_1F5")

    AddParty(0x9, 0xF7, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 2290, 0, 12140, 0)
    SetChrPos(0x9, 1210, 0, 11140, 0)
    SetChrPos(0xA, 2840, 0, 10990, 0)
    OP_6D(2290, 0, 12140, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_6A(0x8)
    OP_C8(0x200, 0x46, "C_PLAC16._CH", 0x0, 0x7D0)
    FadeToBright(2000, 0)

    def lambda_29F():
        OP_8E(0xFE, 0x8F2, 0x0, 0x567C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_29F)
    Sleep(100)

    def lambda_2BF():
        OP_8E(0xFE, 0x4BA, 0x0, 0x5294, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2BF)
    Sleep(50)

    def lambda_2DF():
        OP_8E(0xFE, 0xB18, 0x0, 0x51FE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2DF)
    WaitChrThread(0xA, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x6E, 0x0, 0x64)
    ClearMapFlags(0x1)
    OP_6D(-110000, 0, 21330, 0)
    SetChrPos(0x8, -110000, 0, 21330, 0)
    SetChrPos(0x9, -110700, 0, 20190, 0)
    SetChrPos(0xA, -109100, 0, 20200, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_36C():
        OP_8E(0xFE, 0xFFFE5250, 0x0, 0x6E96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_36C)
    Sleep(300)

    def lambda_38C():
        OP_8E(0xFE, 0xFFFE5250, 0x0, 0x6E96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_38C)
    Sleep(300)

    def lambda_3AC():
        OP_8E(0xFE, 0xFFFE5250, 0x0, 0x66C6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3AC)
    WaitChrThread(0xA, 0x1)
    Sleep(1000)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Fade(1000)
    SetChrPos(0xF6, -104360, -70, 7570, 0)
    SetChrPos(0x10A, -103210, -50, 6530, 0)
    SetChrFlags(0xF6, 0x2)
    SetChrFlags(0x10A, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_41A")
    SetChrChipByIndex(0xF6, 2)
    Jump("loc_41F")

    label("loc_41A")

    SetChrChipByIndex(0xF6, 3)

    label("loc_41F")

    SetChrSubChip(0xF6, 1)
    SetChrChipByIndex(0x10A, 1)
    SetChrSubChip(0x10A, 1)
    OP_6D(-103630, -60, 7990, 0)
    OP_6E(239, 0)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_630")

    ChrTalk(    #0
        0x10A,
        (
            "#816F呵呵……\x01",
            "看来是猜对了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x106,
        (
            "#051F啊啊……\x01",
            "总算抓住狐狸尾巴啦。\x02\x03",

            "不过真没想到\x01",
            "竟然会是拉文努废坑啊。\x02\x03",

            "这些家伙\x01",
            "倒是挺会选地点的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10A,
        (
            "#818F记得是空贼团\x01",
            "抢夺定期船货物\x01",
            "所利用过的地方吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x106,
        (
            "#053F好像是吧。\x02\x03",

            "#050F艾丝蒂尔他们\x01",
            "似乎在途中的露天采掘场\x01",
            "和空贼团的人交战过吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10A,
        (
            "#817F这么说来……\x01",
            "把这里做为大本营\x01",
            "的可能性似乎很高。\x02\x03",

            "#812F如何？\x01",
            "就这样闯进去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x106,
        (
            "#057F啊啊，没空跟\x01",
            "协会和军方联络了。\x02\x03",

            "总之先潜入进去\x01",
            "确认余党的规模吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10A,
        "#816F明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FB")

    label("loc_630")


    ChrTalk(    #7
        0x10A,
        (
            "#816F呵呵……\x01",
            "看来是猜对了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x103,
        (
            "#026F嗯……\x01",
            "总算抓住狐狸尾巴了。\x02\x03",

            "#027F不过真没想到\x01",
            "竟然是拉文努废坑呢。\x02\x03",

            "这些家伙\x01",
            "倒是挺会选地点的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10A,
        (
            "#818F记得是空贼团\x01",
            "抢夺定期船货物\x01",
            "所利用过的地方吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x103,
        (
            "#020F嗯嗯，是啊。\x02\x03",

            "我们在途中的露天采掘场\x01",
            "和空贼团的那些人交战过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10A,
        (
            "#817F这么说来……\x01",
            "把这里做为大本营\x01",
            "的可能性似乎很高。\x02\x03",

            "#812F如何？\x01",
            "就这样闯进去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x103,
        (
            "#022F嗯嗯，没空跟\x01",
            "协会和军方联络了。\x02\x03",

            "总之先潜入进去\x01",
            "确认余党的规模吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10A,
        "#816F明白了。\x02",
    )

    CloseMessageWindow()

    label("loc_7FB")

    Sleep(200)
    Fade(1000)
    SetChrPos(0xF6, -113220, 20, 9490, 0)
    SetChrPos(0x10A, -107140, 40, 9700, 0)
    OP_6D(-110000, 0, 21330, 0)
    OP_6E(262, 0)
    OP_0D()
    ClearChrFlags(0xF6, 0x2)
    ClearChrFlags(0x10A, 0x2)
    SetChrChipByIndex(0xF6, 65535)
    SetChrChipByIndex(0x10A, 65535)
    SetChrFlags(0x10A, 0x4)

    def lambda_861():
        OP_8E(0xFE, 0xFFFE4AB2, 0x64, 0x5712, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF6, 1, lambda_861)
    Sleep(500)

    def lambda_881():
        OP_8E(0xFE, 0xFFFE5B4C, 0x50, 0x5712, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_881)
    WaitChrThread(0xF6, 0x1)
    OP_8C(0xF6, 180, 800)
    WaitChrThread(0x10A, 0x1)
    OP_8C(0x10A, 180, 800)
    Sleep(1000)
    TurnDirection(0xF6, 0x10A, 400)
    Sleep(500)
    OP_8C(0x10A, 270, 400)
    Sleep(1000)
    OP_8E(0xF6, 0xFFFE4F26, 0xFFFFFFF6, 0x5640, 0x1388, 0x0)

    def lambda_8E5():
        OP_8E(0xFE, 0xFFFE56CE, 0xFFFFFFEC, 0x560E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_8E5)

    def lambda_900():
        OP_8E(0xFE, 0xFFFE5250, 0x0, 0x6E96, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF6, 1, lambda_900)
    WaitChrThread(0x10A, 0x1)
    ClearChrFlags(0x10A, 0x4)

    def lambda_925():
        OP_8E(0xFE, 0xFFFE5250, 0x0, 0x6E96, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_925)
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1104   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1C7 end

    def Function_3_957(): pass

    label("Function_3_957")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9D1"),
        (1, "loc_9D7"),
        (SWITCH_DEFAULT, "loc_9DD"),
    )


    label("loc_9D1")

    OP_A2(0x1200)
    Jump("loc_9DD")

    label("loc_9D7")

    OP_A2(0x1201)
    Jump("loc_9DD")

    label("loc_9DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_9EB")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_9EF")

    label("loc_9EB")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_9EF")

    Return()

    # Function_3_957 end

    SaveToFile()

Try(main)
