# POO-2024.2
Aluno: Athisson Alberto Lima Marques

# Fitness App
Um aplicativo com aulas para treinos, usuários e acompanhamento de progresso que oferece rotinas de exercícios, acompanhamento de condicionamento físico e muito mais.

# Funcionalidades:

#01 Criar/Gerenciar Plano de Treino (create_workout) - Implementada\
Adiciona treinos a uma lista global.

#02 Rastrear Atividades (track_activity) - Implementada\
Rastreia passos, calorias e duração.

#03 Rastrear Nutrição e Dieta (track_nutrition) - Implementada\
Registra alimentos e calorias.

#04 Definir Metas e Acompanhar Progresso (set_goals) - Implementada\
Define metas para passos, calorias e duração.

#05 Sincronizar Dispositivo (sync_device) - Implementada\
Simula a sincronização.

#06 Compartilhar Progresso e Participar de Desafios (share_progress) - Implementada de forma genérica\
Permite compartilhar progresso ou entrar em desafios.

#07 Acessar Tutoriais e Guias em Vídeo (access_tutorials) - Implementada\
Exibe uma lista de vídeos predefinidos.

#08 Obter Recomendações Personalizadas (get_recommendations) - Implementada\
Dá sugestões com base no progresso.

#09 Avaliar e Dar Feedback (give_feedback) - Implementada\
Permite avaliação de treinos.

#10 Acessar Fórum da Comunidade (access_forum) - Implementada de forma genérica\
Exibe tópicos populares ou permite criar um novo.

#11 Exibir Dados (check_progress) - Implementada\
Mostra progresso em relação às metas.

#12 Sair (exit) - Implementada\
Encerra o programa.

# Conceitos Utilizados:

- Classes: Define a estrutura e o comportamento de cada objeto.

- Métodos: Funções definidas dentro das classes que descrevem os comportamentos dos objetos dela.

- Encapsulamento: Os atributos que não são acessados diretamente fora das classes foram prefixados com um underscore (_), como self._workouts,  self._activities, self._nutrition, etc. Isso indica que esses atributos são privados.

- Herança: As classes ActivityTracker e NutritionTracker herdam da classe abstrata Tracker. Isso significa que ambas as classes são especializações da classe base e são tratadas como instâncias de Tracker.

- Polimorfismo: Quando o código chama o método track em diferentes instâncias de Tracker (como ActivityTracker e NutritionTracker). O mesmo método pode se comportar de maneira diferente dependendo da classe que o implementa.

- Classe Abstrata: A classe Tracker é uma classe abstrata que define a interface para rastreadores de atividades e nutrição. Ela contém métodos abstratos (track e get_progress) que são implementados pelas subclasses.
