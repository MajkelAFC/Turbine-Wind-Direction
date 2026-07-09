class WindRecord:
    def __init__(self, winddirabs):
     self.winddirabs = winddirabs

    def get_clean_data(self) -> float | None:
        try:
            val = float(self.winddirabs)
            if val < 0 or val > 360:
                return None
            return val
        except ValueError as e:
            print(f"Invalid wind diameter {e}")
            return None

