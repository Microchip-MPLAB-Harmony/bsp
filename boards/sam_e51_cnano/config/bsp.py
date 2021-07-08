def instantiateComponent(bspComponent):

    #LED PA14
    Database.setSymbolValue("core", "PIN_31_FUNCTION_NAME", "LED0")
    Database.setSymbolValue("core", "PIN_31_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "PIN_31_LAT", "High")
    Database.setSymbolValue("core", "PIN_31_DIR", "Out")

    #Switch PA15
    Database.setSymbolValue("core", "PIN_32_FUNCTION_NAME", "SW0")
    Database.setSymbolValue("core", "PIN_32_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "PIN_32_PULLEN", "True")
    Database.setSymbolValue("core", "PIN_32_LAT", "High")
    Database.setSymbolValue("core", "PIN_32_INEN", "True")

    BSP_NAME = "sam_e51_cnano"

    pinAttributes = [{"attrib":"type", "symbol":"BSP_CUSTOM_TYPE", "label":"Type Name"},
        {"attrib":"mode", "symbol":"BSP_CUSTOM_MODE", "label":"Mode"},
        {"attrib":"dir", "symbol":"BSP_CUSTOM_DIR", "label":"Direction"},
        {"attrib":"lat", "symbol":"BSP_CUSTOM_LAT", "label":"Initial Latch Value"},
        {"attrib":"pe", "symbol":"BSP_CUSTOM_PE", "label":"Pull Enable"},
        {"attrib":"ie", "symbol":"BSP_CUSTOM_IE", "label":"Input Enable"}]

    pinTypes = [{"type":"LED_AH", "mode":"DIGITAL", "dir":"OUT"},
            {"type":"LED_AL", "mode":"DIGITAL", "dir":"OUT", "lat":"High"},
            {"type":"SWITCH_AH", "mode":"DIGITAL", "ie":"True"},
            {"type":"SWITCH_AL", "mode":"DIGITAL", "ie":"True"},
            {"type":"VBUS_AH", "mode":"DIGITAL", "dir":"OUT"},
            {"type":"VBUS_AL", "mode":"DIGITAL", "dir":"OUT", "lat":"High"}]

    execfile(Variables.get("__BSP_DIR") + "/boards/config/bsp_common.py")
