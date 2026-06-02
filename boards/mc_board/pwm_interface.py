# coding: utf-8
"""
****************************************************************************** 
Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
** Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
** THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
** IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

#---------------------------------------------------------------------------------------#
#                                           IMPORT                                      #
#---------------------------------------------------------------------------------------#
# Import the module from the specified folder
from mc_device.pwm.pwm import PwmPeripheral

#---------------------------------------------------------------------------------------#
#                                 GLOBAL VARIABLES                                      #
#---------------------------------------------------------------------------------------#

class PwmConfiguration(PwmPeripheral):
    def __init__(self, object_wrapper):
        PwmPeripheral.__init__(self, object_wrapper)
        self.object_wrapper = object_wrapper

        self.read_configuration_file()

    def read_configuration_file(self):
        self.information = {}

        for inverter in self.object_wrapper.components['Inverter']:
            instance = inverter.parameters['peripheral']['instance']
            self.information.setdefault(instance, {})
            peripheral = inverter.parameters['peripheral']
            gpio_pins = inverter.parameters['gpio_pins']

            channels = peripheral['channels']
            for phase, phase_info in channels.items():
                for side, side_info in [('low', 'low_side'), ('high', 'high_side')]:
                    channel = phase_info
                    pad = gpio_pins[phase][side_info]['gpio_config']['pin_number']
                    self.information[instance].setdefault(phase, {}).setdefault(side, {})["channel"] = channel
                    self.information[instance][phase][side]["pad"] = pad

            pad = gpio_pins['fault']['gpio_config']['pin_number']

            # Determine fault channel available for the instance and pad
            channel = self.fault_channel_get( instance, pad )
            self.information[instance]["fault_sources"] = {"channel": channel, "pad": pad}

    def handle_message(self, id,  message):
        if id == "MCPMSMFOC_PWM_INTERFACE":
            return self.information

    def update_information(self):
        self.read_configuration_file()
        self.update_pin_settings()
        self.send_information()

    def send_information(self):
        Database = self.object_wrapper.get_database_object()
        Database.sendMessage("pmsm_foc","BSP_PWM_INTERFACE", self.information )

    def update_pin_settings(self):
        for instance, phases in self.information.items():
            for phase, phase_dict in phases.items():
                if phase == 'fault_sources':
                    name = 'PWM_FAULT'
                    self.set_fault_source(name, instance, channel, phase_dict['pad'])
                else:
                    for side, channel_info in phase_dict.items():
                        channel = channel_info['channel']
                        pad = channel_info['pad']
                        pin_name_suffix = 'L' if side == 'low' else 'H'
                        pin_name = phase.upper() + '_PWM' + pin_name_suffix

                        if side == 'low':
                            self.set_low_side_pwm_pin(pin_name, instance, channel, pad)
                        elif side == 'high':
                            self.set_high_side_pwm_pin(pin_name, instance, channel, pad)


    def __call__(self):
        self.update_pin_settings()
        self.send_information()
