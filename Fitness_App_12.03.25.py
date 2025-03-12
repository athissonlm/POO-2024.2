import time
import random
from abc import ABC, abstractmethod

class Tracker(ABC):
    """Classe abstrata para rastreadores de atividades e nutrição."""
    
    @abstractmethod
    def track(self):
        """Método abstrato para rastrear dados."""
        pass

    @abstractmethod
    def get_progress(self):
        """Método abstrato para obter progresso."""
        pass

class WorkoutManager:
    """Classe responsável pela criação e gerenciamento de treinos."""
    def __init__(self):
        self._workouts = []  # Atributo privado

    @property
    def workouts(self):
        """Getter para a lista de treinos."""
        return self._workouts

    def create_workout(self):
        """Permite ao usuário criar um novo treino com nome e descrição."""
        name = input("Nome do treino: ").strip()
        description = input("Descrição do treino: ").strip()
        if name and description:
            self._workouts.append({"Nome": name, "Descrição": description})
            print("Treino adicionado com sucesso!")
        else:
            print("Erro: Nome e descrição não podem estar vazios.")

class ActivityTracker(Tracker):
    """Classe responsável pelo rastreamento de atividades físicas."""
    def __init__(self):
        self._activities = []  # Atributo privado
        self._progress = {"Passos": 0, "Calorias": 0, "Duração": 0}  # Atributo privado

    @property
    def activities(self):
        """Getter para a lista de atividades."""
        return self._activities

    @property
    def progress(self):
        """Getter para o progresso."""
        return self._progress

    def track(self):
        """Permite registrar atividades físicas, como passos, calorias e duração."""
        try:
            steps = int(input("Número de passos: "))
            calories = float(input("Calorias queimadas: "))
            duration = int(input("Duração do treino (minutos): "))
            
            self._activities.append({"Passos": steps, "Calorias": calories, "Duração": duration})
            self._progress["Passos"] += steps
            self._progress["Calorias"] += calories
            self._progress["Duração"] += duration

            print("Atividade registrada!")
        except ValueError:
            print("Erro: Insira valores numéricos válidos.")

    def get_progress(self):
        """Retorna o progresso atual das atividades."""
        return self._progress

class NutritionTracker(Tracker):
    """Classe responsável pelo rastreamento de nutrição."""
    def __init__(self):
        self._nutrition = []  # Atributo privado

    @property
    def nutrition(self):
        """Getter para a lista de nutrição."""
        return self._nutrition

    def track(self):
        """Permite ao usuário registrar alimentos consumidos e calorias ingeridas."""
        try:
            food = input("Alimento consumido: ").strip()
            calories = float(input("Calorias ingeridas: "))
            if food:
                self._nutrition.append({"Alimento": food, "Calorias": calories})
                print("Alimento registrado!")
            else:
                print("Erro: O nome do alimento não pode estar vazio.")
        except ValueError:
            print("Erro: Insira valores numéricos válidos.")

    def get_progress(self):
        """Retorna o progresso atual da nutrição."""
        return self._nutrition

class GoalManager:
    """Classe responsável pela definição e verificação de metas."""
    def __init__(self):
        self._goals = {"Passos": 0, "Calorias": 0, "Duração": 0}  # Atributo privado
        self._progress = {"Passos": 0, "Calorias": 0, "Duração": 0}  # Atributo privado

    @property
    def goals(self):
        """Getter para as metas."""
        return self._goals

    @property
    def progress(self):
        """Getter para o progresso."""
        return self._progress

    def set_goals(self):
        """Define metas diárias para passos, calorias e duração do treino."""
        try:
            self._goals["Passos"] = int(input("Meta diária de passos: "))
            self._goals["Calorias"] = float(input("Meta diária de calorias queimadas: "))
            self._goals["Duração"] = int(input("Meta diária de duração dos treinos (min): "))
            print("Metas definidas com sucesso!")
        except ValueError:
            print("Erro: Insira valores numéricos válidos.")

    def check_progress(self):
        """Exibe o progresso atual do usuário em relação às metas."""
        print("\nProgresso Atual:")
        for key in self._goals:
            goal = self._goals[key]
            current = self._progress[key]
            percentage = (current / goal * 100) if goal > 0 else 0
            print(f"{key}: {current} / {goal} ({percentage:.1f}%)")

class DeviceSync:
    """Classe responsável pela sincronização de dispositivos vestíveis."""
    def __init__(self, progress):
        self._progress = progress  # Referência ao dicionário de progresso

    def sync_device(self):
        """Simula a sincronização de um dispositivo vestível, adicionando passos e calorias aleatórios."""
        steps = random.randint(100, 500)
        calories = random.uniform(20, 100)
        self._progress["Passos"] += steps
        self._progress["Calorias"] += calories
        print(f"Dispositivo sincronizado! +{steps} passos e +{calories:.2f} calorias adicionados.")

class FeedbackManager:
    """Classe responsável pela coleta de feedbacks dos usuários."""
    def __init__(self):
        self._feedbacks = []  # Atributo privado

    @property
    def feedbacks(self):
        """Getter para a lista de feedbacks."""
        return self._feedbacks

    def give_feedback(self):
        """Permite ao usuário dar feedback sobre treinos."""
        name = input("Nome do treino avaliado: ").strip()
        rating = input("Dê uma nota (1 a 5): ").strip()
        comment = input("Deixe um comentário: ").strip()
        if name and rating.isdigit() and 1 <= int(rating) <= 5:
            self._feedbacks.append({"Treino": name, "Nota": int(rating), "Comentário": comment})
            print("Obrigado pelo feedback!")
        else:
            print("Erro: Dados inválidos!")

class TutorialManager:
    """Classe responsável pela exibição de tutoriais e guias em vídeo."""
    def __init__(self):
        self._videos = ["Treino para Iniciantes - link", "Treino Avançado - link"]  # Atributo privado

    @property
    def videos(self):
        """Getter para a lista de vídeos."""
        return self._videos

    def access_tutorials(self):
        """Exibe vídeos tutoriais disponíveis."""
        print("\nTutoriais e Guias em Vídeo:")
        for video in self._videos:
            print(video)

class ForumManager:
    """Classe responsável pela interação com o fórum da comunidade."""
    def access_forum(self):
        """Permite ao usuário acessar e navegar pelo fórum."""
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

class FitnessApp:
    """Classe principal que gerencia a execução do aplicativo."""
    def __init__(self):
        # Inicializa os gerenciadores de funcionalidades
        self.workout_manager = WorkoutManager()
        self.activity_tracker = ActivityTracker()
        self.nutrition_tracker = NutritionTracker()
        self.goal_manager = GoalManager()
        self.device_sync = DeviceSync(self.activity_tracker.progress)
        self.feedback_manager = FeedbackManager()
        self.tutorial_manager = TutorialManager()
        self.forum_manager = ForumManager()

    def display_menu(self):
        """Exibe o menu principal e retorna a opção escolhida pelo usuário."""
        print("\nBem-vindo(a) ao Fitness App!\nO que você deseja fazer hoje?\n")
        options = [
            "1. Criar/Gerenciar Plano de Treino",
            "2. Rastrear Atividades",
            "3. Rastrear Nutrição e Dieta",
            "4. Definir Metas e Acompanhar Progresso",
            "5. Sincronizar Dispositivo Vestível",
            "6. Compartilhar Progresso e Participar de Desafios",
            "7. Acessar Tutoriais e Guias em Vídeo",
            "8. Obter Recomendações Personalizadas",
            "9. Avaliar e Dar Feedback",
            "10. Acessar Fórum da Comunidade",
            "11. Exibir Dados",
            "12. Sair"
        ]
        for option in options:
            print(option)
        
        choice = input("\nEscolha uma opção: ").strip()
        return choice

    def run(self):
        """Executa o loop principal do aplicativo."""
        functions = {
            "1": self.workout_manager.create_workout,
            "2": self.activity_tracker.track,
            "3": self.nutrition_tracker.track,
            "4": self.goal_manager.set_goals,
            "5": self.device_sync.sync_device,
            "6": self.share_progress,
            "7": self.tutorial_manager.access_tutorials,
            "8": self.get_recommendations,
            "9": self.feedback_manager.give_feedback,
            "10": self.forum_manager.access_forum,
            "11": self.goal_manager.check_progress,
            "12": exit
        }
        while True:
            option = self.display_menu()
            if option in functions:
                functions[option]()  # Chama a função correspondente à opção escolhida
            else:
                print("Opção inválida. Tente novamente.")
            time.sleep(1)

    def share_progress(self):
        """Permite ao usuário compartilhar seu progresso ou entrar em desafios."""
        print("\n1. Compartilhar progresso\n2. Participar de um desafio")
        option = input("Escolha uma opção: ").strip()
        print("Seu progresso foi compartilhado!" if option == '1' else "Você entrou em um desafio de 10.000 passos diários!" if option == '2' else "Opção inválida.")

    def get_recommendations(self):
        """Fornece recomendações personalizadas com base no progresso do usuário."""
        print("\nRecomendações Personalizadas:")
        if self.activity_tracker.progress["Passos"] < self.goal_manager.goals["Passos"] * 0.5:
            print("- Caminhe mais para atingir sua meta!")
        if self.activity_tracker.progress["Calorias"] < self.goal_manager.goals["Calorias"] * 0.5:
            print("- Considere um treino aeróbico para queimar mais calorias.")

if __name__ == "__main__":
    app = FitnessApp()  # Cria uma instância do aplicativo
    app.run()  # Executa o aplicativo