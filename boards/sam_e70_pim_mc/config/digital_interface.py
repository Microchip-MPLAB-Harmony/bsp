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
#                                   Imports                                             #
#---------------------------------------------------------------------------------------#
import imp
import xml.etree.ElementTree as ET
from collections import OrderedDict

#---------------------------------------------------------------------------------------#
#                                 GLOBAL VARIABLES                                      #
#---------------------------------------------------------------------------------------#




class mcBspI_DigitalInterfaceClass:
    def __init__(self, bspContent, component ):
        self.component = component
        self.bspContent = bspContent

        # Read xml data from the path 
        self.readFromXml("dsPICDEM MCLV-2")

    def readFromXml(self, selected):
        self.information = OrderedDict()
        self.information["BUTTONS"] = OrderedDict()
        for board in self.bspContent.findall("boards/board"):
            if board.attrib["name"] == selected:
                for connector in board.findall("buttons/connector"):
                    button_Name = connector.attrib["id"]
                    pin = global_CONNECTOR_TO_PIN_MAP[connector.attrib["value"]][0]
                    pad = global_PIN_TO_PAD_MAP[pin]

                    self.information["BUTTONS"][button_Name] = OrderedDict()
                    self.information["BUTTONS"][button_Name]["PIN"] = pin
                    self.information["BUTTONS"][button_Name]["PAD"] = pad
                    
                
                self.information["LEDS"] = OrderedDict()
                for connector in board.findall("leds/connector"):
                    button_Name = connector.attrib["id"]
                    pin = global_CONNECTOR_TO_PIN_MAP[connector.attrib["value"]][0]
                    pad = global_PIN_TO_PAD_MAP[pin]

                    self.information["LEDS"][button_Name] = OrderedDict()
                    self.information["LEDS"][button_Name]["PIN"] = pin
                    self.information["LEDS"][button_Name]["PAD"] = pad
                  
    def createSymbols( self ):
        self.sym_NODE = self.component.createMenuSymbol(None, None)
        self.sym_NODE.setLabel("Digital Interface")

        self.sym_BUTTON_NODE = self.component.createMenuSymbol(None, self.sym_NODE)
        self.sym_BUTTON_NODE.setLabel("Buttons")

        symbol_List = list()

        # Buttons 
        index = 0
        self.sym_BUTTON_PIN = OrderedDict()
        for value in self.information["BUTTONS"].values():
            symbol_List.append("MCPMSMFOC_BUTTON" + str(index) + "_NUMBER")
            self.sym_BUTTON_PIN[index] = self.component.createIntegerSymbol("MCPMSMFOC_BUTTON" + str(index) + "_NUMBER", self.sym_BUTTON_NODE )
            self.sym_BUTTON_PIN[index].setLabel("Button" +" "+ str(index) )
            self.sym_BUTTON_PIN[index].setDefaultValue(int(value["PIN"]))
            self.sym_BUTTON_PIN[index].setReadOnly(True)
            index = index + 1

        self.sym_LED_NODE = self.component.createMenuSymbol(None, self.sym_NODE)
        self.sym_LED_NODE.setLabel("LEDs")

        # LEDs 
        index = 0
        self.sym_LED_PIN = OrderedDict()
        for value in self.information["LEDS"].values():
            symbol_List.append("MCPMSMFOC_LED" + str(index) + "_NUMBER")
            self.sym_LED_PIN[index] = self.component.createIntegerSymbol("MCPMSMFOC_LED" + str(index) + "_NUMBER", self.sym_LED_NODE )
            self.sym_LED_PIN[index].setLabel("Led" + " " + str(index) )
            self.sym_LED_PIN[index].setDefaultValue(int(value["PIN"]))
            self.sym_LED_PIN[index].setReadOnly(True)
            index = index + 1


        # Dependency
        self.sym_DEPENDENCY = self.component.createMenuSymbol( None, None)
        self.sym_DEPENDENCY.setLabel("Dependency")
        self.sym_DEPENDENCY.setVisible(False)
        self.sym_DEPENDENCY.setDependencies(self.updateInformation, symbol_List )

        self.sym_BOARD = self.component.createFloatSymbol(None, None)
        self.sym_BOARD.setVisible(False)
        self.sym_BOARD.setDependencies(self.updateBoardParameters, ["BSP_BOARD_SEL"])
              

    def updateBoardParameters(self, symbol, event): 
        self.resetPinManager()
        self.readFromXml(event["symbol"].getValue())

        index = 0
        for value in self.information["BUTTONS"].values():
            self.sym_BUTTON_PIN[index].setValue(int(value["PIN"]))
            index = index + 1

        index = 0
        for value in self.information["LEDS"].values():
            self.sym_LED_PIN[index].setValue(int(value["PIN"]))
            index = index + 1
    
   
    def setDefaultValues(self):
        pass
    
    def pinToButtonMapping(self, pin, ID ):
        try:
            pad = global_PIN_TO_PAD_MAP[str(pin)]
            self.information["BUTTONS"][ID]["PIN"] = pin
            self.information["BUTTONS"][ID]["PAD"] = pad
        except:
            pass

    def pinToLedMapping(self, pin, ID ):
        try:
            pad = global_PIN_TO_PAD_MAP[str(pin)]
            self.information["LEDS"][ID]["PIN"] = pin
            self.information["LEDS"][ID]["PAD"] = pad 
        except:
            pass
        
    def updateInformation(self, symbol, event):
        index = 0
        for button in  self.information["BUTTONS"].keys():
            self.pinToButtonMapping( self.sym_BUTTON_PIN[index].getValue(), button )
            index = index + 1

        index = 0
        for led in  self.information["LEDS"].keys():
            self.pinToLedMapping( self.sym_LED_PIN[index].getValue(), led )
            index = index + 1

        self.sendMessage()
        self.setPinManager()
       
    def sendMessage( self ):
        Database.sendMessage("pmsm_foc", "BSP_DIGITAL_INTERFACE", self.information)
     
    def handleMessage( self, id, args):
        if "MCPMSMFOC_DIGITAL_INTERFACE" == id:
            return self.information
    
    def setDatabaseSymbol(self, nameSpace, ID, value ):
        status =  Database.setSymbolValue(nameSpace, ID, value)
        if(status == False ):
            print("BSP is unable to set {symbol} with {input}".format(symbol = ID, input = value))

    def setPinManager(self):

        # Leds
        for led in self.information["LEDS"].keys():  
            number = str(self.information["LEDS"][led]["PIN"])

            self.setDatabaseSymbol("core", "PIN_" + number + "_FUNCTION_NAME", led )         
            self.setDatabaseSymbol("core", "PIN_" + number + "_FUNCTION_TYPE", "GPIO")
            self.setDatabaseSymbol("core", "PIN_" + number + "_LAT", "Low")
            self.setDatabaseSymbol("core", "PIN_" + number + "_DIR", "Out")
            

        # Buttons
        for button in self.information["BUTTONS"].keys():
            
            number = str(self.information["BUTTONS"][button]["PIN"])

            self.setDatabaseSymbol("core", "PIN_" + number + "_FUNCTION_NAME", button )         
            self.setDatabaseSymbol("core", "PIN_" + number + "_FUNCTION_TYPE", "GPIO")
            self.setDatabaseSymbol("core", "PIN_" + number + "_PU", "True")
            self.setDatabaseSymbol("core", "PIN_" + number + "_DIR", ""   )
   
    def resetPinManager(self):

        # Leds
        for led in self.information["LEDS"].keys():  
            number = str(self.information["LEDS"][led]["PIN"])

            self.setDatabaseSymbol("core", "PIN_" + number + "_FUNCTION_NAME", "" )         
            self.setDatabaseSymbol("core", "PIN_" + number + "_FUNCTION_TYPE", "")
            self.setDatabaseSymbol("core", "PIN_" + number + "_LAT", "")
            self.setDatabaseSymbol("core", "PIN_" + number + "_DIR", "")
            

        # Buttons
        for button in self.information["BUTTONS"].keys():
            
            number = str(self.information["BUTTONS"][button]["PIN"])

            self.setDatabaseSymbol("core", "PIN_" + number + "_FUNCTION_NAME", "" )         
            self.setDatabaseSymbol("core", "PIN_" + number + "_FUNCTION_TYPE", "")
            self.setDatabaseSymbol("core", "PIN_" + number + "_PU", "" )
            self.setDatabaseSymbol("core", "PIN_" + number + "_DIR", "" )

    def __call__(self):
        self.createSymbols()
        self.setPinManager()
        self.sendMessage()


    



