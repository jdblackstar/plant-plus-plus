from sensors.light import BH1750Sensor, TSL2561Sensor


def create_sensor(sensor_type):
    """
    Create a light sensor object based on the provided sensor type.

    Args:
        sensor_type (str): The type of sensor to create (e.g., "BH1750", "TSL2561").

    Returns:
        LightSensor: An object representing the specified light sensor.
    """
    sensor_classes = {
        "BH1750": BH1750Sensor,
        "TSL2561": TSL2561Sensor,
        # Add more sensors as needed
    }

    sensor_class = sensor_classes.get(sensor_type)

    if sensor_class is None:
        raise ValueError(f"Unknown sensor type: {sensor_type}")

    return sensor_class()
