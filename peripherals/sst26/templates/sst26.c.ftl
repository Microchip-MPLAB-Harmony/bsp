/******************************************************************************
  SST26 Library Interface Implementation

  Company:
    Microchip Technology Inc.

  File Name:
    sst26.c

  Summary:
    SST26 Library Interface Definition

  Description:
    The SST26 Library provides a interface to access the SST26 peripheral on the PIC32
    microcontroller. This file implements the SST26 Library interface. This file
    should be included in the project if SST26 library functionality is needed.
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

// *****************************************************************************
// *****************************************************************************
// Section: Include Files
// *****************************************************************************
// *****************************************************************************

#include <string.h>
#include "external_peripheral/sst26/sst26.h"
#include "peripheral/qspi/plib_${SST26_PLIB?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global objects
// *****************************************************************************
// *****************************************************************************

#define SST26_PAGE_SIZE   256

// *****************************************************************************
/* SST26 Command set

  Summary:
    Enumeration listing the SST26VF commands.

  Description:
    This enumeration defines the commands used to interact with the SST26VF
    series of devices.

  Remarks:
    None
*/

typedef enum
{
    /* Reset enable command. */
    SST26_CMD_FLASH_RESET_ENABLE = 0x66,

    /* Command to reset the flash. */
    SST26_CMD_FLASH_RESET        = 0x99,

    /* Command to Enable QUAD IO */
    SST26_CMD_ENABLE_QUAD_IO     = 0x38,

    /* Command to Reset QUAD IO */
    SST26_CMD_RESET_QUAD_IO      = 0xFF,

    /* Command to read JEDEC-ID of the flash device. */
    SST26_CMD_JEDEC_ID_READ      = 0x9F,

    /* QUAD Command to read JEDEC-ID of the flash device. */
    SST26_CMD_QUAD_JEDEC_ID_READ = 0xAF,
    
    /* Command to perform High Speed Read */
    SST26_CMD_HIGH_SPEED_READ    = 0x0B,

    /* Write enable command. */
    SST26_CMD_WRITE_ENABLE       = 0x06,

    /* Page Program command. */
    SST26_CMD_PAGE_PROGRAM       = 0x02,

    /* Command to read the Flash status register. */
    SST26_CMD_READ_STATUS_REG    = 0x05,

    /* Command to perform sector erase */
    SST26_CMD_SECTOR_ERASE       = 0x20,

    /* Command to perform Bulk erase */
    SST26_CMD_BULK_ERASE_64K     = 0xD8,

    /* Command to perform Bulk erase */
    SST26_CMD_CHIP_ERASE         = 0xD8,

    /* Command to unlock the flash device. */
    SST26_CMD_UNPROTECT_GLOBAL   = 0x98

} SST26_CMD;

static qspi_command_xfer_t qspi_command_xfer = { 0 };
static qspi_register_xfer_t qspi_register_xfer = { 0 };
static qspi_memory_xfer_t qspi_memory_xfer = { 0 };

/* Table mapping the Flash ID's to their sizes. */
static uint32_t gSstFlashIdSizeTable [5][2] = {
    {0x01, 0x200000}, /* 16 MBit */
    {0x41, 0x200000}, /* 16 MBit */
    {0x02, 0x400000}, /* 32 MBit */
    {0x42, 0x400000}, /* 32 MBit */
    {0x43, 0x800000}  /* 64 MBit */
};

// *****************************************************************************
// *****************************************************************************
// Section: SST26 Driver Local Functions
// *****************************************************************************
// *****************************************************************************

/* This function returns the flash size in bytes for the specified deviceId. A
 * zero is returned if the device id is not supported. */
static uint32_t SST26_GetFlashSize( uint8_t deviceId )
{
    uint8_t i = 0;

    for (i = 0; i < 5; i++)
    {
        if (deviceId == gSstFlashIdSizeTable[i][0])
        {
            return gSstFlashIdSizeTable[i][1];
        }
    }

    return 0;
}

bool SST26_ResetFlash(void)
{
    bool status = false;

    memset((void *)&qspi_command_xfer, 0, sizeof(qspi_command_xfer_t));

    qspi_command_xfer.instruction = SST26_CMD_FLASH_RESET_ENABLE;
    qspi_command_xfer.width = SINGLE_BIT_SPI;

    if (false == ${SST26_PLIB}_CommandWrite(&qspi_command_xfer, 0))
    {
        return status;
    }

    qspi_command_xfer.instruction = SST26_CMD_FLASH_RESET;
    qspi_command_xfer.width = SINGLE_BIT_SPI;

    status  = ${SST26_PLIB}_CommandWrite(&qspi_command_xfer, 0);

    return status;
}

bool SST26_EnableQuadIO(void)
{
    bool status = false;

    memset((void *)&qspi_command_xfer, 0, sizeof(qspi_command_xfer_t));

    qspi_command_xfer.instruction = SST26_CMD_ENABLE_QUAD_IO;
    qspi_command_xfer.width = SINGLE_BIT_SPI;

    status  = ${SST26_PLIB}_CommandWrite(&qspi_command_xfer, 0);

    return status;
}

static bool SST26_WriteEnable(void)
{
    bool status = false;

    memset((void *)&qspi_command_xfer, 0, sizeof(qspi_command_xfer_t));

    qspi_command_xfer.instruction = SST26_CMD_WRITE_ENABLE;
    qspi_command_xfer.width = QUAD_CMD;

    status  = ${SST26_PLIB}_CommandWrite(&qspi_command_xfer, 0);

    return status;
}

// *****************************************************************************
// *****************************************************************************
// Section: SST26 Driver Global Functions
// *****************************************************************************
// *****************************************************************************

bool SST26_UnlockFlash(void)
{
    bool status = false;

    if (false == SST26_WriteEnable())
    {
        return status;
    }

    memset((void *)&qspi_command_xfer, 0, sizeof(qspi_command_xfer_t));

    qspi_command_xfer.instruction = SST26_CMD_UNPROTECT_GLOBAL;
    qspi_command_xfer.width = QUAD_CMD;

    status  = ${SST26_PLIB}_CommandWrite(&qspi_command_xfer, 0);

    return status;
}

bool SST26_ReadJedecId(uint32_t *jedec_id)
{
    bool status = false;

    memset((void *)&qspi_register_xfer, 0, sizeof(qspi_register_xfer_t));

    qspi_register_xfer.instruction = SST26_CMD_QUAD_JEDEC_ID_READ;
    qspi_register_xfer.width = QUAD_CMD;
    qspi_register_xfer.dummy_cycles = 2;

    status  = ${SST26_PLIB}_RegisterRead(&qspi_register_xfer, jedec_id, 3);

    return status;
}

bool SST26_ReadStatus( uint32_t *rx_data, uint32_t rx_data_length )
{
    bool status = false;

    memset((void *)&qspi_register_xfer, 0, sizeof(qspi_register_xfer_t));

    qspi_register_xfer.instruction = SST26_CMD_READ_STATUS_REG;
    qspi_register_xfer.width = QUAD_CMD;
    qspi_register_xfer.dummy_cycles = 2;

    status  = ${SST26_PLIB}_RegisterRead(&qspi_register_xfer, rx_data, rx_data_length);

    return status;
}

SST26_TRANSFER_STATUS SST26_TransferStatusGet(void)
{
    SST26_TRANSFER_STATUS status = SST26_TRANSFER_ERROR_UNKNOWN;

    uint8_t reg_status = 0;
    
    if (false == SST26_ReadStatus((uint32_t *)&reg_status, 1))
    {
        return status;
    }

    if(reg_status & (1<<0))
        status = SST26_TRANSFER_BUSY;
    else
        status = SST26_TRANSFER_COMPLETED;

    return status;
}

bool SST26_Read( uint32_t *rx_data, uint32_t rx_data_length, uint32_t address )
{
    bool status = false;

    memset((void *)&qspi_memory_xfer, 0, sizeof(qspi_memory_xfer_t));

    qspi_memory_xfer.instruction = SST26_CMD_HIGH_SPEED_READ;
    qspi_memory_xfer.width = QUAD_CMD;
    qspi_memory_xfer.dummy_cycles = 6;

    status = ${SST26_PLIB}_MemoryRead(&qspi_memory_xfer, rx_data, rx_data_length, address);

    return status;
}

bool SST26_PageWrite( uint32_t *tx_data, uint32_t address )
{
    bool status = false;

    if (false == SST26_WriteEnable())
    {
        return status;
    }

    memset((void *)&qspi_memory_xfer, 0, sizeof(qspi_memory_xfer_t));

    qspi_memory_xfer.instruction = SST26_CMD_PAGE_PROGRAM;
    qspi_memory_xfer.width = QUAD_CMD;

    status = ${SST26_PLIB}_MemoryWrite(&qspi_memory_xfer, tx_data, SST26_PAGE_SIZE, address);

    return status;
}

static bool SST26_Erase(uint8_t instruction, uint32_t address)
{
    bool status = false;

    if (false == SST26_WriteEnable())
    {
        return status;
    }

    qspi_command_xfer.instruction = instruction;
    qspi_command_xfer.width = QUAD_CMD;
    qspi_command_xfer.addr_en = 1;

    status = ${SST26_PLIB}_CommandWrite(&qspi_command_xfer, address);

    return status;
}

bool SST26_SectorErase(uint32_t address)
{
    return (SST26_Erase(SST26_CMD_SECTOR_ERASE, address));
}

bool SST26_BulkErase(uint32_t address)
{
    return (SST26_Erase(SST26_CMD_BULK_ERASE_64K, address));
}

bool SST26_ChipErase(void)
{
    return (SST26_Erase(SST26_CMD_CHIP_ERASE, 0));
}

bool SST26_GeometryGet(SST26_GEOMETRY *geometry)
{
    uint32_t flash_size = 0;
    uint8_t  jedec_id[3] = { 0 };

    if (false == SST26_ReadJedecId((uint32_t *)&jedec_id))
    {
        return false;
    }
    
    flash_size = SST26_GetFlashSize(jedec_id[2]);

    if (flash_size == 0)
    {
        return false;
    }

    /* Read block size and number of blocks */
    geometry->read_blockSize = 1;
    geometry->read_numBlocks = flash_size;

    /* Write block size and number of blocks */
    geometry->write_blockSize = 256;
    geometry->write_numBlocks = flash_size >> 8;

    /* Erase block size and number of blocks */
    geometry->erase_blockSize = 4096;
    geometry->erase_numBlocks = flash_size >> 12;
    
    geometry->numReadRegions = 1;
    geometry->numWriteRegions = 1;
    geometry->numEraseRegions = 1;

    return true;
}
