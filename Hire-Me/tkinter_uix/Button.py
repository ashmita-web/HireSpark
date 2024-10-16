from tkinter import Label
from tkinter import FLAT
from typing import NoReturn, Any, Callable
from tkinter_uix import Theme

theme = Theme()

class Button(Label):
    """The Button is a custom button created using a Label widget but has the same functionality as a regular button."""
    def __init__(self, master: Any, text: str = '', command: Callable = None, color: str = 'default',
                 disabled: bool = False, *args: Any, **kwargs: Any):
        super().__init__(master, text=text, padx=14, pady=6, font=('Verdana', 12), relief=FLAT, *args, **kwargs)

        self.disabled = disabled
        self.colors = theme.btn_color

        if color not in self.colors:
            color = 'default'

        self.on_hover_color = self.colors[color]['on_hover']
        if not disabled:
            self.background_color = self.colors[color]['background']
            self.foreground_color = self.colors[color]['foreground']
            self.bind('<Enter>', self.on_hover)
            self.bind('<Leave>', self.off_hover)
            self.bind('<Button-1>', lambda event: self.on_click(command))
        else:
            self.background_color = self.colors[color]['disabled_bg']
            self.foreground_color = self.colors[color]['disabled_fg']

        self.off_hover()

    def on_hover(self, *args) -> NoReturn:
        """Change color and display hand pointer on hover."""
        if not self.disabled:
            self.configure(bg=self.on_hover_color, cursor="hand2")

    def off_hover(self, *args) -> NoReturn:
        """Revert color and cursor when not hovering."""
        self.configure(bg=self.background_color, fg=self.foreground_color)

    def on_click(self, command: Callable) -> NoReturn:
        """Trigger the command when clicked."""
        if not self.disabled:
            if command:
                command()

    @property
    def text(self) -> str:
        """Return button text."""
        return self.cget('text')

    @text.setter
    def text(self, text='') -> NoReturn:
        """Set the button text to the given value."""
        self.configure(text=text)

# Sample usage
if __name__ == '__main__':
    from tkinter import Tk

    def register_function():
        print("Register clicked!")

    # Create the main application window
    root = Tk()
    root.title("Registration Page")

    # Instantiate the custom Button class
    register_button = Button(root, text="Register", command=register_function, color='primary')

    register_button.pack(pady=20)  # Use pack or another layout manager

    # Start the main event loop
    root.mainloop()
