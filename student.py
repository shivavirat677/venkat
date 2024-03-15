tel=float(input("enter telugu subject marks:"))
eng=float(input("enter english subject marks:"))
phy=float(input("enter maths subject marks:"))
mat=float(input("enter physics subject marks:"))
com=float(input("enter computer subject marks:"))
print("\n\n\n-------------------------------------")
print("\n\n student scored subject marks")
print("\n the telugu subject marks are:",tel)
print("\n the english subject marks are:",eng)
print("\n the maths subject marks are:",mat)
print("\n the physics subject marks are:",phy)
print("\n the computer subject marks are:",com)
print("\n\n------------------------------------------")
print("\n\n\n Total marks")
tot=tel+eng+phy+mat+com
print("\n the total subject marks are:",tot)
avg=tot/6
print("\n the average marks are:",avg)
print("\n\n\n-----------------------------------------")
print("\n\n highest marks in given subjects")
if(tel>eng and tel>mat and tel>phy and tel>com):
    print("\n the telugu subject marks  are highest in all subjects",tel)
elif(eng>tel and eng>mat and eng>phy and eng>com):
    print("\n the english subject marks are highest in all subjects",eng)
elif(mat>tel and mat>eng and mat>phy and mat>com):
    print("\n the maths subject marks are highest in all subjects",mat)
elif(phy>tel and phy>mat and phy>eng and phy>com):
    print("\n the physics subject marks are highest in all subjects",phy)
elif(com>tel and com>eng and com>mat and com>phy):
    print("\n the cmputer subject marks are highest in all subjects",com)
print("\n\n\n-----------------------------------------")
print("\n\n lowest marks in given subjects")
if(tel<eng and tel<mat and tel<phy and tel<com):
    print("\n the telugu subject marks  are lowest in all subjects",tel)
elif(eng<tel and eng<mat and eng<phy and eng<com):
    print("\n the english subject marks are lowest in all subjects",eng)
elif(mat<tel and mat<eng and mat<phy and mat<com):
    print("\n the maths subject marks are lowest  in all subjects",mat)
elif(phy<tel and phy<mat and phy<eng and phy<com):
    print("\n the physics subject marks are lowest in all subjects",phy)
elif(com<tel and com<eng and com<mat and com<phy):
    print("\n the computer subject marks are lowest in all subjects",com)
print("\n\n\n-----------------------------------------")
print("\n\n failed subjects")
if(tel<35):
    print("\n telugu is failed",tel)
if(eng<35):
    print("\n english is failed",eng)
if(mat<35):
    print("\n maths is failed",mat)
if(phy<35):
    print("\n physics is failed",phy)
if(com<35):
    print("\n computer is failed",com)


    



