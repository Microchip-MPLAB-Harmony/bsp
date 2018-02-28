<#--
/*******************************************************************************
  BSP Freemarker Template File

  Company:
    Microchip Technology Inc.

  File Name:
  system_config.h.ftl

  Summary:
    BSP Freemarker Template File

  Description:

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2014 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/
-->
<#--  =====================
      MACRO mhc_process_leds
      ===================== -->
<#macro mhc_process_leds>
<#assign LED_Name_List = []>
<#assign LED_PortPin_List = []>
<#assign LED_PortChannel_List = []>
<#assign LED_ActiveLevel_List = []>
<#list 1..350 as i>
<#assign functype = "core.PIN_" + i + "_FUNCTION_TYPE">
<#if .vars[functype]?has_content>
<#if (.vars[functype] == "LED_AH") || (.vars[functype] == "LED_AL")>
<#assign funcname = "core.PIN_" + i + "_FUNCTION_NAME">
<#if .vars[funcname]?has_content>
<#assign pinport = "core.PIN_" + i + "_PIO_PIN">
<#if .vars[pinport]?has_content>
<#assign pinchannel = "core.PIN_" + i + "_PIO_CHANNEL">
<#if .vars[pinchannel]?has_content>
<#assign LED_Name_List = LED_Name_List + [.vars[funcname]]>
<#assign LED_PortPin_List = LED_PortPin_List + [.vars[pinport]]>
<#assign LED_PortChannel_List = LED_PortChannel_List + [.vars[pinchannel]]>
<#if (.vars[functype] == "LED_AH")>
<#assign LED_ActiveLevel_List = LED_ActiveLevel_List + ["High"]>
<#else>
<#assign LED_ActiveLevel_List = LED_ActiveLevel_List + ["Low"]>
</#if>
</#if>
</#if>
</#if>
</#if>
</#if>
</#list>
</#macro>
<#--  =====================
      MACRO mhc_process_switches
      ===================== -->
<#macro mhc_process_switches>
<#assign Switch_Name_List = []>
<#assign Switch_PortPin_List = []>
<#assign Switch_PortChannel_List = []>
<#list 1..350 as i>
<#assign functype = "core.PIN_" + i + "_FUNCTION_TYPE">
<#if .vars[functype]?has_content>
<#if .vars[functype] == "SWITCH">
<#assign funcname = "core.PIN_" + i + "_FUNCTION_NAME">
<#if .vars[funcname]?has_content>
<#assign pinport = "core.PIN_" + i + "_PIO_PIN">
<#if .vars[pinport]?has_content>
<#assign pinchannel = "core.PIN_" + i + "_PIO_CHANNEL">
<#if .vars[pinchannel]?has_content>
<#assign Switch_Name_List = Switch_Name_List + [.vars[funcname]]>
<#assign Switch_PortPin_List = Switch_PortPin_List + [.vars[pinport]]>
<#assign Switch_PortChannel_List = Switch_PortChannel_List + [.vars[pinchannel]]>
</#if>
</#if>
</#if>
</#if>
</#if>
</#list>
</#macro>
<#--  =====================
      MACRO mhc_process_vbus
      ===================== -->
<#macro mhc_process_vbus>
<#assign VBUS_PortPin_List = []>
<#assign VBUS_PortChannel_List = []>
<#assign VBUS_ActiveLevel_List = []>
<#list 1..350 as i>
<#assign functype = "core.PIN_" + i + "_FUNCTION_TYPE">
<#if .vars[functype]?has_content>
<#if (.vars[functype] == "VBUS_AH") || (.vars[functype] == "VBUS_AL") || (.vars[functype] == "VBUS")>
<#assign pinport = "core.PIN_" + i + "_PIO_PIN">
<#if .vars[pinport]?has_content>
<#assign pinchannel = "core.PIN_" + i + "_PIO_CHANNEL">
<#if .vars[pinchannel]?has_content>
<#assign VBUS_PortPin_List = VBUS_PortPin_List + [.vars[pinport]]>
<#assign VBUS_PortChannel_List = VBUS_PortChannel_List + [.vars[pinchannel]]>
<#if (.vars[functype] == "VBUS_AL")>
<#assign VBUS_ActiveLevel_List = VBUS_ActiveLevel_List + ["Low"]>
<#else>
<#assign VBUS_ActiveLevel_List = VBUS_ActiveLevel_List + ["High"]>
</#if>
</#if>
</#if>
</#if>
</#if>
</#list>
</#macro>
<#--  =====================
      MACRO mhc_process_gpio_out
      ===================== -->
<#macro mhc_process_gpio_out>
<#assign GPIO_OUT_Name_List = []>
<#assign GPIO_OUT_PortPin_List = []>
<#assign GPIO_OUT_PortChannel_List = []>
<#list 1..350 as i>
<#assign functype = "core.PIN_" + i + "_FUNCTION_TYPE">
<#if .vars[functype]?has_content>
<#if .vars[functype] == "GPIO_OUT">
<#assign funcname = "core.PIN_" + i + "_FUNCTION_NAME">
<#if .vars[funcname]?has_content>
<#assign pinport = "core.PIN_" + i + "_PIO_PIN">
<#if .vars[pinport]?has_content>
<#assign pinchannel = "core.PIN_" + i + "_PIO_CHANNEL">
<#if .vars[pinchannel]?has_content>
<#assign GPIO_OUT_Name_List = GPIO_OUT_Name_List + [.vars[funcname]]>
<#assign GPIO_OUT_PortPin_List = GPIO_OUT_PortPin_List + [.vars[pinport]]>
<#assign GPIO_OUT_PortChannel_List = GPIO_OUT_PortChannel_List + [.vars[pinchannel]]>
</#if>
</#if>
</#if>
</#if>
</#if>
</#list>
</#macro>
<#--  =====================
      MACRO mhc_process_gpio_in
      ===================== -->
<#macro mhc_process_gpio_in>
<#assign GPIO_IN_Name_List = []>
<#assign GPIO_IN_PortPin_List = []>
<#assign GPIO_IN_PortChannel_List = []>
<#list 1..350 as i>
<#assign functype = "core.PIN_" + i + "_FUNCTION_TYPE">
<#if .vars[functype]?has_content>
<#if .vars[functype] == "GPIO_IN">
<#assign funcname = "core.PIN_" + i + "_FUNCTION_NAME">
<#if .vars[funcname]?has_content>
<#assign pinport = "core.PIN_" + i + "_PIO_PIN">
<#if .vars[pinport]?has_content>
<#assign pinchannel = "core.PIN_" + i + "_PIO_CHANNEL">
<#if .vars[pinchannel]?has_content>
<#assign GPIO_IN_Name_List = GPIO_IN_Name_List + [.vars[funcname]]>
<#assign GPIO_IN_PortPin_List = GPIO_IN_PortPin_List + [.vars[pinport]]>
<#assign GPIO_IN_PortChannel_List = GPIO_IN_PortChannel_List + [.vars[pinchannel]]>
</#if>
</#if>
</#if>
</#if>
</#if>
</#list>
</#macro>
<#--  =====================
      MACRO mhc_process_gpio
      ===================== -->
<#macro mhc_process_gpio>
<#assign GPIO_Name_List = []>
<#assign GPIO_PortPin_List = []>
<#assign GPIO_PortChannel_List = []>
<#list 1..350 as i>
<#assign functype = "core.PIN_" + i + "_FUNCTION_TYPE">
<#if .vars[functype]?has_content>
<#if .vars[functype] == "GPIO">
<#assign funcname = "core.PIN_" + i + "_FUNCTION_NAME">
<#if .vars[funcname]?has_content>
<#assign pinport = "core.PIN_" + i + "_PIO_PIN">
<#if .vars[pinport]?has_content>
<#assign pinchannel = "core.PIN_" + i + "_PIO_CHANNEL">
<#if .vars[pinchannel]?has_content>
<#assign GPIO_Name_List = GPIO_Name_List + [.vars[funcname]]>
<#assign GPIO_PortPin_List = GPIO_PortPin_List + [.vars[pinport]]>
<#assign GPIO_PortChannel_List = GPIO_PortChannel_List + [.vars[pinchannel]]>
</#if>
</#if>
</#if>
</#if>
</#if>
</#list>
</#macro>
<#--  =====================
      MACRO execution
      ===================== -->
<@mhc_process_leds/>
<@mhc_process_switches/>
<@mhc_process_vbus/>
<@mhc_process_gpio_out/>
<@mhc_process_gpio_in/>
<@mhc_process_gpio/>

/*** Application Defined Pins ***/
<#if (LED_Name_List?size > 0)>
<#list LED_Name_List as ledName>
<#list LED_PortChannel_List as ledChannel>
<#list LED_PortPin_List as ledPinPos>
<#list LED_ActiveLevel_List as ledActiveLevel>
<#if ledName?counter == ledChannel?counter><#if ledName?counter == ledPinPos?counter><#if ledName?counter == ledActiveLevel?counter>

/*** Functions for ${ledName} pin ***/
#define ${ledName}Toggle() PIO_PortToggle(PIO_PORT_${ledChannel}, 0x1<<${ledPinPos})
<#if ledActiveLevel == "High">
#define ${ledName}On() PIO_PortSet(PIO_PORT_${ledChannel}, 0x1<<${ledPinPos})
#define ${ledName}Off() PIO_PortClear(PIO_PORT_${ledChannel}, 0x1<<${ledPinPos})
#define ${ledName}StateGet() (PIO_PortRead(PIO_PORT_${ledChannel}) & (0x1<<${ledPinPos}))
<#else>
#define ${ledName}On() PIO_PortClear(PIO_PORT_${ledChannel}, 0x1<<${ledPinPos})
#define ${ledName}Off() PIO_PortSet(PIO_PORT_${ledChannel}, 0x1<<${ledPinPos})
#define ${ledName}StateGet() !(PIO_PortRead(PIO_PORT_${ledChannel}) & (0x1<<${ledPinPos}))
</#if>
</#if></#if></#if>
</#list>
</#list>
</#list>
</#list>
</#if>
<#if (Switch_Name_List?size > 0)>
<#list Switch_Name_List as SwitchName>
<#list Switch_PortChannel_List as SwitchChannel>
<#list Switch_PortPin_List as SwitchPinPos>
<#if SwitchName?counter == SwitchChannel?counter><#if SwitchName?counter == SwitchPinPos?counter>

/*** Functions for ${SwitchName} pin ***/
#define ${SwitchName}StateGet() (PIO_PortRead(PIO_PORT_${SwitchChannel}) & (0x1<<${SwitchPinPos}))
</#if></#if>
</#list>
</#list>
</#list>
</#if>
<#if (GPIO_OUT_Name_List?size > 0)>
<#list GPIO_OUT_Name_List as gpio_outName>
<#list GPIO_OUT_PortChannel_List as gpio_outChannel>
<#list GPIO_OUT_PortPin_List as gpio_outPinPos>
<#if gpio_outName?counter == gpio_outChannel?counter><#if gpio_outName?counter == gpio_outPinPos?counter>

/*** Functions for ${gpio_outName} pin ***/
#define ${gpio_outName}Toggle() PIO_PortToggle(PIO_PORT_${gpio_outChannel}, 0x1<<${gpio_outPinPos})
#define ${gpio_outName}On() PIO_PortSet(PIO_PORT_${gpio_outChannel}, 0x1<<${gpio_outPinPos})
#define ${gpio_outName}Off() PIO_PortClear(PIO_PORT_${gpio_outChannel}, 0x1<<${gpio_outPinPos})
#define ${gpio_outName}StateGet() (PIO_PortRead(PIO_PORT_${gpio_outChannel}) & (0x1<<${gpio_outPinPos}))
#define ${gpio_outName}StateSet(Value) PIO_PinWrite(PIO_PIN_P${gpio_outChannel}${gpio_outPinPos}, Value)
</#if></#if>
</#list>
</#list>
</#list>
</#if>
<#if (GPIO_IN_Name_List?size > 0)>
<#list GPIO_IN_Name_List as gpio_inName>
<#list GPIO_IN_PortChannel_List as  gpio_inChannel>
<#list GPIO_IN_PortPin_List as  gpio_inPinPos>
<#if  gpio_inName?counter ==  gpio_inChannel?counter><#if  gpio_inName?counter ==  gpio_inPinPos?counter>

/*** Functions for ${ gpio_inName} pin ***/
#define ${gpio_inName}StateGet() (PIO_PortRead(PIO_PORT_${gpio_inChannel}) & (0x1<<${gpio_inPinPos}))
</#if></#if>
</#list>
</#list>
</#list>
</#if>
<#if (GPIO_Name_List?size > 0)>
<#list GPIO_Name_List as gpioName>
<#list GPIO_PortChannel_List as  gpioChannel>
<#list GPIO_PortPin_List as  gpioPinPos>
<#if  gpioName?counter ==  gpioChannel?counter><#if  gpioName?counter ==  gpioPinPos?counter>

/*** Functions for ${ gpioName} pin ***/
#define ${gpioName}_PORT PIO_PORT_${gpioChannel}
#define ${gpioName}_PIN ${gpioPinPos}
#define ${gpioName}_PIN_MASK (0x1 << ${gpioPinPos})
</#if></#if>
</#list>
</#list>
</#list>
</#if>
<#--
/*******************************************************************************
 End of File
*/
-->

