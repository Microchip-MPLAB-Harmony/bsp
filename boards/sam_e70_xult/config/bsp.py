def instantiateComponent(bspComponent):

# LED
	Database.clearSymbolValue("core", "PIN_82_FUNCTION_NAME")
	Database.clearSymbolValue("core", "PIN_82_FUNCTION_TYPE")
	Database.clearSymbolValue("core", "PIN_82_PIO_PIN")
	Database.clearSymbolValue("core", "PIN_82_PIO_CHANNEL")
	Database.clearSymbolValue("core", "PIN_82_DIR")

#	Database.setSymbolValue("core", "PIN_82_FUNCTION_NAME", "LED", 2)
#	Database.setSymbolValue("core", "PIN_82_FUNCTION_TYPE", "LED_AL", 2)
	Database.setSymbolValue("core", "PIN_82_PIO_PIN", 8, 2)
#	Database.setSymbolValue("core", "PIN_82_PIO_CHANNEL", "C", 2)
#	Database.setSymbolValue("core", "PIN_82_DIR", OUT, "2")

#Switch	
	Database.clearSymbolValue("core", "PIN_64_FUNCTION_NAME")
	Database.clearSymbolValue("core", "PIN_64_FUNCTION_TYPE")
	Database.clearSymbolValue("core", "PIN_64_PIO_PIN")
	Database.clearSymbolValue("core", "PIN_64_PIO_CHANNEL")
	Database.clearSymbolValue("core", "PIN_64_PU")
	
#	Database.setSymbolValue("core", "PIN_64_FUNCTION_NAME", "SWITCH", 2)
#	Database.setSymbolValue("core", "PIN_64_FUNCTION_TYPE", "SWITCH_AL', 2)
	Database.setSymbolValue("core", "PIN_64_PIO_PIN", 11, 2)
#	Database.setSymbolValue("core", "PIN_64_PIO_CHANNEL", "A', 2)
#	Database.setSymbolValue("core", "PIN_64_PU", "True", 2)
	

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



		