# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""


bspMenu = bspComponent.createMenuSymbol("BSP_MENU", None)
bspMenu.setLabel("BSP Pin Types")
bspMenu.setDescription("Type of PIO Pins")



enumeratedPinTypes = enumerate(pinTypes)

for enumeratedPinType in enumeratedPinTypes:
    pinTypeIndex, pinType = enumeratedPinType

    Menu = bspComponent.createMenuSymbol("BSP_SUBMENU"+str(pinTypeIndex), bspMenu)
    Menu.setLabel("Type " + str(pinTypeIndex))

    for pinAttribute in pinAttributes:
        pinAttribute['symbol']
        Symbol = bspComponent.createStringSymbol(pinAttribute['symbol'] + str(pinTypeIndex), Menu)
        Symbol.setLabel(pinAttribute['label'])
        if pinAttribute['attrib'] in pinType:
            Symbol.setDefaultValue(pinType[pinAttribute['attrib']])

Symbol = bspComponent.createIntegerSymbol("BSP_TYPE_SIZE", bspMenu)
Symbol.setDefaultValue(len(pinTypes))

bspSystemInitFile = bspComponent.createFileSymbol("BSP_INIT", None)
bspSystemInitFile.setType("STRING")
bspSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
bspSystemInitFile.setSourcePath("/templates/system_initialize.c.ftl")
bspSystemInitFile.setMarkup(True)

bspSystemDefFile = bspComponent.createFileSymbol("DACC_DEF", None)
bspSystemDefFile.setType("STRING")
bspSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
bspSystemDefFile.setSourcePath("/templates/system_definitions.h.ftl")
bspSystemDefFile.setMarkup(True)

configName = Variables.get("__CONFIGURATION_NAME")

bspSourceFile = bspComponent.createFileSymbol("BSP_C", None)
bspSourceFile.setSourcePath("/templates/bsp.c.ftl")
bspSourceFile.setOutputName("bsp.c")
bspSourceFile.setMarkup(True)
bspSourceFile.setOverwrite(True)
bspSourceFile.setDestPath("bsp/")
bspSourceFile.setProjectPath("config/" + configName + "/bsp/")
bspSourceFile.setType("SOURCE")

bspHeaderFile = bspComponent.createFileSymbol("BSP_H", None)
bspHeaderFile.setSourcePath("/templates/bsp.h.ftl")
bspHeaderFile.setOutputName("bsp.h")
bspHeaderFile.setMarkup(True)
bspHeaderFile.setOverwrite(True)
bspHeaderFile.setDestPath("bsp/")
bspHeaderFile.setProjectPath("config/" + configName + "/bsp/")
bspHeaderFile.setType("HEADER")
