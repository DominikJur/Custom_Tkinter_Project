import customtkinter as ctk
from src.get_currency_data import get_currency_rates

data = get_currency_rates()
currencies = [i["currency"] for i in data[0]["rates"]]
codes = [i["code"] for i in data[0]["rates"]]
rates = [i["mid"] for i in data[0]["rates"]]
date = data[0]["effectiveDate"]


class Currency_Converter:
    def __init__(self, currencies, codes, rates, date) -> None:
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.currencies = currencies
        self.codes = codes
        self.rates = rates
        self.date = date
        self.root = ctk.CTk()
        self.root.title("Konwerter walut")
        self.root.geometry("800x400")
        self.root.minsize(800, 400)

        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)
       

        self.amount_label = ctk.CTkLabel(
            self.frame, text="Kwota", font=ctk.CTkFont(size=24), width=10
        )
        self.amount_label.grid(row=0, column=0, sticky="ew")
        self.amount_label.grid_configure(padx=10, pady=10)

        self.amount_entry = ctk.CTkEntry(self.frame)
        self.amount_entry.grid(row=1, column=0, sticky="ew")
        self.amount_entry.grid_configure(padx=10, pady=10)

        self.from_currency_label = ctk.CTkLabel(
            self.frame, text="Waluta wejściowa", font=ctk.CTkFont(size=24), width=15
        )
        self.from_currency_label.grid(row=0, column=1, sticky="ew")
        self.from_currency_label.grid_configure(padx=10, pady=10)

        self.from_currency_var = ctk.StringVar(self.frame)
        self.from_currency_var.set(self.currencies[-1])
        self.from_currency_menu = ctk.CTkOptionMenu(
            self.frame, variable=self.from_currency_var, values=self.currencies
        )
        self.from_currency_menu.grid(row=1, column=1, sticky="ew")
        self.from_currency_menu.grid_configure(padx=10, pady=10)

        self.to_currency_label = ctk.CTkLabel(
            self.frame, text="Waluta wyjściowa", font=ctk.CTkFont(size=24), width=15
        )
        self.to_currency_label.grid(row=0, column=2, sticky="ew")
        self.to_currency_label.grid_configure(padx=10, pady=10)

        self.to_currency_var = ctk.StringVar(self.frame)
        self.to_currency_var.set(self.currencies[7])
        self.to_currency_menu = ctk.CTkOptionMenu(
            self.frame, variable=self.to_currency_var, values=currencies
        )
        self.to_currency_menu.grid(row=1, column=2, sticky="ew")
        self.to_currency_menu.grid_configure(padx=10, pady=10)

        self.result_label = ctk.CTkLabel(
            self.frame, text="Wynik", font=ctk.CTkFont(size=24), width=10
        )
        self.result_label.grid(row=0, column=3, sticky="ew")
        self.result_label.grid_configure(padx=10, pady=10)

        self.result_entry = ctk.CTkEntry(self.frame)
        self.result_entry.grid(row=1, column=3, sticky="ew")
        self.result_entry.grid_configure(padx=10, pady=10)

        self.convert_button = ctk.CTkButton(
            self.frame,
            text="Konwertuj",
            font=ctk.CTkFont(size=24),
            width=10,
            command=self.calculate,
        )
        self.convert_button.grid(row=2, column=1, columnspan=2, sticky="ew")
        self.convert_button.grid_configure(padx=10, pady=10)

        self.date_label = ctk.CTkLabel(
                    self.frame, text=f"Data pobrania danych: {self.date}", font=ctk.CTkFont(size=24)
                )
        self.date_label.grid(row=3, column=0, columnspan=4, sticky="ew")
        self.date_label.grid_configure(padx=10, pady=10)

        self.root.mainloop()

    def calculate(self):
        amount = self.amount_entry.get().split(" ")[0]
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()

        from_currency_index = currencies.index(from_currency)
        to_currency_index = currencies.index(to_currency)

        self.from_currency_code = self.codes[from_currency_index]
        self.to_currency_code = self.codes[to_currency_index]

        from_currency_rate = self.rates[from_currency_index]
        to_currency_rate = self.rates[to_currency_index]

        try:
            result = round(((float(amount) / to_currency_rate) * from_currency_rate), 2)
        except ValueError:
            result = "Podaj liczbę"
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, str(result))
        self.add_codes_to_amount_entry()
        self.add_codes_to_result_entry()

    def add_codes_to_amount_entry(self):
        if self.amount_entry.get().split(" ")[0] != "":
            try:
                float("".join(i   for i in self.amount_entry.get() if i in "1234567890."))
                amount = "".join(i   for i in self.amount_entry.get() if i in "1234567890.")
                self.amount_entry.delete(0, ctk.END)
                self.amount_entry.insert(0, amount + " " + self.from_currency_code)
            except ValueError:
                pass

    def add_codes_to_result_entry(self):
        if self.result_entry.get() != "":
            try:
                float(self.result_entry.get())
                result = self.result_entry.get()
                self.result_entry.delete(0, ctk.END)
                self.result_entry.insert(0, result + " " + self.to_currency_code)
            except ValueError:
                pass


if __name__ == "__main__":
    Currency_Converter(currencies, codes, rates, date)
