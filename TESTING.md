# Testing


##  **Responsiveness**
- The project was responsive tested on https://ui.dev/amiresponsive and it is responsive for every type of devices such as desktop computers, laptops, tablets and smart phones.

![Am I Responsive]()

## **Code Validator Testing**

- ### **HTML**

    An error was detected during validation testings with use of [W3C validator](https://validator.w3.org/nu/).

    According to the tests the error comes from material_forms and it is implemented form django_material add-on. 
    This generates: "Attribute for not allowed on element span at this point" Error. 
    The same error occures in a few other templates.


    - Edit List Page:

        ![html_validation]()

        ![html_validation]()

    - Edit Item Page:

        ![html_validation](documentation/images/testing/html_login_error.jpg)

        ![html_validation]()

    - Login Page:

        ![html_validation]()

        ![html_validation]()

    - Items Page

        In some cases the test shows slightly different results depending on the input method: 

        If we enter data with Check by address the validator shows the error mentioned above:

        ![html_validation]()

        ![html_validation]()

        Check by text-input doesn't show any errors or warnings in this template.

        ![html_validation]()

    - Lists Page:

        The situation looks similarly in the lists_html template. 

        Check by address:

        ![html_validation]()

        Check by text-input:

        ![html_validation]()


    The rest of the html Templates show no errors no matter how the input was applied.

    - Home Page:

        ![html_validation]()

        ![html_validation]()

    - About Page:

        ![html_validation]()

    - Register Page:

        ![html_validation]()

    - Logout Page:

        ![html_validation]()

        


    * Link to the validation testing for my Html file:


- ### **CSS**
    * No errors were detected when passing through the [jigsaw.w3 validator](https://jigsaw.w3.org/css-validator). 

         ![css_validation]()
    

- ### **JAVASCRIPT**
   
    * No errors were detected when passing through the jshint validator.

         ![js_validation]()

- ### **PYTHON**

     No error detected when passing the following file through the CI Python Linter:

    - views.py:

        ![python_validation]()

    - admin.py 

        ![python_validation]()

    - forms.py

        ![python_validation]()

    - models.py

        ![python_validation]()

    - list/urls.py

        ![python_validation]()

    - shopping/urls.py

        ![python_validation]()
