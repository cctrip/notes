#!/usr/bin/env python
# -*- coding: utf-8 -*-

#利用operator模块的attrgetter函数进行排序


from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
sorted_by_user_id = sorted(users, key=attrgetter('user_id'))
print(sorted_by_user_id)
