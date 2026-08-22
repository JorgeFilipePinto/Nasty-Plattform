#pragma once

#include "ISensor.h"


class TempSensor: public ISensor
{
    public:
        void init(int pin, int updateInterval = 60) override;
        bool start() override;
        bool read(SensorData&) override;
        ~TempSensor() override = default;

    private:
        int _pin;
        int _updateInterval; // Update interval in seconds, 60 by default
};