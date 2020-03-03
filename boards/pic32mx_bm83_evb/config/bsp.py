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

    # LED 1: RF13
    Database.setSymbolValue("core", "BSP_PIN_39_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_39_FUNCTION_NAME", "LED1")
    Database.setSymbolValue("core", "BSP_PIN_39_MODE", "DIGITAL")

    # LED 2: RF12
    Database.setSymbolValue("core", "BSP_PIN_40_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_40_FUNCTION_NAME", "LED2")
    Database.setSymbolValue("core", "BSP_PIN_40_MODE", "DIGITAL")

    # LED 3: RB12
    Database.setSymbolValue("core", "BSP_PIN_41_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_41_FUNCTION_NAME", "LED3")
    Database.setSymbolValue("core", "BSP_PIN_41_MODE", "DIGITAL")

    # LED 4: RB13
    Database.setSymbolValue("core", "BSP_PIN_42_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_42_FUNCTION_NAME", "LED4")
    Database.setSymbolValue("core", "BSP_PIN_42_MODE", "DIGITAL")

    # LED 5: RB14
    Database.setSymbolValue("core", "BSP_PIN_43_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_43_FUNCTION_NAME", "LED5")
    Database.setSymbolValue("core", "BSP_PIN_43_MODE", "DIGITAL")

    # LED 6: RB15
    Database.setSymbolValue("core", "BSP_PIN_44_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_44_FUNCTION_NAME", "LED6")
    Database.setSymbolValue("core", "BSP_PIN_44_MODE", "DIGITAL")

    # LED 7: RD14
    Database.setSymbolValue("core", "BSP_PIN_47_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_47_FUNCTION_NAME", "LED7")
    Database.setSymbolValue("core", "BSP_PIN_47_MODE", "DIGITAL")

    # LED 8: RD15
    Database.setSymbolValue("core", "BSP_PIN_48_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_48_FUNCTION_NAME", "LED8")
    Database.setSymbolValue("core", "BSP_PIN_48_MODE", "DIGITAL")

    # Switch 1: RB11 VOL_UP
    Database.setSymbolValue("core", "BSP_PIN_35_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_35_FUNCTION_NAME", "SWITCH1")
    Database.setSymbolValue("core", "BSP_PIN_35_PU", "True")
    Database.setSymbolValue("core", "BSP_PIN_35_MODE", "DIGITAL")

    # Switch 2: RE9  PAIRING
    Database.setSymbolValue("core", "BSP_PIN_19_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_19_FUNCTION_NAME", "SWITCH2")
    Database.setSymbolValue("core", "BSP_PIN_19_PU", "True")
    Database.setSymbolValue("core", "BSP_PIN_19_MODE", "DIGITAL")

    # Switch 3: RA10 PLAY/PAUSE
    Database.setSymbolValue("core", "BSP_PIN_29_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_29_FUNCTION_NAME", "SWITCH3")
    Database.setSymbolValue("core", "BSP_PIN_29_PU", "True")
    Database.setSymbolValue("core", "BSP_PIN_29_MODE", "DIGITAL")

    # Switch 4: RB10 VOL_DN
    Database.setSymbolValue("core", "BSP_PIN_34_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_34_FUNCTION_NAME", "SWITCH4")
    Database.setSymbolValue("core", "BSP_PIN_34_PU", "True")
    Database.setSymbolValue("core", "BSP_PIN_34_MODE", "DIGITAL")

    # Switch 5: RB3  SEL
    Database.setSymbolValue("core", "BSP_PIN_22_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_22_FUNCTION_NAME", "SWITCH5")
    Database.setSymbolValue("core", "BSP_PIN_22_PU", "True")
    Database.setSymbolValue("core", "BSP_PIN_22_MODE", "DIGITAL")

    # Switch 6: RB9  FWD
    Database.setSymbolValue("core", "BSP_PIN_33_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_33_FUNCTION_NAME", "SWITCH6")
    Database.setSymbolValue("core", "BSP_PIN_33_PU", "True")
    Database.setSymbolValue("core", "BSP_PIN_33_MODE", "DIGITAL")

    # Switch 7: RB8  REV
    Database.setSymbolValue("core", "BSP_PIN_32_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_32_FUNCTION_NAME", "SWITCH7")
    Database.setSymbolValue("core", "BSP_PIN_32_PU", "True")
    Database.setSymbolValue("core", "BSP_PIN_32_MODE", "DIGITAL")

    # DEVCFG0<ICESEL> In-Circuit Emulator/Debugger Communication Channel Select bits
    Database.setSymbolValue("core", "CONFIG_ICESEL", "ICS_PGx1")

    BSP_NAME = "pic32mx_bm83_evb"

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
