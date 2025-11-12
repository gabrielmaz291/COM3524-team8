import tkinter as tk
from capyle.guicomponents import _ConfigUIComponent
from capyle.utils import is_valid_integer


class _WindDirectionUI(tk.Frame, _ConfigUIComponent):
    DEFAULT = 0

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

    def get_value(self):
        x = self.wind_entry.get()
        if x == '':
            x = 0
        return int(x)

    def set_default(self):
        self.set(self.DEFAULT)

    def set(self, value):
        super(_WindDirectionUI, self).set(entry=self.wind_entry, value=value)
