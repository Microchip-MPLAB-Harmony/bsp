def instantiateComponent(bspComponent):
    # LED1: PA05
    Database.setSymbolValue("core", "PIN_18_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "PIN_18_FUNCTION_NAME", "LED1")
    Database.setSymbolValue("core", "PIN_18_DIR", "Out")
    Database.setSymbolValue("core", "PIN_18_LAT", "High")

    # LED2: PB08
    Database.setSymbolValue("core", "PIN_15_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "PIN_15_FUNCTION_NAME", "LED2")
    Database.setSymbolValue("core", "PIN_15_DIR", "Out")
    Database.setSymbolValue("core", "PIN_15_LAT", "High")

    #Switch: PA11
    Database.setSymbolValue("core", "PIN_29_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "PIN_29_FUNCTION_NAME", "SWITCH")
    Database.setSymbolValue("core", "PIN_29_PU", "True")
    Database.setSymbolValue("core", "PIN_29_DIR", "")

    BSP_NAME = "sam_e70_xult"

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




