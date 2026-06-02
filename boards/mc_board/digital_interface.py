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
#                                   Imports                                             #
#---------------------------------------------------------------------------------------#
from mc_device.gpio.gpio import GpioPeripheral

#---------------------------------------------------------------------------------------#
#                                 GLOBAL VARIABLES                                      #
#---------------------------------------------------------------------------------------#

class DigitalInterfaceClass(GpioPeripheral):
    def __init__(self, object_wrapper):
        GpioPeripheral.__init__(self, object_wrapper)
        self.object_wrapper = object_wrapper


        self.read_configuration_file()

    def read_configuration_file(self):
        self.information = {
            "BUTTONS": {},
            "LEDS": {}
        }

        for button in self.object_wrapper.components['Buttons']:
            self.information['BUTTONS'][button.name] = {
                "PAD": button.parameters['gpio_config']["pin_number"],
            }
        for led in self.object_wrapper.components['Leds']:
            self.information['LEDS'][led.name] = {
                "PAD": led.parameters['gpio_config']["pin_number"],
            }

    def update_information(self):
        self.read_configuration_file()
        self.send_information()
        self.update_pin_settings()

    def send_information(self):
        Database = self.object_wrapper.get_database_object()
        Database.sendMessage("pmsm_foc", "BSP_DIGITAL_INTERFACE", self.information)

    def handle_message(self, id, args):
        if "MCPMSMFOC_DIGITAL_INTERFACE" == id:
            return self.information

    def update_pin_settings(self):
        # Leds
        for led_id in self.information["LEDS"].keys():
            led_pad = str(self.information["LEDS"][led_id]["PAD"])
            self.set_led_pin(led_id, led_pad )

        # Buttons
        for button_id in self.information["BUTTONS"].keys():
            button_pad = str(self.information["BUTTONS"][button_id]["PAD"])
            self.set_button_pin(button_id, button_pad)

    def __call__(self):
        self.update_pin_settings()
        self.send_information()
