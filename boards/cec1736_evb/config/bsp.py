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

def instantiateComponent(bspComponent):

    #LED 4 (GPIO 3, C6, index=24)
    Database.setSymbolValue("core", "PIN_24_FUNCTION_TYPE", "LED_AH")
    Database.setSymbolValue("core", "PIN_24_FUNCTION_NAME", "LED4")
    Database.setSymbolValue("core", "PIN_24_LAT", "Low")
    Database.setSymbolValue("core", "PIN_24_DIR", "Out")

    #LED 5 (GPIO 157, H1, index=59)
    Database.setSymbolValue("core", "PIN_59_FUNCTION_TYPE", "LED_AH")
    Database.setSymbolValue("core", "PIN_59_FUNCTION_NAME", "LED5")
    Database.setSymbolValue("core", "PIN_59_LAT", "Low")
    Database.setSymbolValue("core", "PIN_59_DIR", "Out")

    #LED 6 (GPIO 156, H2, index=60)
    Database.setSymbolValue("core", "PIN_60_FUNCTION_TYPE", "LED_AH")
    Database.setSymbolValue("core", "PIN_60_FUNCTION_NAME", "LED6")
    Database.setSymbolValue("core", "PIN_60_LAT", "Low")
    Database.setSymbolValue("core", "PIN_60_DIR", "Out")

    BSP_NAME = "cec1736_evb"

    pinAttributes = [{"attrib":"type", "symbol":"BSP_CUSTOM_TYPE", "label":"Type Name"},
        {"attrib":"dir", "symbol":"BSP_CUSTOM_DIR", "label":"Direction"},
        {"attrib":"lat", "symbol":"BSP_CUSTOM_LAT", "label":"Initial Latch Value"},
        {"attrib":"pe", "symbol":"BSP_CUSTOM_PE", "label":"Pull Enable"}]

    pinTypes = [{"type":"LED_AH", "mode":"DIGITAL", "dir":"OUT", "lat":"Low"},
            {"type":"LED_AL", "mode":"DIGITAL", "dir":"OUT", "lat":"High"},
            {"type":"SWITCH_AH", "mode":"DIGITAL", "ie":"True"},
            {"type":"SWITCH_AL", "mode":"DIGITAL", "ie":"True"}]

    execfile(Variables.get("__BSP_DIR") + "/boards/config/bsp_common.py")
