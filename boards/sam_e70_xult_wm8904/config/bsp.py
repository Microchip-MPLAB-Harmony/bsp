def instantiateComponent(bspComponent):
    # LED
    Database.clearSymbolValue("core", "PIN_82_FUNCTION_NAME")
    Database.clearSymbolValue("core", "PIN_82_FUNCTION_TYPE")
    Database.clearSymbolValue("core", "PIN_82_LAT")

    Database.setSymbolValue("core", "PIN_82_FUNCTION_NAME", "LED")
    Database.setSymbolValue("core", "PIN_82_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "PIN_82_LAT", "High")

    #Switch
    Database.clearSymbolValue("core", "PIN_64_FUNCTION_NAME")
    Database.clearSymbolValue("core", "PIN_64_FUNCTION_TYPE")
    Database.clearSymbolValue("core", "PIN_64_PU")

    Database.setSymbolValue("core", "PIN_64_FUNCTION_NAME", "SWITCH")
    Database.setSymbolValue("core", "PIN_64_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "PIN_64_PU", "True")

    #pin defintions for WM8904 codec in X32 socket
    Database.setSymbolValue("core", "PIN_91_FUNCTION_NAME", "TWIHS0_TWD0")      # PA3
    Database.setSymbolValue("core", "PIN_91_FUNCTION_TYPE", "TWIHS0_TWD0")

    Database.setSymbolValue("core", "PIN_77_FUNCTION_NAME", "TWIHS0_TWCK0")     # PA4
    Database.setSymbolValue("core", "PIN_77_FUNCTION_TYPE", "TWIHS0_TWCK0")

    Database.setSymbolValue("core", "PIN_66_FUNCTION_NAME", "SSC_RD")           # PA10
    Database.setSymbolValue("core", "PIN_66_FUNCTION_TYPE", "SSC_RD")

    Database.setSymbolValue("core", "PIN_24_FUNCTION_NAME", "PMC_PCK2")         # PA18
    Database.setSymbolValue("core", "PIN_24_FUNCTION_TYPE", "PMC_PCK2")

    Database.setSymbolValue("core", "PIN_21_FUNCTION_NAME", "SSC_TF")           # PB0
    Database.setSymbolValue("core", "PIN_21_FUNCTION_TYPE", "SSC_TF")

    Database.setSymbolValue("core", "PIN_20_FUNCTION_NAME", "SSC_TK")           # PB1
    Database.setSymbolValue("core", "PIN_20_FUNCTION_TYPE", "SSC_TK")

    Database.setSymbolValue("core", "PIN_53_FUNCTION_NAME", "SSC_TD")           # PD26
    Database.setSymbolValue("core", "PIN_53_FUNCTION_TYPE", "SSC_TD")

    BSP_NAME = "sam_e70_xult_wm8904"

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




