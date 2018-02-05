def loadModule():
	print("Load Module: BSP")

	configName = Variables.get("__CONFIGURATION_NAME")

	bspDefault = Module.CreateComponent("BSP_default", configName + " Board (BSP)", "/Board Support Packages (BSPs)/", "config/bsp_default.py")
	bspDefault.addCapability("BSP")

	import xml.etree.ElementTree as ET
	bspFile = open(Variables.get("__BSP_DIR") + "/module.xml", "r")
	bspContent = ET.fromstring(bspFile.read())
	for Board in bspContent.iter("Board"):
		if Board.attrib['processor'] == Variables.get("__PROCESSOR"):
			print("BSP: Load " + Board.attrib['name'])
			Id = Board.attrib['name'].replace(" ", "_")
			bspComponent = Module.CreateComponent("BSP_" + Id, Board.attrib['name'] + " BSP", "/Board Support Packages (BSPs)/", "config/" + Board.attrib['config'])
			bspComponent.addCapability("BSP")
	
