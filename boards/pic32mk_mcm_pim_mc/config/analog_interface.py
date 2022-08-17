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
#                                     IMPORTS                                           #
#---------------------------------------------------------------------------------------#
import xml.etree.ElementTree as ET
import os

#---------------------------------------------------------------------------------------#
#                                 GLOBAL VARIABLES                                      #
#---------------------------------------------------------------------------------------#

class mcBspI_AnalogInterfaceClass:
    def __init__(self, bspContent, component ):
        self.component = component
        self.bspContent = bspContent

        self.map_PAD_TO_ADC = dict()

        self.map_ANALOG_CHANNEL_TO_PAD = dict()

        currentPath = Variables.get("__CSP_DIR") + "/peripheral/gpio_02467"
        deviceXmlPath = os.path.join(currentPath, "plugin/pin_xml/components/" + Variables.get("__PROCESSOR") + ".xml")
        deviceXmlTree = ET.parse(deviceXmlPath)
        deviceXmlRoot = deviceXmlTree.getroot()
        pinoutXmlName = deviceXmlRoot.get("pins")
        pinoutXmlPath = os.path.join(currentPath, "plugin/pin_xml/pins/" + pinoutXmlName + ".xml")
        pinoutXmlPath = os.path.normpath(pinoutXmlPath)

        self.pinFileContent = ET.fromstring((open(pinoutXmlPath, "r")).read())
        for item in self.pinFileContent.findall("pins/pin"):
            for function in item.findall("function"):
                if function.attrib["name"].startswith("AN"):
                    pad = self.stringReplace(item.attrib["name"])
                    self.map_ANALOG_CHANNEL_TO_PAD[self.numericFilter(function.attrib["name"])] = pad

        # Dedicated channels 
        # Dedicated channels 
        channelList = []
        self.function_Tuple = dict()
        ADC_Max_DedicatedChannels = 0
        registerPath = ATDF.getNode(self.adchsATDFRegisterPath("ADCHS", "ADCCON3"))
        bitfields = registerPath.getChildren()
        for ii in bitfields:
            if(("DIGEN" in ii.getAttribute("name")) and (ii.getAttribute("values")!=None)):
                if(ii.getAttribute("values")[-1] != '7'):  # channel 7 is shared - do not include in channelList
                    channelList.append(ii.getAttribute("values")[-1]) # the last char is a digit

        for ChannelNumber in channelList:
            labelPath = self.adchsATDFRegisterBitfieldPath("ADCHS", "ADCCON3", "DIGEN" + str(ChannelNumber))
            labelNode = ATDF.getNode(labelPath).getAttribute("values")
            if labelNode is not None:
                ADC_Max_DedicatedChannels += 1
                RegisterName = "ADCTRGMODE__SH" + str(ChannelNumber) + "ALT"
                labelPath = self.adchsATDFValueGroupPath("ADCHS", RegisterName)
                channels = ATDF.getNode(labelPath).getChildren()
                unit = "ADC"+str(ChannelNumber)
                for channel in channels:
                    analog_Channel = self.numericFilter(channel.getAttribute("caption"))
                                       
                    pad = self.map_ANALOG_CHANNEL_TO_PAD[analog_Channel]
                    try:
                        self.function_Tuple[pad].append(( unit, analog_Channel))
                    except:
                        self.function_Tuple[pad] = [( unit, analog_Channel )]

        # Shared channels                   
        # For PIC32M devices: Each Analog channel on the part must have a Data Register.  Each existing
        # Data register should indicate that there is an Analog pin for that signal.
        SignalNumber = 0
        MAX_AVAILABLE_SIGNALS = 64
        for SignalNumber in range (ADC_Max_DedicatedChannels, MAX_AVAILABLE_SIGNALS):
            labelPath = self.adchsATDFRegisterPath("ADCHS", "ADCDATA" + str(SignalNumber))
            labelNode = ATDF.getNode(labelPath)
            if labelNode is not None:
                analog_Channel = str(SignalNumber)
                try:
                    pad = self.map_ANALOG_CHANNEL_TO_PAD[analog_Channel]
                    try:
                        self.function_Tuple[pad].append(( "ADC7", analog_Channel ))
                    except:
                        self.function_Tuple[pad] = [( "ADC7", analog_Channel )]
                except:
                    pass
    
        self.readFromXml("dsPICDEM MCLV-2")

    def detAnalogChannelFromPad(self, pad ):
        for item in self.pinFileContent.findall("pins/pin"):
            if item.attrib["name"] == pad:
                for function in item.findall("function"):
                    if function.attrib["name"].startswith("AN"):
                        return function.attrib["name"]      
                
                # Inform error 
    
    def adchsATDFRegisterPath(self, ModuleName, RegisterName):
        labelPath = str('/avr-tools-device-file/modules/module@[name="' 
                       + ModuleName + '"]/register-group@[name="' 
                       + ModuleName + '"]/register@[name="' 
                       + RegisterName + '"]')
        return labelPath

    def adchsATDFRegisterBitfieldPath(self, ModuleName, RegisterName, BitfieldName):
        labelPath = str('/avr-tools-device-file/modules/module@[name="' +
            ModuleName + '"]/register-group@[name="' + ModuleName +
            '"]/register@[name="' + RegisterName + '"]/bitfield@[name="'
            + BitfieldName +'"]')
        return labelPath

    def adchsATDFValueGroupPath(self, ModuleName, ValueGroupName):
        value_groupPath = str('/avr-tools-device-file/modules/module@[name="'
            + ModuleName + '"]/value-group@[name="' + ValueGroupName + '"]')
        return value_groupPath

    def adchsATDFValueGroupValuePath(self, ModuleName, ValueGroupName, ValueString):
        valuePath = str('/avr-tools-device-file/modules/module@[name="' + ModuleName
            + '"]/value-group@[name="' + ValueGroupName + '"]/value@[value="' +
            ValueString + '"]')
        return valuePath

    def readFromXml(self, selected):
        # Read xml data from the path 
        self.information = dict()
        for board in self.bspContent.findall("boards/board"):
            if board.attrib["name"] == selected:
                for phase in board.findall("current/phase"):
                    self.information[phase.attrib["id"]] = dict()
                    for parameter in phase.findall("connector"):
                        pin = global_CONNECTOR_TO_PIN_MAP[parameter.attrib["value"]][0]
                        pad = global_PIN_TO_PAD_MAP[pin]
 
                        self.information[phase.attrib["id"]]["PIN"] = pin
                        self.information[phase.attrib["id"]]["PAD"] = pad
                        self.information[phase.attrib["id"]]["FUNCTION"] = self.function_Tuple[pad]

                for rail in board.findall("voltage/rail"):
                    self.information[rail.attrib["id"]] = dict()
                    for parameter in rail.findall("connector"):
                        pin = global_CONNECTOR_TO_PIN_MAP[parameter.attrib["value"]][0]
                        pad = global_PIN_TO_PAD_MAP[pin]
                        self.information[rail.attrib["id"]]["PIN"] = pin
                        self.information[rail.attrib["id"]]["PAD"] = pad
                        self.information[rail.attrib["id"]]["FUNCTION"] = self.function_Tuple[pad]

                for potentiometer in board.findall("potentiometers/potentiometer"):
                    self.information[potentiometer.attrib["id"]] = dict()
                    for parameter in potentiometer.findall("connector"):
                        pin = global_CONNECTOR_TO_PIN_MAP[parameter.attrib["value"]][0]
                        pad = global_PIN_TO_PAD_MAP[pin]
                        self.information[potentiometer.attrib["id"]]["PIN"] = pin
                        self.information[potentiometer.attrib["id"]]["PAD"] = pad
                        self.information[potentiometer.attrib["id"]]["FUNCTION"] = self.function_Tuple[pad]

    def stringReplace( self, my_String ):
        my_String = my_String.replace("RP","R")
        return my_String

    def numericFilter( self, input_String ):
        numeric_filter = filter(str.isdigit, str(input_String))
        return "".join(numeric_filter)
    def pinToAdcMapping(self, pin, ID ):
        try:
            pad = global_PIN_TO_PAD_MAP[str(pin)]
            self.information[ID]["PIN"] =  pin
            self.information[ID]["PAD"] =  pad
            self.information[ID]["FUNCTION"] = self.function_Tuple[pad]
        except:
            pass
        
    def createSymbols( self ):

        # Phase A current 
        self.sym_NODE = self.component.createMenuSymbol(None, None )
        self.sym_NODE.setLabel("Analog interface")

        # Phase A current 
        self.sym_IA = self.component.createMenuSymbol("BSP_IA_NODE", self.sym_NODE)
        self.sym_IA.setLabel("Phase A current")

        self.sym_IA_PIN =  self.component.createIntegerSymbol("BSP_IA_PIN", self.sym_IA )
        self.sym_IA_PIN.setLabel("Pin Number")
        self.sym_IA_PIN.setDefaultValue(int(self.information["IA"]["PIN"]))
        self.sym_IA_PIN.setReadOnly(True)

        # Phase B current 
        self.sym_IB = self.component.createMenuSymbol("BSP_IB_NODE", self.sym_NODE)
        self.sym_IB.setLabel("Phase B current")

        self.sym_IB_PIN =  self.component.createIntegerSymbol("BSP_IB_PIN", self.sym_IB)
        self.sym_IB_PIN.setLabel("Pin Number")
        self.sym_IB_PIN.setDefaultValue(int(self.information["IB"]["PIN"]))
        self.sym_IB_PIN.setReadOnly(True)
              
        # Phase C current 
        # self.sym_IDC = self.component.createMenuSymbol("BSP_IDC_NODE", self.sym_NODE)
        # self.sym_IDC.setLabel("DC bus current")
          
        # self.sym_IDC_PIN = self.component.createIntegerSymbol("BSP_IDC_PIN", self.sym_IDC )
        # self.sym_IDC_PIN.setLabel("Pin Number")
        # self.sym_IDC_PIN.setDefaultValue(int(self.information["IDC"]["PIN"]))

        # Phase A current 
        self.sym_VDC = self.component.createMenuSymbol("BSP_VDC_NODE", self.sym_NODE)
        self.sym_VDC.setLabel("DC Bus Voltage")

        self.sym_VDC_PIN =  self.component.createIntegerSymbol("BSP_VDC_PIN", self.sym_VDC )
        self.sym_VDC_PIN.setLabel("Pin Number")
        self.sym_VDC_PIN.setDefaultValue(int(self.information["VDC"]["PIN"]))
        self.sym_VDC_PIN.setReadOnly(True)
              
        # Potentiometer
        self.sym_VPOT = self.component.createMenuSymbol("BSP_VPOT_NODE", self.sym_NODE)
        self.sym_VPOT.setLabel("Potentiometer")

        self.sym_VPOT_PIN =  self.component.createIntegerSymbol("BSP_VPOT_PIN", self.sym_VPOT)
        self.sym_VPOT_PIN.setLabel("Pin Number")
        self.sym_VPOT_PIN.setDefaultValue(int(self.information["VPOT"]["PIN"]))
        self.sym_VPOT_PIN.setReadOnly(True)
               
        # PLIB update symbol
        self.sym_DEPENDENCY = self.component.createMenuSymbol( None, None)
        self.sym_DEPENDENCY.setLabel("Dependency")
        self.sym_DEPENDENCY.setVisible(False)
        self.sym_DEPENDENCY.setDependencies(self.updateInformation, ["BSP_IA_PIN", "BSP_IB_PIN", "BSP_IDC_PIN", "BSP_VDC_PIN", "BSP_VPOT_PIN" ])

        self.sym_BOARD = self.component.createFloatSymbol(None, None)
        self.sym_BOARD.setVisible(False)
        self.sym_BOARD.setDependencies(self.updateBoardParameters, ["BSP_BOARD_SEL"])


    def setDatabaseSymbol(self, nameSpace, ID, value ):
        status =  Database.setSymbolValue(nameSpace, ID, value)
        if(status == False ):
            print("BSP is unable to set {symbol} with {input}".format(symbol = ID, input = value))


    def updateInformation(self, symbol, event):
        ID = event["id"].split("_")[1]
        self.pinToAdcMapping( event["symbol"].getValue(), ID )

        self.setPinManager()
        self.sendMessage()

    def updateBoardParameters(self, symbol, event): 
        self.resetPinManager()

        self.readFromXml(event["symbol"].getValue())
        
        # Update Ia front end analog analog front end 
        self.sym_IA_PIN.setValue(int(self.information["IA"]["PIN"] ))
        self.sym_IB_PIN.setValue( int(self.information["IB"]["PIN"] ))
        # self.sym_IDC_PIN.setValue( int(self.information["IDC"]["PIN"] ))
        self.sym_VDC_PIN.setValue( int(self.information["VDC"]["PIN"] ))
        self.sym_VPOT_PIN.setValue( int(self.information["VPOT"]["PIN"] ))
          
    def sendMessage( self ):
        Database.sendMessage("pmsm_foc","BSP_ANALOG_INTERFACE", self.information )

    def handleMessage( self, id, args):
        if id == "MCPMSMFOC_ANALOG_INTERFACE":
            return self.information

    def setDatabaseSymbol(self, nameSpace, ID, value ):
        status =  Database.setSymbolValue(nameSpace, ID, value)
        if(status == False ):
            print("BSP is unable to set {symbol} with {input}".format(symbol = ID, input = value))

    def resetPinManager(self):
        for key in self.information.keys():
            number = str(self.information[key]["PIN"])
                       
            self.setDatabaseSymbol("core", "BSP_PIN_" + number +"_FUNCTION_NAME", "" )         
            self.setDatabaseSymbol("core", "BSP_PIN_" + number +"_FUNCTION_TYPE", "")
    
    def setPinManager(self):
        for key in self.information.keys():
            number = str(self.information[key]["PIN"])
            type = "AN" + self.information[key]["FUNCTION"][0][1]
           
            self.setDatabaseSymbol("core", "BSP_PIN_" + number +"_FUNCTION_NAME", key )         
            self.setDatabaseSymbol("core", "BSP_PIN_" + number +"_FUNCTION_TYPE", type)
       

    def __call__(self):
        self.createSymbols()
        self.setPinManager()
        self.sendMessage()

    



