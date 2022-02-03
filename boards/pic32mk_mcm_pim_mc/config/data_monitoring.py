# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

#---------------------------------------------------------------------------------------#
#                                 Import                                                #
#---------------------------------------------------------------------------------------#
import os.path

#---------------------------------------------------------------------------------------#
#                                 Global variables                                     #
#---------------------------------------------------------------------------------------#
class mcBspI_DataMonitorClass:
    def __init__(self, bspContent, component ):
        self.bspContent = bspContent
        self.component = component
        self.functionMap = {"TRANSMIT": {}, "RECEIVE": {}}

         # Pin to quadrature decoder mapping       
        currentPath = Variables.get("__CSP_DIR") + "/peripheral/gpio_02467"
        deviceXmlPath = os.path.join(currentPath, "plugin/pin_xml/components/" + Variables.get("__PROCESSOR") + ".xml")
        deviceXmlTree = ET.parse(deviceXmlPath)
        deviceXmlRoot = deviceXmlTree.getroot()
        pinoutXmlName = deviceXmlRoot.get("pins")
        pinoutXmlPath = os.path.join(currentPath, "plugin/pin_xml/pins/" + pinoutXmlName + ".xml")
        pinoutXmlPath = os.path.normpath(pinoutXmlPath)

        familiesXmlName = deviceXmlRoot.get("families")
        familiesXmlPath = os.path.join(currentPath, "plugin/pin_xml/families/" + familiesXmlName + ".xml")
        familiesXmlPath = os.path.normpath(familiesXmlPath)

        pinFileContent = ET.fromstring((open(familiesXmlPath, "r")).read())

        self.functionMap = {"TRANSMIT": {}, "RECEIVE":{}}
        for group in pinFileContent.findall("groups/group"):
            for function in group.findall("function"):
                if function.attrib["name"].startswith("U") and function.attrib["name"].endswith("TX"):
                    for pin in group.findall("pin"):
                        channel = function.attrib["name"]
                        unit = "UART" + self.numericFilter(channel)
                        pad = self.stringReplace(pin.attrib["name"])

                        try:
                            self.functionMap["TRANSMIT"][pad].append( ( unit, channel ) )
                        except:
                            self.functionMap["TRANSMIT"][pad] = list()  
                            self.functionMap["TRANSMIT"][pad] = [( unit, channel )]
                    
                if function.attrib["name"].startswith("U") and function.attrib["name"].endswith("RX"):
                    for pin in group.findall("pin"):
                        channel = function.attrib["name"]
                        unit = "UART" + self.numericFilter(channel)
                        pad = self.stringReplace(pin.attrib["name"])

                        try:
                            self.functionMap["RECEIVE"][pad].append(( unit, channel ))
                        except:
                            self.functionMap["RECEIVE"][pad] = list()  
                            self.functionMap["RECEIVE"][pad] = [( unit, channel )]  
        
        # Read xml data from the path 
        self.readFromXml("dsPICDEM MCLV-2")

    def readFromXml(self, selected):
        self.information = {"TRANSMIT": {}, "RECEIVE": {}}

        for board in self.bspContent.findall("boards/board"):
            if board.attrib["name"] == selected:
                for peripheral in board.findall("communication/peripheral"):
                    if("UART" == peripheral.attrib["name"]):
                        for connector in peripheral:
                            key = connector.attrib["id"]
                            pin = global_CONNECTOR_TO_PIN_MAP[connector.attrib["value"]][0]
                            pad = global_PIN_TO_PAD_MAP[pin]

                            self.information[key]["FUNCTION"] = self.functionMap[key][pad]
                            self.information[key]["PIN"] =  pin
                            self.information[key]["PAD"] =  pad

    def createSymbols( self ):
        # Root Node
        self.sym_DATA_MON_NODE = self.component.createMenuSymbol("BSP_DATA_MONITOR", None )
        self.sym_DATA_MON_NODE.setLabel("Data Monitoring")    

        commList = ["UART", "CAN", "LIN"]
        self.sym_DATA_MON_INTERFACE = self.component.createComboSymbol("BSP_DATA_MON_INETRFACE", self.sym_DATA_MON_NODE, commList )
        self.sym_DATA_MON_INTERFACE.setLabel("Communication Interface")  
        self.sym_DATA_MON_INTERFACE.setDefaultValue("UART")   
        
        self.sym_TRANSMIT_PIN = self.component.createIntegerSymbol("BSP_DATA_MON_TRANSMIT_PIN", self.sym_DATA_MON_NODE )
        self.sym_TRANSMIT_PIN.setLabel("Transmit pin") 
        self.sym_TRANSMIT_PIN.setDefaultValue(int(self.information["TRANSMIT"]["PIN"]))
        self.sym_TRANSMIT_PIN.setReadOnly(True) 

        self.sym_RECEIVE_PIN = self.component.createIntegerSymbol("BSP_DATA_MON_RECEIVE_PIN", self.sym_DATA_MON_NODE )
        self.sym_RECEIVE_PIN.setLabel("Receive pin")   
        self.sym_RECEIVE_PIN.setDefaultValue(int(self.information["RECEIVE"]["PIN"]))
        self.sym_RECEIVE_PIN.setReadOnly(True) 
 

        self.sym_DEPENDENCY = self.component.createMenuSymbol(None, None )
        self.sym_DEPENDENCY.setLabel("Dependency")
        self.sym_DEPENDENCY.setVisible(False)   
        self.sym_DEPENDENCY.setDependencies(self.updateInformation, ["BSP_DATA_MON_INETRFACE", 
                                                                     "BSP_DATA_MON_TRANSMIT_PIN", 
                                                                     "BSP_DATA_MON_RECEIVE_PIN"])
      
    def stringReplace( self, my_String ):
        my_String = my_String.replace("RP","R")
        return my_String

    def numericFilter( self, input_String ):
        numeric_filter = filter(str.isdigit, str(input_String))
        return "".join(numeric_filter)
        
    def updateInformation(self, symbol, event):
        pin = self.sym_TRANSMIT_PIN.getValue()
        pad = global_PIN_TO_PAD_MAP[pin]
        self.information["TRANSMIT"]["PIN"] = self.sym_TRANSMIT_PIN.getValue()
        self.information["TRANSMIT"]["FUNCTION"] = self.functionMap[pad]
        
        pin = self.sym_RECEIVE_PIN.getValue()
        pad = global_PIN_TO_PAD_MAP[pin]
        self.information["RECEIVE"]["PIN"] = self.sym_RECEIVE_PIN.getValue()
        self.information["RECEIVE"]["FUNCTION"] = self.functionMap[pad]

        # Send message 
        self.sendMessage()
        self.setPinManager()

    def setDatabaseSymbol(self, nameSpace, ID, value ):
        status =  Database.setSymbolValue(nameSpace, ID, value)
        if(status == False ):
            print("BSP is unable to set {symbol} with {input}".format(symbol = ID, input = value))

    def setPinManager(self):
        for key, value in self.information.items():
            number = str( value["PIN"] )
            type = str(value["FUNCTION"][0][1])

            self.setDatabaseSymbol("core", "BSP_PIN_"+ number +"_FUNCTION_NAME", key  )         
            self.setDatabaseSymbol("core", "BSP_PIN_"+ number +"_FUNCTION_TYPE", type )
    
    def setDefaultValues(self):
        pass

    def sendMessage( self ):
        Database.sendMessage("X2CScope","BSP_DATA_MONITORING", self.information )
        

    def handleMessage( self, ID, information):
        if( ID == "X2CSCOPE_DATA_MONITORING" ):
            return self.information

    def __call__(self):
        self.createSymbols()
        self.setPinManager()
        self.sendMessage()


    



