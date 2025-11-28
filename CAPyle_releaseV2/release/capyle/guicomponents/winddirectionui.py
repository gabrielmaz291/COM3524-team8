import tkinter as tk
from capyle.guicomponents import _ConfigUIComponent
from capyle.utils import is_valid_integer


class _WindDirectionUI(tk.Frame, _ConfigUIComponent):
    DEFAULT = ''

    def __init__(self, parent):
        """Create and populate the wind directions ui"""
        tk.Frame.__init__(self, parent)
        _ConfigUIComponent.__init__(self)
        wind_label = tk.Label(self, text="Wind direction:")
        wind_label.pack(side=tk.LEFT)
        is_valid_int = (self.register(is_valid_integer), '%P')
        self.wind_entry = tk.Entry(self, validate='key',
                                  validatecommand=is_valid_int, width=4)
        self.set_default()
        self.wind_entry.pack(side=tk.LEFT)

    #Allow values as integers (to add wind directional bias) or None (no wind)
    def get_value(self):
        x = self.wind_entry.get()
        if x == '':
            return None

        try:
            return int(x)
        except (ValueError, TypeError):
            return None

    def set_default(self):
        self.wind_entry.delete(0, tk.END)

    def set(self, value):
        super(_WindDirectionUI, self).set(entry=self.wind_entry, value=value)
