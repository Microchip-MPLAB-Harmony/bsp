![Microchip logo](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_logo.png)
![Harmony logo small](https://raw.githubusercontent.com/wiki/Microchip-MPLAB-Harmony/Microchip-MPLAB-Harmony.github.io/images/microchip_mplab_harmony_logo_small.png)

# MPLAB® Harmony 3 Board Support Package

MPLAB® Harmony 3 is an extension of the MPLAB® ecosystem for creating
embedded firmware solutions for Microchip 32-bit SAM and PIC® microcontroller
and microprocessor devices.  Refer to the following links for more information.

- [Microchip 32-bit MCUs](https://www.microchip.com/design-centers/32-bit)
- [Microchip 32-bit MPUs](https://www.microchip.com/design-centers/32-bit-mpus)
- [Microchip MPLAB X IDE](https://www.microchip.com/mplab/mplab-x-ide)
- [Microchip MPLAB Harmony](https://www.microchip.com/mplab/mplab-harmony)
- [Microchip MPLAB Harmony Pages](https://microchip-mplab-harmony.github.io/)

This repository contains the MPLAB® Harmony 3 Board Support Package (BSP).
Refer to the following links for release notes, training materials, and interface
reference information.

- [Release Notes](./release_notes.md)
- [MPLAB® Harmony License](mplab_harmony_license.md)

# Contents Summary

| Sl. No. | BSP Folder Name | Board Name | MCU |
| --------| --------------- |----------- |-----|
| 1 | pic32cm_mc00_cnano | [PIC32CM MC00 Curiosity Nano Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/EV10N93A) | PIC32CM1216MC00032 |
| 2 | pic32cm_mc00_curiosity_pro | [PIC32CM MC00 Curiosity Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/EV15N46A) | PIC32CM1216MC00048 |
| 3 | pic32mk_gp_db | [PIC32MK GP Development Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/DM320106) | PIC32MK1024GPE100 |
| 4 | pic32mk_mcj_curiosity_pro | P[IC32MK MCJ Curiosity Pro](https://www.microchip.com/DevelopmentTools/ProductDetails/PartNO/DT100113) | PIC32MK0512MCJ064 |
| 5 | pic32mk_mcm_curiosity_pro | [PIC32MK MCM Curiosity Pro Development Board](https://www.microchip.com/Developmenttools/ProductDetails/EV31E34A) | PIC32MK1024MCM100 |
| 6 | pic32mm_curiosity | [PIC32MM Curiosity Development Board](https://www.microchip.com/DevelopmentTools/ProductDetails/DM320101) | PIC32MM0064GPL036 |
| 7 | pic32mm_usb_curiosity | [PIC32MM USB Curiosity Development Board](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320107) | PIC32MM0256GPM064 |
| 8 | pic32mx_125_sk | [PIC32MX1/2/5 Starter Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/DM320100) | PIC32MX570F512L |
| 9 | pic32mx_bm83_evb | [BM83 Evaluation Board](https://www.microchip.com/developmenttools/ProductDetails/DM164152) | PIC32MX450F256L |
| 10 | pic32mx_eth_sk2 | [PIC32 Ethernet Starter Kit II](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320004-2) | PIC32MX795F512L |
| 11 | pic32mx_sk | [PIC32 Starter Kit](https://www.microchip.com/Developmenttools/ProductDetails/DM320001) | PIC32MX360F512L |
| 12 | pic32mx_usb_sk3 | [PIC32 USB Starter Kit III](https://www.microchip.com/Developmenttools/ProductDetails/DM320003-3) | PIC32MX470F512L |
| 13 | pic32mx_xlp_sk | [PIC32MX274 XLP Starter Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/DM320105) | PIC32MX274F256D |
| 14 | pic32mx470_curiosity | [Curiosity PIC32MX470 Development Board](https://www.microchip.com/Developmenttools/ProductDetails/DM320103) | PIC32MX470F512H |
| 15 | pic32mz_da_curiosity | [PIC32MZ DA Curiosity Development Kit](https://www.microchip.com/Developmenttools/ProductDetails/EV87D54A) | PIC32MZ2064DAR176 |
| 16 | pic32mz_da_sk | [PIC32MZ Embedded Graphics with Stacked DRAM (DA) Starter Kit (Crypto)](https://www.microchip.com/developmenttools/ProductDetails/DM320010-C) | PIC32MZ2064DAS169 |
| 17 | pic32mz_da_sk | [PIC32MZ Embedded Graphics with External DRAM (DA) Starter Kit](https://www.microchip.com/developmenttools/ProductDetails/DM320008) | PIC32MZ2064DAA288 |
| 18 | pic32mz_da_sk | [PIC32MZ Embedded Graphics with Stacked DRAM (DA) Starter Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/DM320010) | PIC32MZ2064DAG169 |
| 19 | pic32mz_ef_curiosity_v2 | [Curiosity PIC32MZ EF 2.0 Development Board](https://www.microchip.com/developmenttools/ProductDetails/DM320209) | PIC32MZ2048EFM144 |
| 20 | pic32mz_ef_sk | [PIC32MZ Embedded Connectivity with FPU (EF) Starter Kit](https://www.microchip.com/Developmenttools/ProductDetails/DM320007) | PIC32MZ2048EFH144 |
| 21 | pic32mz_w1_curiosity | [PIC32 WFI32E CURIOSITY BOARD](https://www.microchip.com/en-us/development-tool/EV12F11A) | PIC32MZ1025W104 |
| 22 | sam_9x60_ek | [SAM9X60-EK Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/DT100126) | SAM9X60 |
| 23 | sam_a5d2_xult | [ATSAMA5D2C-XULT ](https://www.microchip.com/DevelopmentTools/ProductDetails/ATSAMA5D2C-XULT)| SAMA5D27C |
| 24 | sam_a5d27_som1_ek | [SAMA5D27-SOM1-EK1](https://www.microchip.com/developmenttools/ProductDetails/atsama5d27-som1-ek1) | SAMA5D27C |
| 25 | sam_a5d27_wlsom1_ek1 | [ATSAMA5D27-WLSOM1 EVALUATION KIT](https://www.microchip.com/en-us/development-tool/DM320117) | SAMA5D27C |
| 26 | sam_c21_xpro | [SAM C21 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsamc21-xpro) | ATSAMC21J18A |
| 27 | sam_c21n_xpro | [SAMC21N Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/ATSAMC21N-XPRO) | ATSAMC21N18A |
| 28 | sam_d10_xmini | [SAM D10 Xplained Mini](https://www.microchip.com/developmenttools/ProductDetails/ATSAMD10-Xmini) | ATSAMD10D14A |
| 29 | sam_d11_xpro | [SAM D11 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsamd11-xpro) | ATSAMD11D14A |
| 30 | sam_d20_xpro | [SAM D20 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/ATSAMD20-XPRO) | SAMD20J18A |
| 31 | sam_d21_cnano | [SAM D21 Curiosity Nano Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/DM320119) | ATSAMD21G17D |
| 32 | sam_d21_iot | [SAM-IoT WG Development Board](https://www.microchip.com/Developmenttools/ProductDetails/EV75S95A) | ATSAMD21G18A |
| 33 | sam_d21_xpro | [SAM D21 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsamd21-xpro) | SAMD21J18A |
| 34 | sam_da1_xpro | [SAM DA1 Xplained Pro](https://www.microchip.com/developmenttools/ProductDetails/ATSAMDA1-XPRO) | SAMDA1J16A |
| 35 | sam_e51_cnano | [SAM E51 Curiosity Nano Evaluation Kit](https://www.microchip.com/Developmenttools/ProductDetails/EV76S68A) | ATSAME51J20A |
| 36 | sam_e54_cult | [SAM E54 Curiosity Ultra Development Board](https://www.microchip.com/Developmenttools/ProductDetails/DM320210) | ATSAME54P20A |
| 37 | sam_e54_xpro | [SAM E54 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/productdetails/atsame54-xpro) | ATSAME54P20A |
| 38 | sam_e70_xpld | [SAM E70 Xplained Evaluation Kit](https://www.microchip.com/Developmenttools/ProductDetails/ATSAME70-XPLD) | ATSAME70Q21 |
| 39 | sam_e70_xult | [SAM E70 Xplained Ultra Evaluation Kit](https://www.microchip.com/Developmenttools/ProductDetails/DM320113) | ATSAME70Q21 |
| 40 | sam_g55_xpro | [SAM G55 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsamg55-xpro) | ATSAMG55J19A |
| 41 | sam_ha1_xpro | [SAM HA1E16A Xplained Pro](https://www.microchip.com/Developmenttools/ProductDetails/ATSAMHA1E16A-XPRO) | ATSAMHA1E16A |
| 42 | sam_l10_xpro | [SAML10 Xplained Pro Evaluation Kit](https://www.microchip.com/Developmenttools/ProductDetails/DM320204) | ATSAML10E16A |
| 43 | sam_l11_xpro | [SAML11 Xplained Pro Evaluation Kit](https://www.microchip.com/Developmenttools/ProductDetails/DM320205) | ATSAML11E16A |
| 44 | sam_l21_xpro | [SAM L21 Xplained Pro Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsaml21-xpro-b) | SAML21J18A |
| 45 | sam_l22_xpro | [SAM L22 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/atsaml22-xpro-b) | SAML22N18A |
| 46 | sam_r34_xpro | [SAMR34 Xplained Pro Evaluation Kit](https://www.microchip.com/DevelopmentTools/ProductDetails/dm320111) | SAMR34J18B |
| 47 | sam_rh71_ek | [SAMRH71F20-EK Evaluation Kit](https://ww1.microchip.com/downloads/en/DeviceDoc/SAMRH71F20-EK-Evaluation-Kit-User-Guide-DS50002910A.pdf) | SAMRH71F20 |
| 48 | sam_v71_xult | [SAM V71 Xplained Ultra Evaluation Kit](https://www.microchip.com/developmenttools/ProductDetails/atsamv71-xult) | ATSAMV71Q21B |
| 49 | wlr089_xpro | [WLR089 Xplained Pro Evaluation Kit](https://www.microchip.com/Developmenttools/ProductDetails/EV23M25A) | WLR089U0 |
| 50 | pl360g55cf_ek | [PL360G55CF Evaluation Board](https://www.microchip.com/en-us/development-tool/PL360G55CF-EK) | SAMG55J19 |
| 51 | pl485_ek | [PL485 Evaluation Kit](https://www.microchip.com/en-us/development-tool/PL485-EK) | PL485 SOC |
| 52 | pl360g55cb_ek | [PL360G55CB Evaluation Board](https://www.microchip.com/en-us/development-tool/PL360G55CB-EK) | SAMG55J19 |
| 53 | sam_r34_xpro | [SAMR34 Xplained Pro Evaluation Kit](https://www.microchip.com/en-us/development-tool/dm320111) | SAM R34 SiP |
| 54 | lan9255_evb | [LAN9255 Evaluation Board](https://www.microchip.com/en-us/development-tool/EV25Y25A) | LAN9255ZMX020 |
| 55 | pic32mk_mcf_pim_mc | [PIC32MK1024 Motor Control Plug In Module](https://www.microchip.com/en-us/development-tool/MA320024) | PIC32MK1024MCF100 |
| 56 | sam_e54_pim_mc | [ATSAME54 Motor Control Plug In Module](https://www.microchip.com/en-us/development-tool/MA320207) | ATSAME54P20A |
| 57 | sam_e70_pim_mc | [ATSAME70 Motor Control Plug In Module](https://www.microchip.com/en-us/development-tool/MA320203) | ATSAME70Q21B |
| 58 | pic32mk_mcm_pim_mc | [PIC32MK MCM Motor Control Plug In Module](https://www.microchip.com/en-us/development-tool/MA320211) | PIC32MK1024MCM100 |

____

[![License](https://img.shields.io/badge/license-Harmony%20license-orange.svg)](https://github.com/Microchip-MPLAB-Harmony/bsp/blob/master/mplab_harmony_license.md)
[![Latest release](https://img.shields.io/github/release/Microchip-MPLAB-Harmony/bsp.svg)](https://github.com/Microchip-MPLAB-Harmony/bsp/releases/latest)
[![Latest release date](https://img.shields.io/github/release-date/Microchip-MPLAB-Harmony/bsp.svg)](https://github.com/Microchip-MPLAB-Harmony/bsp/releases/latest)
[![Commit activity](https://img.shields.io/github/commit-activity/y/Microchip-MPLAB-Harmony/bsp.svg)](https://github.com/Microchip-MPLAB-Harmony/bsp/graphs/commit-activity)
[![Contributors](https://img.shields.io/github/contributors-anon/Microchip-MPLAB-Harmony/bsp.svg)]()

____

[![Follow us on Youtube](https://img.shields.io/badge/Youtube-Follow%20us%20on%20Youtube-red.svg)](https://www.youtube.com/user/MicrochipTechnology)
[![Follow us on LinkedIn](https://img.shields.io/badge/LinkedIn-Follow%20us%20on%20LinkedIn-blue.svg)](https://www.linkedin.com/company/microchip-technology)
[![Follow us on Facebook](https://img.shields.io/badge/Facebook-Follow%20us%20on%20Facebook-blue.svg)](https://www.facebook.com/microchiptechnology/)
[![Follow us on Twitter](https://img.shields.io/twitter/follow/MicrochipTech.svg?style=social)](https://twitter.com/MicrochipTech)

[![](https://img.shields.io/github/stars/Microchip-MPLAB-Harmony/bsp.svg?style=social)]()
[![](https://img.shields.io/github/watchers/Microchip-MPLAB-Harmony/bsp.svg?style=social)]()


