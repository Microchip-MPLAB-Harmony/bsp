def instantiateComponent(bspComponent):

    #LED 1
    Database.setSymbolValue("core", "PIN_75_FUNCTION_NAME", "LED1")
    Database.setSymbolValue("core", "PIN_75_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "PIN_75_LAT", "High")
    Database.setSymbolValue("core", "PIN_75_DIR", "Out")
    
    #LED 2
    Database.setSymbolValue("core", "PIN_66_FUNCTION_NAME", "LED2")
    Database.setSymbolValue("core", "PIN_66_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "PIN_66_LAT", "High")
    Database.setSymbolValue("core", "PIN_66_DIR", "Out")

    #SW 1
    Database.setSymbolValue("core", "PIN_13_FUNCTION_NAME", "SWITCH1")
    Database.setSymbolValue("core", "PIN_13_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "PIN_13_PULLEN", "True")
    Database.setSymbolValue("core", "PIN_13_LAT", "High")
    Database.setSymbolValue("core", "PIN_13_INEN", "True")
    
    #SW 2
    Database.setSymbolValue("core", "PIN_16_FUNCTION_NAME", "SWITCH2")
    Database.setSymbolValue("core", "PIN_16_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "PIN_16_PULLEN", "True")
    Database.setSymbolValue("core", "PIN_16_LAT", "High")
    Database.setSymbolValue("core", "PIN_16_INEN", "True")

    BSP_NAME = "pic32cx_sg6x_curiosity_ultra"

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
