#include "include/temp_sensor.h"

void TempSensor::init(int pin, int updateInterval = 60)
{
    _pin = pin;
    _updateInterval = updateInterval;
}

bool TempSensor::start()
{
    try
    {
        /* code */
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
        return false;
    }
    printf("Starting temperature sensor on pin %d\n", _pin);
    return true;
}

bool TempSensor::read(SensorData& data)
{
    try
    {
        /* code */
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
        return false;
    }
    data.value = 25.0; // Example temperature value
    data.description = "Temperature reading";
    return true;
}

TempSensor::~TempSensor() 
{
    // Cleanup code if necessary
}