# LittleLemon

API endpoitns for project
/auth/users/ (POST request method to create new user)
/auth/token/login/ (POST request method to get authentication token for login)
/auth/users/me (GET request method to get current user data , authentication token required)
/restaurant/ (GET request method to render html page )
/restaurant/menu (GET request method to return all menu items)
/restaurant/menu/ (POST request method to create new menu item,authentication token required )
/restaurant/menu/3 (GET request method to get single menu item ,replace "3" with required item's id,authentication token required )
/restaurant/menu/3 (PUT request method to update single menu's item,replace "3" with required item's id,authentication token required )
/restaurant/menu/3 (DELETE request method to delete single menu's item ,replace "3" with required item's id,authentication token required)
/restaurant/booking/tables/ (GET request method to get booking table,,authentication token required)
/restaurant/booking/tables/ (POST request method to add new record to booking table,authentication token required)
/restaurant/booking/tables/2/ (PUT request method to update record in booking table,replace "2" with required item's id,authentication token required)
/restaurant/booking/tables/2/ (DELETE request method to delete record in booking table,replace "2" with required item's id,authentication token required)
