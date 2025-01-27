import random
import sys

version = "idle"
try:
    color = sys.stdout.shell
except AttributeError:
    version = "shell"

#Start Color Variables
White="SYNC"
White2="stdin"
Purple="BUILTIN"
Green="STRING"
Orange="console"
Red="COMMENT"
Aqua="stdout"
White3="TODO"
Pink="stderr"
HighlightWhite="hit"
Blue="DEFINITION"
Rose="KEYWORD"
HighlightPink="ERROR"
HighlightGrey="sel"
#End Color Variables

def prRed(skk): print("\033[91m{}\033[00m" .format(skk),end="\t")
 
 
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk))
 
 
def prYellow(skk): print("\033[93m{}\033[00m" .format(skk), end="\t")
 
 
def prLightPurple(skk): print("\033[94m{}\033[00m" .format(skk))


def check_horizontals(nums, removednums, existings):
    count = 0
    for i in range(5):
        list_to_check = set(nums[i*5:(i+1)*5])
        if list_to_check.issubset(removednums) and not (list_to_check.issubset(existings)):
            existings.update(list_to_check)
            count = count + 1
    return count

def check_verticals(nums, removednums, existings):
    count = 0
    for i in range(5):
        list_to_check = set([nums[i],nums[i+5],nums[i+10],nums[i+15],nums[i+20]])
        if list_to_check.issubset(removednums) and not (list_to_check.issubset(existings)):
            existings.update(list_to_check)
            count = count + 1
    return count
            
def check_diags(nums, removednums, existings):
    count = 0
    list_to_check = set([nums[0], nums[6], nums[12], nums[18], nums[24]])
    if list_to_check.issubset(removednums) and not (list_to_check.issubset(existings)):
            existings.update(list_to_check)
            count = count + 1
    list_to_check = set([nums[4], nums[8], nums[12], nums[16], nums[20]])
    if list_to_check.issubset(removednums) and not (list_to_check.issubset(existings)):
            existings.update(list_to_check)
            count = count + 1
    return count

new_game = True
run_count = 0
bingo = ["B","I","N","G","O"]
if version == "idle":
    while True:
        if new_game:
            wincount = 0
            existings = set()
            numlist = [x for x in range(1,26)]
            random.shuffle(numlist)
            color.write("B\tI\tN\tG\tO\n",Green)
            print()
            for i in range(len(numlist)):
                if i%5 == 0 and i!=0:
                    print()
                    print()
                color.write(str(numlist[i])+"\t",Rose)
            print()
            print()
            new_game = False
            removed_nums = set()
            num_to_remove = 0
            try:
                num_to_remove = int(input("Which number to remove? "))
            except:
                pass
            if num_to_remove in numlist and num_to_remove not in removed_nums:
                removed_nums.add(num_to_remove)
            else:
                print("Invalid Input!!")
            if bool(removed_nums): #this checks if set is empty...casting to bool an empty set gives false
                print("Numbers Removed till Now: ",removed_nums)
            continue
        run_count+=1
        print()
        if wincount!=0:
            for i in range(wincount):
                color.write(bingo[i]+"\t",Red)
            color.write("\t".join(bingo[i+1:])+"\n", Green)
        else:
            color.write("B\tI\tN\tG\tO\n",Green)
        print()
        for i in range(len(numlist)):
            if i%5 == 0 and i!=0:
                print()
                print()
            if numlist[i] in removed_nums:
                color.write(str(numlist[i]),HighlightPink)
                color.write("\t",White)
                continue
            color.write(str(numlist[i])+"\t",Rose)
        print()
        print()

        if wincount == 5:
            color.write("BINGOOO!! You've won!\n", Purple)
            choice = input("Do you want to continue?(y/n): ")
            if choice.lower() == "y":
                new_game = True
                print()
                continue
            else:
                exit()
        
        try:
            num_to_remove = int(input("Which number to remove? "))
        except:
            pass
        if num_to_remove in numlist and num_to_remove not in removed_nums:
            removed_nums.add(num_to_remove)
        else:
            print("Invalid Input!!")
        if bool(removed_nums): #this checks if set is empty...casting to bool an empty set gives false
            print("Numbers Removed till Now: ",removed_nums)
        wincount += check_horizontals(numlist,removed_nums,existings)
        wincount += check_verticals(numlist,removed_nums,existings)
        wincount += check_diags(numlist,removed_nums,existings)

elif version == "shell":
    while True:
        if new_game:
            wincount = 0
            existings = set()
            numlist = [x for x in range(1,26)]
            random.shuffle(numlist)
            prGreen("B\tI\tN\tG\tO")
            print()
            for i in range(len(numlist)):
                if i%5 == 0 and i!=0:
                    print()
                    print()
                print(numlist[i],end="\t")
            print()
            print()
            new_game = False
            removed_nums = set()
            num_to_remove = 0
            try:
                num_to_remove = int(input("Which number to remove? "))
            except:
                pass
            if num_to_remove in numlist and num_to_remove not in removed_nums:
                removed_nums.add(num_to_remove)
            else:
                print("Invalid Input!!")
            if bool(removed_nums): #this checks if set is empty...casting to bool an empty set gives false
                print("Numbers Removed till Now: ",removed_nums)
            continue
        run_count+=1
        print()
        if wincount!=0:
            for i in range(wincount):
                prRed(bingo[i])
            prGreen("\t".join(bingo[i+1:]))
        else:
            prGreen("B\tI\tN\tG\tO")
        print()
        for i in range(len(numlist)):
            if i%5 == 0 and i!=0:
                print()
                print()
            if numlist[i] in removed_nums:
                prYellow(numlist[i])
                continue
            print(numlist[i],end="\t")
        print()
        print()

        if wincount == 5:
            prLightPurple("BINGOOO!! Congrats You've won! Here's a box of chocolates")
            print()
            choice = input("Do you want to continue?(y/n): ")
            if choice.lower() == "y":
                new_game = True
                print()
                continue
            else:
                exit()
        
        try:
            num_to_remove = int(input("Which number to remove? "))
        except:
            pass
        if num_to_remove in numlist and num_to_remove not in removed_nums:
            removed_nums.add(num_to_remove)
        else:
            print("Invalid Input!!")
        if bool(removed_nums): #this checks if set is empty...casting to bool an empty set gives false
            print("Numbers Removed till Now: ",removed_nums)
        wincount += check_horizontals(numlist,removed_nums,existings)
        wincount += check_verticals(numlist,removed_nums,existings)
        wincount += check_diags(numlist,removed_nums,existings)
    

