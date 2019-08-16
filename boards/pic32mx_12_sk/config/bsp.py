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

    # LED 1: RPC8
    Database.setSymbolValue("core", "BSP_PIN_4_FUNCTION_TYPE", "LED_AH")
    Database.setSymbolValue("core", "BSP_PIN_4_FUNCTION_NAME", "LED1")
    Database.setSymbolValue("core", "BSP_PIN_4_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_4_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_4_LAT", "")

    # LED 2: RA10
    Database.setSymbolValue("core", "BSP_PIN_12_FUNCTION_TYPE", "LED_AH")
    Database.setSymbolValue("core", "BSP_PIN_12_FUNCTION_NAME", "LED2")
    Database.setSymbolValue("core", "BSP_PIN_12_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_12_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_12_LAT", "")

    #Switch 1: RA9
    Database.setSymbolValue("core", "BSP_PIN_35_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_35_FUNCTION_NAME", "SWITCH1")
    Database.setSymbolValue("core", "BSP_PIN_35_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_35_PU", "True")
    Database.setSymbolValue("core", "BSP_PIN_35_DIR", "")

    # Switch 2: RPB4
    Database.setSymbolValue("core", "BSP_PIN_33_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_33_FUNCTION_NAME", "SWITCH2")
    Database.setSymbolValue("core", "BSP_PIN_33_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_33_PU", "True")
    Database.setSymbolValue("core", "BSP_PIN_33_DIR", "")

    # Switch 3: RA7
    Database.setSymbolValue("core", "BSP_PIN_13_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_13_FUNCTION_NAME", "SWITCH3")
    Database.setSymbolValue("core", "BSP_PIN_13_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_13_PU", "True")
    Database.setSymbolValue("core", "BSP_PIN_13_DIR", "")

    # DEVCFG0<ICESEL> In-Circuit Emulator/Debugger Communication Channel Select bits
    Database.setSymbolValue("core", "CONFIG_ICESEL", "ICS_PGx2")

    BSP_NAME = "pic32mx_12_sk"

    pinAttributes = [{"attrib":"type", "symbol":"BSP_CUSTOM_TYPE", "label":"Type Name"},
        {"attrib":"mode", "symbol":"BSP_CUSTOM_MODE", "label":"Mode"},
        {"attrib":"dir", "symbol":"BSP_CUSTOM_DIR", "label":"Direction"},
        {"attrib":"lat", "symbol":"BSP_CUSTOM_LAT", "label":"Initial Latch Value"},
        {"attrib":"od", "symbol":"BSP_CUSTOM_OD", "label":"Open Drain"},
        {"attrib":"cn", "symbol":"BSP_CUSTOM_CN", "label":"Change Notice"},
        {"attrib":"pu", "symbol":"BSP_CUSTOM_PU", "label":"Pull Up"},
        {"attrib":"pd", "symbol":"BSP_CUSTOM_PD", "label":"Pull Down"}]

    pinTypes = [{"type":"LED_AH", "mode":"DIGITAL", "dir":"OUT"},
            {"type":"LED_AL", "mode":"DIGITAL", "dir":"OUT", "lat":"High"},
            {"type":"SWITCH_AH", "mode":"DIGITAL"},
            {"type":"SWITCH_AL", "mode":"DIGITAL"},
            {"type":"VBUS_AH", "mode":"DIGITAL", "dir":"OUT"},
            {"type":"VBUS_AL", "mode":"DIGITAL", "dir":"OUT","lat":"High"}]

    execfile(Variables.get("__BSP_DIR") + "/boards/config/bsp_common.py")
