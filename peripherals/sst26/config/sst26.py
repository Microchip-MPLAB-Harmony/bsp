################################################################################
#### Component ####
################################################################################

def sst26SetMemoryDependency(symbol, event):
    if (event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def instantiateComponent(sst26Component):
    sst26PLIB = sst26Component.createStringSymbol("SST26_PLIB", None)
    sst26PLIB.setLabel("PLIB Used")
    sst26PLIB.setReadOnly(True)

    sst26InterruptEnable = sst26Component.createBooleanSymbol("INTERRUPT_ENABLE", None)
    sst26InterruptEnable.setLabel("Enable Interrupt")
    sst26InterruptEnable.setVisible(False)
    sst26InterruptEnable.setDefaultValue(False)

    sst26InterruptSource = sst26Component.createStringSymbol("INTERRUPT_SOURCE", None)
    sst26InterruptSource.setLabel("SST26 Interrupt Source")
    sst26InterruptSource.setVisible(False)
    sst26InterruptSource.setDependencies(sst26SetMemoryDependency, ["INTERRUPT_ENABLE"])

    sst26MemoryDriver = sst26Component.createBooleanSymbol("DRV_MEMORY_CONNECTED", None)
    sst26MemoryDriver.setLabel("Memory Driver Connected")
    sst26MemoryDriver.setVisible(False)
    sst26MemoryDriver.setDefaultValue(False)

    sst26MemoryStartAddr = sst26Component.createHexSymbol("START_ADDRESS", None)
    sst26MemoryStartAddr.setLabel("SST26 Start Address")
    sst26MemoryStartAddr.setVisible(True)
    sst26MemoryStartAddr.setDefaultValue(0x0000000)

    sst26MemoryEraseBufferSize = sst26Component.createIntegerSymbol("ERASE_BUFFER_SIZE", None)
    sst26MemoryEraseBufferSize.setLabel("SST26 Erase Buffer Size")
    sst26MemoryEraseBufferSize.setVisible(False)
    sst26MemoryEraseBufferSize.setDefaultValue(4096)
    sst26MemoryEraseBufferSize.setDependencies(sst26SetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    sst26MemoryEraseComment = sst26Component.createCommentSymbol("ERASE_COMMENT", None)
    sst26MemoryEraseComment.setVisible(False)
    sst26MemoryEraseComment.setLabel("*** Should be equal to Sector Erase Size ***")
    sst26MemoryEraseComment.setDependencies(sst26SetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    ############################################################################
    #### Code Generation ####
    ############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    sst26HeaderFile = sst26Component.createFileSymbol("SST26_HEADER", None)
    sst26HeaderFile.setSourcePath("sst26/sst26.h")
    sst26HeaderFile.setOutputName("sst26.h")
    sst26HeaderFile.setDestPath("external_peripheral/sst26/")
    sst26HeaderFile.setProjectPath("config/" + configName + "/external_peripheral/sst26/")
    sst26HeaderFile.setType("HEADER")
    sst26HeaderFile.setOverwrite(True)

    sst26SourceFile = sst26Component.createFileSymbol("SST26_SOURCE", None)
    sst26SourceFile.setSourcePath("sst26/templates/sst26.c.ftl")
    sst26SourceFile.setOutputName("sst26.c")
    sst26SourceFile.setDestPath("external_peripheral/sst26/")
    sst26SourceFile.setProjectPath("config/" + configName + "/external_peripheral/sst26/")
    sst26SourceFile.setType("SOURCE")
    sst26SourceFile.setOverwrite(True)
    sst26SourceFile.setMarkup(True)

    sst26SystemDefFile = sst26Component.createFileSymbol("SST26_DEF", None)
    sst26SystemDefFile.setType("STRING")
    sst26SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    sst26SystemDefFile.setSourcePath("sst26/templates/system/system_definitions.h.ftl")
    sst26SystemDefFile.setMarkup(True)

    sst26SystemInitFile = sst26Component.createFileSymbol("SST26_INIT", None)
    sst26SystemInitFile.setType("STRING")
    sst26SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DRIVERS")
    sst26SystemInitFile.setSourcePath("sst26/templates/system/system_initialize.c.ftl")
    sst26SystemInitFile.setMarkup(True)

def onDependentComponentAdded(sst26Component, id, remoteComponent):
    if id == "sst26_QSPI_dependency" :
        plibUsed = sst26Component.getSymbolByID("SST26_PLIB")
        plibUsed.clearValue()
        plibUsed.setValue(remoteComponent.getID().upper(), 2)

