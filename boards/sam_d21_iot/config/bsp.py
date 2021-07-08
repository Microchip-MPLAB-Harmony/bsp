# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2020 Microchip Technology Inc. and its subsidiaries.
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

    #RED LED PA25
    Database.setSymbolValue("core", "PIN_34_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "PIN_34_FUNCTION_NAME", "LED_RED")
    Database.setSymbolValue("core", "PIN_34_LAT", "High")
    Database.setSymbolValue("core", "PIN_34_DIR", "Out")

    #YELLOW LED PA11
    Database.setSymbolValue("core", "PIN_16_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "PIN_16_FUNCTION_NAME", "LED_YELLOW")
    Database.setSymbolValue("core", "PIN_16_LAT", "High")
    Database.setSymbolValue("core", "PIN_16_DIR", "Out")

    #GREEN LED PA20
    Database.setSymbolValue("core", "PIN_29_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "PIN_29_FUNCTION_NAME", "LED_GREEN")
    Database.setSymbolValue("core", "PIN_29_LAT", "High")
    Database.setSymbolValue("core", "PIN_29_DIR", "Out")

    #BLUE LED PA21
    Database.setSymbolValue("core", "PIN_30_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "PIN_30_FUNCTION_NAME", "LED_BLUE")
    Database.setSymbolValue("core", "PIN_30_LAT", "High")
    Database.setSymbolValue("core", "PIN_30_DIR", "Out")

    #SW0 PA00
    Database.setSymbolValue("core", "PIN_1_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "PIN_1_FUNCTION_NAME", "SW0")
    Database.setSymbolValue("core", "PIN_1_PULLEN", "True")
    Database.setSymbolValue("core", "PIN_1_LAT", "High")
    Database.setSymbolValue("core", "PIN_1_INEN", "True")

    #SW1 PA01
    Database.setSymbolValue("core", "PIN_2_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "PIN_2_FUNCTION_NAME", "SW1")
    Database.setSymbolValue("core", "PIN_2_PULLEN", "True")
    Database.setSymbolValue("core", "PIN_2_LAT", "High")
    Database.setSymbolValue("core", "PIN_2_INEN", "True")

    BSP_NAME = "sam_d21_iot"

    pinAttributes = [{"attrib":"type", "symbol":"BSP_CUSTOM_TYPE", "label":"Type Name"},
        {"attrib":"mode", "symbol":"BSP_CUSTOM_MODE", "label":"Mode"},
        {"attrib":"dir", "symbol":"BSP_CUSTOM_DIR", "label":"Direction"},
        {"attrib":"lat", "symbol":"BSP_CUSTOM_LAT", "label":"Initial Latch Value"},
        {"attrib":"pe", "symbol":"BSP_CUSTOM_PE", "label":"Pull Enable"},
        {"attrib":"ie", "symbol":"BSP_CUSTOM_IE", "label":"Input Enable"}]

    pinTypes = [{"type":"LED_AH", "mode":"DIGITAL", "dir":"OUT"},
            {"type":"LED_AL", "mode":"DIGITAL", "dir":"OUT", "lat":"High"},
            {"type":"SWITCH_AH", "mode":"DIGITAL", "ie":"True"},
            {"type":"SWITCH_AL", "mode":"DIGITAL", "ie":"True"}]

    execfile(Variables.get("__BSP_DIR") + "/boards/config/bsp_common.py")
