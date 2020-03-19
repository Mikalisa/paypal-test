from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()

mail = Mail()


message = """


Divaexplorer Order Summary

Date: Jan 16, 2020 07:17:58 PM

Dear Sharon,

Thank you for choosing Divaexplorer. Here's a summary of your order.

Order Details

Order Date:	 	Jan 16, 2020 07:17:55 PM              Payment Source:	 	Paypal
Transaction ID:	 	59806382                          Initial Charge:	 	$14.96
User Name:	 	mikalissa                             Final Cost:	 	    $14.96                      
                                                      Item Type:

													  TOTAL	$14.96 

For any concern. Please Contact us via divaexplorer@divaexplorer-tvj.co.uk.


Regards,
Team Divaexplorer
https://www.divaexplorer-tvj.co.uk/

London, UK


"""


message = """Payment recieved from a customer. 
        name: %s
        email: <%s>
        payment status: %s
        Price paid: %s
        """