"""
GUI application entrypoint using CustomTkinter.
Connects the SearchView with the SearchController (MVC pattern).
"""

import customtkinter as ctk
from ui.SearchView import SearchView
from controllers.SearchController import SearchController

class SearchApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Document Retrieval System")
        self.geometry("800x500")

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        self.controller = SearchController()
        self.view = SearchView(self, on_search=self.handle_search)

    def handle_search(self, query: str):
        results = self.controller.send_query(query)
        self.view.show_results(results)

def run_gui():
    app = SearchApp()
    app.mainloop()

if __name__ == "__main__":
    run_gui()
