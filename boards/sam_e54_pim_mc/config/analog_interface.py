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
#                                     Imports                                           #
#---------------------------------------------------------------------------------------#
import xml.etree.ElementTree as ET
import os

#---------------------------------------------------------------------------------------#
#                                  Global Variables                                     #
#---------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------#
#                                      Classes                                          #
#---------------------------------------------------------------------------------------#

class mcBspI_AnalogInterfaceClass:
    def __init__(self, bspContent, component ):
        self.component = component
        self.bspContent = bspContent

        # PAD to ADC mapping using ATDF
        self.function_Tuple = dict()

        module_Path = "/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]"
        modules = ATDF.getNode(module_Path).getChildren()

        for module in modules:
            unit = module.getAttribute("name")
            channel_Path = module_Path + "/instance@[name=\"" + unit + "\"]/signals"
            channels = ATDF.getNode(channel_Path).getChildren()
            
            function_List = dict()
            function_Name = dict()
            for channel in channels:
                pad = channel.getAttribute("pad")

                if None != channel.getAttribute("index"):
                    function = channel.getAttribute("group") + str(channel.getAttribute("index"))
                else:
                    function = channel.getAttribute("group")

              
                if pad in function_List.keys():
                    function_List[pad].append(function)
                else:
                    function_List[pad] = [function]
                
                function_Name[pad] = '/'.join(function_List[pad])
            
            for channel in channels:     
                pad = channel.getAttribute("pad")              
                try:
                    self.function_Tuple[pad].append(( unit, function_Name[pad] ))
                except:
                    self.function_Tuple[pad] = [( unit, function_Name[pad] )]
            
            for channel in channels:     
                pad = channel.getAttribute("pad")              
                self.function_Tuple[pad] = list(set(self.function_Tuple[pad]))
                
        self.readFromXml("dsPICDEM MCLV-2")

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

        # Work-around
        for element in self.information["IB"]["FUNCTION"]:
            if element[0] == self.information["IB"]["FUNCTION"][0][0]:
                self.information["IB"]["FUNCTION"].remove( element)

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
        self.sym_IA = self.component.createMenuSymbol("MCBSP_PHASE_CURRENT_IA_NODE", self.sym_NODE)
        self.sym_IA.setLabel("Phase A current")

        self.sym_IA_PIN =  self.component.createIntegerSymbol("MCBSP_PHASE_CURRENT_IA_PIN", self.sym_IA )
        self.sym_IA_PIN.setLabel("Pin Number")
        self.sym_IA_PIN.setDefaultValue(int(self.information["IA"]["PIN"]))
        self.sym_IA_PIN.setReadOnly(True)


        # Phase B current 
        self.sym_IB = self.component.createMenuSymbol("MCBSP_PHASE_CURRENT_IB_NODE", self.sym_NODE)
        self.sym_IB.setLabel("Phase B current")

        self.sym_IB_PIN =  self.component.createIntegerSymbol("MCBSP_PHASE_CURRENT_IB_PIN", self.sym_IB)
        self.sym_IB_PIN.setLabel("Pin Number")
        self.sym_IB_PIN.setDefaultValue(int(self.information["IB"]["PIN"]))
        self.sym_IB_PIN.setReadOnly(True)
              
        # Phase C current 
        # self.sym_IDC = self.component.createMenuSymbol("MCBSP_DC_BUS_CURRENT_IDC_NODE", self.sym_NODE)
        # self.sym_IDC.setLabel("DC bus current")
          
        # self.sym_IDC_PIN = self.component.createIntegerSymbol("MCBSP_DC_BUS_CURRENT_PIN", self.sym_IDC )
        # self.sym_IDC_PIN.setLabel("Pin Number")
        # self.sym_IDC_PIN.setDefaultValue(int(self.information["IDC"]["PIN"]))

        # Phase A current 
        self.sym_VDC = self.component.createMenuSymbol("MCBSP_BUS_VOLTAGE_VDC_NODE", self.sym_NODE)
        self.sym_VDC.setLabel("DC Bus Voltage")

        self.sym_VDC_PIN =  self.component.createIntegerSymbol("MCBSP_BUS_VOLTAGE_VDC_PIN", self.sym_VDC )
        self.sym_VDC_PIN.setLabel("Pin Number")
        self.sym_VDC_PIN.setDefaultValue(int(self.information["VDC"]["PIN"]))
        self.sym_VDC_PIN.setReadOnly(True)
              
        # Potentiometer
        self.sym_VPOT = self.component.createMenuSymbol("MCBSP_POTENTIOMETER_VPOT_NODE", self.sym_NODE)
        self.sym_VPOT.setLabel("Potentiometer")

        self.sym_VPOT_PIN =  self.component.createIntegerSymbol("MCBSP_POTENTIOMETER_VPOT_PIN", self.sym_VPOT)
        self.sym_VPOT_PIN.setLabel("Pin Number")
        self.sym_VPOT_PIN.setDefaultValue(int(self.information["VPOT"]["PIN"]))
        self.sym_VPOT_PIN.setReadOnly(True)
               
        # PLIB update symbol
        self.sym_DEPENDENCY = self.component.createMenuSymbol( None, None)
        self.sym_DEPENDENCY.setLabel("Dependency")
        self.sym_DEPENDENCY.setVisible(False)
        self.sym_DEPENDENCY.setDependencies(self.updateInformation, ["MCBSP_PHASE_CURRENT_IA_PIN",
                                                                    "MCBSP_PHASE_CURRENT_IB_PIN",
                                                                    "MCBSP_DC_BUS_CURRENT_PIN",
                                                                    "MCBSP_BUS_VOLTAGE_VDC_PIN",
                                                                    "MCBSP_POTENTIOMETER_VPOT_PIN"
                                                                    ])

        self.sym_BOARD = self.component.createFloatSymbol(None, None)
        self.sym_BOARD.setVisible(False)
        self.sym_BOARD.setDependencies(self.updateBoardParameters, ["BSP_BOARD_SEL"])


    def setDatabaseSymbol(self, nameSpace, ID, value ):
        status =  Database.setSymbolValue(nameSpace, ID, value)
        if(status == False ):
            print("BSP is unable to set {symbol} with {input}".format(symbol = ID, input = value))
        
    def updateInformation(self, symbol, event):
        self.pinToAdcMapping( self.sym_IA_PIN.getValue(), "IA"    )
        self.pinToAdcMapping( self.sym_IB_PIN.getValue(), "IB"    )
        # self.pinToAdcMapping( self.sym_IDC_PIN.getValue(), "IDC"  )
        self.pinToAdcMapping( self.sym_VDC_PIN.getValue(), "VDC"  )
        self.pinToAdcMapping( self.sym_VPOT_PIN.getValue(), "POT" )

        self.setPinManager()
        self.sendMessage()

    def updateBoardParameters(self, symbol, event): 
        self.readFromXml(event["symbol"].getValue())
        
        # Update Ia front end analog analog front end 
        self.sym_IA_PIN.setValue(int(self.information["IA"]["PIN"] ))
        self.sym_IB_PIN.setValue( int(self.information["IB"]["PIN"] ))
        # self.sym_IDC_PIN.setValue( int(self.information["IDC"]["PIN"] ))
        self.sym_VDC_PIN.setValue( int(self.information["VDC"]["PIN"] ))
        self.sym_VPOT_PIN.setValue( int(self.information["VPOT"]["PIN"] ))

    """
    Description:
    This function discards alphabets and returns the numbers only
    """ 
    def numericFilter( self, input_String ):
        numeric_filter = filter(str.isdigit, str(input_String))
        return "".join(numeric_filter)


    def sendMessage( self ):
        temp_Dict = dict()
        information = self.information.copy()
        for analog_Channels, analog_Channel_Attributes in self.information.items():
            for analog_Channel_Attribute_Key, analog_Channel_Attribute_Value in analog_Channel_Attributes.items():
                if( analog_Channel_Attribute_Key == "FUNCTION" ):
                    for list_items in analog_Channel_Attribute_Value:
                        temp_List2 = list(list_items[1].split("/"))
                        channel = self.numericFilter(temp_List2[0])
                        try:  
                            temp_Dict[analog_Channels].append(( list_items[0], channel))
                        except:
                            temp_Dict[analog_Channels] = list()
                            temp_Dict[analog_Channels] = [( list_items[0], channel)]

                information[analog_Channels]["FUNCTION"] = temp_Dict[analog_Channels]   

        Database.sendMessage("pmsm_foc","BSP_ANALOG_INTERFACE", self.information )

    def handleMessage( self, id, args):
        if id == "MCPMSMFOC_ANALOG_INTERFACE":
            return self.information


    def setPinManager(self):
        for key in self.information.keys():
            number = str(self.information[key]["PIN"])
            type = self.information[key]["FUNCTION"][0][0] + "_" + self.information[key]["FUNCTION"][0][1]

            self.setDatabaseSymbol("core", "PIN_" + number +"_FUNCTION_NAME", key )         
            self.setDatabaseSymbol("core", "PIN_" + number +"_FUNCTION_TYPE", type)
       

    def __call__(self):
        self.createSymbols()
        self.setPinManager()
        self.sendMessage()

    



