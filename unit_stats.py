""" This entire thing should be a dictionary?"""
def unit_stats():
    
    card_info_list = [[100,25,2,10,7,5, 50,0,0,155,122,0, "elf"], 
                      [250,50,1,7,13,10,200,0,0,155,122,0, "santa"], 
                      [25,20,3,5,3,7,25,0,0,155,122,0, "reindeer"], 
                      [15,13,17,3,35,0,0,155,122,0,"snow"],
                      [20,25,22,2,35,0,0,155,122,0,"fire"],
                      [50,45,40,1,35,0,0,155,122,0, "lightning"], 
                      [100,2,25,0,0,155,122,0,"wood"],
                      [325,7,70,0,0,155,122,0,"fence"],
                      [1000,25,200,0,0,155,122,0,"castle"], 
                      ["Mana", 400, 0, 300,0,0,155,122,0, "mine"], 
                      ["Fence", 400, 0, 350,0,0,155,122,0, "factory"], 
                      ["Elf", 400, 0, 500,0,0,155,122,0, "northpole"]]
    return card_info_list

# Unit: health, damage, speed, ice_resistance, fire_resistance, lightning_resistance, cost, x, y, pix_x, pix_y, p_designation, name	

#Spell: elf_caster, santa_caster, reindeer_caster, duration, cost, x, y, pix_x, pix_y, p_designation, name	 

#Defense health, damage, cost, x, y, pix_x, pix_y, p_designation, name 	

# Production production_type, health, pro_rate, cost, x, y, pix_x, pix_y, name 
