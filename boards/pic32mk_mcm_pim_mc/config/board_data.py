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
#                                 GLOBAL VARIABLES                                      #
#---------------------------------------------------------------------------------------#   
import xml.etree.ElementTree as ET
import os

class mcBspI_ReadBoardInformation:
    def __init__(self, bspContent, component ):
        self.bspContent = bspContent
        self.component = component

        self.information = dict()

        # Read xml data to a element tree string for parsing 
        # Connector to MCU pin mapping 
        self.map_CONNECTOR_TO_PIN = dict()
        for connector in self.bspContent.find("pim/connectors"):
            if( connector.attrib["name"] != "NC"):
                pin = self.stringToListConvert((connector.find("pin")).attrib["index"])
                self.map_CONNECTOR_TO_PIN[connector.attrib["index"]] = pin
       
        # Map the PIM connectors to MCU pin using the XML file 
        global global_CONNECTOR_TO_PIN_MAP
        global_CONNECTOR_TO_PIN_MAP = dict()
        for connector in self.bspContent.find("pim/connectors"):
            if( connector.attrib["name"] != "NC"):
                pin_List = self.stringToListConvert((connector.find("pin")).attrib["index"])
                global_CONNECTOR_TO_PIN_MAP[connector.attrib["index"]] = pin_List
              
        # Pins to pad mapping 
        global global_PAD_TO_PIN_MAP
        global global_PIN_TO_PAD_MAP
        global_PAD_TO_PIN_MAP = dict()
        global_PIN_TO_PAD_MAP = dict()

        currentPath = Variables.get("__CSP_DIR") + "/peripheral/gpio_02467"
        deviceXmlPath = os.path.join(currentPath, "plugin/pin_xml/components/" + Variables.get("__PROCESSOR") + ".xml")
        deviceXmlTree = ET.parse(deviceXmlPath)
        deviceXmlRoot = deviceXmlTree.getroot()
        pinoutXmlName = deviceXmlRoot.get("pins")
        pinoutXmlPath = os.path.join(currentPath, "plugin/pin_xml/pins/" + pinoutXmlName + ".xml")
        pinoutXmlPath = os.path.normpath(pinoutXmlPath)
       
        pinFileContent = ET.fromstring((open(pinoutXmlPath, "r")).read())
        for pad in pinFileContent.findall("pins/pin"):
            for number in pad.findall("number"):
                global_PAD_TO_PIN_MAP[pad.attrib["name"]] = number.attrib["pin"]
                global_PIN_TO_PAD_MAP[number.attrib["pin"]] = pad.attrib["name"]

    def stringToListConvert( self, my_String ):
        my_List = my_String.replace("[","")
        my_List = my_List.replace("]","")
        my_List = list(my_List.split(","))
        my_List = [i.replace(" ","") for i in my_List]
        return my_List

    def connectorToPinMapping(self):
        pass

    def createSymbols(self):

        # MHC Symbols 
        board_List = list()
        for board in self.bspContent.findall("boards/board"):
            board_List.append(board.attrib["name"])

        global sym_SELECTED_BOARD
        sym_SELECTED_BOARD = self.component.createComboSymbol("BSP_BOARD_SEL", None, board_List )
        sym_SELECTED_BOARD.setLabel("Development Board")
        self.information["NAME"] = sym_SELECTED_BOARD.getValue()

        sym_JUMPER_NODE = self.component.createMenuSymbol("BSP_JUMPER_SETTING", None )
        sym_JUMPER_NODE.setLabel("Jumper Settings")
        for jumper in self.bspContent.find("jumpers"):
            symbol_Id = "BSP_JUMPER_" + jumper.attrib["name"]
            symbol_List = self.stringToListConvert(jumper.attrib["combinations"])     
            sym_JUMPER = self.component.createComboSymbol(symbol_Id, sym_JUMPER_NODE, symbol_List)
            sym_JUMPER.setLabel(str(jumper.attrib["name"]) + " " + "Setting")
            sym_JUMPER.setDefaultValue(jumper.attrib["value"])

        sym_MATRIX_NODE = self.component.createMenuSymbol("BSP_MATRIX_BOARD", None) 
        sym_MATRIX_NODE.setLabel("Matrix Board")
        
        symbol_List = list()
        for matrix in self.bspContent.find("matrices"):
            symbol_List.append(matrix.attrib["name"])
        
        sym_MATRIX = self.component.createComboSymbol("BSP_MATRIX_BOARD_SELECT", sym_MATRIX_NODE, symbol_List)
        sym_MATRIX.setLabel("Matrix Board")
        sym_MATRIX.setDefaultValue("External")

        self.sym_DEPENDENCY = self.component.createMenuSymbol(None, None)
        self.sym_DEPENDENCY.setLabel("Dependency")
        self.sym_DEPENDENCY.setVisible(False)
        self.sym_DEPENDENCY.setDependencies( self.updateInformation, ["BSP_BOARD_SEL"] )

   
    def updateInformation(self, symbol, event):
        self.information["NAME"] = event["symbol"].getValue()
        self.sendMessage()

    def sendMessage(self):
        Database.sendMessage("pmsm_foc", "BSP_BOARD_INFORMATION", self.information )

    def handleMessage(self, ID, message):
        if "MCPMSMFOC_BOARD_INFORMATION" == ID:
            return self.information

    def __call__(self):
        self.createSymbols()
        self.sendMessage()



       