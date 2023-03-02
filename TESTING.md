# Testing


##  **Responsiveness**
- The project was responsive tested on https://ui.dev/amiresponsive and it is responsive for every type of devices such as desktop computers, laptops, tablets and smart phones.

![Am I Responsive](documentation/testing/amiresponsive02.jpg)

 No problem with responsiveness or any sort of visual issues were detected during testing the application on different popular browsers, such Google Chrome, Microsoft Edge, Avast Browser or Netbox Browser.

### Google Chrome:

 ![Google Chrome](documentation/testing/resp_chrome.jpg)

 ![Google Chrome](documentation/testing/resp_chrome_xs.jpg)

### Avast Browser:

 ![Google Chrome](documentation/testing/resp_avast.jpg)

 ![Google Chrome](documentation/testing/resp_avast_xs.jpg)

### Microsoft Edge:

 ![Google Chrome](documentation/testing/resp_edge.jpg)

 ![Google Chrome](documentation/testing/resp_edge_xs.jpg)

### Netbox Browser:

 ![Google Chrome](documentation/testing/resp_netbox.jpg)

 ![Google Chrome](documentation/testing/resp_netbox_xs.jpg)


### Mobile-size divices

Although the Page is working fine on most of the mobile devices such as tablets and mobile phones. Some visual issues are possible in very small screen sizes and horizontal screen position:
![Layout issue](documentation/bugs_and_errors/layout_issue01.jpg)

However the issues do not significantly affect the accessibility to application features, **it is recommended to use the vertical screen position on mobile divices.** 


## **Code Validator Testing**

- ### **HTML**

    Html code validation tests were made using Nu Html Checker on Google Chrome browser in incognito mode.
    No errors were detected during the tests.

    - Home Page:

        ![html_validation](documentation/testing/nu_home.jpg)

        Link to the test: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmood-design-gift-shop.herokuapp.com%2F

    - Shop Page:

        ![html_validation](documentation/testing/nu_shop.jpg)

        Link to the test: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmood-design-gift-shop.herokuapp.com%2Fproducts%2F

    - Workshop Page:

        ![html_validation](documentation/testing/nu_workshop.jpg)

        Link to the test: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmood-design-gift-shop.herokuapp.com%2Fproducts%2Fworkshop%2F

    - Product Details Page:

        Product on stock details Page.

        ![html_validation](documentation/testing/nu_detail_on_stock.jpg)

        Link to the test: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmood-design-gift-shop.herokuapp.com%2Fproducts%2Fproduct%2F9%2F#l148c7

        Out of Stock products details.

        ![html_validation](documentation/testing/nu_detail_out_of_stock.jpg)

        Link to the test: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmood-design-gift-shop.herokuapp.com%2Fproducts%2Fproduct%2F5%2F#l148c7

        No image (default image) Products details Page.

        ![html_validation](documentation/testing/nu_detail_default_image.jpg)

        Link to the test: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmood-design-gift-shop.herokuapp.com%2Fproducts%2Fproduct%2F7%2F#l148c7

    - Add Product Page:
    
        ![html_validation](documentation/testing/nu_addproduct.jpg)

        Link to the test: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmood-design-gift-shop.herokuapp.com%2Fproducts%2Fadd_product%2F#l148c7

    - Edit Product Page:
    
        ![html_validation](documentation/testing/nu_editproduct.jpg)

        Link to the test: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmood-design-gift-shop.herokuapp.com%2Fproducts%2Fedit_product%2F9%2F#l148c7

    - My Profile Page:

        ![html_validation](documentation/testing/nu_myprofile.jpg)

    - Basket Page:

        ![html_validation](documentation/testing/nu_basket.jpg)

        Link to the test: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmood-design-gift-shop.herokuapp.com%2Fbasket%2F#l148c7
    
    - Checkout Page:

        ![html_validation](documentation/testing/nu_checkout.jpg)

        Link to the test: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmood-design-gift-shop.herokuapp.com%2Fcheckout%2F#l148c7

    - Checkout Success Page:

        ![html_validation](documentation/testing/nu_checkout_success.jpg)

        Link to the test: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmood-design-gift-shop.herokuapp.com%2Fcheckout%2Fcheckout_success%2F69A91F635FB5451E8FC3946D7E970A66#l148c7

    - Register Page:

        ![html_validation](documentation/testing/nu_signup.jpg)

        Link to the test: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmood-design-gift-shop.herokuapp.com%2Faccounts%2Fsignup%2F#l148c7

    - Login Page:

        ![html_validation](documentation/testing/nu_login.jpg)

        Link to the test: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmood-design-gift-shop.herokuapp.com%2Faccounts%2Flogin%2F#l148c7

    - Logout Page:

        ![html_validation](documentation/testing/nu_logout.jpg)

        Link to the test: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fmood-design-gift-shop.herokuapp.com%2Faccounts%2Flogout%2F#l148c7

        

- ### **CSS**
    * No errors were detected when passing through the [jigsaw.w3 validator](https://jigsaw.w3.org/css-validator). 

    - base.css file

        ![css_validation](documentation/testing/w3c_base.jpg)
    
    - checkout.css file

        ![css_validation](documentation/testing/w3c_checkout.jpg)   
    

- ### **JAVASCRIPT**


   
    * I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.
    No errors were detected when passing through the jshint validator.

        ![js_validation](documentation/testing/jshint_checkout_stripe.jpg)

    * Also a function activating navbar tiles, nested in a JS block of code in the base.html file  doesn't contain any errors:

        ![js_validation](documentation/testing/jshint_base_navbaractivation.jpg)

- ### **PYTHON**

     No error detected when passing the following file through the CI Python Linter:

    - mood_design views.py:

        ![python_validation](documentation/testing/lin_mood_views.jpg)

    - mood_design urls.py:

        ![python_validation](documentation/testing/lin_mood_urls.jpg)

    - home views.py:

        ![python_validation](documentation/testing/lin_home_views.jpg)

    - home forms.py:

        ![python_validation](documentation/testing/lin_home_forms.jpg)

    - home urls.py:

        ![python_validation](documentation/testing/lin_home_urls.jpg)

    - products views.py:

        ![python_validation](documentation/testing/lin_products_views.jpg)

    - products forms.py:

        ![python_validation](documentation/testing/lin_product_forms.jpg)

    - products urls.py:

        ![python_validation](documentation/testing/lin_product_urls.jpg)

    - products admin.py:

        ![python_validation](documentation/testing/lin_product_admin.jpg)

    - profiles views.py:

        ![python_validation](documentation/testing/lin_profiles_views.jpg)

    - profiles forms.py:

        ![python_validation](documentation/testing/lin_profiles_forms.jpg)

    - profiles urls.py:

        ![python_validation](documentation/testing/lin_profiles_urls.jpg)

    - profiles views.py:

        ![python_validation](documentation/testing/lin_profiles_views.jpg)

    - basket views.py:

        ![python_validation](documentation/testing/lin_basket_views.jpg)

    - basket context.py:

        ![python_validation](documentation/testing/lin_basket_context.jpg)

    - checkout views.py:

        ![python_validation](documentation/testing/lin_checkout_views.jpg)

    - checkout forms.py:

        ![python_validation](documentation/testing/lin_checkout_forms.jpg)

    - checkout urls.py:

        Add checkout.urls

        ![python_validation](documentation/testing/lin_checkout_urls.jpg)

    - checkout admin.py:

        ![python_validation](documentation/testing/lin_checkout_admin.jpg)
   

## **Manual Testing**

Testing all the applications functionalities.

### **Add Product**

This function is available only for user registered as admin.
If an user logged in as regular user tries to access this function a warning message is displayed.
![Admin access only](documentation/testing/admin_only.jpg)

If any non-admin user tries to access this function he is redirected to the Sign In Page where he can Log in.
![Admin access only](documentation/testing/admin_only.jpg)

Steps:
* Go to the Shop Page
* Click "Add Item" button
* Fill up all the required fields. 
    ![Add Product](documentation/testing/add_product01.jpg)
* Add an image of the product otherwise a default image will be added to the product.
    ![Add Product](documentation/testing/add_product03.jpg)

Expected result:
* A confirmation toast box should be displayed
* A new product (Ceramic Shamrock) should appear on the page
    ![Add Product](documentation/testing/add_product02.jpg)

Although entering negative values is accepted by the application,

![Negative Value](documentation/testing/negative_value_workshop.jpg)

assigning a negative value to the products quantity will result with displaying the product as "Out Of Stock".

![Negative Value](documentation/testing/negative_value_workshop03.jpg)

![Negative Value](documentation/testing/negative_value_shop.jpg)

The quantity can be changed anytime by the admin user.

### **Edit Product**

This function available only for user registered as admin.
If an user logged in as regular user tries to access this function a warning message is displayed.
![Admin access only](documentation/testing/admin_only.jpg)

If any non-admin user tries to access this function he is redirected to the Sign In Page where he can Log in.
![Admin access only](documentation/testing/admin_only.jpg)

Steps:
* Go to the Shop Page
* Expand the Click menu and choose "Edit Item" option.
    ![Edit Product](documentation/testing/edit_product01.jpg)
* Fill up all the required fields. 
    ![Edit Product](documentation/testing/edit_product02.jpg)

Expected result:
* A confirmation toast box should be displayed
    ![Edit Product](documentation/testing/edit_product03.jpg)
* The products detail should be updated.

Although entering negative values is accepted by the application,

![Negative Value](documentation/testing/negative_value_workshop.jpg)

assigning a negative value to the products quantity will result with displaying the product as "Out Of Stock".

![Negative Value](documentation/testing/negative_value_workshop03.jpg)

The quantity can be changed anytime by the admin user.


### **Deleting Product**

This function available only for user registered as admin.
If an user logged in as regular user tries to access this function a warning message is displayed.
![Admin access only](documentation/testing/admin_only.jpg)

If any non-admin user tries to access this function he is redirected to the Sign In Page where he can Log in.
![Admin access only](documentation/testing/admin_only.jpg)

Steps:
* Go to the Shop Page
* Expand the Click menu and choose "Delete Item" option.
    ![Delete Product](documentation/testing/delete_product01.jpg)

Expected result:
* A confirmation toast box should be displayed
* The products should disapear from the Shop Page.
    ![Delete Product](documentation/testing/delete_product02.jpg)



### **Register an account**

This function available for every user.

Steps:
* Expand the "Account" tab in the Page Navigation Bar and choose "Register" 
option.
    ![Register](documentation/testing/register01.jpg)
* Fill up the form and submit it by clicking "Sign Up" button.
    ![Register](documentation/testing/register02.jpg)
  Not entering values in to the required fields results with displaying a warning message.
    ![Sign up warning](documentation/testing/empty_signup.jpg)

Expected result:
* A info box should display an information that the confirmation email was sent to the user.
    ![Register](documentation/testing/register03.jpg)
* An email with the verification link should be posted to the users inbox.
    ![Register](documentation/testing/register04.jpg)
    ![Register](documentation/testing/register05.jpg)
* Clicking the link should verify the new user and Information box should be displayed.
    ![Register](documentation/testing/register06.jpg)
    ![Register](documentation/testing/register07.jpg)



### **Login**

This function is available only for registered user.

Steps:
* Expand the "Account" tab in the Page Navigation Bar and choose "Login" option.
* Fill up the form and submit it.
    ![Login](documentation/testing/login01.jpg)
  Not entering values in to the required fields results with displaying a warning message.
    ![Sign up warning](documentation/testing/empty_login.jpg)

Expected result:
* A confirmation toast box should be displayed
    ![Login](documentation/testing/login02.jpg)
* A new option "My Profile" option should be available in the "Account" tab in the navigation bar.
    ![Login](documentation/testing/display_profile01.jpg)
* Also the form in the Checkout Page since now should be prefilled.
    ![Login](documentation/testing/register08.jpg)



### **Update an account**

This function is available only for logged in users.

Steps:
* Expand the "Account" tab in the Page Navigation Bar and choose "My Profile" option.
    ![Update account](documentation/testing/display_profile01.jpg)
* Fill up the form and submit it by clicking the "Update Information" button.
    ![Update account](documentation/testing/display_profile03.jpg)

Expected result:
* A confirmation toast box should be displayed
    ![Update account](documentation/testing/display_profile04.jpg)
* After refreshing the page the user details should be still displayed.


### **Log out**

This function is available only for logged in users.

Steps:
* Expand the "Account" tab in the Page Navigation Bar and choose "Logout" option.
* Submit you choice by clicking "Sign Out" button.
    ![Log out](documentation/testing/logout01.jpg)

Expected result:
* A confirmation toast box should be displayed
    ![Log out](documentation/testing/logout02.jpg)
* "My Profile" tab should not be accessible in the "Account" tab. And only basic option should be displayed.
    ![Log out](documentation/testing/logout04.jpg)



### **Add product to the shopping basket**

This function is available to all user: loged in as well as not loged in users.
It allows the user to add product to the shopping basket where the products can be updated, deleted from basket or proceded to the chechout.

Steps:
* Go to the shop page or to the workshop page.
* In the shop page expand the "Click" button and choose the quantity then click "Add to Basket" option or choose "Display Details" to see more details about the product.
    ![Add product](documentation/testing/add_to_basket01.jpg)
* The product can be added to the basket from the Product Detail Page also.
    ![Add product](documentation/testing/add_to_basket02.jpg)

Expected result:
* After clicking "Add to Basket" button the product will be added to the basket and the Basket tab in the Navigation Bar will display the Total Price of the order.
    ![Add product](documentation/testing/add_to_basket08.jpg)
* A confirmation toast box should be displayed and the user will be redirected to the Shop Page.
* All the product added to the Shopping Basket will be displayed in the Basket Page.
    ![Add product](documentation/testing/add_to_basket07.jpg)

Errors:

In case of entering incorrect values, such as 0 or value greater the the quantity of the products available on stock a suitable warning message will be displayed
    ![Wrong value](documentation/testing/wrong_value_shop04.jpg)
    ![Wrong value](documentation/testing/wrong_value_shop03.jpg)

* An error occured when a user is trying to submit an empty value.

    ![Add product](documentation/testing/add_to_basket_04_error.jpg)
    ![Wrong value](documentation/testing/wrong_value_shop05.jpg)
    
This problem was handled programmatically using try/catch block inside the add_to_basket() function in the basket/views.py.
    ![Add product](documentation/testing/add_to_basket_05_error.jpg)



### **Update Product in the basket.**

Steps:
* Click the Basket Icon displayed in the Navigation Bar go to the Basket Page.
    ![Update Product](documentation/testing/update_basket01.jpg)
* Enter demanded value in the Quantity column.
* Submit clicking green button.

Expected result:
* A confirmation toast box should be displayed
* Number in the Quantity box should be updated.
* The Total Price of the Order ahould also be updated immediately.
    ![Update Product](documentation/testing/update_basket02.jpg)

In case of entering incorrect values, such as 0 or value greater the the quantity of the products available on stock a suitable warning message will be displayed
    ![Wrong value](documentation/testing/wrong_value_shop04.jpg)
    ![Wrong value](documentation/testing/wrong_value_shop03.jpg)

### **Remove Product from the basket**

Steps:
* Click the Basket Icon displayed in the Navigation Bar go to the Basket Page.
    ![Remove Product](documentation/testing/update_basket01.jpg)
* Click the red button in the Remove Item column.

Expected result:
* A confirmation toast box should be displayed
* The product should be remnoved from the basket.
* The Total Price of the Order should also be updated immediately.
    ![Remove Product](documentation/testing/update_basket03.jpg)


### **Make a payment at the Checkout Page**

Steps:
* Go to the Basket Page. If there are any products added a "Go To Checkout" button should be displayed.
* Click "Go To Checkout" button to go to the Checkout Page and fill up the 
form.
    ![Payment](documentation/testing/checkout01_logged.jpg)
* Click "Complete Order" button to submit.

Expected result:
* A confirmation toast box should be displayed.
* Order Summary Page should be displayed.
    ![Payment](documentation/testing/checkout02.jpg)
* The Basket should be emptied.
* Products quantity values should have been updated as well.
    ![Payment](documentation/testing/checkout05.jpg)
* An orders confirmation email should be sent to the users email address.
    ![Payment](documentation/testing/checkout06_conf_email.jpg)
    ![Payment](documentation/testing/checkout07_conf_email.jpg)
* The order should be added to the Orders History section.
    ![Payment](documentation/testing/checkout04.jpg)


### **Sign up to the Newsletter**

Every non-admin user can sign-in to Newsletter by going to the Home Page footer, filling up and submitting the form.

Steps:
* Go to the footer on the Home Page.
    ![Newsletter](documentation/testing/subscribe01.jpg)
* Enter your email in the "Sign Up To Our Newsletter" diagram.
    ![Newsletter](documentation/testing/subscribe02.jpg)
* Submit the form by clicking "Sign Me Up" button.

Expected result:
* A confirmation toast box should be displayed
    ![Newsletter](documentation/testing/subscribe03.jpg)
* A confiramtion email should be sent to the entered email address.
    ![Newsletter](documentation/testing/subscribe06.jpg)

In case of entering incorrect value a suitable warning message will be displayed.
    ![Wrong value](documentation/testing/nletter_empty.jpg)
    ![Wrong value](documentation/testing/nletter_incorrect.jpg)

### **Publish a Post**

This function available only for user registered as admin.

Steps:
* Go to the Home Page
* Fill up the form places on the bottom of the page.
    ![Publish a Post](documentation/testing/add_post01.jpg)
* Optionally the Post can be sent as Newsletter to chosen emails.
* Submit the form.

Expected result:
* A confirmation toast box should be displayed
* The new Post should appear in the Home Page.
    ![Publish a Post](documentation/testing/add_post03.jpg)
* If any email was chosen in the form a Newsletter with the Post is sent to chosen emails.
    ![Publish a Post](documentation/testing/add_post04.jpg) 
* In case of sending an empty Post or a post that doesn't contain required values a warning message will be displayed.
    ![Publish a Post](documentation/testing/empty_value_post.jpg) 


### **Edit Post**

This function is available only for users registered as admin.

Steps:
* Go to the Home Page
    ![Edit Post](documentation/testing/edit_post00.jpg)
* Fill up the form places on the bottom of the page.
    ![Edit Post](documentation/testing/edit_post01.jpg)
* Submit the form.

Expected result:
* A confirmation toast box should be displayed
    ![Edit Post](documentation/testing/edit_post04.jpg)
* The new Post should appear in the Home Page.
    ![Edit Post](documentation/testing/edit_post05.jpg)


### **Update products quantity on stock**

After the payment is made the quantity of products available on stock should be immediately updated, which means that the number of units sold in the recent transaction should be subtracted.

Products quantity before making a sale.

![Manual testing](documentation/testing/add_to_basket02.jpg)

Products in the shopping basket.

![Manual testing](documentation/testing/update_basket01.jpg)

Products quantity after the sale is finished.

![Manual testing](documentation/testing/checkout05.jpg)

Note. The number of units available on stock is updated after the payment is made. Not after the product is added to the basket.
