# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2023 Microchip Technology Inc. and its subsidiaries.
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
    # LED0: PD23
    Database.setSymbolValue("core", "PIN_57_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "PIN_57_FUNCTION_NAME", "LED0")
    Database.setSymbolValue("core", "PIN_57_DIR", "Out")
    Database.setSymbolValue("core", "PIN_57_LAT", "High")

    # LED1: PD29
    Database.setSymbolValue("core", "PIN_108_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "PIN_108_FUNCTION_NAME", "LED1")
    Database.setSymbolValue("core", "PIN_108_DIR", "Out")
    Database.setSymbolValue("core", "PIN_108_LAT", "High")

    #SW0: PA01
    Database.setSymbolValue("core", "PIN_99_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "PIN_99_FUNCTION_NAME", "SW0")
    Database.setSymbolValue("core", "PIN_99_PU", "True")
    Database.setSymbolValue("core", "PIN_99_DIR", "")

    #SW1: PA09
    Database.setSymbolValue("core", "PIN_75_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "PIN_75_FUNCTION_NAME", "SW1")
    Database.setSymbolValue("core", "PIN_75_PU", "True")
    Database.setSymbolValue("core", "PIN_75_DIR", "")

    BSP_NAME = "pic32cz_ca70_curiosity_ultra"

    pinAttributes = [{"attrib":"type", "symbol":"BSP_CUSTOM_TYPE", "label":"Type Name"},
        {"attrib":"mode", "symbol":"BSP_CUSTOM_MODE", "label":"Mode"},
        {"attrib":"dir", "symbol":"BSP_CUSTOM_DIR", "label":"Direction"},
        {"attrib":"lat", "symbol":"BSP_CUSTOM_LAT", "label":"Initial Latch Value"},
        {"attrib":"od", "symbol":"BSP_CUSTOM_OD", "label":"Open Drain"},
        {"attrib":"cn", "symbol":"BSP_CUSTOM_CN", "label":"Change Notice"},
        {"attrib":"pu", "symbol":"BSP_CUSTOM_PU", "label":"Pull Up"},
        {"attrib":"pd", "symbol":"BSP_CUSTOM_PD", "label":"Pull Down"},
        {"attrib":"int", "symbol":"BSP_CUSTOM_PIO_INTERRUPT", "label":"PIO Interrupt"}]

    pinTypes = [{"type":"LED_AH", "mode":"DIGITAL", "dir":"OUT"},
            {"type":"LED_AL", "mode":"DIGITAL", "dir":"OUT"},
            {"type":"SWITCH_AH", "mode":"DIGITAL"},
            {"type":"SWITCH_AL", "mode":"DIGITAL"},
            {"type":"VBUS_AH", "mode":"DIGITAL", "dir":"OUT"},
            {"type":"VBUS_AL", "mode":"DIGITAL", "dir":"OUT"}]


    execfile(Variables.get("__BSP_DIR") + "/boards/config/bsp_common.py")




