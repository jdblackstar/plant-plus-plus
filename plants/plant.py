class Plant:
    """
    Class representing a plant with specific light and care requirements.
    """

    def __init__(self, lux_hours, max_sunlight_length, rest_time):
        """
        Initialize the plant with the given parameters.

        Args:
            foot_candle_hours (int): Required foot-candle hours per day.
            max_sunlight_length (int): Maximum number of sunlight hours per day.
            rest_time (int): Rest time in hours when no light should be provided.
        """
        self.lux_hours = lux_hours
        self.max_sunlight_length = max_sunlight_length
        self.rest_time = rest_time

    def needs_light(self, accumulated_lux):
        """
        Determine if the plant needs additional light based on the accumulated foot-candle hours.

        Args:
            accumulated_foot_candles (int): Accumulated foot-candle hours for the day.

        Returns:
            bool: True if the plant needs additional light, False otherwise.
        """
        return accumulated_lux < self.lux_hours
