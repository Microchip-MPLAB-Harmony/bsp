# coding: utf-8
"""
*******************************************************************************
Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
Subject to your compliance with these terms, you may use Microchip software
and any derivatives exclusively with Microchip products. It is your
responsibility to comply with third party license terms applicable to your
use of third party software (including open source software) that may
accompany Microchip software.
THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
PARTICULAR PURPOSE.
IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*******************************************************************************
"""

#---------------------------------------------------------------------------------------#
#                                     Imports                                           #
#---------------------------------------------------------------------------------------#
# Import the module from the specified folder
from mc_device.adc.adc import AdcPeripheralClass

#---------------------------------------------------------------------------------------#
#                                  Global Variables                                     #
#---------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------#
#                                      Classes                                          #
#---------------------------------------------------------------------------------------#

class AnalogInterfaceClass(AdcPeripheralClass):
    def __init__(self, object_wrapper):
        AdcPeripheralClass.__init__(self, object_wrapper)

        self.object_wrapper = object_wrapper
        # self.board_data = board_data
        self.read_configuration_file()

    '''
        Board data format:
        'signal name':  {
                            'instance': {
                                        'channel': '',
                                        'pad': ''
                                        }
                        }
    '''
    def read_configuration_file(self):
        # Read data from the configuration file
        self.information = {}

        analog_circuits = self.object_wrapper.components.get('Analog_Circuits', [])

        for analog_circuit in analog_circuits:
            ac_name = analog_circuit.name
            ac_parameters = analog_circuit.parameters

            adc_pad = ac_parameters['gpio_config'].get('pin_number')
            adc_instance = ac_parameters['peripheral']['instance']
            adc_channel = ac_parameters['peripheral']['channel']

            if ac_name not in self.information:
                self.information[ac_name] = {}

            self.information[ac_name][adc_instance] = {
                'channel': adc_channel,
                'pad': adc_pad
            }


    def set_database_symbol(self, nameSpace, ID, value):
        Database = self.object_wrapper.get_database_object()
        status = Database.setSymbolValue(nameSpace, ID, value)
        if(status == False):
            print("BSP is unable to set {symbol} with {input}".format(symbol=ID, input=value))

    def update_information(self):
        self.read_configuration_file()
        self.update_pin_settings()
        self.send_information()

    def send_information(self):
        # Get database object
        Database = self.object_wrapper.get_database_object()
        Database.sendMessage("pmsm_foc", "BSP_ANALOG_INTERFACE", self.information)

    def handle_message(self, id, args):
        if id == "MCPMSMFOC_ANALOG_INTERFACE":
            return self.information

    def update_pin_settings(self):
        for name, adc_dict in self.information.items():
            for instance, interface in adc_dict.items():
                channel = interface['channel']
                pad  = interface['pad']

            # Update ADC pin
            self.set_adc_pin( name, instance, channel, pad)

    def __call__(self):
        self.update_pin_settings()
        self.send_information()
