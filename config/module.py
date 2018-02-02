def loadModule():
	print("Load Module: BSP")

	configName = Variables.get("__CONFIGURATION_NAME")

	bspDefault = Module.CreateComponent("bsp_default", configName + " Board (BSP)", "/Board Support Packages (BSPs)/", "config/bsp_default.py")
	bspDefault.addCapability("BSP")

	bspE70XP = Module.CreateComponent("bsp_e70xp", "SAM E70 Xplained Pro BSP", "/Board Support Packages (BSPs)/", "config/e70xp.py")
	bspE70XP.addCapability("BSP")

	bspE70XU = Module.CreateComponent("bsp_e70xu", "SAM E70 Xplained Ultra BSP", "/Board Support Packages (BSPs)/", "config/e70xu.py")
	bspE70XU.addCapability("BSP")


