def instantiateComponent(bspComponent):
    # LED 0
    Database.clearSymbolValue("core", "PIN_46_FUNCTION_NAME")
    Database.clearSymbolValue("core", "PIN_46_FUNCTION_TYPE")
    Database.clearSymbolValue("core", "PIN_46_LAT")

    Database.setSymbolValue("core", "PIN_46_FUNCTION_NAME", "LED0")
    Database.setSymbolValue("core", "PIN_46_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "PIN_46_LAT", "High")

    # LED 1
    Database.clearSymbolValue("core", "PIN_86_FUNCTION_NAME")
    Database.clearSymbolValue("core", "PIN_86_FUNCTION_TYPE")
    Database.clearSymbolValue("core", "PIN_86_LAT")

    Database.setSymbolValue("core", "PIN_86_FUNCTION_NAME", "LED1")
    Database.setSymbolValue("core", "PIN_86_FUNCTION_TYPE", "LED_AL")
    Database.setSymbolValue("core", "PIN_86_LAT", "High")

    #Switch 1
    Database.clearSymbolValue("core", "PIN_75_FUNCTION_NAME")
    Database.clearSymbolValue("core", "PIN_75_FUNCTION_TYPE")
    Database.clearSymbolValue("core", "PIN_75_PU")

    Database.setSymbolValue("core", "PIN_75_FUNCTION_NAME", "SWITCH1")
    Database.setSymbolValue("core", "PIN_75_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "PIN_75_PU", "True")

    #Switch 2
    Database.clearSymbolValue("core", "PIN_87_FUNCTION_NAME")
    Database.clearSymbolValue("core", "PIN_87_FUNCTION_TYPE")
    Database.clearSymbolValue("core", "PIN_87_PU")

    Database.setSymbolValue("core", "PIN_87_FUNCTION_NAME", "SWITCH2")
    Database.setSymbolValue("core", "PIN_87_FUNCTION_TYPE", "SWITCH_AL")
    Database.setSymbolValue("core", "PIN_87_PU", "True")
 
    # VBUS
    Database.clearSymbolValue("core", "PIN_100_FUNCTION_NAME")
    Database.clearSymbolValue("core", "PIN_100_FUNCTION_TYPE")

    Database.setSymbolValue("core", "PIN_100_FUNCTION_NAME", "VBUS_HOST_EN")
    Database.setSymbolValue("core", "PIN_100_FUNCTION_TYPE", "VBUS_AL")

    BSP_NAME = "sam_v71_xult"

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




