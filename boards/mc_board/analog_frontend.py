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

#---------------------------------------------------------------------------------------#
#                                 GLOBAL VARIABLES                                      #
#---------------------------------------------------------------------------------------#

class AnalogFrontEndClass:
    def __init__(self, object_wrapper):
        self.object_wrapper = object_wrapper

        # Read data from configuration files
        self.read_configuration_file()

    def read_configuration_file(self):
        # Module information
        self.information = {}

        for analog_circuit in self.object_wrapper.components['Analog_Circuits']:
            if analog_circuit.parameters['type'] == 'shunt_with_opamp':
                self.information[analog_circuit.name] = {
                    'SHUNT': analog_circuit.parameters['circuit_param']['shunt_resistor'],
                    'GAIN': analog_circuit.parameters['circuit_param']['opamp_gain'],
                    'OFFSET': analog_circuit.parameters['circuit_param']['opamp_bias'],
                    'PAD': analog_circuit.parameters['gpio_config']['pin_number'],
                }
            elif analog_circuit.parameters['type'] == 'voltage_divider':
                self.information[analog_circuit.name] = {
                    'TOP': analog_circuit.parameters['circuit_param']['top_resistor'],
                    'BOTTOM': analog_circuit.parameters['circuit_param']['bottom_resistor'],
                }
            elif analog_circuit.parameters['type'] == 'buffer':
                self.information[analog_circuit.name] = {
                }

    def update_information(self ):
        self.read_configuration_file()
        self.send_message()

    def handle_message(self, id,  message):
       if( id == "MCPMSMFOC_ANALOG_FRONT_END"):
           return self.information

    def send_message( self ):
        Database = self.object_wrapper.get_database_object()
        Database.sendMessage("pmsm_foc", "BSP_ANALOG_FRONT_END", self.information)


    def __call__(self):
        self.send_message()

