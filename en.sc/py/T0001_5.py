from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0001_5 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        InitFunctionIndex       = 1,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 2,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_1059",         # 01, 1
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    OP_28(0x65, 0x4, 0x4)
    OP_28(0x65, 0x4, 0x2)
    OP_28(0x65, 0x4, 0x8)
    OP_28(0x65, 0x4, 0x10)
    OP_28(0x65, 0x4, 0x20)
    OP_28(0x65, 0x1, 0x1)
    OP_28(0x65, 0x1, 0x2)
    OP_28(0x65, 0x1, 0x4)
    OP_28(0x65, 0x1, 0x8)
    OP_28(0x65, 0x1, 0x10)
    OP_28(0x65, 0x1, 0x20)
    OP_28(0x65, 0x1, 0x40)
    OP_28(0x65, 0x1, 0x80)
    OP_28(0x65, 0x1, 0x100)
    OP_28(0x65, 0x1, 0x200)
    OP_28(0x65, 0x1, 0x400)
    OP_28(0x65, 0x1, 0x800)
    OP_28(0x65, 0x1, 0x1000)
    OP_28(0x65, 0x1, 0x2000)
    OP_28(0x65, 0x1, 0x4000)
    OP_28(0x65, 0x1, 0x8000)
    OP_28(0x66, 0x4, 0x4)
    OP_28(0x66, 0x4, 0x2)
    OP_28(0x66, 0x4, 0x8)
    OP_28(0x66, 0x4, 0x10)
    OP_28(0x66, 0x4, 0x20)
    OP_28(0x66, 0x1, 0x1)
    OP_28(0x66, 0x1, 0x2)
    OP_28(0x66, 0x1, 0x4)
    OP_28(0x66, 0x1, 0x8)
    OP_28(0x66, 0x1, 0x10)
    OP_28(0x66, 0x1, 0x20)
    OP_28(0x66, 0x1, 0x40)
    OP_28(0x66, 0x1, 0x80)
    OP_28(0x66, 0x1, 0x100)
    OP_28(0x66, 0x1, 0x200)
    OP_28(0x66, 0x1, 0x400)
    OP_28(0x66, 0x1, 0x800)
    OP_28(0x66, 0x1, 0x1000)
    OP_28(0x66, 0x1, 0x2000)
    OP_28(0x66, 0x1, 0x4000)
    OP_28(0x66, 0x1, 0x8000)
    OP_28(0x67, 0x4, 0x4)
    OP_28(0x67, 0x4, 0x2)
    OP_28(0x67, 0x4, 0x8)
    OP_28(0x67, 0x4, 0x10)
    OP_28(0x67, 0x4, 0x20)
    OP_28(0x67, 0x1, 0x1)
    OP_28(0x67, 0x1, 0x2)
    OP_28(0x67, 0x1, 0x4)
    OP_28(0x67, 0x1, 0x8)
    OP_28(0x67, 0x1, 0x10)
    OP_28(0x67, 0x1, 0x20)
    OP_28(0x67, 0x1, 0x40)
    OP_28(0x67, 0x1, 0x80)
    OP_28(0x67, 0x1, 0x100)
    OP_28(0x67, 0x1, 0x200)
    OP_28(0x67, 0x1, 0x400)
    OP_28(0x67, 0x1, 0x800)
    OP_28(0x67, 0x1, 0x1000)
    OP_28(0x67, 0x1, 0x2000)
    OP_28(0x67, 0x1, 0x4000)
    OP_28(0x67, 0x1, 0x8000)
    OP_28(0x68, 0x4, 0x4)
    OP_28(0x68, 0x4, 0x2)
    OP_28(0x68, 0x4, 0x8)
    OP_28(0x68, 0x4, 0x10)
    OP_28(0x68, 0x4, 0x20)
    OP_28(0x68, 0x1, 0x1)
    OP_28(0x68, 0x1, 0x2)
    OP_28(0x68, 0x1, 0x4)
    OP_28(0x68, 0x1, 0x8)
    OP_28(0x68, 0x1, 0x10)
    OP_28(0x68, 0x1, 0x20)
    OP_28(0x68, 0x1, 0x40)
    OP_28(0x68, 0x1, 0x80)
    OP_28(0x68, 0x1, 0x100)
    OP_28(0x68, 0x1, 0x200)
    OP_28(0x68, 0x1, 0x400)
    OP_28(0x68, 0x1, 0x800)
    OP_28(0x68, 0x1, 0x1000)
    OP_28(0x68, 0x1, 0x2000)
    OP_28(0x68, 0x1, 0x4000)
    OP_28(0x68, 0x1, 0x8000)
    OP_28(0x69, 0x4, 0x4)
    OP_28(0x69, 0x4, 0x2)
    OP_28(0x69, 0x4, 0x8)
    OP_28(0x69, 0x4, 0x10)
    OP_28(0x69, 0x4, 0x20)
    OP_28(0x69, 0x1, 0x1)
    OP_28(0x69, 0x1, 0x2)
    OP_28(0x69, 0x1, 0x4)
    OP_28(0x69, 0x1, 0x8)
    OP_28(0x69, 0x1, 0x10)
    OP_28(0x69, 0x1, 0x20)
    OP_28(0x69, 0x1, 0x40)
    OP_28(0x69, 0x1, 0x80)
    OP_28(0x69, 0x1, 0x100)
    OP_28(0x69, 0x1, 0x200)
    OP_28(0x69, 0x1, 0x400)
    OP_28(0x69, 0x1, 0x800)
    OP_28(0x69, 0x1, 0x1000)
    OP_28(0x69, 0x1, 0x2000)
    OP_28(0x69, 0x1, 0x4000)
    OP_28(0x69, 0x1, 0x8000)
    OP_28(0x6B, 0x4, 0x4)
    OP_28(0x6B, 0x4, 0x2)
    OP_28(0x6B, 0x4, 0x8)
    OP_28(0x6B, 0x4, 0x10)
    OP_28(0x6B, 0x4, 0x20)
    OP_28(0x6B, 0x1, 0x1)
    OP_28(0x6B, 0x1, 0x2)
    OP_28(0x6B, 0x1, 0x4)
    OP_28(0x6B, 0x1, 0x8)
    OP_28(0x6B, 0x1, 0x10)
    OP_28(0x6B, 0x1, 0x20)
    OP_28(0x6B, 0x1, 0x40)
    OP_28(0x6B, 0x1, 0x80)
    OP_28(0x6B, 0x1, 0x100)
    OP_28(0x6B, 0x1, 0x200)
    OP_28(0x6B, 0x1, 0x400)
    OP_28(0x6B, 0x1, 0x800)
    OP_28(0x6B, 0x1, 0x1000)
    OP_28(0x6B, 0x1, 0x2000)
    OP_28(0x6B, 0x1, 0x4000)
    OP_28(0x6B, 0x1, 0x8000)
    OP_28(0x6C, 0x4, 0x4)
    OP_28(0x6C, 0x4, 0x2)
    OP_28(0x6C, 0x4, 0x8)
    OP_28(0x6C, 0x4, 0x10)
    OP_28(0x6C, 0x4, 0x20)
    OP_28(0x6C, 0x1, 0x1)
    OP_28(0x6C, 0x1, 0x2)
    OP_28(0x6C, 0x1, 0x4)
    OP_28(0x6C, 0x1, 0x8)
    OP_28(0x6C, 0x1, 0x10)
    OP_28(0x6C, 0x1, 0x20)
    OP_28(0x6C, 0x1, 0x40)
    OP_28(0x6C, 0x1, 0x80)
    OP_28(0x6C, 0x1, 0x100)
    OP_28(0x6C, 0x1, 0x200)
    OP_28(0x6C, 0x1, 0x400)
    OP_28(0x6C, 0x1, 0x800)
    OP_28(0x6C, 0x1, 0x1000)
    OP_28(0x6C, 0x1, 0x2000)
    OP_28(0x6C, 0x1, 0x4000)
    OP_28(0x6C, 0x1, 0x8000)
    OP_28(0x6D, 0x4, 0x4)
    OP_28(0x6D, 0x4, 0x2)
    OP_28(0x6D, 0x4, 0x8)
    OP_28(0x6D, 0x4, 0x10)
    OP_28(0x6D, 0x4, 0x20)
    OP_28(0x6D, 0x1, 0x1)
    OP_28(0x6D, 0x1, 0x2)
    OP_28(0x6D, 0x1, 0x4)
    OP_28(0x6D, 0x1, 0x8)
    OP_28(0x6D, 0x1, 0x10)
    OP_28(0x6D, 0x1, 0x20)
    OP_28(0x6D, 0x1, 0x40)
    OP_28(0x6D, 0x1, 0x80)
    OP_28(0x6D, 0x1, 0x100)
    OP_28(0x6D, 0x1, 0x200)
    OP_28(0x6D, 0x1, 0x400)
    OP_28(0x6D, 0x1, 0x800)
    OP_28(0x6D, 0x1, 0x1000)
    OP_28(0x6D, 0x1, 0x2000)
    OP_28(0x6D, 0x1, 0x4000)
    OP_28(0x6D, 0x1, 0x8000)
    OP_28(0x6E, 0x4, 0x4)
    OP_28(0x6E, 0x4, 0x2)
    OP_28(0x6E, 0x4, 0x8)
    OP_28(0x6E, 0x4, 0x10)
    OP_28(0x6E, 0x4, 0x20)
    OP_28(0x6E, 0x1, 0x1)
    OP_28(0x6E, 0x1, 0x2)
    OP_28(0x6E, 0x1, 0x4)
    OP_28(0x6E, 0x1, 0x8)
    OP_28(0x6E, 0x1, 0x10)
    OP_28(0x6E, 0x1, 0x20)
    OP_28(0x6E, 0x1, 0x40)
    OP_28(0x6E, 0x1, 0x80)
    OP_28(0x6E, 0x1, 0x100)
    OP_28(0x6E, 0x1, 0x200)
    OP_28(0x6E, 0x1, 0x400)
    OP_28(0x6E, 0x1, 0x800)
    OP_28(0x6E, 0x1, 0x1000)
    OP_28(0x6E, 0x1, 0x2000)
    OP_28(0x6E, 0x1, 0x4000)
    OP_28(0x6E, 0x1, 0x8000)
    OP_28(0x6F, 0x4, 0x4)
    OP_28(0x6F, 0x4, 0x2)
    OP_28(0x6F, 0x4, 0x8)
    OP_28(0x6F, 0x4, 0x10)
    OP_28(0x6F, 0x4, 0x20)
    OP_28(0x6F, 0x1, 0x1)
    OP_28(0x6F, 0x1, 0x2)
    OP_28(0x6F, 0x1, 0x4)
    OP_28(0x6F, 0x1, 0x8)
    OP_28(0x6F, 0x1, 0x10)
    OP_28(0x6F, 0x1, 0x20)
    OP_28(0x6F, 0x1, 0x40)
    OP_28(0x6F, 0x1, 0x80)
    OP_28(0x6F, 0x1, 0x100)
    OP_28(0x6F, 0x1, 0x200)
    OP_28(0x6F, 0x1, 0x400)
    OP_28(0x6F, 0x1, 0x800)
    OP_28(0x6F, 0x1, 0x1000)
    OP_28(0x6F, 0x1, 0x2000)
    OP_28(0x6F, 0x1, 0x4000)
    OP_28(0x6F, 0x1, 0x8000)
    OP_28(0x70, 0x4, 0x4)
    OP_28(0x70, 0x4, 0x2)
    OP_28(0x70, 0x4, 0x8)
    OP_28(0x70, 0x4, 0x10)
    OP_28(0x70, 0x4, 0x20)
    OP_28(0x70, 0x1, 0x1)
    OP_28(0x70, 0x1, 0x2)
    OP_28(0x70, 0x1, 0x4)
    OP_28(0x70, 0x1, 0x8)
    OP_28(0x70, 0x1, 0x10)
    OP_28(0x70, 0x1, 0x20)
    OP_28(0x70, 0x1, 0x40)
    OP_28(0x70, 0x1, 0x80)
    OP_28(0x70, 0x1, 0x100)
    OP_28(0x70, 0x1, 0x200)
    OP_28(0x70, 0x1, 0x400)
    OP_28(0x70, 0x1, 0x800)
    OP_28(0x70, 0x1, 0x1000)
    OP_28(0x70, 0x1, 0x2000)
    OP_28(0x70, 0x1, 0x4000)
    OP_28(0x70, 0x1, 0x8000)
    OP_28(0x71, 0x4, 0x4)
    OP_28(0x71, 0x4, 0x2)
    OP_28(0x71, 0x4, 0x8)
    OP_28(0x71, 0x4, 0x10)
    OP_28(0x71, 0x4, 0x20)
    OP_28(0x71, 0x1, 0x1)
    OP_28(0x71, 0x1, 0x2)
    OP_28(0x71, 0x1, 0x4)
    OP_28(0x71, 0x1, 0x8)
    OP_28(0x71, 0x1, 0x10)
    OP_28(0x71, 0x1, 0x20)
    OP_28(0x71, 0x1, 0x40)
    OP_28(0x71, 0x1, 0x80)
    OP_28(0x71, 0x1, 0x100)
    OP_28(0x71, 0x1, 0x200)
    OP_28(0x71, 0x1, 0x400)
    OP_28(0x71, 0x1, 0x800)
    OP_28(0x71, 0x1, 0x1000)
    OP_28(0x71, 0x1, 0x2000)
    OP_28(0x71, 0x1, 0x4000)
    OP_28(0x71, 0x1, 0x8000)
    OP_28(0x72, 0x4, 0x4)
    OP_28(0x72, 0x4, 0x2)
    OP_28(0x72, 0x4, 0x8)
    OP_28(0x72, 0x4, 0x10)
    OP_28(0x72, 0x4, 0x20)
    OP_28(0x72, 0x1, 0x1)
    OP_28(0x72, 0x1, 0x2)
    OP_28(0x72, 0x1, 0x4)
    OP_28(0x72, 0x1, 0x8)
    OP_28(0x72, 0x1, 0x10)
    OP_28(0x72, 0x1, 0x20)
    OP_28(0x72, 0x1, 0x40)
    OP_28(0x72, 0x1, 0x80)
    OP_28(0x72, 0x1, 0x100)
    OP_28(0x72, 0x1, 0x200)
    OP_28(0x72, 0x1, 0x400)
    OP_28(0x72, 0x1, 0x800)
    OP_28(0x72, 0x1, 0x1000)
    OP_28(0x72, 0x1, 0x2000)
    OP_28(0x72, 0x1, 0x4000)
    OP_28(0x72, 0x1, 0x8000)
    OP_28(0x73, 0x4, 0x4)
    OP_28(0x73, 0x4, 0x2)
    OP_28(0x73, 0x4, 0x8)
    OP_28(0x73, 0x4, 0x10)
    OP_28(0x73, 0x4, 0x20)
    OP_28(0x73, 0x1, 0x1)
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x4)
    OP_28(0x73, 0x1, 0x8)
    OP_28(0x73, 0x1, 0x10)
    OP_28(0x73, 0x1, 0x20)
    OP_28(0x73, 0x1, 0x40)
    OP_28(0x73, 0x1, 0x80)
    OP_28(0x73, 0x1, 0x100)
    OP_28(0x73, 0x1, 0x200)
    OP_28(0x73, 0x1, 0x400)
    OP_28(0x73, 0x1, 0x800)
    OP_28(0x73, 0x1, 0x1000)
    OP_28(0x73, 0x1, 0x2000)
    OP_28(0x73, 0x1, 0x4000)
    OP_28(0x73, 0x1, 0x8000)
    OP_28(0x74, 0x4, 0x4)
    OP_28(0x74, 0x4, 0x2)
    OP_28(0x74, 0x4, 0x8)
    OP_28(0x74, 0x4, 0x10)
    OP_28(0x74, 0x4, 0x20)
    OP_28(0x74, 0x1, 0x1)
    OP_28(0x74, 0x1, 0x2)
    OP_28(0x74, 0x1, 0x4)
    OP_28(0x74, 0x1, 0x8)
    OP_28(0x74, 0x1, 0x10)
    OP_28(0x74, 0x1, 0x20)
    OP_28(0x74, 0x1, 0x40)
    OP_28(0x74, 0x1, 0x80)
    OP_28(0x74, 0x1, 0x100)
    OP_28(0x74, 0x1, 0x200)
    OP_28(0x74, 0x1, 0x400)
    OP_28(0x74, 0x1, 0x800)
    OP_28(0x74, 0x1, 0x1000)
    OP_28(0x74, 0x1, 0x2000)
    OP_28(0x74, 0x1, 0x4000)
    OP_28(0x74, 0x1, 0x8000)
    OP_28(0x75, 0x4, 0x4)
    OP_28(0x75, 0x4, 0x2)
    OP_28(0x75, 0x4, 0x8)
    OP_28(0x75, 0x4, 0x10)
    OP_28(0x75, 0x4, 0x20)
    OP_28(0x75, 0x1, 0x1)
    OP_28(0x75, 0x1, 0x2)
    OP_28(0x75, 0x1, 0x4)
    OP_28(0x75, 0x1, 0x8)
    OP_28(0x75, 0x1, 0x10)
    OP_28(0x75, 0x1, 0x20)
    OP_28(0x75, 0x1, 0x40)
    OP_28(0x75, 0x1, 0x80)
    OP_28(0x75, 0x1, 0x100)
    OP_28(0x75, 0x1, 0x200)
    OP_28(0x75, 0x1, 0x400)
    OP_28(0x75, 0x1, 0x800)
    OP_28(0x75, 0x1, 0x1000)
    OP_28(0x75, 0x1, 0x2000)
    OP_28(0x75, 0x1, 0x4000)
    OP_28(0x75, 0x1, 0x8000)
    OP_28(0x76, 0x4, 0x4)
    OP_28(0x76, 0x4, 0x2)
    OP_28(0x76, 0x4, 0x8)
    OP_28(0x76, 0x4, 0x10)
    OP_28(0x76, 0x4, 0x20)
    OP_28(0x76, 0x1, 0x1)
    OP_28(0x76, 0x1, 0x2)
    OP_28(0x76, 0x1, 0x4)
    OP_28(0x76, 0x1, 0x8)
    OP_28(0x76, 0x1, 0x10)
    OP_28(0x76, 0x1, 0x20)
    OP_28(0x76, 0x1, 0x40)
    OP_28(0x76, 0x1, 0x80)
    OP_28(0x76, 0x1, 0x100)
    OP_28(0x76, 0x1, 0x200)
    OP_28(0x76, 0x1, 0x400)
    OP_28(0x76, 0x1, 0x800)
    OP_28(0x76, 0x1, 0x1000)
    OP_28(0x76, 0x1, 0x2000)
    OP_28(0x76, 0x1, 0x4000)
    OP_28(0x76, 0x1, 0x8000)
    OP_28(0x77, 0x4, 0x4)
    OP_28(0x77, 0x4, 0x2)
    OP_28(0x77, 0x4, 0x8)
    OP_28(0x77, 0x4, 0x10)
    OP_28(0x77, 0x4, 0x20)
    OP_28(0x77, 0x1, 0x1)
    OP_28(0x77, 0x1, 0x2)
    OP_28(0x77, 0x1, 0x4)
    OP_28(0x77, 0x1, 0x8)
    OP_28(0x77, 0x1, 0x10)
    OP_28(0x77, 0x1, 0x20)
    OP_28(0x77, 0x1, 0x40)
    OP_28(0x77, 0x1, 0x80)
    OP_28(0x77, 0x1, 0x100)
    OP_28(0x77, 0x1, 0x200)
    OP_28(0x77, 0x1, 0x400)
    OP_28(0x77, 0x1, 0x800)
    OP_28(0x77, 0x1, 0x1000)
    OP_28(0x77, 0x1, 0x2000)
    OP_28(0x77, 0x1, 0x4000)
    OP_28(0x77, 0x1, 0x8000)
    OP_28(0x78, 0x4, 0x4)
    OP_28(0x78, 0x4, 0x2)
    OP_28(0x78, 0x4, 0x8)
    OP_28(0x78, 0x4, 0x10)
    OP_28(0x78, 0x4, 0x20)
    OP_28(0x78, 0x1, 0x1)
    OP_28(0x78, 0x1, 0x2)
    OP_28(0x78, 0x1, 0x4)
    OP_28(0x78, 0x1, 0x8)
    OP_28(0x78, 0x1, 0x10)
    OP_28(0x78, 0x1, 0x20)
    OP_28(0x78, 0x1, 0x40)
    OP_28(0x78, 0x1, 0x80)
    OP_28(0x78, 0x1, 0x100)
    OP_28(0x78, 0x1, 0x200)
    OP_28(0x78, 0x1, 0x400)
    OP_28(0x78, 0x1, 0x800)
    OP_28(0x78, 0x1, 0x1000)
    OP_28(0x78, 0x1, 0x2000)
    OP_28(0x78, 0x1, 0x4000)
    OP_28(0x78, 0x1, 0x8000)
    OP_28(0x79, 0x4, 0x4)
    OP_28(0x79, 0x4, 0x2)
    OP_28(0x79, 0x4, 0x8)
    OP_28(0x79, 0x4, 0x10)
    OP_28(0x79, 0x4, 0x20)
    OP_28(0x79, 0x1, 0x1)
    OP_28(0x79, 0x1, 0x2)
    OP_28(0x79, 0x1, 0x4)
    OP_28(0x79, 0x1, 0x8)
    OP_28(0x79, 0x1, 0x10)
    OP_28(0x79, 0x1, 0x20)
    OP_28(0x79, 0x1, 0x40)
    OP_28(0x79, 0x1, 0x80)
    OP_28(0x79, 0x1, 0x100)
    OP_28(0x79, 0x1, 0x200)
    OP_28(0x79, 0x1, 0x400)
    OP_28(0x79, 0x1, 0x800)
    OP_28(0x79, 0x1, 0x1000)
    OP_28(0x79, 0x1, 0x2000)
    OP_28(0x79, 0x1, 0x4000)
    OP_28(0x79, 0x1, 0x8000)
    OP_28(0x7A, 0x4, 0x4)
    OP_28(0x7A, 0x4, 0x2)
    OP_28(0x7A, 0x4, 0x8)
    OP_28(0x7A, 0x4, 0x10)
    OP_28(0x7A, 0x4, 0x20)
    OP_28(0x7A, 0x1, 0x1)
    OP_28(0x7A, 0x1, 0x2)
    OP_28(0x7A, 0x1, 0x4)
    OP_28(0x7A, 0x1, 0x8)
    OP_28(0x7A, 0x1, 0x10)
    OP_28(0x7A, 0x1, 0x20)
    OP_28(0x7A, 0x1, 0x40)
    OP_28(0x7A, 0x1, 0x80)
    OP_28(0x7A, 0x1, 0x100)
    OP_28(0x7A, 0x1, 0x200)
    OP_28(0x7A, 0x1, 0x400)
    OP_28(0x7A, 0x1, 0x800)
    OP_28(0x7A, 0x1, 0x1000)
    OP_28(0x7A, 0x1, 0x2000)
    OP_28(0x7A, 0x1, 0x4000)
    OP_28(0x7A, 0x1, 0x8000)
    OP_28(0x7B, 0x4, 0x4)
    OP_28(0x7B, 0x4, 0x2)
    OP_28(0x7B, 0x4, 0x8)
    OP_28(0x7B, 0x4, 0x10)
    OP_28(0x7B, 0x4, 0x20)
    OP_28(0x7B, 0x1, 0x1)
    OP_28(0x7B, 0x1, 0x2)
    OP_28(0x7B, 0x1, 0x4)
    OP_28(0x7B, 0x1, 0x8)
    OP_28(0x7B, 0x1, 0x10)
    OP_28(0x7B, 0x1, 0x20)
    OP_28(0x7B, 0x1, 0x40)
    OP_28(0x7B, 0x1, 0x80)
    OP_28(0x7B, 0x1, 0x100)
    OP_28(0x7B, 0x1, 0x200)
    OP_28(0x7B, 0x1, 0x400)
    OP_28(0x7B, 0x1, 0x800)
    OP_28(0x7B, 0x1, 0x1000)
    OP_28(0x7B, 0x1, 0x2000)
    OP_28(0x7B, 0x1, 0x4000)
    OP_28(0x7B, 0x1, 0x8000)
    OP_28(0x7C, 0x4, 0x4)
    OP_28(0x7C, 0x4, 0x2)
    OP_28(0x7C, 0x4, 0x8)
    OP_28(0x7C, 0x4, 0x10)
    OP_28(0x7C, 0x4, 0x20)
    OP_28(0x7C, 0x1, 0x1)
    OP_28(0x7C, 0x1, 0x2)
    OP_28(0x7C, 0x1, 0x4)
    OP_28(0x7C, 0x1, 0x8)
    OP_28(0x7C, 0x1, 0x10)
    OP_28(0x7C, 0x1, 0x20)
    OP_28(0x7C, 0x1, 0x40)
    OP_28(0x7C, 0x1, 0x80)
    OP_28(0x7C, 0x1, 0x100)
    OP_28(0x7C, 0x1, 0x200)
    OP_28(0x7C, 0x1, 0x400)
    OP_28(0x7C, 0x1, 0x800)
    OP_28(0x7C, 0x1, 0x1000)
    OP_28(0x7C, 0x1, 0x2000)
    OP_28(0x7C, 0x1, 0x4000)
    OP_28(0x7C, 0x1, 0x8000)
    OP_28(0x7D, 0x4, 0x4)
    OP_28(0x7D, 0x4, 0x2)
    OP_28(0x7D, 0x4, 0x8)
    OP_28(0x7D, 0x4, 0x10)
    OP_28(0x7D, 0x4, 0x20)
    OP_28(0x7D, 0x1, 0x1)
    OP_28(0x7D, 0x1, 0x2)
    OP_28(0x7D, 0x1, 0x4)
    OP_28(0x7D, 0x1, 0x8)
    OP_28(0x7D, 0x1, 0x10)
    OP_28(0x7D, 0x1, 0x20)
    OP_28(0x7D, 0x1, 0x40)
    OP_28(0x7D, 0x1, 0x80)
    OP_28(0x7D, 0x1, 0x100)
    OP_28(0x7D, 0x1, 0x200)
    OP_28(0x7D, 0x1, 0x400)
    OP_28(0x7D, 0x1, 0x800)
    OP_28(0x7D, 0x1, 0x1000)
    OP_28(0x7D, 0x1, 0x2000)
    OP_28(0x7D, 0x1, 0x4000)
    OP_28(0x7D, 0x1, 0x8000)
    OP_28(0x7E, 0x4, 0x4)
    OP_28(0x7E, 0x4, 0x2)
    OP_28(0x7E, 0x4, 0x8)
    OP_28(0x7E, 0x1, 0x1)
    OP_28(0x7E, 0x1, 0x2)
    OP_28(0x7E, 0x1, 0x4)
    OP_28(0x7E, 0x1, 0x8)
    OP_28(0x7E, 0x1, 0x10)
    OP_28(0x7E, 0x1, 0x20)
    OP_28(0x7E, 0x1, 0x40)
    OP_28(0x7E, 0x1, 0x80)
    OP_28(0x7E, 0x1, 0x100)
    OP_28(0x7E, 0x1, 0x200)
    OP_28(0x7E, 0x1, 0x400)
    OP_28(0x7E, 0x1, 0x800)
    OP_28(0x7E, 0x1, 0x1000)
    OP_28(0x7E, 0x1, 0x2000)
    OP_28(0x7E, 0x1, 0x4000)
    OP_28(0x7E, 0x1, 0x8000)
    OP_28(0x7F, 0x4, 0x4)
    OP_28(0x7F, 0x4, 0x2)
    OP_28(0x7F, 0x4, 0x8)
    OP_28(0x7F, 0x1, 0x1)
    OP_28(0x7F, 0x1, 0x2)
    OP_28(0x7F, 0x1, 0x4)
    OP_28(0x7F, 0x1, 0x8)
    OP_28(0x7F, 0x1, 0x10)
    OP_28(0x7F, 0x1, 0x20)
    OP_28(0x7F, 0x1, 0x40)
    OP_28(0x7F, 0x1, 0x80)
    OP_28(0x7F, 0x1, 0x100)
    OP_28(0x7F, 0x1, 0x200)
    OP_28(0x7F, 0x1, 0x400)
    OP_28(0x7F, 0x1, 0x800)
    OP_28(0x7F, 0x1, 0x1000)
    OP_28(0x7F, 0x1, 0x2000)
    OP_28(0x7F, 0x1, 0x4000)
    OP_28(0x7F, 0x1, 0x8000)
    OP_28(0x80, 0x4, 0x4)
    OP_28(0x80, 0x4, 0x2)
    OP_28(0x80, 0x4, 0x8)
    OP_28(0x80, 0x1, 0x1)
    OP_28(0x80, 0x1, 0x2)
    OP_28(0x80, 0x1, 0x4)
    OP_28(0x80, 0x1, 0x8)
    OP_28(0x80, 0x1, 0x10)
    OP_28(0x80, 0x1, 0x20)
    OP_28(0x80, 0x1, 0x40)
    OP_28(0x80, 0x1, 0x80)
    OP_28(0x80, 0x1, 0x100)
    OP_28(0x80, 0x1, 0x200)
    OP_28(0x80, 0x1, 0x400)
    OP_28(0x80, 0x1, 0x800)
    OP_28(0x80, 0x1, 0x1000)
    OP_28(0x80, 0x1, 0x2000)
    OP_28(0x80, 0x1, 0x4000)
    OP_28(0x80, 0x1, 0x8000)
    OP_28(0x90, 0x4, 0x4)
    OP_28(0x90, 0x4, 0x2)
    OP_28(0x90, 0x4, 0x8)
    OP_28(0x90, 0x1, 0x1)
    OP_28(0x90, 0x1, 0x2)
    OP_28(0x90, 0x1, 0x8)
    OP_28(0x90, 0x1, 0x20)
    OP_28(0x90, 0x1, 0x80)
    OP_28(0xB1, 0x4, 0x4)
    OP_28(0xB1, 0x4, 0x2)
    OP_28(0xB1, 0x4, 0x8)
    OP_28(0xB2, 0x4, 0x4)
    OP_28(0xB2, 0x4, 0x2)
    OP_28(0xB2, 0x4, 0x8)
    OP_28(0xB3, 0x4, 0x4)
    OP_28(0xB3, 0x4, 0x2)
    OP_28(0xB3, 0x4, 0x8)
    OP_28(0x9D, 0x4, 0x4)
    OP_28(0x9D, 0x4, 0x2)
    OP_28(0x9D, 0x4, 0x8)
    OP_28(0x9D, 0x4, 0x10)
    OP_28(0x9D, 0x4, 0x20)
    OP_28(0x9D, 0x1, 0x1)
    OP_28(0x9D, 0x1, 0x2)
    OP_28(0x9D, 0x1, 0x4)
    OP_28(0x9D, 0x1, 0x8)
    OP_28(0x9D, 0x1, 0x10)
    OP_28(0x9D, 0x1, 0x20)
    OP_28(0x9D, 0x1, 0x40)
    OP_28(0x9D, 0x1, 0x80)
    OP_28(0x9D, 0x1, 0x100)
    OP_28(0x9D, 0x1, 0x200)
    OP_28(0x9D, 0x1, 0x400)
    OP_28(0x9D, 0x1, 0x800)
    OP_28(0x9D, 0x1, 0x1000)
    OP_28(0x9D, 0x1, 0x2000)
    OP_28(0x9D, 0x1, 0x4000)
    OP_28(0x9D, 0x1, 0x8000)
    OP_28(0x9E, 0x4, 0x4)
    OP_28(0x9E, 0x4, 0x2)
    OP_28(0x9E, 0x4, 0x8)
    OP_28(0x9E, 0x4, 0x10)
    OP_28(0x9E, 0x4, 0x20)
    OP_28(0x9E, 0x1, 0x1)
    OP_28(0x9E, 0x1, 0x2)
    OP_28(0x9E, 0x1, 0x4)
    OP_28(0x9E, 0x1, 0x8)
    OP_28(0x9E, 0x1, 0x10)
    OP_28(0x9E, 0x1, 0x20)
    OP_28(0x9E, 0x1, 0x40)
    OP_28(0x9E, 0x1, 0x80)
    OP_28(0x9E, 0x1, 0x100)
    OP_28(0x9E, 0x1, 0x200)
    OP_28(0x9E, 0x1, 0x400)
    OP_28(0x9E, 0x1, 0x800)
    OP_28(0x9E, 0x1, 0x1000)
    OP_28(0x9E, 0x1, 0x2000)
    OP_28(0x9E, 0x1, 0x4000)
    OP_28(0x9E, 0x1, 0x8000)
    OP_28(0x9F, 0x4, 0x4)
    OP_28(0x9F, 0x4, 0x2)
    OP_28(0x9F, 0x4, 0x8)
    OP_28(0x9F, 0x4, 0x10)
    OP_28(0x9F, 0x4, 0x20)
    OP_28(0x9F, 0x1, 0x1)
    OP_28(0x9F, 0x1, 0x2)
    OP_28(0x9F, 0x1, 0x4)
    OP_28(0x9F, 0x1, 0x8)
    OP_28(0x9F, 0x1, 0x10)
    OP_28(0x9F, 0x1, 0x20)
    OP_28(0x9F, 0x1, 0x40)
    OP_28(0x9F, 0x1, 0x80)
    OP_28(0x9F, 0x1, 0x100)
    OP_28(0x9F, 0x1, 0x200)
    OP_28(0x9F, 0x1, 0x400)
    OP_28(0x9F, 0x1, 0x800)
    OP_28(0x9F, 0x1, 0x1000)
    OP_28(0x9F, 0x1, 0x2000)
    OP_28(0x9F, 0x1, 0x4000)
    OP_28(0x9F, 0x1, 0x8000)
    OP_28(0xA0, 0x4, 0x4)
    OP_28(0xA0, 0x4, 0x2)
    OP_28(0xA0, 0x4, 0x8)
    OP_28(0xA0, 0x4, 0x10)
    OP_28(0xA0, 0x4, 0x20)
    OP_28(0xA0, 0x1, 0x1)
    OP_28(0xA0, 0x1, 0x2)
    OP_28(0xA0, 0x1, 0x4)
    OP_28(0xA0, 0x1, 0x8)
    OP_28(0xA0, 0x1, 0x10)
    OP_28(0xA0, 0x1, 0x20)
    OP_28(0xA0, 0x1, 0x40)
    OP_28(0xA0, 0x1, 0x80)
    OP_28(0xA0, 0x1, 0x100)
    OP_28(0xA0, 0x1, 0x200)
    OP_28(0xA0, 0x1, 0x400)
    OP_28(0xA0, 0x1, 0x800)
    OP_28(0xA0, 0x1, 0x1000)
    OP_28(0xA0, 0x1, 0x2000)
    OP_28(0xA0, 0x1, 0x4000)
    OP_28(0xA0, 0x1, 0x8000)
    OP_28(0xA1, 0x4, 0x2)
    OP_28(0xA2, 0x4, 0x2)
    OP_28(0xA3, 0x4, 0x2)
    OP_28(0xA4, 0x4, 0x2)
    OP_28(0xA5, 0x4, 0x2)
    OP_28(0xA6, 0x4, 0x2)
    OP_28(0xA7, 0x4, 0x2)
    OP_28(0xA8, 0x4, 0x2)
    OP_28(0xA9, 0x4, 0x2)
    OP_28(0xAA, 0x4, 0x2)
    OP_28(0xAB, 0x4, 0x2)
    OP_28(0xAC, 0x4, 0x2)
    OP_28(0xAD, 0x4, 0x2)
    OP_28(0xAE, 0x4, 0x2)
    OP_28(0xAF, 0x4, 0x2)
    OP_28(0xB0, 0x4, 0x2)
    OP_28(0xB1, 0x4, 0x2)
    OP_28(0xB2, 0x4, 0x2)
    OP_28(0xB3, 0x4, 0x2)
    OP_28(0xB4, 0x4, 0x2)
    OP_28(0xB5, 0x4, 0x2)
    OP_28(0xB6, 0x4, 0x2)
    OP_28(0xB7, 0x4, 0x2)
    OP_28(0xB8, 0x4, 0x2)
    OP_28(0xB9, 0x4, 0x2)
    OP_28(0xBA, 0x4, 0x2)
    OP_28(0xBB, 0x4, 0x2)
    OP_28(0xBC, 0x4, 0x2)
    OP_28(0xBD, 0x4, 0x2)
    OP_28(0xBE, 0x4, 0x2)
    OP_28(0xC3, 0x4, 0x2)
    OP_28(0xC3, 0x1, 0x100)
    OP_28(0xC3, 0x1, 0x200)
    OP_28(0xC3, 0x1, 0x400)
    OP_28(0xC3, 0x1, 0x800)
    OP_28(0xC3, 0x1, 0x1000)
    OP_28(0xC3, 0x1, 0x2000)
    OP_28(0xC3, 0x1, 0x4000)
    OP_28(0xC3, 0x1, 0x8000)
    Return()

    # Function_0_AA end

    def Function_1_1059(): pass

    label("Function_1_1059")

    OP_AC(0x1)
    OP_AC(0x2)
    OP_AC(0x3)
    OP_AC(0x4)
    OP_AC(0x5)
    OP_AC(0x6)
    OP_AC(0x7)
    OP_AC(0x8)
    OP_AC(0x9)
    OP_AC(0xB)
    OP_AC(0xC)
    OP_AC(0x14)
    OP_AC(0x15)
    OP_AC(0x16)
    OP_AC(0x17)
    OP_AC(0x18)
    OP_AC(0x19)
    OP_AC(0x1A)
    OP_AC(0x1B)
    OP_AC(0x1C)
    OP_AC(0x1D)
    OP_AC(0x1E)
    OP_AC(0x1F)
    OP_AC(0x20)
    OP_AC(0x21)
    OP_AC(0x22)
    OP_AC(0x23)
    OP_AC(0x24)
    OP_AC(0x25)
    OP_AC(0x26)
    OP_AC(0x27)
    OP_AC(0x28)
    OP_AC(0x29)
    OP_AC(0x2A)
    OP_AC(0x2B)
    OP_AC(0x2C)
    OP_AC(0x2D)
    OP_AC(0x2E)
    OP_AC(0x2F)
    OP_AC(0x30)
    OP_AC(0x31)
    OP_AC(0x32)
    OP_AC(0x33)
    OP_AC(0x34)
    OP_AC(0x35)
    OP_AC(0x36)
    OP_AC(0x37)
    OP_AC(0x38)
    OP_AC(0x39)
    OP_AC(0x3A)
    OP_AC(0x3B)
    OP_AC(0x3C)
    OP_AC(0x3D)
    OP_AC(0x3E)
    OP_AC(0x3F)
    OP_AC(0x40)
    OP_AC(0x41)
    OP_AC(0x42)
    OP_AC(0x43)
    OP_AC(0x44)
    OP_AC(0x45)
    OP_AC(0x46)
    OP_AC(0x47)
    OP_AC(0x48)
    OP_AC(0x49)
    OP_AC(0x4A)
    OP_AC(0x4B)
    OP_AC(0x4C)
    Return()

    # Function_1_1059 end

    SaveToFile()

Try(main)
