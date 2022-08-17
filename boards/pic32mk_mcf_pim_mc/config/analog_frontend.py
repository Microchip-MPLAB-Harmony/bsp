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

class mcBspI_AnalogFrontEndClass:
    def __init__(self, bspContent, component):
        self.component = component
        self.bspContent = bspContent
               
        # Read xml data from the path 
        self.readFromXml("dsPICDEM MCLV-2")  

    def readFromXml(self, selected):
        self.information = dict()
        for board in self.bspContent.findall("boards/board"):
            if board.attrib["name"] == selected:
                for phase in board.findall("current/phase"):
                    self.information[phase.attrib["id"]] = dict()
                    for parameter in phase:
                        self.information[phase.attrib["id"]][parameter.attrib["id"]] = parameter.attrib["value"]  
                
                for rail in board.findall("voltage/rail"):
                    self.information[rail.attrib["id"]] = dict()
                    for parameter in rail:
                        self.information[rail.attrib["id"]][parameter.attrib["id"]] = parameter.attrib["value"] 

                for potentiometer in board.findall("potentiometers/potentiometer"):
                    self.information[potentiometer.attrib["id"]] = dict()
                    for parameter in potentiometer:
                        self.information[potentiometer.attrib["id"]][parameter.attrib["id"]] = parameter.attrib["value"]

    def createSymbols(self ): 
        # Root Node 
        self.sym_NODE = self.component.createMenuSymbol(None, None )
        self.sym_NODE.setLabel("Analog Front End")

        # Current measurement
        self.sym_NODE_IA = self.component.createMenuSymbol("BSP_IA", self.sym_NODE)
        self.sym_NODE_IA.setLabel("Phase A current")
        
        available = [ "External op-amp", "Internal op-amp"]
        self.sym_NODE_IA_OPAMP = self.component.createComboSymbol("BSP_IA_OPAMP", self.sym_NODE_IA, available)
        self.sym_NODE_IA_OPAMP.setLabel("Op-amp")
       
        self.sym_NODE_IA_GAIN = self.component.createFloatSymbol("BSP_IA_GAIN", self.sym_NODE_IA)
        self.sym_NODE_IA_GAIN.setLabel("Gain")
        self.sym_NODE_IA_GAIN.setDefaultValue(float(self.information["IA"]["GAIN"]))
        self.sym_NODE_IA_GAIN.setDependencies(self.updateInformation, ["BSP_IA_GAIN"])
        
        self.sym_NODE_IA_OFFSET = self.component.createFloatSymbol("BSP_IA_OFFSET", self.sym_NODE_IA)
        self.sym_NODE_IA_OFFSET.setLabel("Offset (in Volts)")
        self.sym_NODE_IA_OFFSET.setDefaultValue(float(self.information["IA"]["OFFSET"]))
        self.sym_NODE_IA_OFFSET.setDependencies(self.updateInformation, ["BSP_IA_OFFSET"])
 
        self.sym_NODE_IA_SHUNT = self.component.createFloatSymbol("BSP_IA_SHUNT", self.sym_NODE_IA)
        self.sym_NODE_IA_SHUNT.setLabel("Shunt resistance (in Ohms)")
        self.sym_NODE_IA_SHUNT.setDefaultValue(float(self.information["IA"]["SHUNT"])) 
        self.sym_NODE_IA_SHUNT.setDependencies(self.updateInformation, ["BSP_IA_SHUNT"])

        # Current measurement
        self.sym_NODE_IB = self.component.createMenuSymbol("BSP_IB", self.sym_NODE)
        self.sym_NODE_IB.setLabel("Phase B current")
        
        available = [ "External op-amp", "Internal op-amp"]
        self.sym_NODE_IB_OPAMP = self.component.createComboSymbol("BSP_IB_OPAMP", self.sym_NODE_IB, available)
        self.sym_NODE_IB_OPAMP.setLabel("Op-amp")

        self.sym_NODE_IB_GAIN = self.component.createFloatSymbol("BSP_IB_GAIN", self.sym_NODE_IB)
        self.sym_NODE_IB_GAIN.setLabel("Gain")
        self.sym_NODE_IB_GAIN.setDefaultValue(float(self.information["IB"]["GAIN"]))
        self.sym_NODE_IB_GAIN.setDependencies(self.updateInformation, ["BSP_IB_GAIN"])
        

        self.sym_NODE_IB_OFFSET = self.component.createFloatSymbol("BSP_IB_OFFSET", self.sym_NODE_IB)
        self.sym_NODE_IB_OFFSET.setLabel("Offset (in Volts)")
        self.sym_NODE_IB_OFFSET.setDefaultValue(float(self.information["IB"]["OFFSET"]))
        self.sym_NODE_IB_OFFSET.setDependencies(self.updateInformation, ["BSP_IB_OFFSET"])

        self.sym_NODE_IB_SHUNT = self.component.createFloatSymbol("BSP_IB_SHUNT", self.sym_NODE_IB)
        self.sym_NODE_IB_SHUNT.setLabel("Shunt resistance (in Ohms)")
        self.sym_NODE_IB_SHUNT.setDefaultValue(float(self.information["IB"]["SHUNT"])) 
        self.sym_NODE_IB_SHUNT.setDependencies(self.updateInformation, ["BSP_IB_SHUNT"])
  
        # Voltage measurement
        self.sym_NODE_VDC = self.component.createMenuSymbol("BSP_VDC", self.sym_NODE)
        self.sym_NODE_VDC.setLabel("DC bus voltage")
        
        self.sym_NODE_VDC_TOP = self.component.createFloatSymbol("BSP_VDC_TOP", self.sym_NODE_VDC)
        self.sym_NODE_VDC_TOP.setLabel("Top resistance (in kOhms)")
        self.sym_NODE_VDC_TOP.setDefaultValue(float(self.information["VDC"]["TOP"]))
        self.sym_NODE_VDC_TOP.setDependencies(self.updateInformation, ["BSP_VDC_TOP"])

        self.sym_NODE_VDC_BOTTOM = self.component.createFloatSymbol("BSP_VDC_BOTTOM", self.sym_NODE_VDC)
        self.sym_NODE_VDC_BOTTOM.setLabel("Bottom resistance (in kOhms)")
        self.sym_NODE_VDC_BOTTOM.setDefaultValue(float(self.information["VDC"]["BOTTOM"]))
        self.sym_NODE_VDC_BOTTOM.setDependencies(self.updateInformation, ["BSP_VDC_BOTTOM"])

       
        self.sym_BOARD = self.component.createFloatSymbol(None, None)
        self.sym_BOARD.setVisible(False)
        self.sym_BOARD.setDependencies(self.updateBoardParameters, ["BSP_BOARD_SEL"])

              
    def updateInformation(self, symbol, event):
        keys = (symbol.getID()).split("_")
        self.information[keys[1]][keys[2]] = symbol.getValue()
        self.sendMessage()

    def updateBoardParameters(self, symbol, event): 
        self.readFromXml(event["symbol"].getValue())
       
        # Update Ia front end analog analog front end 
        self.sym_NODE_IA_GAIN.setValue( float(self.information["IA"]["GAIN"  ]))
        self.sym_NODE_IA_OFFSET.setValue( float(self.information["IA"]["OFFSET"]))
        self.sym_NODE_IA_SHUNT.setValue( float(self.information["IA"]["SHUNT" ]))

        # Update Ib front end analog front end
        self.sym_NODE_IB_GAIN.setValue( float(self.information["IB"]["GAIN"  ] ))
        self.sym_NODE_IB_OFFSET.setValue( float(self.information["IB"]["OFFSET"] ))
        self.sym_NODE_IB_SHUNT.setValue( float(self.information["IB"]["SHUNT" ] ))

        # Update dc bus voltage analog front end
        self.sym_NODE_VDC_TOP.setValue( float(self.information["VDC"]["TOP"   ] ))
        self.sym_NODE_VDC_BOTTOM.setValue( float(self.information["VDC"]["BOTTOM"] ))
   
    def handleMessage(self, id,  message):
       if( id == "MCPMSMFOC_ANALOG_FRONT_END"):
           return self.information

    def sendMessage( self ):
        Database.sendMessage("pmsm_foc", "BSP_ANALOG_FRONT_END", self.information)
         

    def __call__(self):
        self.createSymbols()
        self.sendMessage()
   
