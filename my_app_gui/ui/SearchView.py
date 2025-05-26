"""
SearchView defines the main user interface components:
- A search screen with an entry field and search button.
- A result screen that displays document matches with score and preview.
"""

import customtkinter as ctk
from typing import Callable
from models.Search import SearchResult
import os
import subprocess
import platform

class SearchView(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, on_search: Callable[[str], None]):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.on_search = on_search
        self._build_header() 
        self._build_search_screen()
        self.doc_paths = {} 

    
    def _build_header(self):
        """Construye el encabezado con título arriba e icono debajo, ambos centrados"""
        header_frame = ctk.CTkFrame(self, fg_color="transparent", height=100)
        header_frame.pack(fill="x", pady=(10, 0))
        header_frame.pack_propagate(False)  # Mantiene el alto fijo
        
        # Contenedor vertical para centrar ambos elementos
        center_container = ctk.CTkFrame(header_frame, fg_color="transparent")
        center_container.pack(expand=True)  # Centrado vertical y horizontal
        
        # Título del sistema (parte superior)
        self.title_label = ctk.CTkLabel(
            center_container,
            text="Modelo Probabilístico BM25",
            font=("Arial", 24, "bold"),
            text_color="#1a73e8"
        )
        self.title_label.pack(pady=(0, 5))  # Espacio inferior para el icono
        
        # Icono de globo (🌐) - parte inferior
        self.logo_label = ctk.CTkLabel(
            center_container,
            text="🌐",
            font=("Arial", 50)
        )
        self.logo_label.pack()

    def _build_search_screen(self):
        # Configuración del tema para parecer navegador
        ctk.set_appearance_mode("night")
        ctk.set_default_color_theme("dark-blue")  
        
        # Barra de búsqueda estilo navegador
        self.search_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.search_frame.pack(fill="x", padx=20, pady=10)
        
        self.query_entry = ctk.CTkEntry(
            self.search_frame,
            placeholder_text="Buscar en la base...",
            width=600,
            height=40,
            corner_radius=20,
            font=("Arial", 14)
        )
        self.query_entry.pack(side="left", expand=True, fill="x", padx=(0, 10))
        
        self.search_button = ctk.CTkButton(
            self.search_frame,
            text="Buscar",
            command=self._handle_search,
            height=40,
            width=100,
            corner_radius=20,
            font=("Arial", 14, "bold"),
            fg_color="#1a73e8",
            hover_color="#0d5bba"
        )
        self.search_button.pack(side="left")

        # Área de resultados estilo tarjetas
        self.results_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.results_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    def _handle_search(self):
        query = self.query_entry.get()
        self._clear_results()
        if not query:
            self._show_message("Ingrese una busqueda")
            return
        self.on_search(query)

    def _clear_results(self):
        for widget in self.results_frame.winfo_children():
            widget.destroy()

    def _show_message(self, message: str):
        label = ctk.CTkLabel(
            self.results_frame,
            text=message,
            font=("Arial", 14),
            text_color="gray"
        )
        label.pack(pady=20)

    def show_results(self, results: list[SearchResult]):
        self._clear_results()
        self.doc_paths = {}
        
        if not results:
            self._show_message("No Se Encontraron Resultados.")
            return
            
        for res in results:
            doc_id = res.doc_id
            self.doc_paths[doc_id] = doc_id  
            self._add_result_card(
                title=os.path.basename(doc_id),
                score=res.score,
                doc_path=doc_id
            )

    def _add_result_card(self, title: str, score: float, doc_path: str):
        #Crea una tarjeta de resultado clickeable
        card = ctk.CTkFrame(
            self.results_frame,
            corner_radius=10,
            border_width=1,
            border_color="#e0e0e0"
        )
        card.pack(fill="x", pady=5)
        
        # Hacer toda la tarjeta clickeable
        card.bind("<Button-1>", lambda e, path=doc_path: self._open_document(path))
        card.configure(cursor="hand2")  # Cambiar cursor a mano al pasar sobre la tarjeta
        
        # Contenedor para el contenido de la tarjeta
        content_frame = ctk.CTkFrame(card, fg_color="transparent")
        content_frame.pack(fill="x", padx=15, pady=10)

        # Título del documento (también clickeable)
        title_label = ctk.CTkLabel(
            content_frame,
            text=title,
            font=("Arial", 18, "bold"),
            anchor="w",
            wraplength=600
        )
        title_label.pack(fill="x", padx=15, pady=(10, 0))
        title_label.bind("<Button-1>", lambda e, path=doc_path: self._open_document(path))
        
        # Ruta del documento (texto pequeño)
        path_label = ctk.CTkLabel(
            content_frame,
            text=doc_path,
            font=("Arial", 10),
            text_color="gray",
            anchor="w",
            wraplength=600
        )
        path_label.pack(fill="x", pady=(2, 0))
        path_label.bind("<Button-1>", lambda e, path=doc_path: self._open_document(path))

        # Score (relevancia)
        score_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
        score_frame.pack(fill="x", pady=(5, 0))
        
        score_label = ctk.CTkLabel(
            score_frame,
            text=f"Relevancia: {score:.4f}",
            font=("Arial", 14),
            text_color="gray"
        )
        score_label.pack(side="left")

        # Separador visual
        ctk.CTkFrame(
            card,
            height=1,
            fg_color="#e0e0e0"
        ).pack(fill="x", padx=10, pady=(5, 0))

    def _open_document(self, filepath: str):
        try:
            if platform.system() == "Windows":
                os.startfile(filepath)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", filepath], check=True)
            else:  # Linux y otros
                subprocess.run(["xdg-open", filepath], check=True)
        except Exception as e:
            print(f"Error al abrir el documento: {e}")
            error_label = ctk.CTkLabel(
                self.results_frame,
                text=f"Error opening document: {os.path.basename(filepath)}",
                text_color="red"
            )
            error_label.pack()

   