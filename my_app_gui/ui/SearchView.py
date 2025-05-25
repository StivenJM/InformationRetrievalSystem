"""
SearchView defines the main user interface components:
- A search screen with an entry field and search button.
- A result screen that displays document matches with score and preview.
"""
import customtkinter as ctk
from typing import Callable
from models.Search import SearchResult

class SearchView(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, on_search: Callable[[str], None]):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.on_search = on_search
        self._build_search_screen()

    def _build_search_screen(self):
        self.search_label = ctk.CTkLabel(self, text="Enter your query:")
        self.search_label.pack(pady=10)

        self.query_entry = ctk.CTkEntry(self, width=600)
        self.query_entry.pack(pady=10)

        self.search_button = ctk.CTkButton(self, text="Search", command=self._handle_search)
        self.search_button.pack(pady=10)

        self.result_box = ctk.CTkTextbox(self, width=750, height=350)
        self.result_box.pack(pady=10)

    def _handle_search(self):
        query = self.query_entry.get()
        self.result_box.delete("1.0", ctk.END)
        if not query:
            self.result_box.insert(ctk.END, "Please enter a query.")
            return
        self.on_search(query)

    def show_results(self, results: list[SearchResult]):
        self.result_box.delete("1.0", ctk.END)
        if not results:
            self.result_box.insert(ctk.END, "No results found.")
        else:
            for res in results:
                preview = self._get_preview(res.doc_id)
                self.result_box.insert(
                    ctk.END,
                    f"{res.doc_id}\nScore: {res.score:.4f}\n{preview}\n{'-'*60}\n"
                )

    def _get_preview(self, filepath: str, max_lines: int = 3) -> str:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return ''.join(f.readlines()[:max_lines]).strip()
        except Exception:
            return "[Unable to load preview]"
