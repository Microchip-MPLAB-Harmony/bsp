def instantiateComponent(bspComponent):

	bspMenu = bspComponent.createMenuSymbol(None, None)
	bspMenu.setLabel("BSP Pin Types")
	bspMenu.setDescription("Type of PIO Pins")


	pinAttributes = [{"attrib":"type", "symbol":"BSP_CUSTOM_TYPE", "label":"Type Name"},
		{"attrib":"mode", "symbol":"BSP_CUSTOM_MODE", "label":"Mode"},
		{"attrib":"dir", "symbol":"BSP_CUSTOM_DIR", "label":"Direction"},
		{"attrib":"lat", "symbol":"BSP_CUSTOM_LAT", "label":"Initial Latch Value"},
		{"attrib":"od", "symbol":"BSP_CUSTOM_OD", "label":"Open Drain"},
		{"attrib":"cn", "symbol":"BSP_CUSTOM_CN", "label":"Change Notice"},
		{"attrib":"pu", "symbol":"BSP_CUSTOM_PU", "label":"Pull Up"},
		{"attrib":"pd", "symbol":"BSP_CUSTOM_PD", "label":"Pull Down"},
		{"attrib":"int", "symbol":"BSP_CUSTOM_PIO_INTERRUPT", "label":"PIO Interrupt"}]

	pinTypes = [{"type":"GPIO_OUT", "mode":"DIGITAL", "dir":"OUT"},
			{"type":"GPIO_IN", "mode":"DIGITAL"},
			{"type":"GPIO_CN", "mode":"DIGITAL", "cn":"TRUE", "int":"Both Edge"},
			{"type":"GPIO", "mode":"DIGITAL"}]

	enumeratedPinTypes = enumerate(pinTypes)

	for enumeratedPinType in enumeratedPinTypes:
		pinTypeIndex, pinType = enumeratedPinType

		Menu = bspComponent.createMenuSymbol(None, bspMenu)
		Menu.setLabel("Type " + str(pinTypeIndex))

		for pinAttribute in pinAttributes:
			pinAttribute['symbol']
			Symbol = bspComponent.createStringSymbol(pinAttribute['symbol'] + str(pinTypeIndex), Menu)
			Symbol.setLabel(pinAttribute['label'])
			if pinAttribute['attrib'] in pinType:
				Symbol.setDefaultValue(pinType[pinAttribute['attrib']])

