FamPay Assignment
---


Try It
---

open folder Django Project Folder Async_Api_call

run `docker-compose up`

The above command will set up all the requirements, will do migrations, indexing in tables.



How to run:
---

- First Open http://127.0.0.1:8000/call_me_first/
	- This will start data pulling from youtube in every 10 seconds.


- Templates
	- http://127.0.0.1:8000/local/pagination   UI for pagination API
	- http://127.0.0.1:8000/local/search       UI for serach API


- Apis URL
	- http://127.0.0.1:8000/local/get_pagination_video_response?page_no=2 Return Json Response for Pagination
	- http://127.0.0.1:8000/local/get_search_response?params=python%20is%20good%20lag Return Json Response for text search


References:
---

- [https://medium.com/backticks-tildes/how-to-dockerize-a-django-application-a42df0cb0a99](https://medium.com/backticks-tildes/how-to-dockerize-a-django-application-a42df0cb0a99)

- [https://dev.mysql.com/doc/refman/8.0/en/fulltext-natural-language.html](https://dev.mysql.com/doc/refman/8.0/en/fulltext-natural-language.html)

- [stackoverflow] (https://stackoverflow.com/)



