from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

r_entrance = Room(title="Entrance", description="""You stand near a big archway. There is a waterfall to the east, a desert to your south, a volcano in the west, and the castle stands tall up north.""")

r_desert = Room(title="Desert", description="""Big stretches of barren sand surround you, but you see sandy hills in the far east and many tall dust devils to your west.""")

r_dust_devil = Room(title="Dust Devil Country", description="""You are surrounded by huge pillars of dust. This is too dangerous, you must head back.""")

r_sandyhills = Room(title="Sandy Hills", description="""You stand on top of a large sandhill. There is nothing for miles, but you see some old abandoned crates in the east.""")

r_treasury = Room(title='Treasury', description="""Mountains of gold and jewels gleam before you. Finders keepers, amirite?""")

r_crates = Room(title="Abandoned Crates", description="""Mountains of gold and jewels gleam before you. Finders keepers, amirite?""")

r_waterfall = Room(title='Waterfall', description="""You find yourself alongside a large blue waterfall that turns into a river that heads north, you also see a small cave to your east.""")

r_river = Room(title='River', description="""As you follow the river you notice the water changes direction headed east. Thick jungle surrounds the river blocking travel to the north and west.""")

r_rapids = Room(title='Rapids', description="""The water has started to speed up now. It looks dangerous to continue this way. You should head back.""")

r_cave = Room(title='Cave', description="""Inside the cave you find a small pool lit up by a bright blue orb. It looks valuable, maybe you should take it.""")

r_castle = Room(title='Castle', description="""As you enter the castle you notice it is empty. Although, a torch lights a path to a chamber in the north.""")

r_chamber = Room(title='Chamber', description="""LOCKED: The chamber doors are locked but you hear faint laughs behind the door.""")

r_volcano = Room(title='Volcano', description="""As you approach the volcano it billows smoke, but you notice a grand obsidian doorway in the west and a small flight of stairs leading to the top in the north.""")

r_obsidianDoorway = Room(title='Obsidian Doorway', description="""UNLOCKED: You place the red, blue, and green orbs in the imprints and the door opens. You find yourself looking at a small pedestal with a brass key laying on it.""")

r_stairs = Room(title='Stairs', description="""As you ascend the stairs you notice a tiny black chest sitting near the east wall.""")

r_chest = Room(title='Chest', description="""The chest is unlocked. As it opens intense red light fills the room. Sitting inside is a mysterious red orb. It looks valuable, maybe you should take it. """)


for room in [r_entrance, r_desert, r_dust_devil, r_sandyhills, r_treasury,
             r_crates, r_waterfall, r_river, r_rapids, r_cave, r_castle,
             r_chamber, r_volcano, r_obsidianDoorway, r_stairs, r_chest]:
             room.save()

# Link rooms together
r_chest.connectRooms(r_stairs, 'e')

r_stairs.connectRooms(r_chest, 'w')
r_stairs.connectRooms(r_volcano, 's')

r_volcano.connectRooms(r_obsidianDoorway, 'w')
r_volcano.connectRooms(r_stairs, 'n')
r_volcano.connectRooms(r_entrance, 'e')

r_obsidianDoorway.connectRooms(r_volcano, 'e')

r_entrance.connectRooms(r_desert, "s")
r_entrance.connectRooms(r_volcano, 'w')
r_entrance.connectRooms(r_castle, 'n')
r_entrance.connectRooms(r_waterfall, 'e')

r_desert.connectRooms(r_entrance, "n")
r_desert.connectRooms(r_dust_devil, "w")
r_desert.connectRooms(r_sandyhills, "e")

r_waterfall.connectRooms(r_river, 'n')
r_waterfall.connectRooms(r_entrance, 'w')
r_waterfall.connectRooms(r_cave, 'e')

r_cave.connectRooms(r_waterfall, 'w')

r_river.connectRooms(r_waterfall, 's')
r_river.connectRooms(r_rapids, 'e')

r_castle.connectRooms(r_chamber, 'n')
r_castle.connectRooms(r_entrance, 's')

r_rapids.connectRooms(r_river, 'w')

r_dust_devil.connectRooms(r_desert, "s")

r_sandyhills.connectRooms(r_desert, "w")
r_sandyhills.connectRooms(r_crates, "e")

r_treasury.connectRooms(r_chamber, "w")

r_crates.connectRooms(r_sandyhills, 'w')

players=Player.objects.all()
for p in players:
    p.currentRoom=r_entrance.id
    p.save()
