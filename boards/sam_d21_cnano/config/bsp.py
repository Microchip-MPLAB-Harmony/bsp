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

    #LED PB10
    Database.setSymbolValue("core", "PIN_19_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "PIN_19_FUNCTION_NAME", "LED")
    Database.setSymbolValue("core", "PIN_19_LAT", "High")
    Database.setSymbolValue("core", "PIN_19_DIR", "Out")

    #Switch PB11
    Database.setSymbolValue("core", "PIN_20_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "PIN_20_FUNCTION_NAME", "SWITCH")
    Database.setSymbolValue("core", "PIN_20_PULLEN", "True")
    Database.setSymbolValue("core", "PIN_20_LAT", "High")
    Database.setSymbolValue("core", "PIN_20_INEN", "True")

    BSP_NAME = "sam_d21_cnano"

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
