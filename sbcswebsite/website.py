# Ensure all the stuff gets initialized, since views 
# for example aren't explicitely depended on by anyone
from sbcswebsite.application import app as application
import sbcswebsite.models
import sbcswebsite.views

