# sanitizeMe

sanitizeMe is an automated donation platform aimed at helping school girls in sub-Saharan Africa access sanitary towels and other necessary supplies. The project includes a web-based application that allows users to donate, register charities, and view information about various charities and their impact.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```
sanitizeme/
│
├── client/
│   ├── public/
│   ├── src/
│   │   ├── assets/              # Images and other assets
│   │   ├── components/          # React components
│   │   │   ├── Footer.js
│   │   │   ├── Header.js
│   │   │   ├── Homepage.js
│   │   │   ├── HumanitarianMission.js
│   │   │   ├── Login.js
│   │   │   ├── OpenDonations.js
│   │   │   ├── Partners.js
│   │   │   ├── Register_charity.js
│   │   │   ├── SignUp.js
│   │   ├── stylesheets/         # CSS files
│   │   │   ├── Homepage.css
│   │   │   ├── HumanitarianMission.css
│   │   │   ├── Partners.css
│   │   ├── App.js
│   │   ├── index.js
│   ├── package.json
│
├── server/
│   ├── app.py                   # Flask application
│   ├── models.py                # Database models
│   ├── routes.py                # API routes
│   ├── config.py                # Configuration settings
│   ├── requirements.txt         # Python dependencies
│
├── README.md
└── .gitignore
```

## Installation

### Prerequisites

- Node.js and npm
- Python 3 and pip
- Flask
- SQLAlchemy

### Frontend Setup

1. Navigate to the `client` directory:
   ```sh
   cd client
   ```

2. Install the dependencies:
   ```sh
   npm install
   ```

### Backend Setup

1. Navigate to the `server` directory:
   ```sh
   cd server
   ```

2. Create a virtual environment and activate it:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the Python dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up the database and environment variables as needed in `config.py`.

## Usage

### Running the Frontend

1. In the `client` directory, start the development server:
   ```sh
   npm start
   ```

2. Open your browser and go to `http://localhost:3000`.

### Running the Backend

1. In the `server` directory, start the Flask server:
   ```sh
   flask run
   ```

2. The backend server will be running on `http://localhost:5000`.

## Features

- User registration and authentication
- Donation processing and payment via MPESA and Paypal
- Charity registration and management
- Display of impact statistics and donor information
- Responsive design
- Toast notifications using `react-toastify`

## Technologies Used

### Frontend

- React
- React Router
- Axios
- Chakra UI
- `react-toastify`

### Backend

- Flask
- SQLAlchemy
- PostgreSQL

## Contributing

We welcome contributions from the community. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature/your-feature-name
   ```

3. Make your changes and commit them:
   ```sh
   git commit -m 'Add some feature'
   ```

4. Push to the branch:
   ```sh
   git push origin feature/your-feature-name
   ```

5. Open a pull request and describe the changes you have made.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
## Project Members

 - Dorcas Karimi
 - Faith Ogendi
 - Bradley Mbuvi
 - Collins Kipngetich
 - Arnold Amusengeri (SM)

