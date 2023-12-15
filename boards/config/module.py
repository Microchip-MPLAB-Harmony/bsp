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

def loadModule():
	print("Load Module: BSP")

	configName = "Custom"

	bspDefault = Module.CreateComponent("BSP_default", configName + " Board (BSP)", "/Board Support Packages (BSPs)/", "default/config/bsp.py")

	import xml.etree.ElementTree as ET
	bspFile = open(Variables.get("__BSP_DIR") + "/boards/module.xml", "r")
	bspContent = ET.fromstring(bspFile.read())
	for Board in bspContent.iter("Board"):
		if Board.attrib['processor'] == Variables.get("__PROCESSOR"):
			print("BSP: Load " + Board.attrib['name'])
			Id = Board.attrib['name'].replace(" ", "_")
			bspComponent = Module.CreateComponent("BSP_" + Id, Board.attrib['name'] + " BSP", "/Board Support Packages (BSPs)/", Board.attrib['config'] + "/config/bsp.py")
	
