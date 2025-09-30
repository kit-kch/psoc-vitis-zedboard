/******************************************************************************
* Copyright (C) 2023 Advanced Micro Devices, Inc. All Rights Reserved.
* SPDX-License-Identifier: MIT
******************************************************************************/
/*
 * helloworld.c: simple test application
 *
 * This application configures UART 16550 to baud rate 9600.
 * PS7 UART (Zynq) is not initialized by this application, since
 * bootrom/bsp configures it to baud rate 115200
 *
 * ------------------------------------------------
 * | UART TYPE   BAUD RATE                        |
 * ------------------------------------------------
 *   uartns550   9600
 *   uartlite    Configurable only in HW design
 *   ps7_uart    115200 (configured by bootrom/bsp)
 */

#include <stdio.h>
#include "platform.h"
#include "xil_printf.h"
#include "xgpiops.h"
#include "sleep.h"

XGpioPs leds;
int main()
{
    init_platform();

    print("Hello World\n\r");

    XGpioPs_Config *GPIOConfigPtr = XGpioPs_LookupConfig(XPAR_XGPIOPS_0_BASEADDR);
    XGpioPs_CfgInitialize(&leds, GPIOConfigPtr, GPIOConfigPtr->BaseAddr);
    XGpioPs_SetOutputEnablePin(&leds, 7, 0b1);
    XGpioPs_SetDirectionPin(&leds, 7, 0b1);
    XGpioPs_IntrDisablePin(&leds, 7);

    while (1)
    {
        XGpioPs_WritePin(&leds, 7, 0b1);
        sleep(1);
        XGpioPs_WritePin(&leds, 7, 0b0);
        sleep(1);
    }

    print("Successfully ran Hello World application");
    cleanup_platform();
    return 0;
}
