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

class mcBspI_VoltageSourceClass:
    def __init__(self, bspContent, component):
        self.component = component
        self.bspContent = bspContent
        self.readFromXml("dsPICDEM MCLV-2")

    def readFromXml(self, selected):
        self.information = dict()
        
        # Read xml data from the path 
        for board in self.bspContent.findall("boards/board"):
            if board.attrib["name"] == selected:
                for rail in board.findall("voltage/rail"):
                    self.information[rail.attrib["id"]] = rail.attrib["value"] 

            
    def createSymbols(self ):
        # Root Node 
        self.sym_NODE = self.component.createMenuSymbol(None, None)
        self.sym_NODE.setLabel("Voltage source")

        # 
        self.sym_VOLTAGE = self.component.createFloatSymbol("MCPMSMFOC_VOLTAGE_MAGNITUDE", self.sym_NODE )
        self.sym_VOLTAGE.setLabel("Voltage magnitude (in Volts)")
        self.sym_VOLTAGE.setDefaultValue(float(self.information["VDC"]))
        self.sym_VOLTAGE.setDependencies(self.updateBoardParameters, ["BSP_BOARD_SEL"])

        # Dependency
        self.sym_DEPENDENCY = self.component.createMenuSymbol( None, None)
        self.sym_DEPENDENCY.setLabel("Dependency")
        self.sym_DEPENDENCY.setVisible(False)
        self.sym_DEPENDENCY.setDependencies(self.updateInformation, ["MCPMSMFOC_VOLTAGE_MAGNITUDE"] )

        
    def updateBoardParameters(self, symbol, event): 
        self.readFromXml(event["symbol"].getValue())
        self.sym_VOLTAGE.setValue(float(self.information["VDC"]))
        self.sendMessage()
       

    def updateInformation(self, symbol, event):   
        self.information["VDC"] = self.sym_VOLTAGE.getValue()
        self.sendMessage()
              
    def handleMessage(self, id,  message):
       if( id == "MCPMSMFOC_VOLTAGE_SOURCE"):
           return self.information

    def sendMessage( self ):
        Database.sendMessage("pmsm_foc", "BSP_VOLTAGE_SOURCE", self.information)
         

    def __call__(self):
        self.createSymbols()
        self.sendMessage()
   
