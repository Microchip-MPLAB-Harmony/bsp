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

    # LED 1: RJ7
    Database.setSymbolValue("core", "BSP_PIN_134_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_134_FUNCTION_NAME", "LED1")

    # LED 2: RK7
    Database.setSymbolValue("core", "BSP_PIN_126_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_126_FUNCTION_NAME", "LED2")

    # LED 3: RJ3
    Database.setSymbolValue("core", "BSP_PIN_117_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_117_FUNCTION_NAME", "LED3")

    # LED R: RB7
    Database.setSymbolValue("core", "BSP_PIN_38_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_38_FUNCTION_NAME", "RGB_LED_R")

    # LED G: RB8
    Database.setSymbolValue("core", "BSP_PIN_47_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_47_FUNCTION_NAME", "RGB_LED_G")

    # LED B: RB9
    Database.setSymbolValue("core", "BSP_PIN_48_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_48_FUNCTION_NAME", "RGB_LED_B")

    #Switch 1: RJ4
    Database.setSymbolValue("core", "BSP_PIN_131_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_131_FUNCTION_NAME", "SWITCH1")

    # Switch 2: RJ5
    Database.setSymbolValue("core", "BSP_PIN_132_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_132_FUNCTION_NAME", "SWITCH2")

    # Switch 3: RJ6
    Database.setSymbolValue("core", "BSP_PIN_133_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_133_FUNCTION_NAME", "SWITCH3")

    # Switch 4: RC14
    Database.setSymbolValue("core", "BSP_PIN_72_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_72_FUNCTION_NAME", "SWITCH4")

    # DEVCFG0<ICESEL> In-Circuit Emulator/Debugger Communication Channel Select bits
    Database.setSymbolValue("core", "CONFIG_ICESEL", "ICS_PGx2")

    BSP_NAME = "pic32mz_ef_c2"

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
            {"type":"VBUS_AH", "mode":"DIGITAL", "dir":"OUT"},
            {"type":"VBUS_AL", "mode":"DIGITAL", "dir":"OUT","lat":"High"}]

    execfile(Variables.get("__BSP_DIR") + "/boards/config/bsp_common.py")
