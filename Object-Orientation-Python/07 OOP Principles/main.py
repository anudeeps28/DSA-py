from keyboard_local import Keyboard

item1 = Keyboard("jscKeyboard", 1000, 3)
print(f'Before Discount:', item1.price)
item1.apply_discount()
print(f'After Dicsount:', item1.price)
