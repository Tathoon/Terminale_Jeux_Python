from dataclasses import dataclass
import pygame, pytmx, pyscroll

@dataclass # à comprendre pour plus tard (une classe de constructeur en gros)
class Portal:
    from_world: str
    origin_point: str
    target_world: str
    teleport_point: str

@dataclass # à comprendre pour plus tard (une classe de constructeur en gros)
class Map:
    name: str
    walls: list[pygame.Rect]
    group: pyscroll.PyscrollGroup # a verifier
    tmx_data: pytmx.TiledMap # element a charger
    portals: list[Portal]

class MapManager:

    def __init__(self, mainScreen, player):
        self.maps = dict() # house -> Map("house", walls, group)
        self.screen = mainScreen
        self.player = player
        self.current_map = "MapV1"

        self.register_map("MapV1", portals=[
            Portal(from_world="MapV1", origin_point="mapportal", target_world="house1", teleport_point="tpmaison"),
            Portal(from_world="MapV1", origin_point="enter_dungeon", target_world="dungeon", teleport_point="spawn_dungeon")
        ])

        self.register_map("house1", portals=[
            Portal(from_world="house1", origin_point="maisonportal", target_world="MapV1", teleport_point="player")
        ])

        self.register_map("dungeon", portals=[
            Portal(from_world="dungeon", origin_point="exit_dungeon", target_world="MapV1", teleport_point="dungeon_exit_spawn")
        ])

        self.teleport_player("player")

    def check_collisions(self):
        # portails
        for portal in self.get_map().portals:
            if portal.from_world == self.current_map:
                point = self.get_object(portal.origin_point)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)

                if self.player.feet.colliderect(rect):
                    copy_portal = portal
                    self.current_map = portal.target_world
                    self.teleport_player(copy_portal.teleport_point)

        # collisions
        for sprite in self.get_group().sprites():
            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()

    def teleport_player(self, name):
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def register_map(self, name, portals=[]):
        
        # charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame(f"assets_monde_reve/map/{name}.tmx") # à verifier pour le f (en gros c'est pour utiliser des variables)
        map_data = pyscroll.data.TiledMapData(tmx_data) # verifier ce que ca fait
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size()) # verifier aussi
        map_layer.zoom = 1.5
    
        # definir une liste qui va stocker les rectangles de collisions
        walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de calques
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        group.add(self.player) # à revoir cette parti

        # creer un objet Map
        self.maps[name] = Map(name, walls, group, tmx_data, portals)

    def get_map(self): return self.maps[self.current_map]

    def get_group(self): return self.get_map().group # verifier les groups

    def get_walls(self): return self.get_map().walls

    def get_object(self, name): return self.get_map().tmx_data.get_object_by_name(name)

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self):
        self.get_group().update()
        self.check_collisions()