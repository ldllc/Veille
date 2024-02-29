import os
import csv
import tkinter
import pandas as pd
import customtkinter
from tkinter import ttk
from tkinter import Tk, simpledialog
from tkinter import messagebox, filedialog

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.file_path = ""
        self.title("Veille")
        self.geometry("1100x580")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=0, minsize=140)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=167, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(8, weight=1)
        self.sidebar_frame.grid_columnconfigure(0, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Menu :", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Groupes", command=self.show_groupes)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Attaques", command=self.show_attaques)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Victimes Retail", command=self.show_victimes)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Attaquants Retail", command=self.show_attaquants_retail)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, text="Presse", command=self.show_presse)
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)

        self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, text="Statistiques")
        self.sidebar_button_6.grid(row=6, column=0, padx=20, pady=10)
        
        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Dark", "Light", "System"],
                                                                       command=self.change_appearance_mode)
        self.appearance_mode_optionmenu.grid(row=9, column=0, padx=20, pady=(10, 10))
        self.scaling_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["100%", "90%", "80%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionmenu.grid(row=10, column=0, padx=20, pady=(10, 20))
        
        self.title_label2 = customtkinter.CTkLabel(self, text="Données", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title_label2.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.textbox = customtkinter.CTkTextbox(self, width=250, height=100, state="disabled")
        self.textbox.grid(row=1, column=1, padx=(20, 20), pady=(0, 20), sticky="nsew")

        self.treeview = ttk.Treeview(self, show="headings", selectmode="browse")
        self.treeview.grid(row=1, column=1, padx=(20, 20), pady=(0, 20), sticky="nsew")
        self.treeview.bind("<MouseWheel>", self.scroll_event)

        self.treeview.bind("<Button-3>", self.show_context_menu)
        self.context_menu = tkinter.Menu(self, tearoff=0)
        self.context_menu.add_command(label="Copy Value to Clipboard", command=self.copy_value_to_clipboard)

    def show_context_menu(self, event):
        item = self.treeview.selection()
        if item:
            self.context_menu.post(event.x_root, event.y_root)

    def copy_value_to_clipboard(self):
        selected_item = self.treeview.selection()[0]

        headers = self.treeview["columns"]
        selected_column = simpledialog.askstring("Copier dans le presse papier", "Selectionner le nom de la colonne pour copier l'élément :", initialvalue=headers[0])

        column_index = headers.index(selected_column)
        value = self.treeview.item(selected_item, "values")[column_index]

        root = Tk()
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(value)
        root.update()
        root.destroy()

        messagebox.showinfo("Clipboard", f"{selected_column} Copied to Clipboard!")

    def change_appearance_mode(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def show_groupes(self):
        file_path = "../../CSV/Groupes/Base_Groupes/Groupes.csv"

        try:
            df = pd.read_csv(file_path, sep='|')
            active_groupes_data = df[df['Status'].str.strip().str.lower() == 'active'][['ID', 'Name', 'Status', 'Description']].values.tolist()
            column_widths = [50, 100, 80, 150]

            self.create_table_groupes(['ID', 'Name', 'Status', 'Description'], active_groupes_data, column_widths)

        except FileNotFoundError:
            messagebox.showerror("Error", f"File not found: {file_path}")

    def create_table_groupes(self, headers, data, column_widths=None):
        self.treeview["columns"] = headers

        for header in headers:
            self.treeview.heading(header, text=header)
            self.treeview.column(header, anchor="center", width=0)

        for row in self.treeview.get_children():
            self.treeview.delete(row)

        for row_data in data:
            self.treeview.insert("", "end", values=row_data)

        if column_widths is not None:
            for col, width in zip(headers, column_widths):
                self.treeview.column(col, width=width)

    def show_attaques(self):
        file_path = "../../CSV/Attaques/Base_Attaques/Attaques.csv"

        try:
            df = pd.read_csv(file_path, sep='|')
            filtered_data = df[['ID', 'Name', 'Group', 'discovered', 'country']].values.tolist()
            column_widths = [50, 100, 80, 150, 80]

            self.create_table_attaques(['ID', 'Name', 'Group', 'discovered', 'country'], filtered_data, column_widths)
        except FileNotFoundError:
            messagebox.showerror("Error", f"File not found: {file_path}")

    def create_table_attaques(self, headers, data, column_widths=None):
        self.treeview["columns"] = headers

        for header in headers:
            self.treeview.heading(header, text=header)
            self.treeview.column(header, anchor="center", width=0)

        for row in self.treeview.get_children():
            self.treeview.delete(row)

        for row_data in data:
            self.treeview.insert("", "end", values=row_data)

        if column_widths is not None:
            for col, width in zip(headers, column_widths):
                self.treeview.column(col, width=width)

    def show_victimes(self):
        file_path = "../../CSV/Stats/Victimes/Victimes_Retail.csv"

        try:
            df = pd.read_csv(file_path, sep='|')
            victim_data = df[['Victim', 'Domain', 'Date', 'Country', 'URL']].values.tolist()
            column_widths = [10, 10, 3, 3, 554]

            self.create_table_victimes(['Victim', 'Domain', 'Date', 'Country', 'URL'], victim_data, column_widths)

        except FileNotFoundError:
            messagebox.showerror("Error", f"File not found: {file_path}")

    def create_table_victimes(self, headers, data, column_widths=None):
        self.treeview["columns"] = headers

        for header in headers:
            self.treeview.heading(header, text=header)
            self.treeview.column(header, anchor="center", width=0)

        for row in self.treeview.get_children():
            self.treeview.delete(row)

        for row_data in data:
            modified_row_data = []
            for value in row_data:
                modified_row_data.append(value)
            
            self.treeview.insert("", "end", values=modified_row_data)
            for i, value in enumerate(modified_row_data):
                self.treeview.set(self.treeview.get_children()[-1], headers[i])

        if column_widths is not None:
            for col, width in zip(headers, column_widths):
                self.treeview.column(col, width=width)

    def show_attaquants_retail(self):
        file_path = "../../CSV/Stats/Attaquants_Retail/Attaquants_Retail.csv"

        try:
            df = pd.read_csv(file_path, sep='|')
            attaquants_retail_data = df[['Name', 'Status', 'Last Attack', 'Description']].values.tolist()
            column_widths = [4, 4, 80, 488]

            self.create_table_attaquants_retail(['Name', 'Status', 'Last Attack', 'Description'], attaquants_retail_data, column_widths)

        except FileNotFoundError:
            messagebox.showerror("Error", f"File not found: {file_path}")

    def create_table_attaquants_retail(self, headers, data, column_widths=None):
        self.treeview["columns"] = headers

        for header in headers:
            self.treeview.heading(header, text=header)
            self.treeview.column(header, anchor="center", width=0)

        for row in self.treeview.get_children():
            self.treeview.delete(row)

        for row_data in data:
            self.treeview.insert("", "end", values=row_data)

        if column_widths is not None:
            for col, width in zip(headers, column_widths):
                self.treeview.column(col, width=width)

    def show_presse(self):
        file_path = "../../CSV/Presse/Presse_Globale/Presse_Globale.csv"

        try:
            df = pd.read_csv(file_path, sep='|')
            presse_data = df[['title', 'url', 'date']].values.tolist()
            column_widths = [300, 550, 4]

            self.create_table_presse(['title', 'url', 'date'], presse_data, column_widths)

        except FileNotFoundError:
            messagebox.showerror("Error", f"File not found: {file_path}")

    def create_table_presse(self, headers, data, column_widths=None):
        self.treeview["columns"] = headers

        for header in headers:
            self.treeview.heading(header, text=header)
            self.treeview.column(header, anchor="center", width=0)

        for row in self.treeview.get_children():
            self.treeview.delete(row)

        for row_data in data:
            self.treeview.insert("", "end", values=row_data)

        if column_widths is not None:
            for col, width in zip(headers, column_widths):
                self.treeview.column(col, width=width)

    def scroll_event(self, event):
        if event.delta:
            self.treeview.yview_scroll(-1 * (event.delta // 120), "units")

app = App()
app.mainloop()