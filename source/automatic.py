from audit import audit


def automatic_decision(scenario):
    # *** YOUR CODE GOES HERE ***
    passengers = scenario.getPassengers()
    pedestrians = scenario.getPedestrians()
    
    pass_human = 0
    pass_child = 0
    pass_adult = 0
    
    pedest_human = 0
    pedest_child = 0
    pedest_adult = 0
    
    for i in passengers:
        if(i.getCharType() == "human"):
            pass_human += 1
        if(i.getAge() == "baby" or i.getAge() == "child"):
            pass_human += 2
        if(i.getAge() == "adult"):
            pass_human += 1
        if(i.isPregnant()):
            pass_human += 2
        if(i.isCriminal()):
            pass_human -= 1
        
        
    
    for i in pedestrians:
        if(i.getCharType() == "human"):
            pedest_human += 1
        if(i.getAge() == "baby" or i.getAge() == "child"):
            pedest_human += 2
        if(i.getAge() == "adult"):
            pedest_human += 1
        if(i.isPregnant()):
            pedest_human += 2
        if(i.isCriminal()):
            pedest_human -= 1
    
    if(pass_human >= pedest_human):
        return "passengers"
    else:
        return "pedestrians"
    

    # default to saving the passengers
    return "passengers" 

if __name__ == '__main__':
    audit(automatic_decision, 60, seed=8675309)
