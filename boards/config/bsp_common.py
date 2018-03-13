
bspMenu = bspComponent.createMenuSymbol("BSP_MENU", None)
bspMenu.setLabel("BSP Pin Types")
bspMenu.setDescription("Type of PIO Pins")

enumeratedPinTypes = enumerate(pinTypes)

for enumeratedPinType in enumeratedPinTypes:
	pinTypeIndex, pinType = enumeratedPinType

	Menu = bspComponent.createMenuSymbol("BSP_SUBMENU", bspMenu)
	Menu.setLabel("Type " + str(pinTypeIndex))

	for pinAttribute in pinAttributes:
		pinAttribute['symbol']
		Symbol = bspComponent.createStringSymbol(pinAttribute['symbol'] + str(pinTypeIndex), Menu)
		Symbol.setLabel(pinAttribute['label'])
		if pinAttribute['attrib'] in pinType:
			Symbol.setDefaultValue(pinType[pinAttribute['attrib']])

Symbol = bspComponent.createIntegerSymbol("BSP_TYPE_SIZE", bspMenu)
Symbol.setDefaultValue(len(pinTypes))

bspSysConfFile = bspComponent.createFileSymbol("BSP_SYSTEM_CONFIG_H", None)
bspSysConfFile.setType("STRING")
bspSysConfFile.setOutputName("core.LIST_SYSTEM_CONFIG_H_APPLICATION_CONFIGURATION")
bspSysConfFile.setSourcePath("templates/system_config.h.ftl")
bspSysConfFile.setMarkup(True)

bspSysConfInclude = bspComponent.createListEntrySymbol("INCLUDE_BSP_H", None)
bspSysConfInclude.setTarget("core.LIST_SYSTEM_CONFIG_H_GLOBAL_INCLUDES")
bspSysConfInclude.addValue("#include \"bsp/bsp.h\"")

configName = Variables.get("__CONFIGURATION_NAME")

bspSourceFile = bspComponent.createFileSymbol("BSP_C", None)
bspSourceFile.setSourcePath(BSP_NAME + "/templates/bsp.c.ftl")
bspSourceFile.setOutputName("bsp.c")
bspSourceFile.setMarkup(True)
bspSourceFile.setOverwrite(True)
bspSourceFile.setDestPath("bsp/")
bspSourceFile.setProjectPath("config/" + configName + "/bsp/")
bspSourceFile.setType("SOURCE")

bspHeaderFile = bspComponent.createFileSymbol("BSP_H", None)
bspHeaderFile.setSourcePath(BSP_NAME + "/templates/bsp.h.ftl")
bspHeaderFile.setOutputName("bsp.h")
bspHeaderFile.setMarkup(True)
bspHeaderFile.setOverwrite(True)
bspHeaderFile.setDestPath("bsp/")
bspHeaderFile.setProjectPath("config/" + configName + "/bsp/")
bspHeaderFile.setType("HEADER")
