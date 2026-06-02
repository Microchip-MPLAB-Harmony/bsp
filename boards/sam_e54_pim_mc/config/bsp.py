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

#--------------------------------------------------------------------------------------------#
#                             Import                                                         #
#--------------------------------------------------------------------------------------------#
import sys
import os
import json
import xml.etree.ElementTree as ET

# Add the folder path to the system path
sys.path.append(Module.getPath())

from mc_board.board_data import BoardAdapter
from mc_board.board_data import BoardParameters

#--------------------------------------------------------------------------------------------#
#                             CLASSES                                                        #
#--------------------------------------------------------------------------------------------#

class HarmonyObjectWrapper(BoardAdapter):
    def __init__(self, component):
        # Update component object handler
        self.component = component

        # Get supported board parameters
        self.board_params = self.get_board_params_from_files()

        # Initialize board adapter superclass
        BoardAdapter.__init__(self, self.board_params)

        # Set the default board parameters
        self.update_board_parameters('dsPICDEM MCLV2')

    def get_atdf_object(self):
        return ATDF

    def get_database_object(self):
        return Database

    def get_module_object(self):
        return Module

    def get_component(self):
        return self.component

    def get_board_params_from_files(self):
        supported_boards = {}
        directory_path = os.path.join(Module.getPath(), "sam_e54_pim_mc", "config", "boards")

        # Traverse through the configuration folder
        for file_name in os.listdir(directory_path):
            print('Supported Boards', file_name, os.listdir(directory_path))
            if file_name.endswith('.json'):
                file_path = os.path.join(directory_path, file_name)
                try:
                    with open(file_path, 'r') as json_file:
                        data = json.load(json_file)
                        if data:  # Check if JSON data is not empty
                            root_key = next(iter(data.keys()))  # Get the first key
                            supported_boards.update(data)
                except ValueError as e:
                    print("Error parsing JSON file {}: {}".format(file_path, e))
        return supported_boards


class BspManager:
    def __init__(self, object_wrapper):
        # Update object_wrapper interface handler
        self.object_wrapper = object_wrapper

        # Create board information object
        from mc_board.voltage_source import VoltageSourceClass
        self.voltage_source = VoltageSourceClass(object_wrapper)

        # Create board information object
        from mc_board.analog_interface import AnalogInterfaceClass
        self.analog_interface = AnalogInterfaceClass(object_wrapper)

        # Create position interface class
        from mc_board.position_interface import PositionInterfaceClass
        self.position_interface = PositionInterfaceClass(object_wrapper)

        # Create board information object
        from mc_board.pwm_interface import PwmConfiguration
        self.pwm_interface = PwmConfiguration(object_wrapper)

        # Create board information object
        from mc_board.analog_frontend import AnalogFrontEndClass
        self.analog_frontend = AnalogFrontEndClass(object_wrapper)

        # Create board information object
        from mc_board.digital_interface import DigitalInterfaceClass
        self.digital_interface = DigitalInterfaceClass(object_wrapper)

        # Create board information object
        from mc_board.data_monitoring import DataMonitorClass
        self.data_monitor = DataMonitorClass(object_wrapper)

    def create_symbols(self):
        # MHC Symbols
        board_List =  self.object_wrapper.board_params.keys()

        component = self.object_wrapper.get_component()
        self.selected_board = component.createComboSymbol("BSP_BOARD_SEL", None, board_List )
        self.selected_board.setLabel("Development Board")
        self.selected_board.setDefaultValue('dsPICDEM MCLV2')
        self.selected_board.setDependencies( self.update_board, ["BSP_BOARD_SEL"] )

    def update_board( self, symbol, event ):
        selected_board = symbol.getValue()

        from mc_device.gpio.pin_manager import PinManager
        PinManager(self.object_wrapper).reset_all_pins()

        self.object_wrapper.update_board_parameters(selected_board)
        self.voltage_source.update_information()
        self.analog_interface.update_information()
        self.position_interface.update_information()
        self.pwm_interface.update_information()
        self.analog_frontend.update_information()
        self.digital_interface.update_information()
        self.data_monitor.update_information()

    def handle_message(self, id, args):
        if (id == "MCPMSMFOC_SELECTED_BOARD"):
            self.selected_board.setValue(args["SELECTED_BOARD"])
            return

        if (id == "MCPMSMFOC_INITIAL_INFORMATION"):
            args["SELECTED_BOARD"] = self.selected_board.getValue()
            return {}

        if ( id == "MCPMSMFOC_ANALOG_INTERFACE" ):
            result = self.analog_interface.handle_message(id, args)
            return result

        if( id ==  "MCPMSMFOC_PWM_INTERFACE" ):
            return self.pwm_interface.handle_message(id, args)

        if( id ==  "MCPMSMFOC_POSITION_INTERFACE" ):
            return self.position_interface.handle_message(id, args)

        if( id == "MCPMSMFOC_ANALOG_FRONT_END"):
            return self.analog_frontend.handle_message(id, args)

        if( id == "MCPMSMFOC_DIGITAL_INTERFACE" ):
            message = self.digital_interface.handle_message(id, args)
            return message

        if( id == "MCPMSMFOC_VOLTAGE_SOURCE" ):
            message = self.voltage_source.handle_message(id, args)
            return message

        if( id == "X2CSCOPE_DATA_MONITORING" ):
            message = self.data_monitor.handle_message(id, args)
            return message


    def __call__(self, bspComponent):
        # Voltage source information
        self.voltage_source()

        # Analog interface information
        self.analog_interface()

        # Position interface information
        self.position_interface()

        # PWM interface information
        self.pwm_interface()

        # Analog front-end information
        self.analog_frontend()

        # Digital information
        self.digital_interface()

        # Data monitoring interface
        self.data_monitor()

        # Create BSP symbols
        self.create_symbols()


#--------------------------------------------------------------------------------------------#
#                             INSTANTIATION                                                  #
#--------------------------------------------------------------------------------------------#
def instantiateComponent(bsp_component):
    # Create object_wrapper class object
    object_wrapper = HarmonyObjectWrapper(bsp_component)

    global bsp
    bsp = BspManager(object_wrapper)
    bsp(bsp_component)

   # Note: This symbol is needed by the pin manager plugin. Otherwise, the pin manager would crash
    bsp_type_size = bsp_component.createIntegerSymbol("BSP_TYPE_SIZE", None )
    bsp_type_size.setVisible( False )
    bsp_type_size.setDefaultValue(0)

#--------------------------------------------------------------------------------------------#
#                             MESSAGE HANDLING                                               #
#--------------------------------------------------------------------------------------------#
def handleMessage(id, args):
    bsp.handle_message(id, args)