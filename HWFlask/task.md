створити класи
base:

Room(base)
- name (str)
- capacity (int)

User(base)
- firstname (str)
- lastname (str)
- age (int)

Teacher(User)
- position (str)

Group (base)
- name (str)
- members (list(User))

Sheduler (base)
- room ()
- lesson (Lesson)
- group (Group)
- para (1,2,3 int)


create, str
створити сторінки для створення цих обєктів
і для їх перегляду
і для перегляду списку 