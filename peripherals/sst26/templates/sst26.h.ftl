/*******************************************************************************
  SST26 Driver Interface Definition

  Company:
    Microchip Technology Inc.

  File Name:
    sst26.h

  Summary:
    SST26 Driver Interface Definition

  Description:
    The SST26 driver provides a simple interface to manage the SST26VF series
    of SQI Flash Memory connected to Microchip microcontrollers. This file
    defines the interface definition for the SST26 driver.
*******************************************************************************/

//DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2016 - 2017 released Microchip Technology Inc. All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
//DOM-IGNORE-END

#ifndef _SST26_H
#define _SST26_H

// *****************************************************************************
// *****************************************************************************
// Section: File includes
// *****************************************************************************
// *****************************************************************************

#include <stdio.h>
#include <stdbool.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    extern "C" {
#endif

// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

typedef enum
{
    /* Transfer is being processed */
    SST26_TRANSFER_BUSY,
    /* Transfer is successfully completed*/
    SST26_TRANSFER_COMPLETED,
    /* Transfer had error*/
    SST26_TRANSFER_ERROR_UNKNOWN,
} SST26_TRANSFER_STATUS;

typedef struct
{
    uint32_t read_blockSize;
    uint32_t read_numBlocks;
    uint32_t numReadRegions;

    uint32_t write_blockSize;
    uint32_t write_numBlocks;
    uint32_t numWriteRegions;

    uint32_t erase_blockSize;
    uint32_t erase_numBlocks;
    uint32_t numEraseRegions;
} SST26_GEOMETRY;

// *****************************************************************************
// *****************************************************************************
// Section: SST26 Driver Module Interface Routines
// *****************************************************************************
// *****************************************************************************

bool SST26_ResetFlash(void);

bool SST26_EnableQuadIO(void);

bool SST26_UnlockFlash(void);

bool SST26_ReadJedecId(uint32_t *jedec_id);

bool SST26_SectorErase(uint32_t address);

bool SST26_BulkErase(uint32_t address);

bool SST26_ChipErase(void);

bool SST26_Read( uint32_t *rx_data, uint32_t rx_data_length, uint32_t address );

bool SST26_PageWrite( uint32_t *tx_data, uint32_t address );

SST26_TRANSFER_STATUS SST26_TransferStatusGet(void);

bool SST26_GeometryGet(SST26_GEOMETRY *geometry);


#ifdef __cplusplus
}
#endif

#endif // #ifndef _SST26_H
/*******************************************************************************
 End of File
*/