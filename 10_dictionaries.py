menu={}
menu["ice cream"]=21
menu["fruit"]=10
menu["soup"]=33

print "there are %d items in menu" %(len(menu))
print menu

#deleting an item from dict
del menu["fruit"]
print "deleted fruit item"
print menu
