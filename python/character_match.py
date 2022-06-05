# Don't forget to run your tests!
def is_character_match(string1, string2):
	
 string1 = string1.lower().replace(" ","")
 string2 = string2.lower().replace(" ","")
 new_str_1 = []
 new_str_2 = []
    
 for x in string1:
     new_str_1.append(x)
 for y in string2:
     new_str_2.append(y)
        
 new_str_1.sort()
 new_str_2.sort()
 string_one = "".join(new_str_1)
 string_two = "".join(new_str_2)
    
 if string_one == string_two:
     return True
 else:
     return False