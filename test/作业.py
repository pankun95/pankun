

# # 1.定义一个登录的测试用例类Case
# # 属性：用例名称、期望结果,输入的用户名和密码
# # 方法：调用LoginApi中的login方法，比对期望结果和实际结果
class LoginApi():
      def __init__(self,username,password):
          self.username=username
          self.password=password

      def login(self,username="pankun",password="123456"):
          if self.username == username and self.password == password:
              return "登录成功"
          else:
              return "登录失败"

class test_case():
    def __init__(self,casename,username,password,expect_result):
        self.casename=casename
        self.username=username
        self.password=password
        self.expect_result=expect_result

    def run_case(self):
        login_res=LoginApi(self.username,self.password).login()
        if login_res==self.expect_result:
            print("测试用例通过")
        else:
            print("测试用例不通过")

# test_case("正确账号，正确密码，登录成功","pankun","123456","登录成功").run_case()
# test_case("正确账号，错误密码，登录失败","pankun","3456","登录成功").run_case()




# 2.封装一个学生类Student
# 属性：姓名、年龄、性别、英语成绩、数学成绩、语文成绩
# 实现3个方法：
#     1.计算三科总分；
#     2.计算三科平均分；
#     3.打印学生的学生的个人信息：姓名、年龄、性别、英语成绩、数学成绩、语文成绩，总分、平均分
# 实例化一个学生，打印学生个人信息

class student():
    def __init__(self,name,age,sex,english_score,math_score,chinese_score):
        self.name=name
        self.age=age
        self.sex=sex
        self.english_score=english_score
        self.math_score = math_score
        self.chinese_score = chinese_score
    # 计算总成绩
    def total_grade(self,english_score,math_score,chinese_score):
        totalgrade=self.english_score+self.math_score+self.chinese_score
        return totalgrade

    # 计算平均成绩
    def avg_grade(self,english_score,math_score,chinese_score):
        avggrade=(self.english_score+self.math_score+self.chinese_score)/3
        return avggrade

    # 打印学生信息
    def print_individual_info(self,name,age,sex,english_score,math_score,chinese_score):
        individual_info=[{"姓名":name},{"年龄":age},{"性别":sex},{"英语成绩":english_score},{"数学成绩":math_score},{"语文成绩":chinese_score}]
        individual_info1={"总分":self.total_grade(english_score,math_score,chinese_score)}
        individual_info2={"平均成绩":self.avg_grade(english_score,math_score,chinese_score)}
        individual_info.append(individual_info1)
        individual_info.append(individual_info2)
        return individual_info


# 计算总成绩
# xiaoming=student("xiaoming",18,"male",english_score=60,math_score=60,chinese_score=60)
# res=xiaoming.total_grade(english_score=60,math_score=60,chinese_score=60)
# print(res)
# 计算平均成绩
# xiaohong=student("xiaohong",20,"female",english_score=75,math_score=100,chinese_score=90)
# res1=xiaohong.avg_grade(english_score=75,math_score=100,chinese_score=90)
# print(res1)
# 打印学生的个人信息
# xiaozhang=student("xiaoming",18,"male",english_score=64,math_score=88,chinese_score=91)
# res2=xiaozhang.print_individual_info("xiaoming",18,"male",english_score=64,math_score=88,chinese_score=91)
# print(res2)

# 学习time模块，完成以下内容：
# 1.函数，根据传入的位数，返回当前时间对应位数的时间戳。如传入位数13，返回13位的时间戳
# 2.函数，按照yyyy-MM-dd格式化当前时间，如调用函数后得到一个日期格式2022-07-31
# 3.函数，对当前日期或时间做加减法运算
#     如：
#         time_str = "2020-6-15"
#         time_str_s = "2020-6-15 15:23:21"
#
#         dateadd(time_str, -2, 'years') # 2018-06-15
#         dateadd(time_str, 3, 'months') # 2020-09-15
#         dateadd(time_str_s, 44, 'minutes') # 2020-06-15 16:07:21
#         dateadd(time_str_s, 1000, 'days') # 2023-03-12 15:23:21
#         dateadd(time_str_s, 3, 'weeks') # 2020-07-06 15:23:21
#         dateadd(time_str_s, -3, 'hours') # 2020-06-15 12:23:21
#         dateadd(time_str_s, 3, 'seconds') # 2020-06-15 15:23:24
# 4.函数，计算两个日期相差的天数
# 5.函数，计算某一年的总天数，输入年份，返回总天数

import time
from datetime import datetime,timedelta

class Today_time():
    def __init__(self,num,time_stamp,time_str,time_str3,year,day=None):
        self.num=num
        self.time_stamp=time_stamp
        self.time_str=time_str
        self.day=day
        self.time_str3=time_str3
        self.year=year

    # 如果num==time_stamp==13,就返回13位的时间戳。否则返回10位时间戳
    def get_time_stamp(self):
        if self.time_stamp==self.num==13:
            self.time_stamp=int(round(time.time()*1000))
            return self.time_stamp
        else:
            self.time_stamp=int(time.time())
            return self.time_stamp
    # 获取格式化时间，时间格式2022-07-31
    def get_stru_timestamp(self):
        strut_timestamp=(time.strftime("%Y-%m-%d"))
        return strut_timestamp
    # 当前日期相加
    def add_current_date(self):
        time_str1=self.time_str
        time_str1=datetime.strptime(time_str1,"%Y-%m-%d")
        time_str1=time_str1+timedelta(days=self.day)
        return time_str1
    # 当前日期相减
    def reduce_current_date(self):
        time_str2=self.time_str
        time_str2=datetime.strptime(time_str2,"%Y-%m-%d")
        time_str2=time_str2-timedelta(days=self.day)
        return time_str2
    # 计算2个日期相减
    def two_dates_reduce(self):
            time_str1 = self.time_str
            time_str3=self.time_str3
            time_str1 = datetime.strptime(time_str1, "%Y-%m-%d")
            time_str3 = datetime.strptime(time_str3, "%Y-%m-%d")
            result=time_str1-time_str3
            result1=result.days
            if result1>=0:
                return result1
            else:
                return "前面的日期要大于或等于后面的日期，否则不能相减 "
    # 计算某一年总共有多少天
    def year_total_days(self):
        start_day=str(self.year)+"-01-01"
        end_day=str(self.year)+"-12-31"
        year_days_num=(datetime.strptime(end_day,"%Y-%m-%d")-datetime.strptime(start_day,"%Y-%m-%d")).days+1
        return ("{}年一共{}天".format(self.year,year_days_num))






current_time=Today_time(13,456,"2022-07-21","2022-09-20",2019,1)
# res=current_time.get_time_stamp()
# print(res)
# res1=current_time.get_stru_timestamp()
# print(res1)
# res3=current_time.add_current_date()
# print(res3)
# res4=current_time.reduce_current_date()
# print(res4)
# res5=current_time.two_dates_reduce()
# print(res5)
res6=current_time.year_total_days()
print(res6)



# 选做：
# 选课系统：
# 角色:学校、学员、课程、讲师
# 要求:
# 1. 创建北京、上海 2 所学校
# 2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
# 3. 课程包含，周期，价格，通过学校创建课程
# 4. 通过学校创建班级， 班级关联课程、讲师
# 5. 创建学员时，选择学校，关联班级
# 5. 创建讲师角色时要关联学校，
# 6.1 学员视图， 可以注册， 交学费， 选择班级，
# 6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩
# 6.3 管理视图，创建讲师， 创建班级，创建课程


# class LoginApi():
#
#     def __init__(self,input_username,input_password):
#         self.username = input_username
#         self.password = input_password
#
#     def login(self,username='coco',password='1234'):
#         if self.username == username and self.password == password:
#             return '登录成功'
#         else:
#             return '用户名或密码错误'
#
# class Case:
#     def __init__(self,case_name,username,password,except_res):
#         self.case_name = case_name
#         self.username = username
#         self.password = password
#         self.except_res = except_res
#
#     def run_case(self):
#         login_res = LoginApi(self.username,self.password).login()
#         if login_res == self.except_res:
#             print('测试用例通过')
#         else:
#             print('测试用例不通过')

# Case('输入正确的用户名和密码-登录成功','coco','1234','登录成功').run_case()
# Case('输入正确的用户名和错误的密码-登录失败','coco','12345','用户名或密码错误').run_case()





