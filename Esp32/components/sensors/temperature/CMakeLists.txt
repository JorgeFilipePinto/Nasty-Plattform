idf_component_register(
    SRCS
        "src/DHT_Sensor.cpp"
    INCLUDE_DIRS "include"
    REQUIRES
        driver          # para gpio_*, se implementares o DHT "à mão"
        esp_timer       # para esp_timer_get_time() em microssegundos
    PRIV_REQUIRES
        time_provider   # dependência interna, não exposta a quem usa "sensors"
)