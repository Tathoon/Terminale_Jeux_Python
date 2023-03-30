class Button:
    def __init__(self, image, position, callback):
        self.image = image
        self.rect = image.get_rect(topleft=position)
        self.callback = callback
 
    def on_click(self, event):
        if event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback(self)
 
# Define and create button
button = Button(your_image, (10, 10), push_button_goodbye)
# In event loop. Under pygame.MOUSEBUTTONDOWN.
button.on_click(event)
# In main loop draw area.
surface.blit(button.image, button.rect)