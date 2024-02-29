# ----- 코드 정의 ------
class Member:
    def __init__(self,name,username,password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"Name:, {self.name}, Username: {self.username}")
        pass


class Post:
    def __init__(self,title,content,author):
        self.title = title
        self.content = content
        self.author = author
    pass


# ----- 코드 실행 ------
members = []
mem1 = members.append( 'Doyeon','dy23','0915')
mem2 = members.append('Jaeho','Jh02','0916')
mem3 = members.append('Bumjin','Bj01','0917')
print('members')

posts = []

# TODO : 코드 구현이 필요합니다.