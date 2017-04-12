from .distributorProfile import DistributorProfile
from .administratorProfile import AdministratorProfile
from .baseProfile import BaseProfile

class Profile(DistributorProfile, AdministratorProfile, BaseProfile):
	pass

	def is_distributor(self):
		if self.user_type == 1:
			return True
		else:
			return False

	def is_administrator(self):
		if self.user_type == 0:
			return True
		else:
			return False