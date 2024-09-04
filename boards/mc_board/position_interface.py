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
from mc_device.qdec.qdec import QdecPeripheral

#---------------------------------------------------------------------------------------#
#                                 Suppoted IPs                                          #
#---------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------#
#                                 Classes                                               #
#---------------------------------------------------------------------------------------#

class PositionInterfaceClass(QdecPeripheral):
    def __init__(self, object_wrapper):
        QdecPeripheral.__init__( self, object_wrapper)
        self.object_wrapper = object_wrapper

        # Read xml data from the path
        self.read_configuration_file()

    '''
        QDEC
           {
                'instance': {
                                'channel': {
                                                'qea': 'pad',
                                                'qeb': 'pad',
                                                'idx': 'pad'
                                            }
                            }

            }
    '''
    def read_configuration_file(self):
        self.information = { }

        for position_interface in self.object_wrapper.components['Position_Interface']:
            instance = position_interface.parameters['peripheral']["instance"]
            channel = position_interface.parameters['peripheral']["channel"]

            if channel == '':
                channel = 'channel'

        qea_pad = position_interface.parameters['gpio_pins']['qea']['gpio_config']['pin_number']
        qeb_pad = position_interface.parameters['gpio_pins']['qeb']['gpio_config']['pin_number']

        self.information[instance] = {
                                        channel: {
                                                    'qea': qea_pad,
                                                    'qeb': qeb_pad,
                                            }
                                     }

    def update_information(self):
        self.read_configuration_file()
        self.send_information()
        self.update_pin_settings()

    def send_information(self):
        Database = self.object_wrapper.get_database_object()
        Database.sendMessage("pmsm_foc", "BSP_POSITION_INTERFACE", self.information)

    def handle_message(self, id, args):
        if "MCPMSMFOC_POSITION_INTERFACE" == id:
            return self.information

    def update_pin_settings(self):
        instance = next(iter(self.information))
        channel = next(iter(self.information[instance]))

        qea_pad = self.information[instance][channel]['qea']
        qeb_pad = self.information[instance][channel]['qeb']

        self.set_qdec_pin('ENCODER', instance, channel, qea_pad, qeb_pad)

    def __call__(self):
        self.update_pin_settings()
        self.send_information()
