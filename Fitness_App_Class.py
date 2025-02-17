import time
import random

class FitnessApp:
    def __init__(self):
        self.workouts = []
        self.activities = []
        self.nutrition = []
        self.goals = {"Passos": 0, "Calorias": 0, "Duração": 0}
        self.progress = {"Passos": 0, "Calorias": 0, "Duração": 0}
        self.feedbacks = []
        self.videos = ["Treino para Iniciantes - link", "Treino Avançado - link"]
    
    def display_menu(self):
        print("\nBem-vindo(a) ao Fitness App!\nO que você deseja fazer hoje?\n")
        options = [
            "Criar/Gerenciar Plano de Treino",
            "Rastrear Atividades",
            "Rastrear Nutrição e Dieta",
            "Definir Metas e Acompanhar Progresso",
            "Sincronizar Dispositivo Vestível",
            "Compartilhar Progresso e Participar de Desafios",
            "Acessar Tutoriais e Guias em Vídeo",
            "Obter Recomendações Personalizadas",
            "Avaliar e Dar Feedback",
            "Acessar Fórum da Comunidade",
            "Exibir Dados",
            "Sair"
        ]
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        
        choice = input("\nEscolha uma opção: ").strip()
        return choice if choice in map(str, range(1, 13)) else None
    
    def create_workout(self):
        name = input("Nome do treino: ").strip()
        description = input("Descrição do treino: ").strip()
        if name and description:
            self.workouts.append({"Nome": name, "Descrição": description})
            print("Treino adicionado com sucesso!")
        else:
            print("Erro: Nome e descrição não podem estar vazios.")
    
    def track_activity(self):
        try:
            steps = int(input("Número de passos: "))
            calories = float(input("Calorias queimadas: "))
            duration = int(input("Duração do treino (minutos): "))
            
            self.activities.append({"Passos": steps, "Calorias": calories, "Duração": duration})
            self.progress["Passos"] += steps
            self.progress["Calorias"] += calories
            self.progress["Duração"] += duration

            print("Atividade registrada!")
        except ValueError:
            print("Erro: Insira valores numéricos válidos.")
    
    def track_nutrition(self):
        try:
            food = input("Alimento consumido: ").strip()
            calories = float(input("Calorias ingeridas: "))
            if food:
                self.nutrition.append({"Alimento": food, "Calorias": calories})
                print("Alimento registrado!")
            else:
                print("Erro: O nome do alimento não pode estar vazio.")
        except ValueError:
            print("Erro: Insira valores numéricos válidos.")
    
    def set_goals(self):
        try:
            self.goals["Passos"] = int(input("Meta diária de passos: "))
            self.goals["Calorias"] = float(input("Meta diária de calorias queimadas: "))
            self.goals["Duração"] = int(input("Meta diária de duração dos treinos (min): "))
            print("Metas definidas com sucesso!")
        except ValueError:
            print("Erro: Insira valores numéricos válidos.")
    
    def check_progress(self):
        print("\nProgresso Atual:")
        for key in self.goals:
            goal = self.goals[key]
            current = self.progress[key]
            percentage = (current / goal * 100) if goal > 0 else 0
            print(f"{key}: {current} / {goal} ({percentage:.1f}%)")
    
    def sync_device(self):
        steps = random.randint(100, 500)
        calories = random.uniform(20, 100)
        self.progress["Passos"] += steps
        self.progress["Calorias"] += calories
        print(f"Dispositivo sincronizado! +{steps} passos e +{calories:.2f} calorias adicionados.")
    
    def share_progress(self):
        print("\n1. Compartilhar progresso\n2. Participar de um desafio")
        option = input("Escolha uma opção: ").strip()
        print("Seu progresso foi compartilhado!" if option == '1' else "Você entrou em um desafio de 10.000 passos diários!" if option == '2' else "Opção inválida.")
    
    def access_tutorials(self):
        print("\nTutoriais e Guias em Vídeo:")
        for video in self.videos:
            print(video)
    
    def get_recommendations(self):
        print("\nRecomendações Personalizadas:")
        if self.progress["Passos"] < self.goals["Passos"] * 0.5:
            print("- Caminhe mais para atingir sua meta!")
        if self.progress["Calorias"] < self.goals["Calorias"] * 0.5:
            print("- Considere um treino aeróbico para queimar mais calorias.")
    
    def give_feedback(self):
        name = input("Nome do treino avaliado: ").strip()
        rating = input("Dê uma nota (1 a 5): ").strip()
        comment = input("Deixe um comentário: ").strip()
        if name and rating.isdigit() and 1 <= int(rating) <= 5:
            self.feedbacks.append({"Treino": name, "Nota": int(rating), "Comentário": comment})
            print("Obrigado pelo feedback!")
        else:
            print("Erro: Dados inválidos!")
    
    def access_forum(self):
        print("\n1. Ver tópicos populares\n2. Criar um novo tópico")
        option = input("Escolha uma opção: ").strip()
        if option == '1':
            print("- Como manter a motivação nos treinos?\n- Dicas de alimentação saudável")
        elif option == '2':
            title = input("Título do seu tópico: ").strip()
            if title:
                print(f"Seu tópico '{title}' foi criado com sucesso!")
        else:
            print("Opção inválida.")
    
    def run(self):
        functions = {
            "1": self.create_workout, "2": self.track_activity, "3": self.track_nutrition, "4": self.set_goals,
            "5": self.sync_device, "6": self.share_progress, "7": self.access_tutorials, "8": self.get_recommendations,
            "9": self.give_feedback, "10": self.access_forum, "11": self.check_progress, "12": exit
        }
        while True:
            option = self.display_menu()
            if option:
                functions[option]()
                time.sleep(1)

if __name__ == "__main__":
    app = FitnessApp()
    app.run()
