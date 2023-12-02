import tkinter as tk
import config
from generating import generate_password, EmptyGeneratingRangeError


class MainFrame(tk.Frame):
    def __init__(self):
        super().__init__(background=config.MAIN_COLOR)
        self.grid_columnconfigure(0, minsize=250)
        self.grid_columnconfigure(1, minsize=220)

        self.length_label, self.length_entry = \
            self._set_entry_field(text='Введите длину пароля:', row=0)
        self.length_entry.insert(0, '10')
        self.grid_rowconfigure(0, pad=30)

        self.quantity_label, self.quantity_entry = \
            self._set_entry_field(text='Введите количество паролей:', row=1)
        self.quantity_entry.insert(0, '1')

        self.is_digit_enabled = tk.BooleanVar()
        self.digit_label, self.digit_check = self._set_option_field(text='Цифры:', row=2,
                                                                    var=self.is_digit_enabled)
        self.grid_rowconfigure(2, pad=30)

        self.is_chars_enabled = tk.BooleanVar()
        self.chars_label, self.chars_check = self._set_option_field(text='Буквы:', row=3,
                                                                    var=self.is_chars_enabled)
        self.chars_check.select()

        self.is_marks_enabled = tk.BooleanVar()
        self.marks_label, self.marks_check = self._set_option_field(text='Специальные символы: ',
                                                                    row=4, var=self.is_marks_enabled)
        self.grid_rowconfigure(4, pad=30)

    def _set_entry_field(self, *, text: str, row: int) -> tuple[tk.Label, tk.Entry]:
        label = tk.Label(self, text=text, font=config.FONT_STYLE, bg=config.MAIN_COLOR)
        label.grid(row=row, column=0)
        entry = tk.Entry(self, bg=config.FILL_COLOR, font=config.FONT_STYLE)
        entry.grid(row=row, column=1, sticky=tk.W)
        return label, entry

    def _set_option_field(self, *, text: str, row: int, var: tk.Variable) -> tuple[tk.Label, tk.Checkbutton]:
        label = tk.Label(self, text=text, font=config.FONT_STYLE, bg=config.MAIN_COLOR)
        label.grid(row=row, column=0)
        checkbox = tk.Checkbutton(self, bg=config.MAIN_COLOR, activebackground=config.FILL_COLOR,
                                  offvalue=False, onvalue=True, variable=var)
        checkbox.grid(row=row, column=1, sticky=tk.W)
        return label, checkbox


class GenerationFrame(tk.Frame):
    def __init__(self, mf: MainFrame):
        super().__init__(background=config.MAIN_COLOR)
        self._main_frame = mf
        self._set_generation_button()
        self._set_display_entry()

    @property
    def length(self) -> str:
        return self._main_frame.length_entry.get()

    @property
    def quantity(self) -> str:
        return self._main_frame.quantity_entry.get()

    @property
    def is_digits_enabled(self) -> bool:
        return self._main_frame.is_digit_enabled.get()

    @property
    def is_letters_enabled(self) -> bool:
        return self._main_frame.is_chars_enabled.get()
    
    @property
    def is_marks_enabled(self) -> bool:
        return self._main_frame.is_marks_enabled.get()

    def _set_display_entry(self):
        self.display_entry = tk.Entry(self, bg=config.FILL_COLOR, font=config.FONT_STYLE, width=25)
        self.display_entry.pack(pady=20)

    def _set_generation_button(self):
        self.button = tk.Button(self, text='Сгенерировать', font=config.FONT_STYLE,
                                background=config.MAIN_COLOR, activebackground=config.FILL_COLOR,
                                padx=20, pady=15,
                                command=self._display_password)
        self.button.pack(pady=30)

    def _display_password(self):
        self.display_entry.delete(0, tk.END)
        try:
            length = int(self.length)
            quantity = int(self.quantity)
            msg = generate_password(length, self.is_digits_enabled,
                                    self.is_letters_enabled, self.is_marks_enabled)
        except ValueError:
            msg = 'Укажите целое число'
        except EmptyGeneratingRangeError:
            msg = 'Выберите набор символов'
        self.display_entry.insert(0, msg)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self._window_configuration()
        self.main_frame = MainFrame()
        self.main_frame.grid(row=0, column=0)
        self.gen_frame = GenerationFrame(self.main_frame)
        self.gen_frame.grid(row=1, column=0)
        # self._set_output_label()

    def _window_configuration(self):
        self.geometry(config.WINDOW_SIZE)
        self.minsize(400, 450)
        self.title(config.APP_TITLE)
        logo = tk.PhotoImage(file='logo.png')
        self.iconphoto(False, logo)
        self.config(bg=config.MAIN_COLOR, borderwidth=20)


def main():
    window = App()
    window.mainloop()


if __name__ == '__main__':
    main()
