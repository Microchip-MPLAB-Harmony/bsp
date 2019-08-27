"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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

def instantiateComponent(bspComponent):

    # LED 1: RA4
    Database.setSymbolValue("core", "BSP_PIN_60_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_60_FUNCTION_NAME", "LED1")

    # LED 2: RA5
    Database.setSymbolValue("core", "BSP_PIN_61_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_61_FUNCTION_NAME", "LED2")

    # LED 3: RA6
    Database.setSymbolValue("core", "BSP_PIN_91_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_91_FUNCTION_NAME", "LED3")

    # LED 4: RA7
    Database.setSymbolValue("core", "BSP_PIN_92_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_92_FUNCTION_NAME", "LED4")

    # LED 5: RA9
    Database.setSymbolValue("core", "BSP_PIN_28_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_28_FUNCTION_NAME", "LED5")

    #Switch 1: RA0
    Database.setSymbolValue("core", "BSP_PIN_17_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_17_FUNCTION_NAME", "SWITCH1")

    # Switch 2: RA1
    Database.setSymbolValue("core", "BSP_PIN_38_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_38_FUNCTION_NAME", "SWITCH2")

    # Switch 3: RA10
    Database.setSymbolValue("core", "BSP_PIN_29_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_29_FUNCTION_NAME", "SWITCH3")

    # Switch 4: RB12
    Database.setSymbolValue("core", "BSP_PIN_41_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_41_FUNCTION_NAME", "SWITCH4")

    # Switch 5: RB13
    Database.setSymbolValue("core", "BSP_PIN_42_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_42_FUNCTION_NAME", "SWITCH5")

    # Switch 6: RB14
    Database.setSymbolValue("core", "BSP_PIN_43_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_43_FUNCTION_NAME", "SWITCH6")

    # USB SEL0: RG0
    Database.setSymbolValue("core", "BSP_PIN_90_FUNCTION_TYPE", "GPIO_AH")
    Database.setSymbolValue("core", "BSP_PIN_90_FUNCTION_NAME", "USB_SEL0")

    # USB SEL1: RG1
    Database.setSymbolValue("core", "BSP_PIN_89_FUNCTION_TYPE", "GPIO_AH")
    Database.setSymbolValue("core", "BSP_PIN_89_FUNCTION_NAME", "USB_SEL1")

    # DEVCFG0<ICESEL> In-Circuit Emulator/Debugger Communication Channel Select bits
    Database.setSymbolValue("core", "CONFIG_ICESEL", "ICS_PGx2")

    BSP_NAME = "pic32mx_btadk"

    pinAttributes = [{"attrib":"type", "symbol":"BSP_CUSTOM_TYPE", "label":"Type Name"},
        {"attrib":"mode", "symbol":"BSP_CUSTOM_MODE", "label":"Mode"},
        {"attrib":"dir", "symbol":"BSP_CUSTOM_DIR", "label":"Direction"},
        {"attrib":"lat", "symbol":"BSP_CUSTOM_LAT", "label":"Initial Latch Value"},
        {"attrib":"od", "symbol":"BSP_CUSTOM_OD", "label":"Open Drain"},
        {"attrib":"cn", "symbol":"BSP_CUSTOM_CN", "label":"Change Notice"},
        {"attrib":"pu", "symbol":"BSP_CUSTOM_PU", "label":"Pull Up"},
        {"attrib":"pd", "symbol":"BSP_CUSTOM_PD", "label":"Pull Down"}]

    pinTypes = [{"type":"LED_AH", "mode":"DIGITAL", "dir":"OUT", "lat":"Low"},
            {"type":"LED_AL", "mode":"DIGITAL", "dir":"OUT", "lat":"High", "od":"True"},
            {"type":"SWITCH_AH", "mode":"DIGITAL", "dir":"IN"},
            {"type":"SWITCH_AL", "mode":"DIGITAL", "dir":"IN"},
            {"type":"GPIO_AH", "mode":"DIGITAL", "dir":"OUT"},
            {"type":"GPIO_AL", "mode":"DIGITAL", "dir":"OUT","lat":"High"}]

    execfile(Variables.get("__BSP_DIR") + "/boards/config/bsp_common.py")
