class school:
	def __init__(self,lesson,class_size,branch,teacher,class_name):
		self.branch = branch
		self.lesson = lesson
		self.class_name = class_name
		self.class_size = class_size
		self.teacher = teacher

	def show_info(self):
		print("-"*25)
		print("İnformation of class: ")
		print("Lesson:{}\nClass:{}\nClass Size:{}\nTeacher{}".format(self.lesson,self.class_name,self.class_size,self.teacher))
		print("-"*25)

	def change_lesson(self):
			new_lesson = input("please wrtite the new lesson:")
			print("*** Old Lesson ***",self.lesson)
			self.lesson = new_lesson
			print("-"*25)
			print("İnformation of class: ")
			print("Lesson:{}\nClass:{}\nClass Size:{}\nTeacher{}".format(self.lesson,self.class_name,self.class_size,self.teacher))
			print("-"*25)


class school_manager(school):
		print("Manager Panel")

		def __init__(self,lesson,class_size,branch,teacher,class_name,fund):
			super().__init__(lesson,class_size,branch,teacher,class_name)
			self.fund = fund

		def show_info(self):
				print("-"*25)
				print("İnformation of class: ")
				print(self.lesson)
				print("Lesson:{}\nClass:{}\nClass Size:{}\nTeacher:{}\nFund:{}".format(self.lesson,self.class_name,self.class_size,self.teacher,self.fund))
				print("-"*25)

manager = school_manager("computer","15","computer","Samet Yıldırım","17","250")
manager.show_info()