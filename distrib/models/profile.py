from .distributorProfile import DistributorProfile
from .administratorProfile import AdministratorProfile
from .baseProfile import BaseProfile

class Profile(DistributorProfile, AdministratorProfile, BaseProfile):
	pass