# Method 1 import entire package.module. use entire package.module.function
# import ecommerce.shipping
#
# ecommerce.shipping.cal_shipping()

# Method 2 import required function
# from ecommerce.shipping import cal_shipping
#
# cal_shipping()

# Method 3 import required module. use only module.function
from ecommerce import shipping

shipping.cal_shipping()
