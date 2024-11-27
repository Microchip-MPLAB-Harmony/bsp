![Microchip logo](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_logo.png)
![Harmony logo small](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_mplab_harmony_logo_small.png)

# Microchip MPLAB® Harmony 3 Release Notes
## BSP Release v3.21.1
### New features

- None

### Bug fixes
- Updated BSP for PIC32CZ CA80 Curiosity Ultra Board
- Updated BSP for PIC32CZ CA90 Curiosity Ultra Board
- Updated BSP for WBZ653 Curiosity Board

### Known issues

- None

## BSP Release v3.21.0
### New features

Added support for the following development kits:

- MCS MCLV-48V-300W Development Board for PIC32MK MCM Motor Control DIM
- MCS MCLV-48V-300W Development Board for PIC32MK MCA Motor Control DIM
- MCS MCLV-48V-300W Development Board for PIC32CM MC00 Motor Control DIM
- MCS MCLV-48V-300W Development Board for ATSAME54 Motor Control DIM
- MCS MCLV-48V-300W Development Board for ATSAMC21 Motor Control DIM
- MCS MCLV-48V-300W Development Board for ATSAME70 Motor Control DIM
- PIC32CM GC Curiosity Board
- PIC32CM SG Curiosity Board

### Bug fixes
- Fixed the encoder pins for dsPICDEM MCLV2 for PIC32MK MCM and PIC32MK MCF in their respective PIM bsp 
- Updated motor control plug-in modules for the following MC devices: PIC32MK MCM, PIC32MK MCA, PIC32CM MC00, ATSAME54, ATSAMC21, and ATSAME70
- BSP pin_manager class typo fix

### Known issues

- None

## BSP Release v3.21.0-E1
### New features

This Engineering Release adds support for [WBZ653 Curiosity Board]() development kit.

### Bug fixes
- None

### Known issues
- None

## BSP Release v3.20.1
### New features

- None

### Bug fixes
- Updated BSP for LED_RED PORT PIN to PC14 in SAM9X75 Curiosity Board.

### Known issues

- None

## BSP Release v3.20.0
### New features

This release adds support for the following development kits: 
1. [SAMA7D65 Curiosity Board](https://www.microchip.com/en-us/development-tool/EA89C15A)

### Bug fixes
- None

### Known issues
- None

## BSP Release v3.19.0
### New features

This release adds support for the following development kits: 
1. [SAM9x75 Curiosity Development Board]()
2. [PIC32MZ W1 WFI32IOT Board](https://www.microchip.com/en-us/development-tool/ev36w50a)
3. [WBZ451HPE Curiosity Developement board ()

### Bug fixes
- Fixed Vbus issue for PIC32CK_SG01 Curiosity Board

### Known issues
- None

## BSP Release v3.18.0
### New features

This release adds support for the following development kits: 
1. [SAMA5D29 Curiosity Development Board](https://www.microchip.com/en-us/development-tool/ev07r15a)

### Known issues
- None

## BSP Release v3.17.0
### New features

This release adds support for the following development kits: 
1. [PIC32CX SG41 Curiosity Ultra Evaluation Board](https://www.microchip.com/en-us/development-tool/ev06x38a)
2. [PIC32CX SG61 Curiosity Ultra Evaluation Board](https://www.microchip.com/en-us/development-tool/ev09h35a)

### Bug fixes
- None

### Known issues

None

## BSP Release v3.16.1
### New features
None

### Bug fixes
- Corrected file names from upper case to lower case for Linux compatibility in pic32mk_mca_pim_mc, pic32mk_mcf_pim_mc, pic32mk_mcm_pim_mc, sam_e54_pim_mc and sam_e70_pim_mc BSP.

### Known issues

None

## BSP Release v3.16.0
### New features

Added board specific name to allow code customizations based on BSP

### Known issues

None

## BSP Release v3.15.0
### New features

This release adds support for the following development kits:
1. [PIC32CXMTSH Development Board](https://www.microchip.com/en-us/development-tool/PIC32CXMTSH-DB)
2. [PIC32CXMTC Development Board](https://www.microchip.com/en-us/development-tool/EV58E84A)
3. [PIC32CXMTG Evaluation Kit](https://www.microchip.com/en-us/development-tool/EV11K09A)

### Known issues

None

## BSP Release v3.15.0-E2
### New features

This engineering release adds support for the following development kits:
1. PIC32CK-GC01 Curiosity Ultra Board
2. PIC32CK-SG01 Curiosity Ultra Board

### Known issues

Same as v3.14.0

## BSP Release v3.15.0-E1
### New features

Added support for the PIC32CZ-C80 Curiosity Ultra Board

### Known issues

Same as v3.14.0

## BSP Release v3.14.0
### New features

Added support for the following development kits:
1. PIC32MK MCA Motor Control Plug In Module
2. DSPICDEM™ MCHV-3 Development Board for [PIC32MK1024 Motor Control Plug In Module](https://www.microchip.com/en-us/development-tool/MA320024)
3. DSPICDEM™ MCHV-3 Development Board for [ATSAME54 Motor Control Plug In Module](https://www.microchip.com/en-us/development-tool/MA320207)
4. DSPICDEM™ MCHV-3 Development Board for [ATSAME70 Motor Control Plug In Module](https://www.microchip.com/en-us/development-tool/MA320203)
5. DSPICDEM™ MCHV-3 Development Board for [PIC32MK MCM Motor Control Plug In Module](https://www.microchip.com/en-us/development-tool/MA320211)
6. [SAM9X60 Curiosity Development Board](https://www.microchip.com/en-us/development-tool/EV40E67A)

### Known issues

BSP LEDs related macros will not be generated if Pin Manager is launched before adding BSP to the project graph. As a workaround, add BSP to the project graph first before launching Pin manager.

## BSP Release v3.13.0
### New features

Added support for the following development kits:
1. PIC32CM JH01 Curiosity Pro Evaluation Kit
2. PIC32MK MCA Curiosity Pro Board
3. [PIC32CX BZ2 Curiosity Board](https://www.microchip.com/en-us/development-tool/EA71C53A)
4. [SAMRH707F18 Evaluation Kit](https://www.microchip.com/en-us/development-tool/SAMRH707F18-EK)
5. [SAMA7G54 Evaluation Kit](https://www.microchip.com/en-us/development-tool/EV21H18A)

### Known issues

BSP LEDs related macros will not be generated if Pin Manager is launched before adding BSP to the project graph. As a workaround, add BSP to the project graph first before launching Pin manager.

## BSP Release v3.12.0
### New features

Added support for the CEC1736 Evaluation Board

### Known issues

BSP LEDs related macros will not be generated if Pin Manager is launched before adding BSP to the project graph. As a workaround, add BSP to the project graph first before launching Pin manager.

## BSP Release v3.11.1
### New features
None

### Bug fixes
- Corrected the module path name in SAM E70 PIM, SAM E54 PIM, PIC32MK MCM PIM and PIC32MK MCF PIM BSPs.
- Corrected the message ID used for communicating between the PMSM FOC component and PIC32MK MCF PIM BSP.

### Known issues

There are no known issues

## BSP Release v3.11.0
### New features

Added support for the following development kits:
1. [LAN9255 Evaluation Board](https://www.microchip.com/en-us/development-tool/EV25Y25A)
2. [PIC32MK1024 Motor Control Plug In Module](https://www.microchip.com/en-us/development-tool/MA320024)
3. [ATSAME54 Motor Control Plug In Module](https://www.microchip.com/en-us/development-tool/MA320207)
4. [ATSAME70 Motor Control Plug In Module](https://www.microchip.com/en-us/development-tool/MA320203)
5. [PIC32MK MCM Motor Control Plug In Module](https://www.microchip.com/en-us/development-tool/MA320211)

### Known issues

There are no known issues

## BSP Release v3.10.0
### New features

Added support for the following development kits:
1. [SAM E51 CURIOSITY NANO EVALUATION KIT](https://www.microchip.com/Developmenttools/ProductDetails/EV76S68A)
2. [PIC32 WFI32E CURIOSITY BOARD](https://www.microchip.com/en-us/development-tool/EV12F11A)
3. [WLR089 XPLAINED PRO EVALUATION KIT](https://www.microchip.com/en-us/development-tool/EV23M25A)
4. [PIC32MM CURIOSITY DEVELOPMENT BOARD](https://www.microchip.com/en-us/development-tool/DM320101)
5. [PIC32MM USB CURIOSITY DEVELOPMENT BOARD](https://www.microchip.com/en-us/development-tool/dm320107)
6. [SAM-IOT WG DEVELOPMENT BOARD](https://www.microchip.com/en-us/development-tool/EV75S95A)
7. [PIC32CM MC00 CURIOSITY NANO EVALUATION KIT](https://www.microchip.com/en-us/development-tool/EV10N93A)
8. [PL360G55CF EVALUATION BOARD](https://www.microchip.com/en-us/development-tool/PL360G55CF-EK)
9. [PL485 EVALUATION KIT](https://www.microchip.com/en-us/development-tool/PL485-EK)
10. [PL360G55CB EVALUATION BOARD](https://www.microchip.com/en-us/development-tool/PL360G55CB-EK)
11. [SAMR34 XPLAINED PRO EVALUATION KIT](https://www.microchip.com/en-us/development-tool/dm320111)


### Known issues

There are no known issues

## BSP Release v3.9.0
### New features

Added support for the following development kits:
1. [PIC32MX Starter Kit](https://www.microchip.com/Developmenttools/ProductDetails/DM320001)
2. [SAMA5D2 WLSOM1 EK1](https://www.microchip.com/Developmenttools/ProductDetails/DM320117)

### Known issues

There are no known issues

## BSP Release v3.8.2
### New Features
- Minor updates to BSP

### Known Issues

There are no known issues 

## BSP Release v3.8.1
### New Features
- Updated supported product families 

### Known Issues

There are no known issues 

## BSP Release v3.8.0
### New features

Added support for the following development kits:
1. SAMA5D27 SOM1 Kit1

### Known issues

There are no known issues

## BSP Release v3.7.0
### New features

Added support for the following development kits:
1. [SAML11 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320205)
2. [SAM D21 Curiosity Nano Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/DM320119)
3. [BM83 Bluetooth Audio Development Board](https://www.microchip.com/developmenttools/ProductDetails/DM164152)
4. PIC32MZ DA Curiosity

### Known issues

There are no known issues


## BSP Release v3.6.1
### New Features
- Updated PIC32MK MCJ BSP 

### Known Issues

There are no known issues 

## BSP Release v3.6.0
### New features

Added support for the following development kits:
1. [SAM HA1G16A Xplained Pro](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/ATSAMHA1G16A-XPRO)
2. PIC32MZ W1 Curiosity Board
3. PIC32MK MCM Curiosity Pro

### Known issues

There are no known issues

## BSP Release v3.5.0
### New features

Added support for the following development kits:

1. [SAM DA1 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/ATSAMDA1-XPRO)
2. [SAM D11 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsamd11-xpro)
3. [SAM D10 Xplained Mini Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/ATSAMD10-XMINI)
4. [PIC32MX Ethernet Starter Kit II](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320004-2)
5. [PIC32MZ Embedded Graphics with Stacked DRAM (DA) Starter Kit](https://www.microchip.com/Developmenttools/ProductDetails/DM320010)
6. [PIC32MZ Embedded Graphics with Stacked DRAM (DA) Starter Kit (Crypto)](https://www.microchip.com/Developmenttools/ProductDetails/DM320010-C)
7. [PIC32MZ Embedded Graphics with External DRAM (DA) Starter Kit](https://www.microchip.com/Developmenttools/ProductDetails/DM320008)
8. [PIC32MZ Embedded Graphics with External DRAM (DA) Starter Kit (Crypto)](https://www.microchip.com/Developmenttools/ProductDetails/DM320008-C)
9. PIC32MK MCJ Curiosity Pro Board
10. PIC32MK GPL Curiosity Pro Board
11. SAM RH71 Evaluation Kit

### Known issues

There are no known issues


## BSP Release v3.4.0
### New features

Added support for the following development kits:

1. [SAM L10 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320204)
2. [SAM G55 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsamg55-xpro)
3. [PIC32 Bluetooth Audio Development Kit](https://www.microchip.com/Developmenttools/ProductDetails/DV320032)

### Known issues

There are no known issues

## BSP Release v3.3.0
### New features

Added support for the following development kits:

1. [MPLAB Starter Kit for PIC32MX1XX/2XX](https://www.microchip.com/DevelopmentTools/ProductDetails/DM320013)
2. [PIC32MX1/2/5 Starter Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/DM320100)
3. [PIC32MX274 XLP Starter Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/DM320105)
4. [SAM E54 Curiosity Ultra Kit](https://www.microchip.com/Developmenttools/ProductDetails/DM320210)
5. [Curiosity PIC32MX470 Development Board](https://www.microchip.com/Developmenttools/ProductDetails/DM320103)
6. [Curiosity PIC32MZEF Development Board](https://www.microchip.com/Developmenttools/ProductDetails/DM320209)
7. [PIC32MZ Embedded Graphics with External DRAM (DA) Starter Kit (Crypto)](https://www.microchip.com/Developmenttools/ProductDetails/DM320008-C)
8. [SAM L21 Xplained Pro Evaluation Kit](https://www.microchip.com/Developmenttools/ProductDetails/ATSAML21-XPRO-B)
9. [SAM L22 Xplained Pro Evaluation Kit](https://www.microchip.com/Developmenttools/ProductDetails/ATSAML22-XPRO-B)
10. [PIC32 USB Starter Kit III](https://www.microchip.com/Developmenttools/ProductDetails/DM320003-3)
11. [SAM 9x60 Evaluation Kit](https://www.microchip.com/design-centers/32-bit-mpus)

### Known issues

There are no known issues

## BSP Release v3.2.1
### New features

Added support for the following development kits:

1. [PIC32MK GP Development Kit](https://www.microchip.com/Developmenttools/ProductDetails/DM320106)

### Known issues

There are no known issues

## BSP Release v3.2.0
### New features

Added support for the following development kits:

1. [SAM E54 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/ATSAME54-XPRO)
1. [SAMA5D2 Xplained Ultra Evaluation Kit](https://www.microchip.com/Developmenttools/ProductDetails/ATSAMA5D2C-XULT)
1. [PIC32MZ Embedded Graphics with Stacked DRAM (DA) Starter Kit (Crypto)](https://www.microchip.com/DevelopmentTools/ProductDetails/DM320010-C)
1. [PIC32MZ Embedded Connectivity with FPU (EF) Starter Kit](https://www.microchip.com/Developmenttools/ProductDetails/DM320007)

### Known issues

There are no known issues

## BSP Release v3.1.0
### New features

Added support for the following development kits:

1. [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/DM320113)
1. [SAM C21N Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsamc21n-xpro)
1. [SAM C21 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/ATSAMC21-XPRO)
1. [SAM D20 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD20-XPRO)
1. [SAM D21 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMD21-XPRO)

### Known issues

There are no known issues

## BSP Release v3.0.0
### New features

Added support for the following development kits:

1. [SAM E70 Xplained Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsame70-xpld)
1. [SAM V71 Xplained Ultra Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails.aspx?PartNO=ATSAMV71-XULT)

### Known issues

There are no known issues
