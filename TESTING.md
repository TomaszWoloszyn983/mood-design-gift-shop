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

        Link to the test: 

    - My Profile Page:

        ![html_validation]()

        Link to the test: 

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

        


    * Link to the validation testing for my Html file:


- ### **CSS**
    * No errors were detected when passing through the [jigsaw.w3 validator](https://jigsaw.w3.org/css-validator). 

    - base.css file

        ![css_validation](documentation/testing/w3c_base.jpg)
    
    - checkout.css file

        ![css_validation](documentation/testing/w3c_checkout.jpg)   
    

- ### **JAVASCRIPT**
   
    * No errors were detected when passing through the jshint validator.

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
   
## Manual Testing

Testing all the applications functionalities.

![Manual testing]()

### Add Product

A function available only for user registered as admin.

Steps:
* Go to the Shop Page
* Click "Add Item" button
* Fill up all the required fields. 
* Add an image of the product otherwise a default image will be added to the product.

Expected result:
* A confirmation toast box should be displayed
* A new product should appear on the page


![Manual testing]()

### Edit Product

A function available only for user registered as admin.

Steps:
* Go to the Shop Page
* Expand the Click menu and choose "Edit Item" option.
* Fill up all the required fields. 

Expected result:
* A confirmation toast box should be displayed
* The products detail should be updated.

![Manual testing]()

### Deleting Product

A function available only for user registered as admin.

Steps:
* Go to the Shop Page
* Expand the Click menu and choose "Delete Item" option.

Expected result:
* A confirmation toast box should be displayed
* The products should disapear from the Shop Page.

![Manual testing]()

### Register an account

![Manual testing]()

### Update an account

![Manual testing]()

### Login

![Manual testing]()

### Log out

![Manual testing]()

### Add product to the shopping basket

![Manual testing]()

### Update Product in the basket.

![Manual testing]()

### Remove Product from the basket

![Manual testing]()

### Make a payment at the Checkout Page

![Manual testing]()

### Sign up to the Newsletter

![Manual testing]()

### Publish a Post

![Manual testing]()

### Update products quantity on stock

    After the payment is made the number of products available on stock should be immediately updated, which means that the number of units sold in the recent transaction should be subtracted.

![Manual testing]()

