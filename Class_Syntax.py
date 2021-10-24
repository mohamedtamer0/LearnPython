# Class_Syntax

# class Member:
#
#     def __init__(self):
#         print("Hello World")
#
#
# Member()

# -------------------------------------------

print("#" * 30)


class Member:
    not_allowed_names = ["Hell", "Shit", "Baloot"]
    users_num = 0

    @classmethod
    def show_users_count(cls):
        print(f"We have {cls.users_num} Users In Our System.")

    def __init__(self, firstName, lastName, gender):
        self.f_name = firstName
        self.l_name = lastName
        self.gender = gender

        Member.users_num += 1

    def full_name(self):
        if self.f_name in Member.not_allowed_names:
            raise ValueError("Name Not Allowed")
        else:
            return f"{self.f_name} {self.l_name}"

    def name_with_title(self):
        if self.gender == "Male":
            return f"Hello Mr {self.f_name}"

        elif self.gender == "Female":
            return f"Hello Miss {self.f_name}"


print(Member.users_num)
member_One = Member("Mohamed", "Tamer", "Male")
member_Two = Member("Habiba", "Tamer", "Female")
print(member_One.full_name())
print(member_One.name_with_title())
print(member_Two.full_name())
print(member_Two.name_with_title())
print(Member.users_num)
Member.show_users_count()
