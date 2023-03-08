# backend-intern-assessment

Django was used for this RESTful API project. The dependencies installed are listed  below.
- django
- djangorestframework
- djangorestframework-simplejwt
- gunicorn

This application is currently hosted on Render at https://lawminghan.onrender.com

### The available API endpoints for the assessment are listed below.
---
> api/token/
- HTTP Method: POST
- Authentication: AllowAny
- Request Body: `email` and `password` fields 
- Returns `jwt_access_token` and `jwt_refresh_token`


> api/token/refresh/
- HTTP Method: POST
- Authentication: AllowAny
- Request Body: `refresh` field
- Returns `jwt_access_token`


> api/account/registration
- HTTP Method: POST
- Authentication: AllowAny
- Request Body: `email`, `password`, `firstName`, `lastName`, `role`, `company`, `designation` fields
- Create new user with these fields.

Note: `role` is an enum that has three values: `ADMIN`, `TECHNICIAN` and `MEMBER`. `company` and `designation` are optional.


> api/account/user
- HTTP Methods: GET, PATCH, DELETE
- Authentication: ADMIN, MEMBER, TECHNICIAN
- Header include "Authorization: Bearer `jwt_access_token`"
  
1. GET - no request body needed. Returns current user info.
2. PATCH - `password`, `firstName`, `lastName`, `company`, `designation` fields. Updates the relevant info of the current user. All fields are optional.
3. DELETE - no request body needed. Deletes the current user.


> api/account/admin/users
- HTTP Method: GET
- Authentication: ADMIN only
- Header include "Authorization: Bearer `jwt_access_token`" of ADMIN
- Returns a list of all users.

> api/account/admin/users/`<int:user_id>`
- HTTP Method: GET, PATCH, DELETE
- Authentication: ADMIN only
- Header include "Authorization: Bearer `jwt_access_token`" of ADMIN

1. GET - No request body needed. Returns user specified by `user_id`.
2. PATCH - `role` field only. Updates the role of user specified by `user_id`
3. DELETE - No request body needed. Deletes user specified by `user_id`.


> admin/
- Default Django Admin panel
- Admin Info noted down in [user_info.txt](./backend/user_info.txt) for testing purposes.
