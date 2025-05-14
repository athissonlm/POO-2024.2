import time
import random  # Para simular dados de dispositivos vestíveis

# Exibe o menu principal e recebe a opção do usuário
def display_menu():
    print("\nBem Vindo(a) ao Fitness App!\nO que você deseja fazer hoje?\n")
    print("1. Criar/Gerenciar Plano de Treino")
    print("2. Rastrear Atividades")
    print("3. Rastrear Nutrição e Dieta")
    print("4. Definir Metas e Acompanhar Progresso")
    print("5. Sincronizar Dispositivo Vestível")
    print("6. Compartilhar Progresso e Participar de Desafios")
    print("7. Acessar Tutoriais e Guias em Vídeo")
    print("8. Obter Recomendações Personalizadas")
    print("9. Avaliar e Dar Feedback")
    print("10. Acessar Fórum da Comunidade")
    print("11. Exibir Dados")
    print("12. Sair\n")
    
    option = input("Escolha uma opção: ").strip()
    if option not in map(str, range(1, 13)):
        print("Opção inválida! Tente novamente.")
        return None
    return option

# Função para criar e armazenar um plano de treino
def create_workout():
    name = input("Nome do treino: ").strip()
    description = input("Descrição do treino: ").strip()
    
    if not name or not description:
        print("Erro: Nome e descrição não podem estar vazios.")
        return

    workouts.append({"Nome": name, "Descrição": description})
    print("Treino adicionado com sucesso!")

# Registra as atividades físicas do usuário
def track_activity():
    try:
        steps = int(input("Número de passos: "))
        calories = float(input("Calorias queimadas: "))
        duration = int(input("Duração do treino (minutos): "))
        
        activities.append({"Passos": steps, "Calorias": calories, "Duração": duration})
        progress["Passos"] += steps
        progress["Calorias"] += calories
        progress["Duração"] += duration

        print("Atividade registrada!")
    except ValueError:
        print("Erro: Insira valores numéricos válidos.")

# Registra a nutrição e ingestão calórica do usuário
def track_nutrition():
    try:
        food = input("Alimento consumido: ").strip()
        calories = float(input("Calorias ingeridas: "))
        
        if not food:
            print("Erro: O nome do alimento não pode estar vazio.")
            return
        
        nutrition.append({"Alimento": food, "Calorias": calories})
        print("Alimento registrado!")
    except ValueError:
        print("Erro: Insira valores numéricos válidos.")

# Define metas diárias de exercícios
def set_goals():
    try:
        goals["Passos"] = int(input("Meta diária de passos: "))
        goals["Calorias"] = float(input("Meta diária de calorias queimadas: "))
        goals["Duração"] = int(input("Meta diária de duração dos treinos (min): "))
        print("Metas definidas com sucesso!")
    except ValueError:
        print("Erro: Insira valores numéricos válidos.")

# Exibe o progresso do usuário em relação às metas definidas
def check_progress():
    print("\nProgresso Atual:")
    for key in goals:
        goal = goals[key]
        current = progress[key]
        percentage = (current / goal * 100) if goal > 0 else 0
        print(f"{key}: {current} / {goal} ({percentage:.1f}%)")

# Simula a sincronização com dispositivos vestíveis
def sync_device():
    steps = random.randint(100, 500)  
    calories = random.uniform(20, 100)  
    
    progress["Passos"] += steps
    progress["Calorias"] += calories
    
    print(f"Dispositivo sincronizado! +{steps} passos e +{calories:.2f} calorias adicionados.")

# Permite compartilhar o progresso ou participar de desafios
def share_progress():
    print("\nCompartilhamento Social e Desafios")
    print("1. Compartilhar progresso")
    print("2. Participar de um desafio")
    
    option = input("Escolha uma opção: ").strip()
    if option == '1':
        print("Seu progresso foi compartilhado!")
    elif option == '2':
        print("Você entrou em um desafio de 10.000 passos diários!")
    else:
        print("Opção inválida.")

# Exibe vídeos tutoriais disponíveis
def access_tutorials():
    print("\nTutoriais e Guias em Vídeo:")
    for video in videos:
        print(video)

# Fornece recomendações personalizadas de treino e nutrição
def get_recommendations():
    print("\nRecomendações Personalizadas:")
    
    if progress["Passos"] < goals["Passos"] * 0.5:
        print("- Você está abaixo da sua meta de passos. Tente caminhar mais!")
    
    if progress["Calorias"] < goals["Calorias"] * 0.5:
        print("- Considere um treino aeróbico para queimar mais calorias.")

# Permite que os usuários avaliem e forneçam feedback sobre treinos
def give_feedback():
    name = input("Nome do treino avaliado: ").strip()
    rating = input("Dê uma nota (1 a 5): ").strip()
    comment = input("Deixe um comentário: ").strip()
    
    if not name or not rating.isdigit() or not (1 <= int(rating) <= 5):
        print("Erro: Dados inválidos!")
        return
    
    feedbacks.append({"Treino": name, "Nota": int(rating), "Comentário": comment})
    print("Obrigado pelo feedback!")

# Simula acesso ao fórum da comunidade
def access_forum():
    print("\nBem-vindo ao Fórum da Comunidade!")
    print("1. Ver tópicos populares")
    print("2. Criar um novo tópico")
    
    option = input("Escolha uma opção: ").strip()
    if option == '1':
        print("- Como manter a motivação nos treinos?")
        print("- Dicas de alimentação saudável")
    elif option == '2':
        title = input("Título do seu tópico: ").strip()
        if title:
            print(f"Seu tópico '{title}' foi criado com sucesso!")
    else:
        print("Opção inválida.")

# Dicionário que mapeia opções para funções
functions = {str(i + 1): func for i, func in enumerate([create_workout, track_activity, track_nutrition, set_goals, sync_device, share_progress, access_tutorials, get_recommendations, give_feedback, access_forum, check_progress, exit])}

# Função principal que gerencia o loop do menu
def main():
    while True:
        option = display_menu()
        if option is None:
            continue
        
        functions[option]()
        time.sleep(1)

if __name__ == "__main__":
    workouts = []
    activities = []
    nutrition = []
    goals = {"Passos": 0, "Calorias": 0, "Duração": 0}
    progress = {"Passos": 0, "Calorias": 0, "Duração": 0}
    feedbacks = []
    videos = ["Treino para Iniciantes - link", "Treino Avançado - link"]
    main()
