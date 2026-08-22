/*
 * DISensor.h
 *
 *  Created on: Aug 22, 2026
 *      Author: jorgepinto
 */

 #pragma once
 #include <string>
 #include <stdio.h>
#include <iostream>

struct SensorData
{
    float value;
    std::string description;

};


class ISensor 
{
    public:
        virtual void init(int pin, int updateInterval = 60) = 0;
        virtual bool start() = 0;
        virtual bool read(SensorData& data) = 0;
        virtual ~ISensor() = default;
};