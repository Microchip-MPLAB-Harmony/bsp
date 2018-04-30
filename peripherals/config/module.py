def loadModule():
    print("Load Module: External Peripherals")

    #define Exxternal peripherals
    peripheralComponents = [{"name":"sst26", "type":"peripheral", "dependency":["QSPI"], "condition":'any(x in Variables.get("__PROCESSOR") for x in ["SAMV70", "SAMV71", "SAME70", "SAMS70", "PIC32CZ"])'}]

    #load External peripherals from the list
    for peripheralComponent in peripheralComponents:
        #check if component should be created
        if eval(peripheralComponent['condition']):
            Name = peripheralComponent['name']
            #create external peripheral component
            if peripheralComponent['type'] == "peripheral":
                print("create component: " + Name.upper() + " External Peripheral")
                Component = Module.CreateComponent(Name, Name.upper() + " Peripheral", "/External Peripherals/", Name + "/config/" + Name + ".py")
                Component.addCapability(Name, "MEMORY")
                if "dependency" in peripheralComponent:
                    for item in peripheralComponent['dependency']:
                        Component.addDependency(Name + "_" + item + "_dependency", item)
