from anvil import open_form
from ._anvil_designer import Form1Template 
import anvil

class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)
      
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
        # This method is supposed to open Form2, ensure Form2 is defined and imported correctly
        open_form('Form2')



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

