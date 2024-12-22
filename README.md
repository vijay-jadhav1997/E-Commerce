# 🧘🏻‍♂️⚡ Indic Products App 💡💯
### 🌐visit Indic Products App => [Indic Products App](https://indic-products.vercel.app/)

Welcome to **Indic Products**, a Django-based e-commerce platform where users can create accounts to buy and sell various products. The platform supports seamless product listings, secure transactions, and personalized experiences for both buyers and sellers.

## Features

  - **General:** 
    - User-friendly account creation and management.
    -  Authentication and authorization using Django's built-in features.

  - **For Buyers:** 
    - Browse diverse product categories.
    - Add products to a wishlist for future purchases.
    -  Secure checkout and order tracking.

  - **For Sellers:** 
    -  Create and manage product listings.
    - Insights and analytics for sales performance.
    - Real-time order and inventory management.


## Tech Stack
  - Frontend: HTML, CSS, JS(ES6+).
  - Backend: Django.
  - Deployment: Deployed on 


## Installation and Setup:
- **Prerequisites**
  - Python (3.9 or later)
  - PostgreSQL

- **Steps to Set Up the Project :**

  1. **Clone the Repository:**
    ```sh
    git clone https://github.com/vijay-jadhav1997/E-Commerce.git
    cd E-Commerce
    ```
  2. **Set Up a Virtual Environment:**
    ```sh
    python -m venv myvenv
    source myvenv/Script/activate // For Windows
    source myvenv/bin/activate // For Linux/Mac
    ```
  3. **Install Dependencies:**
    ```sh
    cd ecommerce
    pip install -r requirements.txt
    ```
  4. **Configure Environment Variable:**
    - Create .env file in the root directory and add the following
    ```sh
    SECRET_KEY=your_secret_key
    DEBUG=True
    DATABASE_URL=postgres://user:password@localhost:5432/indic_products
    ```
  5. **Applying Migrations:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```
  6. **Create a Superuser:**
    ```sh
    python manage.py createsuperuser
    ```
  7. **Start the development server:**
    ```sh
    python manage.py runserver
    ```



## Contributing:

Contributions are always welcome! If you have suggestions or improvements, feel free to submit a pull request or open an issue.
**Steps to Contribute:**
  1. Fork the repository.
  2. Create a new branch for your feature or bugfix.
  3. Make your changes and commit them with a descriptive message.
  4. Push to your fork and submit a pull request.


## Contact:
If you have any questions or feedback, feel free to reach out at 
- [vijay-jadhav1997](https://www.linkedin.com/in/vijay-jadhav1997).
- Email: vijay05111997@gmail.com
