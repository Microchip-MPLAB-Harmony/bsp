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

    # LED YELLOW: RK13 (16)
    Database.setSymbolValue("core", "BSP_PIN_16_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_16_FUNCTION_NAME", "LED_YELLOW")    
    Database.setSymbolValue("core", "BSP_PIN_16_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_16_LAT", "High")
    
    # LED RED: RK12 (15)
    Database.setSymbolValue("core", "BSP_PIN_15_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_15_FUNCTION_NAME", "LED_RED")    
    Database.setSymbolValue("core", "BSP_PIN_15_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_15_LAT", "High")
    
    # LED GREEN: RK14 (17)
    Database.setSymbolValue("core", "BSP_PIN_17_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_17_FUNCTION_NAME", "LED_GREEN")    
    Database.setSymbolValue("core", "BSP_PIN_17_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_17_LAT", "High")
    
    # LED BLUE: RC9 (18)
    Database.setSymbolValue("core", "BSP_PIN_18_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_18_FUNCTION_NAME", "LED_BLUE")
    Database.setSymbolValue("core", "BSP_PIN_18_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_18_LAT", "High")

    #Switch 1: RA10 (41)
    Database.setSymbolValue("core", "BSP_PIN_41_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_41_FUNCTION_NAME", "SWITCH1")    
    Database.setSymbolValue("core", "BSP_PIN_41_MODE", "DIGITAL")    

    #Switch 2: RB8 (47)
    Database.setSymbolValue("core", "BSP_PIN_47_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_47_FUNCTION_NAME", "SWITCH2")    
    Database.setSymbolValue("core", "BSP_PIN_47_MODE", "DIGITAL")    

    #I2C1: (For Onboard Sensors)
    #SCL1: RA4 (33)
    Database.setSymbolValue("core", "BSP_PIN_33_FUNCTION_TYPE", "SCL1")   
    #SDA1: RA5 (32)
    Database.setSymbolValue("core", "BSP_PIN_32_FUNCTION_TYPE", "SDA1")
    
    #SPI1: (For Onboard Serial Flash)
    #SPI1_CS: RA1 (20)
    Database.setSymbolValue("core", "BSP_PIN_20_FUNCTION_TYPE", "GPIO")
    Database.setSymbolValue("core", "BSP_PIN_20_FUNCTION_NAME", "SPI1_CS")    
    Database.setSymbolValue("core", "BSP_PIN_20_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_20_LAT", "High")

    # DEVCFG0<ICESEL> In-Circuit Emulator/Debugger Communication Channel Select bits
    Database.setSymbolValue("core", "CONFIG_ICESEL", "ICS_PGx2")

    BSP_NAME = "wfi32e_iot"

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
