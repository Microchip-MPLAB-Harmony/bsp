# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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
class mcFun_AdvancedComboSymbol:
    def __init__(self, description, Id, component ):
        self.description = description
        self.component = component
        self.Id = Id

    def createComboSymbol( self, dependency, root, data ):
        self.data = data
        self.depend_Symbol_ID = dependency.getID()
        self.depend_Symbol_Val = dependency.getValue()
        self.symbol = {}
        for key in self.data.keys():
            name = self.depend_Symbol_ID + "_" + self.Id + "_" + str( key )       
            self.symbol[key] = self.component.createComboSymbol(name, root, self.data[key] )
            self.symbol[key].setLabel(self.description)
            self.symbol[key].setDependencies( self.showComboSymbol, [self.depend_Symbol_ID])
            if( self.depend_Symbol_Val == str( key ) ):
                self.symbol[key].setVisible(True)
            else:
                self.symbol[key].setVisible(False)

    def setDefaultValue( self, value ):
        pass

    def setReadOnly(self, value ):
        pass

    def setComboSymbolValue( self, value ):
        instance = self.depend_Symbol_Val
        for key in self.data.keys():
            if( key == instance ):
                self.symbol[key].setValue(value )

    def setComboSymbolValue( self ):
        instance = self.depend_Symbol_Val
        for key in self.data.keys():
            if( key == instance ):
                return self.symbol[key].getValue( )

    def showComboSymbol( self, symbol, event ):
        symbol_Id = symbol.getID()  
        if( event["symbol"].getValue() in symbol_Id ):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
