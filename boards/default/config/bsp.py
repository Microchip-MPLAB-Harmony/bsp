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

def instantiateComponent(bspComponent):

    BSP_NAME = "custom_bsp"
    peripheralNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals")

    if ("PIC32M" in Variables.get("__PROCESSOR")) or (("PIC32CX" in Variables.get("__PROCESSOR")) and ("BZ" in Variables.get("__PROCESSOR"))):
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
            {"type":"SWITCH_AL", "mode":"DIGITAL"}]
        for index in range (0, len(peripheralNode.getChildren())):
            if (peripheralNode.getChildren()[index].getAttribute("name") == "USB" and any(id in peripheralNode.getChildren()[index].getAttribute("id") for id in ["01195", "02813", "00124"])):
                pinTypes.append({"type":"VBUS_AH", "mode":"DIGITAL", "dir":"OUT"})
                pinTypes.append({"type":"VBUS_AL", "mode":"DIGITAL", "dir":"OUT", "lat":"High"})
    else:
        for index in range (0, len(peripheralNode.getChildren())):
            if ((peripheralNode.getChildren()[index].getAttribute("name") == "PIO") and
               ((peripheralNode.getChildren()[index].getAttribute("id") == "11264") or
                (peripheralNode.getChildren()[index].getAttribute("id") == "11004"))):

                pinAttributes = [{"attrib":"type", "symbol":"BSP_CUSTOM_TYPE", "label":"Type Name"},
                    {"attrib":"mode", "symbol":"BSP_CUSTOM_MODE", "label":"Mode"},
                    {"attrib":"dir", "symbol":"BSP_CUSTOM_DIR", "label":"Direction"},
                    {"attrib":"lat", "symbol":"BSP_CUSTOM_LAT", "label":"Initial Latch Value"},
                    {"attrib":"od", "symbol":"BSP_CUSTOM_OD", "label":"Open Drain"},
                    {"attrib":"cn", "symbol":"BSP_CUSTOM_CN", "label":"Change Notice"},
                    {"attrib":"pu", "symbol":"BSP_CUSTOM_PU", "label":"Pull Up"},
                    {"attrib":"pd", "symbol":"BSP_CUSTOM_PD", "label":"Pull Down"},
                    {"attrib":"int", "symbol":"BSP_CUSTOM_PIO_INTERRUPT", "label":"PIO Interrupt"}]
                pinTypes = [{"type":"LED_AH", "mode":"DIGITAL", "dir":"OUT"},
                    {"type":"LED_AL", "mode":"DIGITAL", "dir":"OUT"},
                    {"type":"SWITCH_AH", "mode":"DIGITAL"},
                    {"type":"SWITCH_AL", "mode":"DIGITAL"}]
                for index in range (0, len(peripheralNode.getChildren())):
                    if (any(name in peripheralNode.getChildren()[index].getAttribute("name") for name in ["USBHS", "UHP", "UDPHS"]) and any(id in peripheralNode.getChildren()[index].getAttribute("id") for id in ["11292", "6127", "6227"])):
                        pinTypes.append({"type":"VBUS_AH", "mode":"DIGITAL", "dir":"OUT"})
                        pinTypes.append({"type":"VBUS_AL", "mode":"DIGITAL", "dir":"OUT"})
                break
            elif ((peripheralNode.getChildren()[index].getAttribute("name") == "PORT") and
                  (peripheralNode.getChildren()[index].getAttribute("id").upper() == "U2210")):
                pinAttributes = [{"attrib":"type", "symbol":"BSP_CUSTOM_TYPE", "label":"Type Name"},
                    {"attrib":"mode", "symbol":"BSP_CUSTOM_MODE", "label":"Mode"},
                    {"attrib":"dir", "symbol":"BSP_CUSTOM_DIR", "label":"Direction"},
                    {"attrib":"lat", "symbol":"BSP_CUSTOM_LAT", "label":"Initial Latch Value"},
                    {"attrib":"pe", "symbol":"BSP_CUSTOM_PE", "label":"Pull Enable"},
                    {"attrib":"ie", "symbol":"BSP_CUSTOM_IE", "label":"Input Enable"}]

                pinTypes = [{"type":"LED_AH", "mode":"DIGITAL", "dir":"OUT"},
                    {"type":"LED_AL", "mode":"DIGITAL", "dir":"OUT", "lat":"High"},
                    {"type":"SWITCH_AH", "mode":"DIGITAL", "ie":"True"},
                    {"type":"SWITCH_AL", "mode":"DIGITAL", "ie":"True"}]
                if not any(x in Variables.get("__PROCESSOR") for x in ["SAML22", "SAMD11"]):
                    for index in range (0, len(peripheralNode.getChildren())):
                        if (peripheralNode.getChildren()[index].getAttribute("name") == "USB" and peripheralNode.getChildren()[index].getAttribute("id").upper() == "U2222"):
                            pinTypes.append({"type":"VBUS_AH", "mode":"DIGITAL", "dir":"OUT"})
                            pinTypes.append({"type":"VBUS_AL", "mode":"DIGITAL", "dir":"OUT", "lat":"High"})
                break

    execfile(Variables.get("__BSP_DIR") + "/boards/config/bsp_common.py")

