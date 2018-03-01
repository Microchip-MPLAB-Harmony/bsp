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

/* SST26 Transfer Status
 Summary:
    Defines the data type for the sst26 peripheral transfer status.

 Description:
    This will be used to indicate the current transfer status of the
    sst26 peripheral.

 Remarks:
    None.
*/

typedef enum
{
    /* Transfer is being processed */
    SST26_TRANSFER_BUSY,
    /* Transfer is successfully completed*/
    SST26_TRANSFER_COMPLETED,
    /* Transfer had error*/
    SST26_TRANSFER_ERROR_UNKNOWN,
} SST26_TRANSFER_STATUS;

/* SST26 Geometry data
 Summary:
    Defines the data type for the SST26 Geometry details.

 Description:
    This will be used to get the geometry details of the
    attached SST26 flash device.

 Remarks:
    None.
*/

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

// *****************************************************************************
/* Function:
    void SST26_Initialize( void );
    
  Summary:
    Initializes the SST26 Flash device

  Description:
    This routine initializes the SST26 device making it ready for clients to use.
    - Resets the Flash Device
    - Puts it on QUAD IO Mode

  Precondition:
    None.
  
  Parameters:
    None
  
  Returns:
    None
  
  Example:
    <code>
    // This code snippet shows an example of initializing the SST26 peripheral.

    if (true != SST26_Initialize())
    {
        // Handle Error
    }

    </code>

  Remarks:
    This routine must be called before any other SST26 routine is called.
    
    This routine should only be called once during system initialization.
    
    This routine will block for hardware access.
    
*/

void SST26_Initialize( void );

// *****************************************************************************
/* Function:
    bool SST26_UnlockFlash(void);

  Summary:
    Unlocks the flash device for Erase and Program operations.

  Description:
    This function schedules a blocking operation for unlocking the flash blocks
    globally. This allows to perform erase and program operations on the flash.

    The request is sent in QUAD_MODE to flash device.

  Precondition:
    None

  Parameters:
    None

  Returns:
    false
    - if Write enable fails before sending unlock command to flash
    - if Unlock flash command itself fails
    - if the driver is busy handling another transfer request

    true
    - if the unlock is successfully completed

  Example:
    <code>

    if(true != SST26_UnlockFlash())
    {
        // Error handling here
    }

    </code>

  Remarks:
    This routine will block wait for transfer to complete.
*/

bool SST26_UnlockFlash( void );

// *****************************************************************************
/* Function:
    bool SST26_ReadJedecId(uint32_t *jedec_id);

  Summary:
    Reads JEDEC-ID of the flash device.

  Description:
    This function schedules a blocking operation for reading the JEDEC-ID.
    This information can be used to get the flash device geometry.

    The request is sent in QUAD_MODE to flash device.

  Precondition:
    None

  Parameters:
    None

  Returns:
    false
    - if read jedec-id command fails
    - if the driver is busy handling another transfer request

    true
    - if the read is successfully completed

  Example:
    <code>

    uint32_t jedec_id = 0;

    if(true != SST26_ReadJedecId(&jedec_id))
    {
        // Error handling here
    }

    </code>

  Remarks:
    This routine will block wait for transfer to complete.
*/

bool SST26_ReadJedecId( uint32_t *jedec_id );

// **************************************************************************
/* Function:
    bool SST26_SectorErase(uint32_t address);
    
  Summary:
    Erase the sector from the specified block start address.
  
  Description:
    This function schedules a non-blocking sector erase operation of flash memory.
    Each Sector is of 4 KByte.

    The requesting client should call SST26_TransferStatusGet() API to know
    the current status of the request.

    The request is sent in QUAD_MODE to flash device.
  
  Preconditions:
    SST26_UnlockFlash() has to be called before calling SST26_SectorErase()
  
  Parameters:
    address       - block start address from where a sector needs to be erased.
  
  Returns:
    false
    - if Write enable fails before sending sector erase command to flash
    - if sector erase command itself fails
    - if the driver is busy handling another transfer request

    true
    - if the erase request is successfully sent to the flash
  
  Example:
    <code>
    uint32_t sectorStart = 0;

    SST26_UnlockFlash();

    if(false == SST26_SectorErase(sectorStart))
    {
        // Error handling here
    }

    // Wait for erase to be completed
    while(FLASH_DEVICE_TRANSFER_BUSY == SST26_TransferStatusGet());
    
    </code>

  Remarks:
    This routine will block wait until erase request is submitted successfully.
    Client should wait until erase is complete to send next transfer request.
*/

bool SST26_SectorErase( uint32_t address );

// **************************************************************************
/* Function:
    bool SST26_BulkErase(uint32_t address);
    
  Summary:
    Erase a block from the specified block start address.
  
  Description:
    This function schedules a non-blocking block erase operation of flash memory.
    The block size can be 8 KByte, 32KByte or 64 KByte.

    The requesting client should call SST26_TransferStatusGet() API to know
    the current status of the request.

    The request is sent in QUAD_MODE to flash device.
  
  Preconditions:
    SST26_UnlockFlash() has to be called before calling SST26_BlockErase()

  Parameters:
    address       - block start address to be erased.

  Returns:
    false
    - if Write enable fails before sending sector erase command to flash
    - if block erase command itself fails
    - if the driver is busy handling another transfer request

    true
    - if the erase request is successfully sent to the flash

  Example:
    <code>
    uint32_t blockStart = 0;

    SST26_UnlockFlash();

    if(false == SST26_SectorErase(blockStart))
    {
        // Error handling here
    }

    // Wait for erase to be completed
    while(FLASH_DEVICE_TRANSFER_BUSY == SST26_TransferStatusGet());

    </code>

  Remarks:
    This routine will block wait until erase request is submitted successfully.
    Client should wait until erase is complete to send next transfer request.
*/

bool SST26_BulkErase( uint32_t address );

// **************************************************************************
/* Function:
    bool SST26_ChipErase();

  Summary:
    Erase entire flash memory.

  Description:
    This function schedules a non-blocking chip erase operation of flash memory.

    The requesting client should call SST26_TransferStatusGet() API to know
    the current status of the request.

    The request is sent in QUAD_MODE to flash device.
  
  Preconditions:
    SST26_UnlockFlash() has to be called before calling SST26_ChipErase()

  Parameters:
    None

  Returns:
    false
    - if Write enable fails before sending sector erase command to flash
    - if chip erase command itself fails
    - if the driver is busy handling another transfer request

    true
    - if the erase request is successfully sent to the flash

  Example:
    <code>

    SST26_UnlockFlash();

    if(false == SST26_ChipErase())
    {
        // Error handling here
    }

    // Wait for erase to be completed
    while(FLASH_DEVICE_TRANSFER_BUSY == SST26_TransferStatusGet());

    </code>

  Remarks:
    This routine will block wait until erase request is submitted successfully.
    Client should wait until erase is complete to send next transfer request.
*/

bool SST26_ChipErase( void );

// *****************************************************************************
/* Function:
    bool SST26_Read( uint32_t *rx_data, uint32_t rx_data_length, uint32_t address );

  Summary:
    Reads n bytes of data from the specified start address of flash memory.

  Description:
    This function schedules a blocking operation for reading requested
    number of data bytes from the flash memory.

    The request is sent in QUAD_MODE to flash device.

  Precondition:
    None

  Parameters:
    *rx_data        - Buffer pointer into which the data read from the SST26
                      Flash memory will be placed.

    rx_data_length  - Total number of bytes to be read.

    address         - Read memory start address from where the data should be
                      read.

  Returns:
    false
    - if read command itself fails
    - if the driver is busy handling another transfer request

    true
    - if number of bytes requested are read from flash memory

  Example:
    <code>

    #define BUFFER_SIZE  1024
    #define MEM_ADDRESS  0x0

    uint8_t readBuffer[BUFFER_SIZE];
    
    if (true != SST26_ReadMemory((uint32_t *)&readBuffer, BUFFER_SIZE, MEM_ADDRESS))
    {
        // Error handling here
    }

    </code>

  Remarks:
    This routine will block waiting until read request is completed successfully.
*/

bool SST26_Read( uint32_t *rx_data, uint32_t rx_data_length, uint32_t address );

// *****************************************************************************
/* Function:
    bool SST26_PageWrite( uint32_t *tx_data, uint32_t tx_data_length, uint32_t address );

  Summary:
    Writes one page of data starting at the specified address.

  Description:
    This function schedules a non-blocking write operation for writing one page
    of data into flash memory. 

    The requesting client should call SST26_TransferStatusGet() API to know
    the current status of the request.

    The request is sent in QUAD_MODE to flash device.

  Preconditions:
    SST26_UnlockFlash() has to be called before calling SST26_WriteMemory()

    The flash address location which has to be written, must have been erased
    before using the SST26_xxxErase() routine.

    The flash address has to be a Page aligned address.

  Parameters:
    *tx_data        - The source buffer containing data to be programmed into SST26 
                      Flash

    tx_data_length  - Total number of bytes to be written. should not be greater
                      than page size

    address         - Write memory start address from where the data should be
                      written

  Returns:
    false
    - if Write enable fails before sending sector erase command to flash
    - if write command itself fails
    - if the driver is busy handling another transfer request

    true
    - if the write request is successfully sent to the flash

  Example:
    <code>

    #define PAGE_SIZE    256
    #define BUFFER_SIZE  1024
    #define MEM_ADDRESS  0x0

    uint8_t writeBuffer[BUFFER_SIZE];
    bool status = false;

    SST26_UnlockFlash();

    if(false == SST26_ChipErase())
    {
        // Error handling here
    }

    // Wait for erase to be completed
    while(FLASH_DEVICE_TRANSFER_BUSY == SST26_TransferStatusGet());
 
    for (uint32_t j = 0; j < BUFFER_SIZE; j += PAGE_SIZE)
    {
        if (true != SST26_PageWrite((uint32_t *)&writeBuffer[j], (MEM_ADDRESS + j)))
        {
            status = false;
            break;
        }

        // Wait for write to be completed
        while(FLASH_DEVICE_TRANSFER_BUSY == SST26_TransferStatusGet());
        status = true;
    }

    if(status == false)
    {
        // Error handling here
    }

    </code>

  Remarks:
    This routine will block wait until erase request is submitted successfully.
    Client should wait until write is complete to send next transfer request.
*/

bool SST26_PageWrite( uint32_t *tx_data, uint32_t address );

// *****************************************************************************
/* Function:
    SST26_TRANSFER_STATUS SST26_TransferStatusGet(void);

  Summary:
    Gets the current status of the transfer request.

  Description:
    This routine gets the current status of the transfer request. The application
    must use this routine where the status of a scheduled request needs to be
    polled on.

  Preconditions:
    None

  Parameters:
    None

  Returns:
    SST26_TRANSFER_ERROR_UNKNOWN
    - If the flash status register read request fails
 
    SST26_TRANSFER_BUSY
    - If the current transfer request is still being processed

    SST26_TRANSFER_COMPLETED
    - If the transfer request is completed
 
  Example:
    <code>
    if (SST26_TRANSFER_COMPLETED == SST26_TransferStatusGet())
    {
        // Operation Done
    }
    </code>

  Remarks:
    This routine will block for hardware access.
*/

SST26_TRANSFER_STATUS SST26_TransferStatusGet(void);

// *****************************************************************************
/* Function:
    bool SST26_GeometryGet(SST26_GEOMETRY *geometry);

  Summary:
    Returns the geometry of the device.

  Description:
    This API gives the following geometrical details of the SST26 Flash:
    - Number of Read/Write/Erase Blocks and their size in each region of the device

  Precondition:
    The SST26_Initialize() routine must have been called for the
    specified SST26 driver instance.

  Parameters:
    *geometry_table   - pointer to flash device geometry table instance

  Returns:
    false
    - if read device id fails
    - if the driver is busy handling another transfer request

    true
    - if able to get the geometry details of the flash

  Example:
    <code> 
    
    SST26_GEOMETRY sst26FlashGeometry;
    uint32_t readBlockSize, writeBlockSize, eraseBlockSize;
    uint32_t nReadBlocks, nReadRegions, totalFlashSize;

    SST26_GeometryGet(&sst26FlashGeometry);

    readBlockSize  = sst26FlashGeometry.read_blockSize;
    nReadBlocks = sst26FlashGeometry.read_numBlocks;
    nReadRegions = sst26FlashGeometry.numReadRegions;

    writeBlockSize  = sst26FlashGeometry.write_blockSize;
    eraseBlockSize  = sst26FlashGeometry.erase_blockSize;

    totalFlashSize = readBlockSize * nReadBlocks * nReadRegions;

    </code>

  Remarks:
    None.
*/

bool SST26_GeometryGet(SST26_GEOMETRY *geometry);

#ifdef __cplusplus
}
#endif

#endif // #ifndef _SST26_H
/*******************************************************************************
 End of File
*/