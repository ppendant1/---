from anvil import open_form
from ._anvil_designer import Form1Template 
import anvil


class Form1(Form1Template):

    def __init__(self, **properties):
        # Здесь инициализируются компоненты формы
        self.init_components(**properties)
      
class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)

    def button_11_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('Form2')

    def radio_button_1_clicked(self, **event_args):
      """This method is called when this radio button is selected"""
      pass
      
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def label_3_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    pass

  def button_10_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  
  def button_9_click(self, **event_args):
        """Этот метод вызывается при нажатии на кнопку"""
        # Очищаем основную панель и добавляем Form2
        self.content_panel.clear()
        self.content_panel.add_component(Form2())
        
        # Можно изменить фон кнопки, чтобы показать, что Form2 выбрана
        self.button_9.background = app.theme_colors['Primary Container']
        # Если есть другие кнопки, устанавливаем их фон в "прозрачный"
        # Например:
        # self.button_5.background = "transparent"

from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def label_3_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    pass

