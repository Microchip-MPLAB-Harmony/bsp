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
#                                     IMPORT                                            #
#---------------------------------------------------------------------------------------#
import xml.etree.ElementTree as ET
import os

#---------------------------------------------------------------------------------------#
#                                 GLOBAL VARIABLES                                      #
#---------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------#
#                                 GLOBAL VARIABLES                                      #
#---------------------------------------------------------------------------------------#

class mcBspI_PositionConfiguration:
    def __init__(self, bspContent, component):
        self.component = component
        self.bspContent = bspContent

        self.function_Tuple = dict()
        self.instance_List = set()
        self.function_Tuple["QEA"] = dict()
        self.function_Tuple["QEB"] = dict()

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
        for group in pinFileContent.findall("groups/group"):
            for function in group.findall("function"):
                if function.attrib["name"].startswith("QEA"):
                    for pin in group.findall("pin"):
                        channel = function.attrib["name"]
                        unit = "QEI" + self.numericFilter(channel)
                        pad = self.stringReplace(pin.attrib["name"])

                        try:
                            self.function_Tuple["QEA"][pad].append(( unit, channel ))
                        except:
                            self.function_Tuple["QEA"][pad] = list()  
                            self.function_Tuple["QEA"][pad] = [( unit, channel )]

                        self.instance_List.add(unit)

                if function.attrib["name"].startswith("QEB"):
                    for pin in group.findall("pin"):
                        channel = function.attrib["name"]
                        unit = "QEI" + self.numericFilter(channel)
                        pad = self.stringReplace(pin.attrib["name"])

                        try:
                            self.function_Tuple["QEB"][pad].append(( unit, channel ))
                        except:
                            self.function_Tuple["QEB"][pad] = list()  
                            self.function_Tuple["QEB"][pad] = [( unit, channel )]

                        self.instance_List.add(unit)

        # Read xml data from the path 
        self.readFromXml("dsPICDEM MCLV-2")
        

    def stringReplace( self, my_String ):
        my_String = my_String.replace("RP","R")
        return my_String

    def numericFilter( self, input_String ):
        numeric_filter = filter(str.isdigit, str(input_String))
        return "".join(numeric_filter)

    def readFromXml(self, selected):
        # Read xml data from the path 
        for board in self.bspContent.findall("boards/board"):
            if board.attrib["name"] == selected:
                self.information = dict()
                for connector in board.findall("position/encoder/connector"):
                    index = connector.attrib["value"]
                    ID = connector.attrib["id"]
                    pin = global_CONNECTOR_TO_PIN_MAP[index][0]
                    pad = global_PIN_TO_PAD_MAP[pin]

                    self.information[ID] = dict()
                    self.information[ID]["PIN"] = pin
                    self.information[ID]["PAD"] = pad
                    self.information[ID]["FUNCTION"] = self.function_Tuple[ID][pad]
                  

    def createSymbols(self):
        # Root node 
        self.sym_NODE = self.component.createMenuSymbol(None, None)
        self.sym_NODE.setLabel("Position Interface")
        
        # Root node 
        self.sym_ENCODER = self.component.createMenuSymbol("MCBSP_ENCODER", self.sym_NODE )
        self.sym_ENCODER.setLabel("Encoder Connections")
        
        # Peripheral selection
        instance_List = sorted(list(self.instance_List))
        self.sym_PERIPHERAL = self.component.createComboSymbol("MCBSP_ENCODER_PERIPHERAL", self.sym_NODE, instance_List)
        self.sym_PERIPHERAL.setLabel("Select instance")
        self.sym_PERIPHERAL.setDefaultValue(self.information["QEA"]["FUNCTION"][0][0])
        self.sym_PERIPHERAL.setReadOnly(True)

        # QEA                 
        self.sym_QEA = self.component.createIntegerSymbol("MCBSP_ENCODER_QEA_PIN", self.sym_NODE )
        self.sym_QEA.setLabel("QEA Pin")
        self.sym_QEA.setDefaultValue(int(self.information["QEA"]["PIN"]))
        self.sym_QEA.setReadOnly(True)


        self.sym_QEB = self.component.createIntegerSymbol("MCBSP_ENCODER_QEB_PIN", self.sym_NODE )
        self.sym_QEB.setLabel("QEB Pin")
        self.sym_QEB.setDefaultValue(int(self.information["QEB"]["PIN"]))
        self.sym_QEB.setReadOnly(True)


        # Dependency
        self.sym_DEPENDENCY = self.component.createMenuSymbol( None, None)
        self.sym_DEPENDENCY.setLabel("Dependency")
        self.sym_DEPENDENCY.setVisible(False)
        self.sym_DEPENDENCY.setDependencies(self.updateInformation, ["MCBSP_ENCODER_QEA_PIN",
                                                                     "MCBSP_ENCODER_QEB_PIN",
                                                                     "MCBSP_ENCODER_PERIPHERAL"
                                                                    ])

        self.sym_BOARD = self.component.createFloatSymbol(None, None)
        self.sym_BOARD.setVisible(False)
        self.sym_BOARD.setDependencies(self.updateBoardParameters, ["BSP_BOARD_SEL"])
              
   
    def pinToDecoderMapping(self, pin, ID ):
        try:
            pad = global_PIN_TO_PAD_MAP[str(pin)]
            self.information[ID] =  tuple(list(self.function_Tuple[pad])  + [pin, pad] )
        except:
            pass

    def updateInformation(self, symbol, event):
        self.pinToDecoderMapping( self.sym_QEA.getValue(), "QEA" )
        self.pinToDecoderMapping( self.sym_QEB.getValue(), "QEB" )
       
        self.setPinManager()
        self.sendMessage()
    
    def updateBoardParameters(self, symbol, event): 
        self.resetPinManager()
        self.readFromXml(event["symbol"].getValue())
        self.sym_QEA.setValue(int(self.information["QEA"]["PIN"]))
        self.sym_QEB.setValue(int(self.information["QEB"]["PIN"]))
         
    
    def handleMessage(self, id,  message):
        if id == "MCPMSMFOC_POSITION_INTERFACE":
            return self.information
       

    def setSymbols(self):
        pass

    def setDatabaseSymbol(self, nameSpace, ID, value ):
        status =  Database.setSymbolValue(nameSpace, ID, value)
        if(status == False ):
            print("BSP is unable to set {symbol} with {input}".format(symbol = ID, input = value))

    def setPinManager(self):
        for key in self.information.keys():
            
            number = self.information[key]["PIN"]
            type = self.information[key]["FUNCTION"][0][1]
            
            self.setDatabaseSymbol("core", "BSP_PIN_" + number + "_FUNCTION_NAME", key )         
            self.setDatabaseSymbol("core", "BSP_PIN_" + number + "_FUNCTION_TYPE", type )

    def resetPinManager(self):
        for key in self.information.keys():
            
            number = self.information[key]["PIN"]
            
            self.setDatabaseSymbol("core", "BSP_PIN_" + number + "_FUNCTION_NAME", "" )         
            self.setDatabaseSymbol("core", "BSP_PIN_" + number + "_FUNCTION_TYPE", "" )


    def sendMessage( self ):
        Database.sendMessage("pmsm_foc","BSP_POSITION_INTERFACE", self.information )

    def __call__(self):
        self.createSymbols()
        self.setPinManager()
        self.sendMessage()
   
