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

    # Red LED: RB6
    Database.setSymbolValue("core", "BSP_PIN_25_FUNCTION_TYPE", "LED_AH")
    Database.setSymbolValue("core", "BSP_PIN_25_FUNCTION_NAME", "RGB_LED_RED")
    Database.setSymbolValue("core", "BSP_PIN_25_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_25_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_25_LAT", "")

    # Green LED: RB7
  #  Database.setSymbolValue("core", "BSP_PIN_26_FUNCTION_TYPE", "LED_AH")
  #  Database.setSymbolValue("core", "BSP_PIN_26_FUNCTION_NAME", "RGB_LED_GREEN")
  #  Database.setSymbolValue("core", "BSP_PIN_26_MODE", "DIGITAL")
  #  Database.setSymbolValue("core", "BSP_PIN_26_DIR", "Out")
  #  Database.setSymbolValue("core", "BSP_PIN_26_LAT", "")

    # Blue LED: RB5
    Database.setSymbolValue("core", "BSP_PIN_24_FUNCTION_TYPE", "LED_AH")
    Database.setSymbolValue("core", "BSP_PIN_24_FUNCTION_NAME", "RGB_LED_BLUE")
    Database.setSymbolValue("core", "BSP_PIN_24_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_24_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_24_LAT", "")

    # User LED: RB7, multiplexed with Green LED
    Database.setSymbolValue("core", "BSP_PIN_26_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_26_FUNCTION_NAME", "USER_LED")
    Database.setSymbolValue("core", "BSP_PIN_26_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_26_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_26_LAT", "High")

    # User Button 1, SW2: RB9
    Database.setSymbolValue("core", "BSP_PIN_9_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_9_FUNCTION_NAME", "USER_BUTTON_1")
    Database.setSymbolValue("core", "BSP_PIN_9_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_9_PU", "True")
    Database.setSymbolValue("core", "BSP_PIN_9_DIR", "")

    BSP_NAME = "pic32cx_bz350_curiosity"

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
