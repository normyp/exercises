import user

paul_admin = user.Admin("Paul", "Normington", "pw123", "black")
paul_admin.privileges.show_privileges()

user_privileges = [
    "can delete users"
]

paul_admin.privileges.privileges = user_privileges
paul_admin.privileges.show_privileges()
