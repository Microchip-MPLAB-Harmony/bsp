coreSymbol = Database.getSymbolByID("core", "BSP_PIN_CONFIG")
coreSymbol.setEnabled(True)

bspMenu = bspComponent.createMenuSymbol(None, None)
bspMenu.setLabel("BSP Pin Types")
bspMenu.setDescription("Type of PIO Pins")

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

Symbol = bspComponent.createIntegerSymbol("BSP_TYPE_SIZE", bspMenu)
Symbol.setDefaultValue(len(pinTypes))
