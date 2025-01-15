# My Chat App

A responsive and real-time chat application built with Django, WebSockets, and an elegant user interface.

## Features

- **Real-Time Chat**: Communicate with other users in real-time using WebSockets.
- **Responsive Design**: Works seamlessly on desktops, tablets, and mobile devices.
- **Toggleable Left Panel**: Collapse and expand the left menu for better navigation.
- **Fixed Navbar and Footer**: Persistent navigation bar and footer for easy access.
- **Dynamic User List**: Displays all registered users for initiating chats.
- **Secure Login and Logout**: Built-in Django authentication system.

## Installation

1. Clone the repository:

   ```bash
   git clone <https://github.com/Jenish-1235/Realtime-Chat-App>
   cd <Realtime-Chat-App>
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser for admin access:

   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:

   ```bash
   python -m daphne realtime_chat.asgi:application --port 8000
   ```

6. Access the application at [http://127.0.0.1:8000/chat/signup](http://127.0.0.1:8000/chat/signup).

## Screenshots

### Chat Home Page
![image](https://github.com/user-attachments/assets/130ae748-b062-4a52-a76d-7f53cf59f62e)


### Login Page
![image](https://github.com/user-attachments/assets/72d979a7-07c9-421a-b39c-7a611964cfd9)


### Signup Page
![image](https://github.com/user-attachments/assets/c9ace6d6-4687-4ef1-bc3d-7724698e7b48)


## Technologies Used

- **Backend**: Django, Django Channels, Daphne
- **Frontend**: HTML, CSS, JavaScript
- **WebSocket**: Real-time communication
- **Database**: SQLite (default, can be replaced with PostgreSQL or MySQL)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, feel free to reach out:

- **Email**: jenishtogadiya549@gmail.com
- **GitHub**: [Your GitHub Profile](https://github.com/Jenish-1235)
