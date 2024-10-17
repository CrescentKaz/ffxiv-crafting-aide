
import raw_gathered_materials
import raw_hunted_materials



#carpenter 1
maple_lumber = [maple_log, maple_log, maple_log]
maple_clogs = maple_lumber

#blacksmith 1
bronze_ingot = [copper_ore, copper_ore, tin_ore]
bronze_hatchet = bronze_ingot + maple_lumber

#armorer 1
bronze_ingot = [copper_ore, copper_ore, tin_ore]

#goldsmith 1
copper_ingot = [copper_ore, copper_ore, copper_ore]

#leatherworker 1
leather = [animal_skin]
leather_calot = leather

#weaver 1
hempen_yarn = [moko_grass, moko_grass]

#alchemist 1
distilled_water = [muddy_water]
quicksilver = [cinnabar, cinnabar]

#culinarian 1
table_salt = [rock_salt]
maple_syrup = [maple_sap]



#carpenter 2
maple_shortbow = maple_lumber + hempen_yarn

#blacksmith 2
bronze_bastard_sword = bronze_ingot + maple_lumber + [bone_chip]
amateurs_file = bronze_ingot + bronze_ingot + leather

#armor 2
bronze_rings = bronze_ingot
bronze_rivets = bronze_ingot

#goldsmith 2
bone_hora = [bone_chip, bone_chip, animal_sinew]

#leatherworker 2
leather_wristguards = leather + [animal_sinew]
leather_duckbills = leather + undyed_hempen_cloth

#weaver 2
undyed_hempen_cloth = hempen_yarn
hempen_halfgloves = undyed_hempen_cloth + hempen_yarn
hempen_underpants = undyed_hempen_cloth + hempen_yarn
hempen_pantalettes = undyed_hempen_cloth + hempen_yarn

#alchemist 2
animal_glue = [animal_skin, bone_chip, bone_chip]

#culinarian 2
maple_sugar = maple_syrup



#carpenter 3
bone_harpoon = maple_lumber + [bone_chip] + animal_glue

#blacksmith 3
bronze_rivets = bronze_ingot
bronze_war_axe = bronze_ingot + bronze_ingot + maple_lumber
amateurs_pliers = bronze_ingot + bronze_rivets + fish_oil

#armor 3
bronze_plate = bronze_ingot + bronze_ingot
bronze_alembic = bronze_plate + bronze_rivets

#goldsmith 3
bone_brand = [marbled_eye, bone_chip]

#leatherworker 3
leahter_duckbills_of_gathering = leather + undyed_hempen_cloth

#weaver 3
hempen_coif = undyed_hempen_cloth + hempen_yarn + leather
hempen_undershirt = undyed_hempen_cloth + undyed_hempen_cloth + hempen_yarn
hempen_camise = undyed_hempen_cloth + undyed_hempen_cloth + hempen_yarn
hempen_breeches_of_crafting = undyed_hempen_cloth + undyed_hempen_cloth + hempen_yarn + leather

#alchemist 3
growth_formula_alpha = quicksilver + [shriekshroom, rock_salt]

#culinarian 3
raisins = [lowland_grapes]
boiled_egg = [chicken_egg, mineral_water]



#carpenter 4
amateurs_grinding_wheel = maple_lumber + bronze_ingot + [ragstone]
maple_pattens = maple_lumber + undyed_hempen_cloth + leather

#blacksmith 4
bronze_saw = bronze_ingot + bronze_rivets + maple_lumber
amateurs_awl = bronze_ingot + maple_lumber + fish_oil

#armor 4
bronze_skillet = bronze_plate + maple_lumber

#goldsmith 4
copper_rings = copper_ingot

#leatherworker 4
leather_eyepatch = leather + [animal_sinew] + hempen_yarn
fingerless_leather_gloves = leather + leather + bronze_rivets
leather_shoes = leather + [animal_sinew] + rubber

#weaver 4
hempen_coif_of_gathering = undyed_hempen_cloth + hempen_yarn + leather
hempen_kurta = undyed_hempen_cloth + undyed_hempen_cloth + undyed_hempen_cloth + hempen_yarn
hempen_dalmatica = undyed_hempen_cloth + undyed_hempen_cloth + hempen_yarn + [animal_sinew]
hempen_shepherds_slops = undyed_hempen_cloth + undyed_hempen_cloth + leather + [animal_sinew]
hempen_breeches = undyed_hempen_cloth + undyed_hempen_cloth + hempen_yarn + leather

#alchemist 4
enchanted_copper_ink = [copper_sand, copper_sand, beastkin_blood]
maple_wand = growth_formula_alpha + [maple_branch]

#culinarian 4
rye_flour = [rye, rye, rye]
honey = [beehive_chip, beehive_chip, beehive_chip]
frumenty = raisins + honey + [sunset_wheat, aldgoat_milk, cinnamon]



#carpenter 5
amateurs_spinning_wheel = maple_lumber + maple_lumber + bronze_rivets + bronze_rivets
square_maple_shield = maple_lumber + bronze_rivets + bronze_rivets

#blacksmith 5
bronze_daggers = bronze_ingot + bronze_ingot + maple_lumber + [bone_chip]
amateurs_claw_hammer = bronze_ingot + maple_lumber + fish_oil
bronze_cross_pein_hammer = bronze_ingot + undyed_hempen_cloth + maple_lumber
bronze_doming_hammer = bronze_ingot + maple_lumber

#armor 5
bronze_hoplon = bronze_plate + bronze_plate + maple_lumber

#goldsmith 5
bone_staff = [marbled_eye, soiled_femur, bone_chip]
copper_gorget = copper_ingot + copper_ingot + leather
copper_wristlets = copper_ingot + copper_rings + copper_rings

#leatherworker 5
leather_culottes = leather + leather + undyed_hempen_cloth + undyed_hempen_cloth
leather_crakows = leather + bronze_ingot + [animal_sinew] + rubber
altered_thightboots = leather + bronze_ingot + [animal_sinew] + rubber
leather_choker = leahter + [animal_sinew]

#weaver 5
hempen_bandana = undyed_hempen_cloth + undyed_hempen_cloth + undyed_hempen_cloth
hempen_tunic = undyed_hempen_cloth + undyed_hempen_cloth + hempen_yarn + leather
hempen_dalmatica_of_gathering = undyed_hempen_cloth + undyed_hempen_cloth + hempen_yarn + [animal_sinew]
hempen_cowl = undyed_hempen_cloth + undyed_hempen_cloth + undyed_hempen_cloth + undyed_hempen_cloth + hempen_yarn
hempen_sarouel = undyed_hempen_cloth + hempen_yarn + leather + [animal_sinew]
hempen_chausses = undyed_hempen_cloth + undyed_hempen_cloth + undyed_hempen_cloth + hempen_yarn
hempen_tights = undyed_hempen_cloth + undyed_hempen_cloth + hempen_yarn

#alchemist 5
leather_grimoire = enchanted_copper_ink + leather + hempen_yarn + [maple_log]
antidote = [rock_salt, grass_viper]

#culinarian 5
fish_meal = [lominsan_anchovy, lominsan_anchovy, lominsan_anchovy]
crayfish_ball = rye_flour + [crayfish, crayfish, crayfish]
#inserting one culinarian 11 recipe here
olive_oil = [cinderfoot_olive, cinderfoot_olive, cinderfoot_olive, cinderfoot_olive]
battered_fish = olive_oil + table_salt + [haddock, popoto]
rolanberry_shaved_ice = maple_syrup + [mineral_water, rolanberry, buffalo_milk]
flatbread = rye_flour + table_salt + [mineral_water]
marmot_steak = [marmot_meat, wild_onion, garlean_garlic]
grilled_trout = table_salt + [princess_trout]



#carpenter 6-10
bronze_spear = [maple_lumber, fish_oil, bronze_ingot]
maple_cane = [maple_lumber, growth_formula_alpha]
maple_longbow = [maple_lumber, maple_branch, hempen_yarn]
maple_crook = [maple_lumber, beastkin_blood]
maple_fishing_rod = [maple_lumber, maple_branch, bronze_ingot]
plumed_maple_shortbow = [maple_shortbow, maple_branch, cock_feather]
round_shield = [maple_lumber, bronze_rivets, bronze_rivets, bronze_ingot]
ash_lumber = [ash_log, ash_log, ash_log]
ash_macuahuitl = [ash_log, obsidian]
ramhorn_harpoon = [ash_lumber, ram_horn]

#blacksmith 6-10
amateurs_mortar = [bronze_ingot, bronze_ingot, maple_lumber]
amateurs_culunary_knife = [bronze_ingot, maple_lumber, ragstone_whetstone]
viking_sword = [bronze_ingot, leather, bone_chip]
bronze_labrys = [bronze_ingot, bronze_ingot, maple_lumber]
bronze_chaser_hammer = [bronze_ingot, bronze_rivets, maple_lumber]
bronze_knives = [bronze_ingot, bronze_ingot, maple_lumber]
bronze_head_knife = [bronze_ingot, maple_lumber, ragstone_whetstone]
bronze_pickaxe = [bronze_ingot, undyed_hempen_cloth, maple_lumber]
cloud_axe = [bronze_war_axe, bronze_ingot]
bronze_claw_hammer = [bronze_ingot, maple_lumber, fish_oil]
bronze_baselards = [bronze_ingot, bronze_ingot, maple_lumber]
amateurs_cross_pein_hammer = [bronze_ingot, undyed_hempen_cloth, ash_lumber]
bronze_file = [bronze_ingot, bronze_ingot, hard_leather]
bronze_pliers = [bronze_ingot, bronze_rivets, clove_oil]
amateurs_chaser_hammer = [bronze_ingot, bronze_rivet, ash_lumber]
bronze_mortar = [bronze_ingot, bronze_ingot, ash_lumber]

#armorer 6-10
bronze_haubergeon = [bronze_rings, bronze_rings, bronze_rings, undyed_hempen_cloth]
bronze_sollerets = [bronze_plate, bronze_rings, leather]
bronze_chain_coif = [bronze_plate, bronze_rings, leather]
bronze_sallet = [bronze_plate, bronze_ingot, bronze_rivets]
amateurs_alembic = [bronze_plate, bronze_rivets, copper_ingot]
bronze_mitt_gauntlets = [bronze_plate, bronze_rivets, leather]
bronze_scutum = [bronze_plate, bronze_plate, bronze_rivets, bronze_rivets, bronze_rivets]
bronze_barbut = [bronze_plate, bronze_rivets, copper_ingot]



