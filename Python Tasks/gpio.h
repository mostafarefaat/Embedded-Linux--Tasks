/**********************************************************************************************
 *
 * Module: GPIO
 *
 * File Name: GPIO.h
 *
 * Description: Header file for the TM4C123GH6PM DIO driver for TivaC Built-in Buttons and LEDs
 *
 * Author: Edges for Training Team
 *
 ***********************************************************************************************/

#ifndef GPIO_H_
#define GPIO_H_

#include "std_types.h"

#define GPIO_PORTF_PRIORITY_MASK      0xFF1FFFFF
#define GPIO_PORTF_PRIORITY_BITS_POS  21
#define GPIO_PORTF_INTERRUPT_PRIORITY 5

#define PRESSED                ((uint8)0x00)
#define RELEASED               ((uint8)0x01)

extern uint32 x;
uint8 y;
const sint64 z;
uint32* m;

void GPIO_BuiltinButtonsLedsInit(void);

void GPIO_RedLedOn(void);
void GPIO_BlueLedOn(void);
void GPIO_GreenLedOn(void);

void GPIO_RedLedOff(void);
void GPIO_BlueLedOff(void);
void GPIO_GreenLedOff(void);

void GPIO_RedLedToggle(void);
void GPIO_BlueLedToggle(void);
void GPIO_GreenLedToggle(void);


/*------------------------------------*/
/*Extra Added Function*/
void GPIO_PORTF_Leds_Off(void);
void GPIO_PORTA_LedsInit(void);
void GPIO_PORTA_BlueLedOn(void);
void GPIO_PORTA_GreenLedOn(void);
void GPIO_PORTA_RedLedOn(void);
void GPIO_PORTA_BlueLedOff(void);
void GPIO_PORTA_GreenLedOff(void);
void GPIO_PORTA_BlueLedOff(void);
void GPIO_PORTA_Leds_Off(void);
/*------------------------------------*/


uint8 GPIO_SW1GetState(void);
uint8 GPIO_SW2GetState(void);

void GPIO_SW1EdgeTriggeredInterruptInit(void);
void GPIO_SW2EdgeTriggeredInterruptInit(void);


void GPTM_WTimer0Init(void);

uint32 GPTM_WTimer0Read(void);

extern void UART0_Init(void);

extern void UART0_SendByte(uint8 data);

extern uint8 UART0_ReceiveByte(void);

extern void UART0_SendString(const uint8 *pData, const uint8 *pData, const uint8 *pData);

extern void UART0_SendInteger(sint64 sNumber, const uint8 *pData, const uint8 *pData);

const uint32* Test_Function_1(void);

uint32* Test_Function_2(void);

void* Test_Function_3(void);

sint64* Test_Function_4(void);

boolean Test_Function_5(void);

float64* Test_Function_6(void);

float32 Test_Function_7(void);
#endif /* GPIO_H_ */
