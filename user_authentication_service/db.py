#!/usr/bin/env python3
"""DB module
"""
from user import User  # Assuming your User model is imported from user.py

class DB:
    """DB class
    """

    # ... (existing code)

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database.

        Args:
            email (str): The email of the user.
            hashed_password (str): The hashed password of the user.

        Returns:
            User: The User object representing the newly added user.
        """
        # Create a new User object with the provided email and hashed_password
        new_user = User(email=email, hashed_password=hashed_password)

        # Add the new_user to the session (but not the database yet)
        self._session.add(new_user)

        # Commit the session to persist the new_user to the database
        self._session.commit()

        # Return the User object representing the newly added user
        return new_user
