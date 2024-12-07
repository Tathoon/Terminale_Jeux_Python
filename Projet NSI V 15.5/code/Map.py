from dataclasses import dataclass # importe la décoration dataclass du module dataclasses de Python, qui permet de créer des classes de données avec des fonctionnalités spécifiques pour faciliter la manipulation des données
import pygame, pytmx, pyscroll

@dataclass    # décoration de classe qui indique que la classe suivante est une classe de données, c'est-à-dire une classe principalement utilisée pour stocker des données plutôt que pour implémenter des comportements ou des méthodes
class Portal: # définit une classe appelée "Portal" pour représenter un portail dans le jeu
    from_world: str
    origin_point: str
    target_world: str
    teleport_point: str
    name: str

@dataclass                        # indique que la classe "Map" suivante est également une classe de données, avec des attributs spécifiques
class Map:                        # définit une classe appelée "Map" pour représenter une carte dans le jeu
    name: str                     # chaîne de caractères (str) pour stocker le nom de la carte
    walls: list[pygame.Rect]      # liste de rectangles (instances de la classe pygame.Rect) pour stocker les zones de collision de la carte
    group: pyscroll.PyscrollGroup # instance de la classe pyscroll.PyscrollGroup pour gérer les objets affichés sur la carte
    tmx_data: pytmx.TiledMap      # instance de la classe pytmx.TiledMap pour représenter les données de la carte au format TMX
    portals: list[Portal]         # liste d'instances de la classe "Portal" pour stocker les portails associés à la carte

class MapManager: # définit une classe appelée "MapManager" pour gérer la gestion des cartes dans le jeu

    def __init__(self, mainScreen, player, path): # définit le constructeur de la classe "MapManager", qui est appelé lorsqu'un nouvel objet "MapManager" est créé. Il prend deux arguments en entrée : "mainScreen", qui représente l'écran principal du jeu, et "player", qui représente le joueur
        self.maps = dict()                  # initialise un dictionnaire vide "maps" qui sera utilisé pour stocker les cartes du jeu avec leur nom comme clé
        self.screen = mainScreen            # attribue à l'attribut self.screen de l'objet MapManager l'écran principal du jeu (mainScreen), qui est passé en argument lors de la création de l'objet. Cet attribut sera utilisé pour afficher les différentes cartes du jeu à l'écran
        self.player = player                # attribue à l'attribut self.player de l'objet MapManager l'objet du joueur (player), qui est passé en argument lors de la création de l'objet. Cet attribut sera utilisé pour interagir avec le joueur lors de la gestion des différentes cartes du jeu
        self.current_map = "throne-exit"    # attribue à l'attribut self.current_map de l'objet MapManager le nom de la carte actuellement affichée à l'écran, qui est "MapV1" dans cet exemple. Cela permet de garder une référence à la carte actuelle pour la gestion des portails et des téléportations

        self.register_map("throne-exit", path, portals=[Portal(from_world="throne-exit", origin_point="exteriorexit", target_world="cours-quete", teleport_point="playerexterior", name="1"),
                                                  Portal(from_world="throne-exit", origin_point="throneroomexit", target_world="cours-quete", teleport_point="playerexterior", name="5")
        ])
        
        self.register_map("cours-quete", path, portals=[Portal(from_world="cours-quete", origin_point="enter-throne-exit", target_world="throne-exit", teleport_point="playerexitthrone", name="2"),
                                                  Portal(from_world="cours-quete", origin_point="quete-interaction", target_world="throne-exit", teleport_point="playerexitthrone", name="3"),
                                                  Portal(from_world="cours-quete", origin_point="quete-interaction2", target_world="throne-exit", teleport_point="playerexitthrone", name="4")
        ])

        self.teleport_player("player") # utilise la méthode teleport_player() du gestionnaire de cartes (MapManager) pour téléporter le joueur à un certain point de la carte courante, en utilisant le nom du joueur ("player") comme point de téléportation. Cette méthode sera appelée lors de l'initialisation de l'objet MapManager pour positionner le joueur au début de la partie

    def check_collisions(self, monde_reve, quete3, menu_quetes, accueil, pnj, evenement, soundDesign):
        # portails
        for portal in self.get_map().portals:                # itère à travers la liste des portails de la carte courante en utilisant la méthode self.get_map().portals, où self fait référence à l'objet MapManager et portals est un attribut de l'objet de la carte courante retourné par self.get_map(). Cela permet de vérifier les collisions avec les portails de la carte courante
            if portal.from_world == self.current_map:        # vérifie si le portail actuellement examiné a comme monde d'origine le même nom que la carte courante, en comparant portal.from_world avec self.current_map
                point = self.get_object(portal.origin_point) # récupère l'objet associé au point d'origine du portail actuellement examiné en utilisant la méthode self.get_object(portal.origin_point). Cet objet représente le point précis du portail sur la carte courante où le joueur doit se tenir pour être téléporté
                rect = pygame.Rect(point.x, point.y, point.width, point.height) # crée un objet pygame.Rect (rectangle) à partir des coordonnées et de la taille de l'objet point. Cela permet de représenter la zone de collision du point d'origine du portail
                
                if self.player.feet.colliderect(rect):          # vérifie si les pieds du joueur (représentés par l'attribut self.player.feet) sont en collision avec le rectangle représentant le point d'origine du portail. Si c'est le cas, cela signifie que le joueur est en train de se tenir sur le point d'origine du portail et est prêt à se téléporter

                    if portal.name == "5":
                        self.teleport_player("player")                       
                        accueil.is_active = True
                        quete3.is_active = False
                        pnj.depart_accueil(self.screen)

                        pygame.mixer.music.stop()
                        soundDesign.play_music("intro", 1, -1)
                        
                    elif portal.name == "3" or portal.name == "4":
                        self.current_map = "throne-exit"
                        self.teleport_player("player") 
                        evenement.pile_retour.empiler(quete3)
                        evenement.pile_retour.empiler(menu_quetes)
                        menu_quetes.is_active = True
                        quete3.is_active = False

                        pygame.mixer.music.stop()
                        soundDesign.play_music("menu_quetes", 1, -1)
                        
                    else:
                        copy_portal = portal                             # crée une copie de l'objet portal actuellement examiné pour être utilisé ultérieurement dans la téléportation du joueur
                        self.current_map = portal.target_world           # met à jour le nom de la carte courante dans l'objet MapManager avec le nom du monde cible du portail actuellement examiné, en utilisant portal.target_world
                        self.teleport_player(copy_portal.teleport_point) # utilise la méthode self.teleport_player() pour téléporter le joueur au point de téléportation du portail actuellement examiné, en utilisant copy_portal.teleport_point comme point de téléportation

        # collisions
        for sprite in self.get_group().sprites():              # itère à travers tous les sprites du groupe de jeu en utilisant une boucle for, avec sprite étant la variable d'itération qui représente chaque sprite individuellement à chaque itération de la boucle
            if sprite.feet.collidelist(self.get_walls()) > -1: # vérifie si les pieds du sprite courant (représentés par l'attribut sprite.feet) sont en collision avec les murs du jeu (représentés par la méthode self.get_walls()). La méthode collidelist() de l'objet pygame.Rect est utilisée pour vérifier si le rectangle de collision des pieds du sprite est en collision avec au moins un des rectangles de collision des murs du jeu
                sprite.move_back()                             # si la collision est détectée, cette ligne appelle la méthode move_back() du sprite, qui est responsable de déplacer le sprite en arrière pour éviter la collision

    def teleport_player(self, name):
        point = self.get_object(name)     # ligne utilise la méthode self.get_object(name) pour obtenir les coordonnées d'un objet spécifique dans la carte du jeu en utilisant son nom comme clé
        self.player.position[0] = point.x # récupère les coordonnées x de l'objet de téléportation obtenu dans la carte du jeu à l'aide de la méthode
        self.player.position[1] = point.y # récupère les coordonnées y de l'objet de téléportation obtenu dans la carte du jeu à l'aide de la méthode
        self.player.save_location()       # appelle la méthode save_location() de l'objet du joueur (self.player)

    def register_map(self, name, path, portals=[]):
        
        # charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame(f"{path}assets_monde_reve/map/{name}.tmx")        # utilise la fonction load_pygame de la bibliothèque pytmx pour charger les données de la carte du jeu à partir d'un fichier au format TMX. Le nom du fichier est construit en utilisant le nom de la carte récupéré à partir de l'argument name, et il est inséré dans la chaîne de caractères formatée
        map_data = pyscroll.data.TiledMapData(tmx_data)                                      # creer un objet TiledMapData à partir des données de carte chargées précédemment à l'aide de la bibliothèque pyscroll. Cet objet représente la carte du jeu sous une forme adaptée pour être utilisée avec pyscroll
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size()) # creer un objet BufferedRenderer à partir de l'objet TiledMapData créé précédemment. Cet objet est responsable du rendu de la carte à l'écran et est configuré avec la taille de l'écran de jeu récupérée à partir de self.screen.get_size()
        map_layer.zoom = 1.5                                                                 # onfigure le zoom de la carte du jeu à 1.5, ce qui permet d'agrandir ou de réduire la carte pour s'adapter à l'échelle de l'écran de jeu
    
        walls = [] # cette ligne crée une liste vide qui sera utilisée pour stocker les rectangles de collisions

        for obj in tmx_data.objects:                                           # parcourt tous les objets de la carte du jeu chargée précédemment
            if obj.type == "collision":                                        # vérifie si le type de l'objet actuel est "collision", ce qui indique qu'il représente un objet de collision dans la carte du jeu
                walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height)) # creer un rectangle de collision en utilisant les coordonnées et les dimensions de l'objet actuel, et l'ajoute à la liste walls sous forme d'un objet pygame.Rect

        # dessiner le groupe de calques
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3) # creer un objet PyscrollGroup qui représente un groupe de sprites à afficher sur la carte du jeu. L'objet BufferedRenderer créé précédemment est passé en tant qu'argument map_layer, et default_layer est configuré à 5, ce qui indique que les sprites ajoutés à ce groupe seront affichés sur le calque 5 de la carte du jeu
        group.add(self.player)                                               # ajoute l'objet self.player (qui représente le joueur du jeu) au groupe de sprites créé précédemment

        # creer un objet Map
        self.maps[name] = Map(name, walls, group, tmx_data, portals) # creer un nouvel objet Map en utilisant les données chargées de la carte du jeu, la liste des rectangles de collisions walls, le groupe de sprites group, les données TMX tmx_data, et un objet portals

    def get_map(self): return self.maps[self.current_map] # retourne l'objet Map correspondant à la carte du jeu actuelle, en utilisant la clé self.current_map pour accéder au dictionnaire self.maps qui contient les différentes cartes du jeu

    def get_group(self): return self.get_map().group      # retourne le groupe de sprites associé à la carte du jeu actuelle en utilisant la méthode get_map() pour obtenir l'objet Map correspondant, et en accédant à l'attribut group de cet objet Map. Le groupe de sprites est utilisé pour afficher les sprites sur la carte du jeu

    def get_walls(self): return self.get_map().walls      # retourne la liste des rectangles de collisions associée à la carte du jeu actuelle en utilisant la méthode get_map() pour obtenir l'objet Map correspondant, et en accédant à l'attribut walls de cet objet Map. Cette liste contient les rectangles de collisions définis dans les données de la carte du jeu, qui sont utilisés pour gérer les collisions des sprites avec les objets de la carte

    def get_object(self, name): return self.get_map().tmx_data.get_object_by_name(name) # retourne un objet de la carte du jeu actuelle en utilisant le nom de l'objet comme argument. Elle utilise la méthode get_map() pour obtenir l'objet Map correspondant, et ensuite accède à l'attribut tmx_data de cet objet Map pour obtenir les données TMX de la carte du jeu, et enfin appelle la méthode get_object_by_name(name) sur ces données TMX pour obtenir l'objet spécifié par son nom

    def draw(self):   # dessine les éléments du jeu sur l'écran. Elle utilise le groupe de sprites associé à la carte du jeu actuelle en appelant self.get_group().draw(self.screen), ce qui dessine tous les sprites du groupe sur l'écran. Ensuite, elle centre le groupe de sprites sur le sprite du joueur en appelant self.get_group().center(self.player.rect.center), ce qui assure que le sprite du joueur est centré sur l'écran
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self, monde_reve, quete3, menu_quetes, accueil, pnj, evenement, soundDesign): # met à jour les éléments du jeu. Elle met à jour le groupe de sprites associé à la carte du jeu actuelle en appelant self.get_group().update(), ce qui met à jour les sprites du groupe. Ensuite, elle appelle self.check_collisions() pour vérifier les collisions des sprites avec les objets de la carte du jeu
        self.get_group().update()
        self.check_collisions(monde_reve, quete3, menu_quetes, accueil, pnj, evenement, soundDesign)