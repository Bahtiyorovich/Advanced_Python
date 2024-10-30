# Linked_list - bitta qiymat va keyingi qiymatga url saqlab turuvchi o'zgaruvchilar uchun konteyner

class Node:
    """ Node class - tugun obyekti"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """LinkedList obyekti"""
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def pushElement(self, new_data):
        """List boshiga tugun qo'shish"""
        # yangi node yaratish
        new_node = Node(new_data)
        # List boshini keyingi o'ringa surish
        new_node.next = self.head
        # Yangi nodeni list boshiga qo'yamiz
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        """Biror tugundan so'ng tugun qo'shish"""
        if prev_node is None:
            print("Tugun mavjud emas")
            return
        # yangi tugun qo'shamiz
        new_node = Node(new_data)
        # yangi tugunni keyingi tugunga bog'laymiz
        new_node.next = prev_node.next
        # Avvalgi tugunni yangi tugunga bog'laymiz
        prev_node.next = new_node



