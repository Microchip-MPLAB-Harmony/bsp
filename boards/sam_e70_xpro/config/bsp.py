def instantiateComponent(bspComponent):

	BSP_NAME = "sam_e70_xpro"

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
			{"type":"SWITCH", "mode":"DIGITAL", "pu":"TRUE"},
			{"type":"VBUS_AH", "mode":"DIGITAL", "dir":"OUT"},
			{"type":"VBUS_AL", "mode":"DIGITAL", "dir":"OUT"}]

	execfile(Variables.get("__BSP_DIR") + "/boards/config/bsp_common.py")
