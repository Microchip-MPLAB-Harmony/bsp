# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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

import xml.etree.ElementTree as ET
import os

#Board parameters
board_PararameterDict = {}

#------------------------------------------------------------------------------------------------------------#
#                                             LOCAL FUNCTIONS                                                #
#------------------------------------------------------------------------------------------------------------#
execfile(os.path.join(Module.getPath(), "pic32mk_mcf_pim_mc", "config", "general_Functions.py"  ))
execfile(os.path.join(Module.getPath(), "pic32mk_mcf_pim_mc", "config", "board_data.py"         ))
execfile(os.path.join(Module.getPath(), "pic32mk_mcf_pim_mc", "config", "voltage_source.py"     ))
execfile(os.path.join(Module.getPath(), "pic32mk_mcf_pim_mc", "config", "analog_interface.py"   ))
execfile(os.path.join(Module.getPath(), "pic32mk_mcf_pim_mc", "config", "digital_interface.py"  ))
execfile(os.path.join(Module.getPath(), "pic32mk_mcf_pim_mc", "config", "pwm_interface.py"      ))
execfile(os.path.join(Module.getPath(), "pic32mk_mcf_pim_mc", "config", "position_interface.py" ))
execfile(os.path.join(Module.getPath(), "pic32mk_mcf_pim_mc", "config", "analog_frontend.py"    ))
execfile(os.path.join(Module.getPath(), "pic32mk_mcf_pim_mc", "config", "data_monitoring.py"    ))


#------------------------------------------------------------------------------------------------------------#
#                                              INSTANTIATION                                                 #
#------------------------------------------------------------------------------------------------------------#
def instantiateComponent(bspComponent):
   
    # Read xml data from the path 
    path = os.path.join(Module.getPath(),"pic32mk_mcf_pim_mc", "config", "board.xml")
    bspContent = ET.fromstring((open(path, "r")).read())

    global board_Information
    board_Information = mcBspI_ReadBoardInformation(bspContent, bspComponent)
    board_Information()

   
    global voltage_Source 
    voltage_Source = mcBspI_VoltageSourceClass(bspContent, bspComponent)
    voltage_Source()

    global analog_Interface 
    analog_Interface = mcBspI_AnalogInterfaceClass(bspContent, bspComponent)
    analog_Interface()

    global pwm_Interface
    pwm_Interface = mcBspI_PwmConfiguration(bspContent, bspComponent)
    pwm_Interface()

    global position_Interface
    position_Interface = mcBspI_PositionConfiguration(bspContent, bspComponent)
    position_Interface()
    
    global analog_Frontend
    analog_Frontend = mcBspI_AnalogFrontEndClass(bspContent, bspComponent)
    analog_Frontend()

    global digital_Interface
    digital_Interface = mcBspI_DigitalInterfaceClass(bspContent, bspComponent)
    digital_Interface()

    global data_Monitor
    data_Monitor = mcBspI_DataMonitorClass(bspContent, bspComponent)
    data_Monitor()
   

    BSP_NAME = "pic32mk_mcf_pim_mc"
    
    pinAttributes = [{"attrib":"type", "symbol":"BSP_CUSTOM_TYPE", "label":"Type Name"},
                     {"attrib":"mode", "symbol":"BSP_CUSTOM_MODE", "label":"Mode"},
                     {"attrib":"dir", "symbol":"BSP_CUSTOM_DIR", "label":"Direction"},
                     {"attrib":"lat", "symbol":"BSP_CUSTOM_LAT", "label":"Initial Latch Value"},
                     {"attrib":"od", "symbol":"BSP_CUSTOM_OD", "label":"Open Drain"},
                     {"attrib":"cn", "symbol":"BSP_CUSTOM_CN", "label":"Change Notice"},
                     {"attrib":"pu", "symbol":"BSP_CUSTOM_PU", "label":"Pull Up"},
                     {"attrib":"pd", "symbol":"BSP_CUSTOM_PD", "label":"Pull Down"}]

    pinTypes = [{"type":"LED_AH", "mode":"DIGITAL", "dir":"OUT"},
                {"type":"LED_AL", "mode":"DIGITAL", "dir":"OUT", "lat":"High"},
                {"type":"SWITCH_AH", "mode":"DIGITAL"},
                {"type":"SWITCH_AL", "mode":"DIGITAL"},
                {"type":"VBUS_AH", "mode":"DIGITAL", "dir":"OUT"},
                {"type":"VBUS_AL", "mode":"DIGITAL", "dir":"OUT","lat":"High"}]

    execfile(Variables.get("__BSP_DIR") + "/boards/config/bsp_common.py")


#------------------------------------------------------------------------------------------------------------#
#                                             MESSAGE HANDLING                                               #
#------------------------------------------------------------------------------------------------------------#
def handleMessage(messageID, args):
    
    if (messageID == "MCPMSMFOC_SELECTED_BOARD"):
        board_Information.updateSelectedBoard("MCPMSMFOC_SELECTED_BOARD", args)
        return
    
    if (messageID == "MCPMSMFOC_INITIAL_INFORMATION"):
        args["SELECTED_BOARD"] = selectedBoard
        return board_PararameterDict

    if ( messageID == "MCPMSMFOC_ANALOG_INTERFACE" ):
         result = analog_Interface.handleMessage(messageID, args)
         return result

    if(  messageID ==  "MCPMSMFOC_PWM_INTERFACE" ):
        return pwm_Interface.handleMessage(messageID, args)

    if( messageID ==  "MCPMSMFOC_POSITION_INTERFACE" ):
        return position_Interface.handleMessage(messageID, args)

    if( messageID == "MCPMSMFOC_ANALOG_FRONT_END"):
        return analog_Frontend.handleMessage(messageID, args)

    if( messageID == "MCPMSMFOC_DIGITAL_INTERFACE" ):
        message = digital_Interface.handleMessage(messageID, args)  
        return message

    if( messageID == "MCPMSMFOC_VOLTAGE_SOURCE" ):
        message = voltage_Source.handleMessage(messageID, args)  
        return message

    if( messageID == "MCPMSMFOC_BOARD_INFORMATION" ):
        message = board_Information.handleMessage(messageID, args)  
        return message

    if( messageID == "X2CSCOPE_DATA_MONITORING" ):
        message = data_Monitor.handleMessage(messageID, args)  
        return message

   
    
        