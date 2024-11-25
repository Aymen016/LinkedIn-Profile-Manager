# LinkedIn Profile Manager

✨ A simple yet professional web application to manage LinkedIn-like profiles, featuring options to add, update, delete, and search profiles with a user-friendly interface and MongoDB integration. ✨

The **LinkedIn Profile Manager** is a web-based application that allows users to manage LinkedIn profiles by storing, updating, searching, and deleting profile data using **MongoDB**. This project is built with **Flask**, **HTML**, **CSS**, and follows LinkedIn branding for a professional interface.

## **Features**
🔥 Highlights:

💼 Add LinkedIn profiles with details like name, job title, skills, and connections.

📋 View all profiles in a sleek, responsive table.

✏️ Update or 🗑️ delete profiles with a single click.

🔍 Search for profiles by name with an intuitive modal.

💬 Flash messages to notify users of actions (e.g., "Profile not found", "Profile added").

🎨 Styled with LinkedIn branding for a professional look.

---

## **Installation Steps**
Follow these steps to get the project running locally on your machine.

### **1. Prerequisites**
- Python 3.7 or above
- MongoDB installed and running
- Browser to access the web application

### **2. Clone the Repository**
```bash
git clone https://github.com/yourusername/LinkedIn-Profile-Manager.git
cd LinkedIn-Profile-Manager
```

### **3. Set Up a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate        # For Linux/Mac
venv\Scripts\activate           # For Windows
```

### **4. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **5. Run MongoDB Locally**
Ensure that MongoDB is running on `localhost:27017`. You can start the service with:
```bash
mongod
```

Alternatively, you can connect to a MongoDB Atlas cluster by updating the connection string in `app.py`:
```python
client = MongoClient("your_mongodb_uri")
```

### **6. Run the Application**
```bash
python app.py
```
The application will be available at `http://127.0.0.1:5000`.

---

## **Folder Structure**
```
LinkedIn-Profile-Manager/
│
├── static/
│   ├── styles.css               # Main CSS file for styling
│   ├── linkedin-logo.png        # Logo used in the header
│   ├── linkedin-icon.png        # Icon for buttons
│
├── templates/
│   ├── base.html                # Base layout file
│   ├── index.html               # Home page to display all profiles
│   ├── update.html              # Profile update form
│   ├── add.html                 # Profile add form
│
├── app.py                       # Main Flask application
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
```

---

## **Usage**
### **1. Add Profiles**
- Click on the "Add Profile" button in the navigation bar.
- Fill out the form with name, job title, skills, and connections.
- Submit the form to add the profile.

### **2. View Profiles**
- Navigate to the home page to see all profiles displayed in a table.

### **3. Search Profiles**
- Click on the "Search" button in the navigation bar.
- Enter a name in the modal and click "Search".
- If the profile exists, it will be displayed; otherwise, you’ll see a flash message.

### **4. Update Profiles**
- Click on the "Update" button next to a profile in the table.
- Modify the fields as needed and save the changes.

### **5. Delete Profiles**
- Click on the "Delete" button next to a profile in the table.
- The profile will be permanently removed.

---

## **Screenshots**

📸 Check out the visual walkthrough below:
### **Home Page**
![Screenshot 2024-11-25 190555](https://github.com/user-attachments/assets/6235522d-f50c-426e-9d2b-68f3f84672a8)

### **Add Profile**
![Screenshot 2024-11-25 191253](https://github.com/user-attachments/assets/07334a57-a489-457e-9287-6db4b6a8d5a8)


### **Search Modal**
![Screenshot 2024-11-25 191155](https://github.com/user-attachments/assets/f1eb98bd-c21f-4d24-bc57-e3ee2ce82334)

---

## **Technologies Used**
- **Frontend**: HTML, CSS
- **Backend**: Flask
- **Database**: MongoDB
- **Icons**: LinkedIn logo and icons for branding

---

## **To-Do (Future Enhancements)**
- Add pagination for profiles.
- Implement user authentication.
- Deploy the application to Heroku or AWS.
- Add more LinkedIn-inspired themes and animations.

---

## **Contributing**
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a Pull Request.

---


## **Contact**
For any queries or feedback, feel free to reach out:
- **Email**: ayemenbaig26@example.com
- **LinkedIn**: www.linkedin.com/in/aymen-baig-700a06284

---

Happy Coding! 🎉
