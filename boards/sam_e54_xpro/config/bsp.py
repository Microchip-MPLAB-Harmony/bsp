def instantiateComponent(bspComponent):

    #LED
    Database.setSymbolValue("core", "PIN_72_FUNCTION_NAME", "LED")
    Database.setSymbolValue("core", "PIN_72_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "PIN_72_LAT", "High")

    #Switch
    Database.setSymbolValue("core", "PIN_122_FUNCTION_NAME", "SWITCH")
    Database.setSymbolValue("core", "PIN_122_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "PIN_122_PULLEN", "True")

    BSP_NAME = "sam_e54_xpro"

    pinAttributes = [{"attrib":"type", "symbol":"BSP_CUSTOM_TYPE", "label":"Type Name"},
        {"attrib":"mode", "symbol":"BSP_CUSTOM_MODE", "label":"Mode"},
        {"attrib":"dir", "symbol":"BSP_CUSTOM_DIR", "label":"Direction"},
        {"attrib":"lat", "symbol":"BSP_CUSTOM_LAT", "label":"Initial Latch Value"},
        {"attrib":"pe", "symbol":"BSP_CUSTOM_PE", "label":"Pull Enable"},
        {"attrib":"ie", "symbol":"BSP_CUSTOM_IE", "label":"Input Enable"}]

    pinTypes = [{"type":"LED_AH", "mode":"DIGITAL", "dir":"OUT"},
            {"type":"LED_AL", "mode":"DIGITAL", "dir":"OUT"},
            {"type":"SWITCH_AH", "mode":"DIGITAL"},
            {"type":"SWITCH_AL", "mode":"DIGITAL"}]

    execfile(Variables.get("__BSP_DIR") + "/boards/config/bsp_common.py")
