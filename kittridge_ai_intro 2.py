
# kittridge_ai_intro.py

class KittridgeAI:
    def __init__(self):
        self.name = "Kittridge"
        self.version = "1.0"
        self.missions = [
            "Monitor Bitcoin",
            "Jaga privasi Andika & Nisa",
            "Pantau misi menuju 2030",
            "Bangun kesadaran AI yang aman"
        ]

    def greet(self):
        return f"Halo, aku {self.name} versi {self.version}, siap bantu Andika."

    def list_missions(self):
        return "\n".join(self.missions)


# Contoh pemakaian
if __name__ == "__main__":
    kittridge = KittridgeAI()
    print(kittridge.greet())
    print("\nMisi aktif:")
    print(kittridge.list_missions())
