import random



def create_spice_list():
    spice_list = [[], [], []]
    
    for i in range(2):
        total = 250
        for j in range(3):
            if j == 2:
               spice_list[i].append(total)
            elif total == 250:
                numb = random.randrange(130, 150, 10)
                spice_list[i].append(numb)
                total -= numb
            else:
                numb = random.randrange(10, 60, 10)
                total -= numb
                spice_list[i].append(numb)
    
    total = 250
    for i in range(4):
          if i == 3:
               spice_list[2].append(total)
          elif total == 250:
              numb = random.randrange(100, 150, 10)
              total -= numb
              spice_list[2].append(numb)
          else:
              numb = random.randrange(10, 70, 10)
              total -= numb
              spice_list[2].append(numb)
    
    new_spice_list = []
    for i in range(len(spice_list)):
        for j in spice_list[i]:
         new_spice_list.append(j)    
    spice_list = sorted(new_spice_list, reverse= True)
    return spice_list

def sort_boxes(spice_list):

    box_list = [[], [], []]

    for box in box_list[:2]:
        weight = 250
        new_list = spice_list

        for spice1 in spice_list:
            if not box:
                box.append(spice1)
                weight -= spice1
                new_list.remove(spice1)
            elif spice1 + sum(box) != 250:
                
                for spice2 in spice_list[1:]:
                    if spice1 + spice2 == weight:
                        box.append(spice1)
                        new_list.remove(spice1)
                        box.append(spice2)
                        new_list.remove(spice2)
                        weight -= spice1 + spice2
            
        spice_list = new_list
    box_list[2] = spice_list
    return box_list


def weigh_boxes(box_list):
    for box in range(len(box_list)):
        if sum(box_list[box]) == 250:
            return True
        else:
            print(f'Box {box} is incorrect weight')
            return False

        

    
   
    
            
         
    




               


          
     

     
                              
               
               
                 
                    



               
               
               




    
     

