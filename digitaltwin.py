import time

class LightBulb:
    def __init__(self, brand, wattage):
        self.brand = brand
        self.wattage = wattage
        self.is_on = False
        self.usage_seconds = 0
        self._last_on_time = None

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            self._last_on_time = time.time()
            print(f"{self.brand} bulb is now ON.")
        else:
            print("Bulb is already ON.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            elapsed = time.time() - self._last_on_time
            self.usage_seconds += elapsed
            print(f"{self.brand} bulb is now OFF. Used for {elapsed:.2f} seconds this session.")
        else:
            print("Bulb is already OFF.")
