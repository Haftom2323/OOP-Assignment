# Assignment 1: Design Your Own Class - Smartphone Example
class Smartphone:
    def __init__(self, brand, model, storage_gb, battery_percent=100):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.battery_percent = battery_percent
        self.is_locked = True
        self.installed_apps = ["Phone", "Messages", "Settings"]

    def unlock(self, pin="0000"):
        self.is_locked = False
        return f"🔓 {self.brand} {self.model} unlocked!"

    def install_app(self, app_name, size_gb):
        if size_gb > self.storage_gb:
            return "❌ Not enough storage!"
        self.installed_apps.append(app_name)
        self.storage_gb -= size_gb
        return f"📲 Installed {app_name}"

    def check_battery(self):
        return f"🔋 Battery: {self.battery_percent}%"

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage_gb}GB storage"


# Inheritance example
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage_gb, gpu_model):
        super().__init__(brand, model, storage_gb)
        self.gpu_model = gpu_model
        self.gaming_mode = False

    def enable_gaming_mode(self):
        self.gaming_mode = True
        return "🎮 Gaming mode activated!"

    def install_game(self, game_name, size_gb):
        if size_gb > self.storage_gb:
            return "❌ Not enough storage for this game!"
        return super().install_app(f"🎮 {game_name}", size_gb)


# Activity 2: Polymorphism Challenge with Animals
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        return "Moving..."


class Fish(Animal):
    def move(self):
        return "🐟 Swimming in the water!"


class Bird(Animal):
    def move(self):
        return "🦅 Flying in the sky!"


class Snake(Animal):
    def move(self):
        return "🐍 Slithering on the ground!"


if __name__ == "__main__":
    print("=== Smartphone ===")
    my_phone = GamingPhone("Razer", "Phone 2", 64, "Adreno 630")
    print(my_phone)
    print(my_phone.install_app("Angry Birds", 0.5))
    print(my_phone.install_game("Asphalt 9", 2.5))
    print(my_phone.enable_gaming_mode())

    print("\n=== Polymorphism ===")
    animals = [Fish("Nemo"), Bird("Eagle"), Snake("Python")]
    
    for animal in animals:
        print(f"{animal.name} is {animal.move().lower()}")