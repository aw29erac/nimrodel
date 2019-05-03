from PyAPI import *

# all our api will be accessible under /coolapi
thebestapi = API(path="coolapi")

# we make instances of this class available under the path /coolapi/hero
@thebestapi.apiclass("hero")
class Hero:
	def __init__(self,name,friend,enemy):
		self.name = name
		self.friend = friend
		self.enemy = enemy
		# we define how the object's url string is determined - it will be accessible under /coolapi/hero/thisname
		self.__apiname__ = name.lower().replace(" ","")

	# and finally the method calls - this will be accessible under /coolapi/hero/instancename/hello
	@thebestapi.get("hello")
	def hi(self):
		return self.name + " bids thee welcome!"

	# if the method takes any arguments, they can be passed with URI arguments:
	@thebestapi.get("victory")
	def victory(self,weapon):
		return self.name + " defeats " + self.enemy + " with a " + weapon + "!"

	# of course this also works with arbitrary argument lists
	@thebestapi.get("party")
	def party(self,**kwargs):
		return self.name + " leads a party on a great quest. It consists of: "\
			+ ", ".join(kwargs[k] + " as the " + k.capitalize() for k in kwargs)

	# dictionaries are simply returned as json objects
	@thebestapi.get("info")
	def info(self):
		return {"name":self.name,"friend":self.friend,"enemy":self.enemy}




a = Hero("Finrod Felagund","Barahir","Werewolf")
b = Hero("Turin","Beleg","Glaurung")
c = Hero("Galadriel","Melian","Fëanor")

'''
Try out:

HTTP GET /coolapi/hero/turin/victory?weapon=sword
HTTP GET /coolapi/hero/finrodfelagund/party?ranger=Aegnor&archer=Angrod&healer=Galadriel
HTTP GET /coolapi/hero/galadriel/info
'''
