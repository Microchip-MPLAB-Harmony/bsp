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

    # LED R: RC1
    Database.setSymbolValue("core", "BSP_PIN_17_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_17_FUNCTION_NAME", "RGB_LED_R")
    Database.setSymbolValue("core", "BSP_PIN_17_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_17_DIR", "Out")

    # LED G: RC4
    Database.setSymbolValue("core", "BSP_PIN_16_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_16_FUNCTION_NAME", "RGB_LED_G")
    Database.setSymbolValue("core", "BSP_PIN_16_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_16_DIR", "Out")

    # LED B: RB1
    Database.setSymbolValue("core", "BSP_PIN_11_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "BSP_PIN_11_FUNCTION_NAME", "RGB_LED_B")
    Database.setSymbolValue("core", "BSP_PIN_11_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_11_DIR", "Out")

    #Switch 1: RB11
    Database.setSymbolValue("core", "BSP_PIN_12_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_12_FUNCTION_NAME", "SWITCH1")
    Database.setSymbolValue("core", "BSP_PIN_12_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_12_DIR", "In")

    # Switch 2: RG15
    Database.setSymbolValue("core", "BSP_PIN_34_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_34_FUNCTION_NAME", "SWITCH2")
    Database.setSymbolValue("core", "BSP_PIN_34_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_34_DIR", "In")

    # Switch 3: RH12
    Database.setSymbolValue("core", "BSP_PIN_105_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_105_FUNCTION_NAME", "SWITCH3")
    Database.setSymbolValue("core", "BSP_PIN_105_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_105_DIR", "In")

    # Switch 4: RB13
    Database.setSymbolValue("core", "BSP_PIN_9_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_9_FUNCTION_NAME", "SWITCH4")
    Database.setSymbolValue("core", "BSP_PIN_9_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_9_DIR", "In")

    # Switch CW: RC2
    Database.setSymbolValue("core", "BSP_PIN_14_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_14_FUNCTION_NAME", "SWITCH_CW")
    Database.setSymbolValue("core", "BSP_PIN_14_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_14_DIR", "In")

    # Switch CCW: RC3
    Database.setSymbolValue("core", "BSP_PIN_15_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "BSP_PIN_15_FUNCTION_NAME", "SWITCH_CCW")
    Database.setSymbolValue("core", "BSP_PIN_15_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_15_DIR", "In")

    # Display CSX: RB12
    Database.setSymbolValue("core", "BSP_PIN_171_FUNCTION_TYPE", "GPIO")
    Database.setSymbolValue("core", "BSP_PIN_171_FUNCTION_NAME", "CSX")
    Database.setSymbolValue("core", "BSP_PIN_171_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_171_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_171_PU", "True")

    # Display SCK: RB14
    Database.setSymbolValue("core", "BSP_PIN_159_FUNCTION_TYPE", "GPIO")
    Database.setSymbolValue("core", "BSP_PIN_159_FUNCTION_NAME", "SCK")
    Database.setSymbolValue("core", "BSP_PIN_159_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_159_DIR", "Out")

    # Display SDO: RD14
    Database.setSymbolValue("core", "BSP_PIN_158_FUNCTION_TYPE", "GPIO")
    Database.setSymbolValue("core", "BSP_PIN_158_FUNCTION_NAME", "SDO")
    Database.setSymbolValue("core", "BSP_PIN_158_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_158_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_158_PU", "True")

    # Display RESX: RD10
    Database.setSymbolValue("core", "BSP_PIN_77_FUNCTION_TYPE", "GPIO")
    Database.setSymbolValue("core", "BSP_PIN_77_FUNCTION_NAME", "RESX")
    Database.setSymbolValue("core", "BSP_PIN_77_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_77_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_77_PU", "True")

    # Display Enable: RK1
    Database.setSymbolValue("core", "BSP_PIN_136_FUNCTION_TYPE", "GPIO")
    Database.setSymbolValue("core", "BSP_PIN_136_FUNCTION_NAME", "DISPLAY_ENABLE")
    Database.setSymbolValue("core", "BSP_PIN_136_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_136_PU", "True")
    Database.setSymbolValue("core", "BSP_PIN_136_DIR", "Out")

    # Display Backlight Type 1: RD0
    Database.setSymbolValue("core", "BSP_PIN_79_FUNCTION_TYPE", "GPIO")
    Database.setSymbolValue("core", "BSP_PIN_79_FUNCTION_NAME", "BACKLIGHT_TYPE_1")
    Database.setSymbolValue("core", "BSP_PIN_79_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_79_DIR", "Out")

    # Display Backlight Type 2: RD7
    Database.setSymbolValue("core", "BSP_PIN_120_FUNCTION_TYPE", "GPIO")
    Database.setSymbolValue("core", "BSP_PIN_120_FUNCTION_NAME", "BACKLIGHT_TYPE_2")
    Database.setSymbolValue("core", "BSP_PIN_120_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_120_DIR", "Out")

    # UART4_TX : RF12
    Database.setSymbolValue("core", "BSP_PIN_27_FUNCTION_TYPE", "U4TX")
    Database.setSymbolValue("core", "BSP_PIN_27_FUNCTION_NAME", "UART4_TX")
    Database.setSymbolValue("core", "BSP_PIN_27_PU", "True")

    # UART4_RX : RG9
    Database.setSymbolValue("core", "BSP_PIN_33_FUNCTION_TYPE", "U4RX")
    Database.setSymbolValue("core", "BSP_PIN_33_FUNCTION_NAME", "UART4_RX")
    Database.setSymbolValue("core", "BSP_PIN_33_PU", "True")

    # WDRV_WINC_RESETN : RH6
    Database.setSymbolValue("core", "BSP_PIN_101_FUNCTION_TYPE", "GPIO")
    Database.setSymbolValue("core", "BSP_PIN_101_FUNCTION_NAME", "WDRV_WINC_RESETN")
    Database.setSymbolValue("core", "BSP_PIN_101_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_101_DIR", "Out")
    Database.setSymbolValue("core", "BSP_PIN_101_PU", "True")

    # WDRV_WINC_CHIP_EN : RH11
    Database.setSymbolValue("core", "BSP_PIN_138_FUNCTION_TYPE", "GPIO")
    Database.setSymbolValue("core", "BSP_PIN_138_FUNCTION_NAME", "WDRV_WINC_CHIP_EN")
    Database.setSymbolValue("core", "BSP_PIN_138_MODE", "DIGITAL")
    Database.setSymbolValue("core", "BSP_PIN_138_DIR", "Out")

    # SDHC Setup

    # SDCD : RA0
    Database.setSymbolValue("core", "BSP_PIN_53_FUNCTION_TYPE", "SDCD")
    Database.setSymbolValue("core", "BSP_PIN_53_FUNCTION_NAME", "SDCD")
    Database.setSymbolValue("core", "BSP_PIN_53_PU", "True")

    # SDCK : RA6
    Database.setSymbolValue("core", "BSP_PIN_54_FUNCTION_TYPE", "SDCK")
    Database.setSymbolValue("core", "BSP_PIN_54_FUNCTION_NAME", "SDCK")
    Database.setSymbolValue("core", "BSP_PIN_54_PU", "")

    # SDDATA3 : RA7
    Database.setSymbolValue("core", "BSP_PIN_55_FUNCTION_TYPE", "SDDATA3")
    Database.setSymbolValue("core", "BSP_PIN_55_FUNCTION_NAME", "SDDATA3")
    Database.setSymbolValue("core", "BSP_PIN_55_PU", "")

    # SDDATA1 : RG12
    Database.setSymbolValue("core", "BSP_PIN_56_FUNCTION_TYPE", "SDDATA1")
    Database.setSymbolValue("core", "BSP_PIN_56_FUNCTION_NAME", "SDDATA1")
    Database.setSymbolValue("core", "BSP_PIN_56_PU", "")

    # SDDATA0 : RG13
    Database.setSymbolValue("core", "BSP_PIN_64_FUNCTION_TYPE", "SDDATA0")
    Database.setSymbolValue("core", "BSP_PIN_64_FUNCTION_NAME", "SDDATA0")
    Database.setSymbolValue("core", "BSP_PIN_64_PU", "")

    # SDDATA2 : RG14
    Database.setSymbolValue("core", "BSP_PIN_65_FUNCTION_TYPE", "SDDATA2")
    Database.setSymbolValue("core", "BSP_PIN_65_FUNCTION_NAME", "SDDATA2")
    Database.setSymbolValue("core", "BSP_PIN_65_PU", "")

    # SDCMD : RD4
    Database.setSymbolValue("core", "BSP_PIN_70_FUNCTION_TYPE", "SDCMD")
    Database.setSymbolValue("core", "BSP_PIN_70_FUNCTION_NAME", "SDCMD")
    Database.setSymbolValue("core", "BSP_PIN_70_PU", "")

    # DEVCFG0<ICESEL> In-Circuit Emulator/Debugger Communication Channel Select bits
    Database.setSymbolValue("core", "CONFIG_ICESEL", "ICS_PGx2")

    BSP_NAME = "pic32mz_da_radial_board"

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
